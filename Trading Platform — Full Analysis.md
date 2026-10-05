# Trading Platform — Full Analysis

**Project:** `D:\glm crawl\project-folder-for-claw`
**Code under analysis:** `latest-code-with-gemini/` (broker-platform · mt5-admin-web · trade-server)
**Compared against:** MT5 vendor reference corpus, real MT5 server exports, 19 vendored trading engines
**Date:** 2026-09-29
**Method:** 5 parallel read-only investigators (MT5 docs · matching-engines · trading core · platform/infra · integrations) plus 1 independent verifier for the highest-severity claims.

> **Evidence discipline.** Every status in this document comes from **reading source**, not from executing it. No test suite, lint pass, proof script or gate was run. Where a number comes from project documentation rather than a re-read, it is marked *(documented)*. Where a claim was independently re-verified, it is marked *(confirmed twice)*.

---

## A. Executive Summary

**The core trading logic is genuinely good. The platform plumbing around it has serious holes.**

### What the project does well — and this is unusual

- The **margin engine** is a faithful implementation of MT5's four-stage calculation (basic formula → currency conversion → margin rate → aggregation), including all three margin modes (leverage-based, symbol rate matrix, fixed value) and hedged/covered netting.
- **Pricing** follows MT5's exact ordering (symbol spread → group `SpreadDiff`), and cross-currency conversion is side-aware with proper triangulation that raises an error rather than guessing 1.0.
- The **OMS** handles both netting and hedging correctly — weighted-average entry price, partial close, in-place reversal, close-by.
- The **MT5 configuration codec** (export/import JSON) is empirically derived from a real server export (362 symbols × 121 fields, 20 groups), and it correctly keeps `Point` and `TickSize` separate — they differ on **131 of 362 symbols**.

### What is wrong — in plain terms

| # | Problem | Severity |
|---|---|---|
| 1 | **Five security controls are dead code in production.** Rate limiting, token revocation, 2FA and IP allow-listing are all built, exported — and never registered. *(confirmed twice)* | 🔴 Critical |
| 2 | **Auth invents a $10,000 account** when a user isn't found, instead of returning 401. | 🔴 Critical |
| 3 | **The frontend fabricates order rows** on the live path (`state: 'filled'`), directly contradicting its own non-negotiable rule. | 🔴 Critical |
| 4 | **Stop-out has never fired.** Thresholds are correct (50%), a liquidation planner exists — but it has never run live. | 🔴 High |
| 5 | **Docs certify infrastructure that doesn't run.** A "99.6% compliant / Verified Fact" audit describes ClickHouse, Redis caching and an event store that **no production path instantiates**. | 🔴 High |
| 6 | **The stale-quote guard is defeated** on the trade-server path because the wire timestamp is thrown away — and a unit test contradicts the code. | 🟠 High |
| 7 | **trade-server has zero authentication** — all REST endpoints and both WebSocket endpoints. | 🟠 High |
| 8 | **The event bus has no durability.** Redis pub/sub retains nothing; the one persistent sink has zero callers. | 🟠 Medium |

### One-line verdict

This is a well-researched MT5 clone whose **domain logic** is close to reference-grade, sitting on an **infrastructure layer** that is partly aspirational, partly unwired, and documented more optimistically than it behaves.

**The single most important observation:** the project's best cultural feature is *"refuse honestly"* — an endpoint works or returns an honest 501. That discipline holds at the API surface and erodes at its edges (fabricated frontend rows, fabricated auth accounts, docs certifying unwired components).

---

## B. Current Architecture Map

```
┌──────────────────────────────────────────────────────────────┐
│  mt5-admin-web  (React 18 + TS + Vite + zustand + dockview)  │
│  62-method AdminApi contract · 2 transports (mock | live)    │
│  12 gaps throw BackendGapError · LayoutHost = only dockview  │
└───────────────────────────┬──────────────────────────────────┘
                            │ /api/v1  +  /ws/stream, /ws/user
┌───────────────────────────▼──────────────────────────────────┐
│  broker-platform  (FastAPI)                                  │
│ ┌──────────────────────────────────────────────────────────┐ │
│ │ api/      client + admin + manager routers (160 routes)   │ │
│ │           websockets (stream/user/manager) · auth (JWT)   │ │
│ ├──────────────────────────────────────────────────────────┤ │
│ │ application/  13 commands · 12 queries · 13 services      │ │
│ │               3 workers (sltp, expiration, liquidation)   │ │
│ │               di/ (market_data, pricing, trading setup)   │ │
│ ├──────────────────────────────────────────────────────────┤ │
│ │ core/   12 domains · ports/interfaces.py · domain events  │ │
│ ├──────────────────────────────────────────────────────────┤ │
│ │ infrastructure/  persistence (18 repos + UoW)             │ │
│ │                  messaging (inprocess | redis bus)        │ │
│ │                  mt5 (Administrator config JSON codec)    │ │
│ │                  feeds · gateways · fix · engines ·       │ │
│ │                  security (built but unwired)             │ │
│ └──────────────────────────────────────────────────────────┘ │
└───────┬───────────────────────────────────────┬──────────────┘
        │                                       │
   PostgreSQL/Neon                        Redis (bus + cache)
   (hot, operational)                     └─ ClickHouse: tests only
        ▲
        │ msgpack ticks over WS
┌───────┴──────────────────────────────────────────────────────┐
│  trade-server  (FastAPI + MetaTrader5 SDK)                    │
│  1 worker process per instance · 2 multiprocessing queues     │
│  17 CMD_* / 11 UP_* · 50 ms poll loop (~20 Hz) · NO AUTH      │
└──────────────────────────────────────────────────────────────┘
```

### Layering

| Layer | Contents | Verdict |
|---|---|---|
| `core/` | 12 domains, `ports/interfaces.py`, domain events | Framework-free and DB-free — respected |
| `application/` | 13 commands, 12 queries, 13 services, 3 workers, DI | CQRS split respected |
| `infrastructure/` | Persistence (18 repos + UoW), messaging, MT5 codec, feeds, gateways, FIX, engines, security | Implements core ports |
| `api/` | 4 client routers, admin plane, 11 manager modules, 3 WebSocket channels, JWT auth | 160 route decorators |

**Dependency direction is respected** (`api → application → core`, with infrastructure implementing ports) — verified in the DI wiring. The one real breach: three manager routers construct `TradeServerLiquidityGateway` inline with a hardcoded `127.0.0.1:8000`, bypassing DI and disagreeing on timeouts.

---

## C. MT5 Compatibility Analysis

This is where the project is strongest — **but with one important corpus discovery.**

> ### ⚠️ Corpus correction (important)
>
> `MetaTrader5SDK/` and `mt5 sdk single md file/` are the **MetaQuotes Server/Manager/Gateway/Web SDK** (~1103 documented pages) — **not** the retail `MetaTrader5` Python package.
>
> `symbol_select`, `copy_ticks_from/range`, `copy_rates_*`, `positions_get`, `order_send` and `mt5.initialize` appear **nowhere** in the vendor documentation. Every corpus-wide hit is our own code, a chat transcript, or a project-derived catalogue. **The retail Python SDK is undocumented in this corpus** and needs an external source.

### Compatibility matrix

| Area | Finding | Current implementation | Reference / evidence | Status |
|---|---|---|---|---|
| Margin formula | Forex = vol × contract ÷ leverage; CFD = vol × contract × price; futures flat; fixed overrides all | `core/domains/market_data/margin.py` — all modes, 4-stage pipeline | `MetaTrader5Manager/…/Margin-Calculation-Basic.md` | **MATCH** |
| Margin rates | 16 order-type-specific rates (Initial/Maintenance × Buy/Sell × market/limit/stop/stoplimit) | 8 rates with maintenance→initial inheritance, default rate 1 | `mt5-format-structure/Symbols TCTrader-Live.json`; `Margin.md` | **MATCH** |
| Margin call / stop-out | **Percent** of margin level (export shows 10.00 / 1.00; group `real\real` shows 50.00 / 30.00) | `margin_call_level: 80`, `stop_out_level: 50` — explicitly percent, fraction values rejected | `Groups TCTrader-Live.json`; `Margin.md`; `Accounts-with-Margin-CallStop-Out.md` | **MATCH** |
| Equity / free margin / margin level | Equity = Balance + Credit − Commission ± Floating P/L; Free = Equity − Margin; Level = Equity/Margin×100 | Matches | `Clients-and-Trading-Accounts/Account-Overview.md` | **MATCH** |
| Stop-out behaviour | Delete largest-margin pending → close largest-loss position → repeat until above level; zero-margin orders spared | `liquidation_service.py` sorts worst-loss first, returns a `LiquidationPlan` | `Accounts-with-Margin-CallStop-Out.md` | **PARTIAL** — planner correct, never fired live |
| CalcMode 3 (CFD index) | vol × contract × price × (TickValue / TickSize) | **Raises** — deliberately unimplemented | `Margin-Calculation-Basic.md` | **GAP** (known, documented) |
| Leverage tiers / floating margin | Multi-level profiles keyed by volume or notional; zero maintenance ratio = no margin (unlike symbol settings, where zero falls back to initial) | Per-position leverage resolution (account/group/symbol); tier profiles not modelled | `Margin.md` §§Floating Margin | **PARTIAL** / **UNKNOWN** |
| Volume scaling | 10⁴ for plain fields, 10⁸ for `*Ext` ("105000000 means 1.05 lots") | Codec captures per-field **and per-record** scale and replays it | `IMTConSymbol/VolumeMinExt.md` | **MATCH** |
| Point vs TickSize | Distinct fields; CFD-index margin formula needs both | Codec explicitly refuses to merge them (differs on 131/362 symbols) | `Point.md`, `TickSize.md` | **MATCH** |
| Groups as rule engines | 47 fields incl. commissions, per-path symbol overrides (`"default"` = inherit), auth policy, limits | Config-driven groups with loader-validated YAML | `Groups TCTrader-Live.json`; `groups.png` et al. | **MATCH** (structure) |
| Account types | `real\` / `demo\` / `managers\` prefixes; Preliminary = zero balance, trading disabled | Implemented + identity plane | `Preliminary-Accounts.md`; export (20 groups) | **MATCH** |
| Contest accounts | Corpus **silent** — no definition, no prefix; nearest artefact is `demo\Challenge` | Account types include Contest | corpus silent | **UNKNOWN** |
| Coverage accounts | `Summary-Positions-and-Coverage.md` unread; no coverage group in the export | Coverage repository exists | corpus incomplete | **UNKNOWN** |
| Order states | 10 values: STARTED 0 … REQUEST_CANCEL 9 | 8 order types; state enum thinner | `IMTOrder/Enumerations.md#enorderstate` | **PARTIAL** |
| Order types | 8 incl. STOP_LIMIT; `OP_CLOSE_BY 8` (hedging only) | All 8 modelled; STOP_LIMIT is one call, not two-phase | `IMTOrder/Enumerations.md` | **PARTIAL** |
| Deal taxonomy | 21 actions incl. `DEAL_SO_COMPENSATION 19/20`; entries `IN/OUT/INOUT/OUT_BY` | Standard entries; no stop-out compensation path | `IMTDeal/Enumerations.md` | **PARTIAL** |
| Netting vs hedging | Netting = one position per symbol; hedging = many; **hedging cannot reverse in place** (close + reopen) | Both implemented; weighted averaging; reverse-in-place for netting | `Position-Accounting-System.md` | **MATCH** |
| Deal immutability | **Corpus conflict** — SDK documents `DEAL_BUY_CANCELED`/`DEAL_SELL_CANCELED` and `ModificationFlags`; our design doc asserts immutability | Reversal + correction pattern; no DB-level write-once constraint | `IMTDeal/ModificationFlags.md` vs `code files/3 oms.md` | **PARTIAL** |
| Filling modes | FOK / IOC / Return / BOC, per execution mode (Instant & Request = FOK only; Market = FOK+IOC+Return) | **No filling-mode logic at all** | `Fill-Policy.md`; `#enfillingflags`; `#enorderfilling` | **GAP** |
| Expiration modes | Symbol-level 4 flags + order-level GTC/DAY/SPECIFIED/SPECIFIED_DAY | **Only `SPECIFIED`** implemented; DAY/EOD stated gap | `#enexpirationflags`, `#enordertime` | **GAP** |
| Stops / freeze level | `StopsLevel` 10, `FreezeLevel` 0 (points), overridable per group path | Fields exist; pre-trade enforcement absent | symbol export | **PARTIAL** |
| Sessions | 7-element Sunday-first arrays, minutes from midnight; empty = closed | Modelled and checked in `create_order` | symbol export; `SymbolSessions` | **MATCH** |
| Manager REST API | 124 operations (Main 66, WebSockets 18, Reports 13, Subscriptions 11, Trading 7, Connection 4, Service 4, Admin 1) | ~55% served / ~15% skeleton / ~20% future / ~10% refused *(documented, pre-M18 draft)* | `mtapi-docs/swagger.json` | **PARTIAL** |
| Web API surface | 231 commands across 44 families | Family-level disposition documented per family | `Web-API.md`; `docs/ENDPOINT-CATALOG.md` | **PARTIAL** |
| Trade modification | Order send/modify/delete/close/activate; deal modify/update/perform/delete at admin level | Reversal + correction implemented; HTTP surface partial | swagger `Trading` family; `Trade-Modifications.md` | **PARTIAL** |

### ⚠️ Critical unresolved conflict — deal immutability

The corpus contains **no normative statement** that deals are immutable. What it *does* contain:

- `DEAL_BUY_CANCELED 13` / `DEAL_SELL_CANCELED 14` — the earlier executed deal's **type is replaced** via Gateway `TE_DEAL_CANCEL`, P/L cleared, position recalculated, difference booked as a separate balance operation.
- `IMTDeal::ModificationFlags` — exists specifically to *"keep track of whether a deal has been modified manually by the administrator, manager or API."*
- Admin-level endpoints `DealModify`, `ModifyDeal`, `DealUpdate`, `AdmTradeRecordsModify`, `AdmTradesDelete`.

Against this, our project's `code files/3 oms.md` (a **project design doc**, secondary source) asserts *"dealers NEVER modify existing deals."*

**This must be decided before the OMS hardens further.** It is a defensible design choice — but it is a choice, not an MT5 requirement.

---

## D. Trading Lifecycle Analysis

### Order → fill → position, as actually implemented

```
POST /order → create_order.py::CreateOrderHandler
  1. account + symbol fetch
  2. session check · direction check · volume validation      (ValueError on fail)
  3. market price resolved BEFORE risk (no price → REJECTED, persisted)
     · RuntimeError (stale quote → NoQuoteError) treated the same
  4. risk_service.validate_order(..., publish_events=False) under a per-account lock
  5. persist state PLACED → on save failure, _release_reservation()
  6. publish OrderCreated → OrderApproved
  7. re-read loop (_MARKET_REFRESH_WINDOW_S = 1.5) until FILLED
       ↓
execution_orchestrator.handle_order_approved
  → SmartOrderRouter.route
      · MT5 request-policy table first (delay_ms / delay_ticks, clear_sl / clear_tp)
      · terminal actions: REJECT / DEALER / REQUOTE→REJECT / CANCEL_ORDER→REJECT
      · _route_house matches house rules by priority
      · no match → default_destination (B_BOOK) with a warning
      · rules never loaded → raise
  → _execute_a_book | _execute_b_book | _execute_in_house | _send_to_dealer | _reject_order
       ↓
B-Book fill via matching_engine.on_fill()      A-Book via LP gateway
       ↓
Position.apply_deal(deal, position_mode)
  HEDGING : opposite side → new opposite Position; same side → average in
  NETTING : same side → add; opposite → _close_or_reverse (close / close+new / reduce)
```

### Correct behaviours observed

- The full request → risk → route → fill → deal → position chain exists and is coherent.
- **Bid/ask side conventions match MT5**: SL/TP for BUY checked against **BID**, for SELL against **ASK**; SL checked before TP.
- SL/TP closes at market with proper reason codes (`SL` / `TP`).
- Market orders price **before** risk with no price → persisted `REJECTED` (an honest refusal, not a silent 0-price fill).
- `_market_price()` uses the live client-quote provider; `NoQuoteError` on a stale quote is handled, not ignored.

### Missing or wrong

| Item | Detail |
|---|---|
| **No filling modes** | FOK/IOC/Return unimplemented. No MT5 filling-mode logic found at any layer. |
| **No internal partial fills** | The engine's `price_order()` returns one price for the whole order; internal fills are all-or-nothing. `PARTIALLY_FILLED` state exists and LP `PARTIAL` is booked, but the internal path cannot produce it. |
| **Expiration only `SPECIFIED`** | DAY/EOD is a stated gap. Sweep runs every 15 s plus once on start. |
| **A-Book close does not unwind the hedge** | `TradeServerLiquidityGateway.close_position()` is *"called by nothing"* (confirmed in `PROJECT-STATE-v4/5/6/7/8`). **Exception:** the SL/TP path *does* call the LP close endpoint when `position.external_id` is set, is LP-first, and refuses to close locally if the LP refuses. |
| **STOP_LIMIT is not two-phase** | Modelled as "arm and price in the same call", not a real arm → trigger → place-limit state. |
| **Delete/​reject/​requote dealer flow absent** | DEALER actions are skipped with a warning when no dealer sessions exist; REQUOTE maps to REJECT ("requote: no dealer terminal"). |

**Status: PARTIAL** — correct chain and MT5 side conventions, but no filling modes and no partial fills.

---

## E. Matching-Engine Analysis

### Our engine

`infrastructure/engines/book_matching_engine.py` states its own scope honestly:

> *"a B-Book / internalisation engine plus a resting-order book for pending orders. It is **NOT** a price-time-priority CLOB that nets client against client."*

- **Structure:** `_books: Dict[symbol, List[Order]]` in **arrival order**, plus cached quotes and a fill-listener list.
- **Market orders:** fill **immediately at the live quote** (BUY = ask, SELL = bid) — instant fill, not depth-matched.
- **Pending orders:** rest in the book; `on_tick()` walks the ticked symbol's book and fills triggered orders; unfillable stops stay resting.
- **Fill-price semantics are correct MT5 behaviour:**
  - BUY_LIMIT at `min(ask, limit)` when `ask <= limit`
  - SELL_LIMIT at `max(bid, limit)`
  - BUY/SELL_STOP at market once triggered, with `max_slippage_points` (**0 = unlimited**)
  - STOP_LIMIT arms, then caps at the limit
- **`_quote_for()` resolution order:** M7 client-quote provider (may raise `NoQuoteError`) → feed tick → cached quote → spread-derived mid around the order price → `NoQuoteError`.
- `cancel_order()` removes from the book; `modify_order()` is cancel/replace to preserve queue position.

**Status: PARTIAL** — correct MT5 fill semantics and a genuine resting book, but no price-time priority, no depth, and no client-vs-client netting.

### What the 19 reference engines actually teach

| Pattern | Source (code-evidenced) | Relevant to us? |
|---|---|---|
| **Pre-trade risk as an explicit gateway with typed denials** | Nautilus `crates/risk/src/engine/mod.rs:93-98`; C++ OMS `risk_engine.hpp:18-49` (`FAT_FINGER=1, POSITION_LIMIT=2, MARGIN=3, NOTIONAL=4`); ULL-FX `fx-risk/src/engine.rs:31-78` | ✅ **Yes** — maps 1:1 onto our `risk_service` + domain events |
| **Hold/reserve margin at accept, refund on reject** | exchange-core `RiskEngine.java:415` (`position.pendingHold`); matching-core `risk_engine.rs:188` (refund = size×hold price×scale + taker fee) | ✅ **Yes** — we already do the hold (m6 reservation); the refund path deserves verification |
| **Two-layer margin monitor — block if *either* layer says no** | C++ OMS `margin_monitor.hpp:15` ("if the local estimate says no margin we block even if REST says ok… if REST says no we block regardless") | ✅ **Yes** — genuinely better than trusting local math alone |
| **Order state machine + typed reject reasons + reduce-only clamp** | C++ OMS `oms_types.hpp:45-53`; Nautilus `validate_fill_for_order` (3187), `check_overfill` (3428), `is_duplicate_closed_fill` (3951) | ✅ **Yes** — our state enum is thinner; their duplicate-fill checks are worth porting |
| **Append-only event log + snapshot + tail-replay** | Nautilus `crates/event_store/src/lib.rs:18-23`, `kernel.rs`; exchange-core journal/snapshot (`DiskSerializationProcessor.java:67-79`) | ✅ **Yes** — we have `SqlEventStore` with **zero callers** |
| **Redis + Postgres as first-class optional backends** | Nautilus `crates/infrastructure/src/lib.rs:22-23,47-48` | ✅ **Yes** — validates our Redis+Postgres split as a real design, not a compromise |
| **LP quote modes: Streaming vs RFQ, venue score, last-look** | ULL-FX `crates/fx-lp/src/lp.rs:7-40`, `quote.rs`, `QuoteMode { Streaming, Rfq }` | ✅ **Yes** — the A-Book primitives we currently lack |
| **B-Book quote skewing + circuit breakers** | market-maker-rs (Avellaneda-Stoikov/GLFT spread, inventory skew, `RiskLimits.check_order`, `scale_order_size`) | ✅ Yes — for B-Book pricing sophistication |
| **RFQ state machine with guarded transitions** | otc-rfq `src/domain/value_objects/rfq_state.rs` (`can_transition_to`) | ✅ Yes — for dealer/OTC flows |
| **Order TTL: timer wheel synthesising CANCELED on timeout** | C++ OMS `TimerWheel` | ✅ Yes — LP order timeouts, cancel-and-replace |
| Lock-free ring buffers, LMAX Disruptor | exchange-core `ExchangeCore.java:54`; OMS-ULL SPSC rings | ❌ **No** — Python's GIL + asyncio cannot reproduce these. Keep only the *structural* idea: single writer per aggregate, shard by symbol |
| ART trees, object pools, SIMD, zero-GC, thread affinity, `alignas(64)` | exchange-core, matching-core, OMS-ULL | ❌ **No** — irrelevant at broker scale; correctness dominates |
| On-disk journal formats (LZ4 offsets, rkyv WAL, redb) | exchange-core, matching-core | ❌ **No** — replace with Postgres/Redis; only the *pattern* transfers |
| exchange-core's matching internals | `OrderBookDirectImpl.java:46-47` | ❌ Mostly no — a retail broker emulates fills from LP quotes. Only price-time-priority/FIFO *semantics* matter for B-Book simulation |
| kernel bypass (eBPF/XDP) | traderx (claim) | ❌ No |

### Source-quality corrections from the research

- **`trading-core-main` is not a matching engine** — it is a TypeScript quant/portfolio library (`applyFill`, `getAverageCost`, RollingZScore, RBTree). Useful only for position-accounting semantics.
- **`Broker-Dealer-main` is a docs + Next.js marketing site**, not a runnable engine (33 TS/TSX files, essentially all `page.tsx`). Claims only — nothing to port.
- **`traderx-main`** claims a "hybrid B-Book/A-Book router (10,109 lines)"; the actual file `packages/dealing-desk/src/hybrid_router.py` is **304 lines** — a **33× doc-vs-code discrepancy**. Treat its claims with suspicion.
- **`hurtrade`** is a real Java/RabbitMQ back-office system; its B-Book concepts (margin calls, account liquidation flag, cover accounts/positions) are in README + model classes only — no matching engine. Deep reading was blocked by Windows MAX_PATH.

> **Per the brief's own warning:** none of the above makes something an MT5 requirement. These are *engineering patterns*, and several would improve our system — but each needs its own justification.

---

## F. Infrastructure Analysis

### 🔴 Critical — verified twice

#### F1. Five security controls are runtime no-ops *(confirmed twice)*

`api/di_providers.py` defines getters — `get_rate_limiter()`, `get_token_blacklist()`, `get_totp_service()`, `get_ip_whitelist()`, `get_auth_service()` — that read from a **plain dict** (`_container`). They are all read-only getters:

```python
# api/di_providers.py:232-264
def get_rate_limiter() -> Any:      return _container.get("rate_limiter")
def get_token_blacklist() -> Any:   return _container.get("token_blacklist")
def get_totp_service() -> Any:      return _container.get("totp_service")
def get_ip_whitelist() -> Any:      return _container.get("ip_whitelist")
```

**Nothing ever registers those keys.** The only registration path is:

- `api/main.py:137` → `register_di_providers(container)` from `default_providers()` (`api/main.py:85-125`)
- which returns **16 persistence keys** (`di_setup.py:66-83`) + `event_bus` + `database`

A targeted regex for every assignment form (`["rate_limiter"] =`, `providers["…"] =`, `_container["…"] =`, `container.register(…)`) returned **zero hits** anywhere in the tree — including `scripts/`, `tests/`, `ops/`, `cli/`. The only constructions found are **test-only**.

Every consumer therefore short-circuits:

```python
# api/auth/dependencies.py:81-82
if not rate_limiter:
    return                    # ← the IP and per-login limit checks below are unreachable
```

**Impact:** 20 req/min per IP, 5 req/min per login, JWT revocation, TOTP and manager IP allow-listing **never execute in production**. The classes are complete and unit-tested (`tests/unit/security/test_security.py`), so **no test catches the missing wiring**. This is the most dangerous class of defect: present, tested, documented — and inert.

**Additional finding:** `api/auth/admin_dependencies.py:72-73` explicitly passes `token_blacklist=None` into `get_current_user`, so the admin plane bypasses the blacklist regardless of DI.

#### F2. Auth fabricates a funded account

```python
# api/auth/dependencies.py:47-68
login_id = str(payload.get("sub", "100001"))
login_num = int(login_id) if login_id.isdigit() else 100001
account = Account(
    ...,
    balance=Money(Decimal('10000.00'), "USD"),
    equity=Money(Decimal('10000.00'), "USD"),
    ...
    margin_free=Money(Decimal('10000.00'), "USD"),
)
```

A validly-signed JWT whose account row is absent yields a synthetic **$10,000** account labelled "fallback for dev/test". Used by `api/routers/account.py` (2 call sites) and `api/routers/trade.py` (4 call sites).

The sibling file bans this pattern explicitly: *"F2's lesson: `get_current_user` invents account 100001; this dependency never invents anything"* — the client plane does it anyway.

#### F3. Frontend fabricates data on the live path

```ts
// mt5-admin-web/src/services/transport/http.ts:876-893
relOrders.push({
    ticket: num(orderTicket),
    order_id: String(orderTicket),
    ...
    type: isSell ? 1 : 0,
    state: 'filled',
    ...
})
```

`getTradeOperation` fetches positions, deals, active orders and order history, correlates them by `position_id`, and then **synthesises order rows the backend never returned** — with a derived `type` code and a fabricated `state: 'filled'` rendered to the dealer as if it came from the API.

This directly contradicts `contract.ts:10-12` (*"The frontend performs NO domain logic… never a fabricated payload"*) and the README's non-negotiable rule.

### 🔴 Doc-vs-reality divergence

`docs/PERSISTENCE_HOT_COLD_SQL_AUDIT.md` claims **"Overall Compliance Score: 99.6% Spec Compliant"**, marking ClickHouse, Redis market-data caching and an event store as **"✅ Verified Fact"** and 18 tables as "✅ Fully Implemented".

Exhaustive construction/caller greps found:

| Component | Reality |
|---|---|
| `ClickHouseClient`, `ClickHouseTickRepository`, `ClickHouseBarRepository`, `TickPersistenceWorker` | Constructed **only** in `tests/unit/persistence/test_clickhouse_persistence.py` |
| `RedisMarketDataCache` | Constructed **only** in `tests/unit/domains/market_data/test_market_data.py:222`; `market_data_setup.py:30` imports it and never calls it |
| `SqlEventStore.append()` | **Zero callers repo-wide** |
| `RedisEventBus` | Stores nothing — Redis pub/sub retains no messages |

Meanwhile the API *honestly refuses*: `skeletons.py:653` ("bar aggregation and storage — the bars table has 0 rows…") and `:661` ("tick history storage (**ClickHouse decision pending**)").

**The contradiction is internal to the repo**, and the doc's own file links point at `file:///e:/references-for-AIs-to-read-main/qwe-agen-broker-platform-backend/work/bp/…` — **a different checkout**. The doc was not written against this tree.

### Other confirmed issues

| Issue | Evidence | Impact |
|---|---|---|
| **Wire timestamp discarded** | `trade_server_feed.py:55` defines `_ts_to_datetime`; `:177` uses `datetime.now(timezone.utc)` instead — the helper is **never called** | `_is_stale` computes `now − now ≈ 0 s`, so `MARKET_DATA_MAX_TICK_AGE_SECONDS` can **never fire** on the trade-server path — the exact "healthy, connected, useless feed" failure the guard's docstring warns about |
| **Test contradicts code** | `tests/unit/test_m10_trade_server_feed.py:103` asserts `tick.timestamp == datetime.fromtimestamp(1757577600.123)` — the **wire** value | Code and test cannot both be current. Which is stale: **UNKNOWN** (tests not run) |
| **trade-server has no auth** | Zero matches for `token\|Authorization\|api_key\|jwt\|Depends(` across all trade-server `.py` files | A live MT5 terminal is reachable by anyone who can reach the port. `/connect` accepts login+password in a plain POST body. CORS `allow_origins=["*"]` **with** `allow_credentials=True` |
| **Event bus has no durability** | `redis_event_bus.py` — `publish()` dispatches locally then `PUBLISH`; pub/sub retains nothing. Module docstring claims it "keeps the same information server-side" — **false** | Messages published while the reader is down are lost |
| **WS drops every ~60 s** | `D13-D15-REPORT.md:193-194` ("keepalive ping timeout — the trade-server does not answer pings"); still open in `PROJECT-STATE-v8.md:111`; repo-wide grep for `ws_ping\|ping_interval\|ping_timeout` returns **nothing** | Price stream for all subscribed symbols interrupts every ~60 s |
| **Redis URL logged with credentials** | `api/main.py:317` logs `redis_url` verbatim, bypassing the existing `_mask_url` / `mask_url` helpers *(confirmed twice)* | For `rediss://user:pass@…` this writes a secret into logs |
| **`PositionClosed` never reaches the client socket** | `event_bridge.py:126-128` — every other handler calls `await self._user_update(...)`; `_on_position_closed` only broadcasts to the manager path *(confirmed twice)* | A client's own book stays open after the close |
| **`/ws/stream` ignores subscriptions** | `endpoints.py` docstring says it processes them; the loop body is `await websocket.receive_text()` — text discarded. `broadcast_tick` sends every tick to every connection | No per-symbol fan-out; cost scales with connections × symbols |
| **`/ws/stream` unauthenticated, uncapped** | By design ("public tick stream"), but combined with F1 the public socket is the cheapest unbounded resource in the process | — |
| **`KEYS md:tick:*`** | `redis_market_data.py:59` *(confirmed twice)* | O(keyspace) blocking command on production Redis |
| **Ticket counters fall back to per-process memory** | `manager/trading.py:60-110` — Redis `INCR` with 1.5 s timeouts; on exception a module-global counter seeded from `MAX(ticket)` | Order/deal **ticket collisions** on a two-node deployment |
| **No cross-node coordination** | Grep for leader election / advisory lock / `SETNX` → **nothing** | Every periodic sweep runs on **both** nodes |
| **No DB-level locking** | No `with_for_update`, no `SKIP LOCKED`, no version column repo-wide | The per-account guard is a single-process `asyncio.Lock`; it does not survive a second process |
| **Concurrency tests prove less than they appear** | `tests/unit/concurrency/test_execution_concurrency.py` runs two deals through **mock** repositories inside `account_lock` | Proves the lock and the arithmetic — not database atomicity |
| **`order_service.py` is 0 bytes** | Verified | An empty OMS service module |
| **`010_sync_schema` undocumented** | Generic revision id (`c8f8333980f2`), empty docstring — unlike 001-009 which each state a "Why" | A future reader cannot tell what drifted. Also the newest change in the tree |
| **Redis reader task never disconnected** | `event_bus.disconnect()` exists and is unused in `api/main.py` shutdown | Left to loop teardown |
| **`InProcessEventBus` silently drops** | Events beyond dispatch depth 32 | Silent loss |
| **`IPWhitelistService.is_allowed`** | Returns `True` for an empty list — fail-open default | Defensible as MT5 semantics, but should be stated |
| **ClickHouse silent in-memory fallback** | `clickhouse_client.py` — connect failure logs a warning and writes to `_mock_tables`, which vanish on restart | "Writes succeeded, reads return nothing" — the F8 shape the project elsewhere bans. Impact nil while unwired |

### ✅ What's genuinely solid

- **`/health`** does real probes — `SELECT 1` with a 4 s timeout plus a bus ping — and answers **503** when degraded.
- **Migrations 001→010** form a contiguous, documented chain with sensible purposes (002 nullable price_current, 004 margin reservation, 005 password hash before which login was "authenticate-in-name-only", 008 reconciliation breaks with dedupe identity, 009 identity plane).
- **UnitOfWork** correctly binds all repositories to **one** session — the docstring names the prior factory-per-repo atomicity bug it fixes. Commits on success, rolls back on exception, raises if entered empty.
- **The surface-honesty gate** (`p1_proof_surface_completion`) is real and mechanical: `_refuse()` returns 501 with a `"NOT WIRED: …"` prefix, routes are flagged `x-not-wired`, and the proof asserts every flagged op answers 501 (never 200), every real GET answers only 200/404, seeded rows appear in seeded reads, and zero stray 501s. **The gate's logic is verified; the gate's current colour is not** (not run).
- **FIX layer** — simulated vs real boundary is explicit and enforced: `SimulatedFixSession` says plainly *"this is NOT a connection to a real LP… It moves no money"*; `QuickFixSession` fails loudly at construction without the native module. A missing execution report is `FixTimeout`, **never an assumed fill**. **MATCH**
- **Worker lifecycle** — overlap protection is structural: `ExpirationWorker.start()` is a single sequential loop that survives exceptions and sleeps after each sweep; `ValuationService.start()` guards re-entry. Shutdown stops components in order.
- **The MT5 config codec** — export **raises** rather than emitting something plausible; `Point` and `TickSize` protected; MarginCall/MarginStopOut treated as percent on both sides.
- **Fee/model honesty in trade-server** — `/api/symbols` returns `[]` when disconnected with the comment "no mock/SIM fallback".

### Worker / scheduler state

Workers start in the FastAPI lifespan: swap and expiration as `asyncio` tasks, `ValuationService.start()`, the tick ingestor, then the WebSocket bridge; liquidation and SL/TP are owned by the trading stack. Liquidation is wired (`api/main.py:686`) and subscribes to `StopOutEntered`. **Missing:** any cross-node coordination, and `event_bus.disconnect()` is never called.

---

## G. Reference-to-Code Mapping

| Our module | MT5 reference | Verdict |
|---|---|---|
| `core/domains/market_data/margin.py` | `Margin-Calculation-Basic.md`, `Margin.md`, symbol export | Faithful 4-stage implementation; only CalcMode 3 unimplemented |
| `core/domains/pricing/engine.py` + `a_book.py` + `translation.py` | `Spread-Commission-and-Swap.md`, group export | Correct spread/SpreadDiff precedence; markup measured vs raw quote; gateway `Translates` honoured (masks with `!`/`**` stored but skipped) |
| `core/domains/risk/engine.py` (conversion) | `Margin.md` §Converting into Deposit Currency | Side-aware (ASK for buy, BID for sell); triangulates over 7 majors; raises rather than guessing |
| `core/domains/oms/entities/*` | `IMTOrder`/`IMTDeal`/platform position accounting | Both modes correct; state enum thinner; deal immutability unresolved |
| `core/domains/ledger/engine.py` | — (MT5 balance operations) | Every mutation recorded with `balance_after`; no update/delete API; withdrawal guarded against negative — but no DB-level write-once |
| `core/domains/reconciliation/engine.py` | Not an MT5 concept (ours) | Real compare, 6 break kinds, severities, aging (`occurrences`/`last_seen`), and a **resolve path** exists (`repo.resolve(break_id, note)`, migration 008) |
| `infrastructure/mt5/codec.py` + `wire.py` | 14-section Administrator config JSON contract | Correctly identified as **config JSON, not the Manager binary DLL wire**; every scalar a string; per-field/per-record decimal scale |
| `api/routers/manager/*` (160 routes) | `swagger.json` (124 ops) | WebSockets 18/18, Subscriptions 11/11, Connection 4/4 exact; Trading 18 vs 7 and Main 74 vs 66 over-supplied; `liquidity`/`risk`/`routing` (6 routes) have **no swagger counterpart** — our own dialect |
| `infrastructure/feeds/trade_server_feed.py` | `MTTick` struct, `HookTick`, tick semantics | Protocol-compatible, correct fault model (`ConnectionError` on clean EOF → back off, not hot-loop) — **timestamp discarded** |
| `infrastructure/gateways/trade_server_gateway.py` | M11 outcomes | Maps 4 outcomes honestly; **no retries** because trade-server accepts no client order id |
| `application/workers/sltp_worker.py` | SL/TP inheritance | Correct Bid/Ask sides, SL before TP; LP-first on A-Book and refuses local close if LP refuses |
| `infrastructure/fix/*` | FIX 4.4 | Message set coherent; documented exclusions are exactly what 4.4 cannot carry |

---

## H. GAP / PARTIAL / UNKNOWN Findings

### 🔴 GAP

| # | Finding | Evidence |
|---|---|---|
| 1 | Rate limiter, token blacklist, 2FA, IP whitelist — **built, never registered** | `di_providers.py:232-264`; `main.py:85-137`; `di_setup.py:66-83` *(confirmed twice)* |
| 2 | Auth invents a $10,000 account (client plane) | `dependencies.py:47-68` |
| 3 | Frontend fabricates order rows on the live path | `http.ts:876-893` |
| 4 | Filling modes (FOK/IOC/Return) entirely absent | no filling-mode logic found |
| 5 | Stop-out never fired live | `PROJECT-STATE-v4…v8` all state it |
| 6 | ~19 of ~25 MT5 pre-trade checks missing (6 present) | `M16-REPORT.md:349-350` |
| 7 | Hot/cold split non-functional — ClickHouse test-only, `SqlEventStore` unused | construction greps |
| 8 | Event bus durability — none | `redis_event_bus.py` |
| 9 | trade-server — zero authentication | zero auth matches across its `.py` files |
| 10 | `CalcMode 3` (CFD index) raises | `margin.py` |
| 11 | Expiration: only `SPECIFIED` mode | `expiration_worker.py` |
| 12 | A-Book close doesn't unwind the hedge | `PROJECT-STATE-v4…v8`; `trade_server_gateway.py:435` |
| 13 | Internal partial fills impossible | `book_matching_engine.price_order()` |
| 14 | `/ws/stream` ignores subscriptions it advertises | `api/websockets/endpoints.py` |
| 15 | `ClickHouseClient` degrades silently to a process-local dict | `clickhouse_client.py` |
| 16 | No cross-node coordination (workers, ticket counters, locks) | greps for leader election/advisory lock/SETNX |

### 🟠 PARTIAL

| # | Finding |
|---|---|
| 17 | Matching engine — real resting book, not a CLOB; no depth, no client-vs-client netting |
| 18 | Order state coverage thinner than MT5's 10 states |
| 19 | Deal immutability — convention (new-object construction), not a storage constraint |
| 20 | Ledger — no mutation API, but no DB-level write-once |
| 21 | Reconciliation — no automatic hedge repair |
| 22 | Manager API fidelity — per-operation coverage unenumerated |
| 23 | UoW coverage — blanket atomicity claim unconfirmed |
| 24 | Concurrency — in-process locks only; doesn't survive a second process |
| 25 | Margin recalc fallback silently substitutes a simplified formula (no currency conversion, no CalcMode) |
| 26 | Frontend — 50/62 live methods, but "live" ≠ honest |
| 27 | trade-server — no server-side MT5 reconnect; 20 Hz shared poll, ~50-symbol cap |
| 28 | `010_sync_schema` undocumented |
| 29 | Leverage tier / floating margin profiles not modelled |

### ⚪ UNKNOWN

| # | Finding | Why unknown |
|---|---|---|
| 30 | Whether the **test** or the **code** is stale (`test_m10_trade_server_feed.py`) | Needs one `pytest` run |
| 31 | Whether M18 actually landed | `ENDPOINT-CATALOG.md` is a self-labelled **"DRAFT for user approval"**, dated 2026-09-14, Part 4 titled *M18 FINAL SCOPE* — a plan, not a status report |
| 32 | `TradePanel.tsx` (930 lines) — the "zero domain logic" claim | File body not read |
| 33 | `test_wire_codec.py` fixture provenance — real-server or synthesised? | `tests/fixtures/` contains only one file (`managers_rights_tctrader_live.json`) |
| 34 | docker-compose service definitions; manager WS auth | Tool budget |
| 35 | Contest / Coverage account types | Corpus silent |
| 36 | All gate colours (pass/fail) | **Nothing was executed** |
| 37 | Exact `evaluate_margin_state()` comparison body; `swap_worker.py` body | Not read |

---

## I. Important Architectural Risks

1. **Security controls that look present and do nothing.** The most dangerous class of bug: the code exists, is unit-tested, is documented — and never runs. A test suite cannot catch missing wiring. (F1)

2. **Documentation certifying unwired infrastructure.** A reader trusting the audit doc will size the system assuming time-series storage, audit trails and quote caching are live. They are not. This is an *internal contradiction* — the API's own skeletons say the opposite. (F5)

3. **Two-node topology with single-node guarantees.** The Redis bus exists to enable a second node; per-account locks, ticket counters, and periodic workers all assume one. Ticket collisions and duplicate sweeps follow.

4. **Honesty drift.** The project's best cultural feature is *"refuse honestly"* — but the frontend fabricates rows and the auth layer fabricates accounts. The discipline exists at the API surface and erodes at its edges.

5. **The deal-immutability conflict is unresolved.** Building an OMS on a premise the reference SDK contradicts is a design risk that compounds.

6. **Freshness guard silently defeated** on the live data path — a "healthy, connected, useless feed" failure the guard's own docstring warns about. (C1)

7. **An undocumented migration at the head of the chain.** `010_sync_schema` is the newest change in the tree and the least documented.

8. **The corpus does not document the retail Python SDK.** trade-server depends on an API this corpus cannot verify.

---

## J. Missing Capabilities

**Trading**
filling modes (FOK/IOC/Return) · partial fills · DAY/EOD expiration · CalcMode 3 · dealer requote/confirm · manager-on-behalf-of (B1) · trade-modification HTTP surface · tick history/stat/chart · DOM/book · symbol-group overrides · allocations · stop-out compensation path.

**Risk**
~19 pre-trade checks (stop-level distance, position/order-count limits, hedge prohibition, FIFO close, spread checks) · second-layer margin reconciliation · automatic hedge repair · stop-out live firing.

**Infrastructure**
durable event log · leader election · cross-node locking · real hot/cold split · per-symbol WS fan-out · WS keepalive policy · MT5 terminal reconnect · trade-server authentication · secret redaction in logs · `SCAN` instead of `KEYS`.

**Process**
per-operation manager-API fidelity map · migration 010 documentation · fixture provenance record · frontend test runner (none configured).

---

## K. Recommended Investigation Areas

Ordered by risk-reduction per unit of effort.

| # | Action | Why |
|---|---|---|
| 1 | **Wire the security adapters** — or make a missing limiter a startup failure | Highest value, smallest change; the project's own fail-closed rule already points this way |
| 2 | **Fix the auth fallback** — 401 instead of a fabricated account | Removes a phantom-money path |
| 3 | **Run one `pytest`** to settle the code-vs-test contradiction on the feed timestamp | One command resolves an UNKNOWN |
| 4 | **Fix or delete the fabrication in `http.ts::getTradeOperation`**, then read `TradePanel.tsx` for the same pattern | Restores the headline honesty contract |
| 5 | **Reconcile the audit docs with reality** — wire ClickHouse/cache/event-store or downgrade their statuses | Removes a false mental model |
| 6 | **Decide deal immutability** against the SDK evidence | Prerequisite for hardening the OMS |
| 7 | **Establish a baseline gate run** — nothing in this session was executed | No one currently knows the true pass/fail state |
| 8 | **Two-node readiness review** — ticket counters, worker coordination, lock scope | The bus enables a topology the code doesn't support |
| 9 | **Consider the two-layer margin monitor** (C++ OMS pattern) | Block if either layer says no — cheap insurance |
| 10 | **Consider the Nautilus duplicate-fill checks** (`validate_fill_for_order`, `check_overfill`, `is_duplicate_closed_fill`) | Directly portable; prevents double-applied fills |

> **Do NOT implement any recommendation as part of this analysis.** This is an analysis document only.

---

## L. Evidence / Source Table

| # | Claim | Source | Confidence |
|---|---|---|---|
| 1 | Security adapters never registered | `api/di_providers.py:232-264`; `api/main.py:85-137`; `di_setup.py:66-83`; independent re-verification | **High** — static, confirmed twice |
| 2 | Auth fabricates $10,000 account | `api/auth/dependencies.py:47-68` | **High** — read directly |
| 3 | Frontend fabricates order rows | `http.ts:876-893` | **High** — read directly |
| 4 | ClickHouse/cache/event-store unwired | Construction greps; `skeletons.py:653,661` contradict the audit doc | **High** |
| 5 | Wire timestamp discarded | `trade_server_feed.py:55` vs `:177` | **High** |
| 6 | Test contradicts code | `tests/unit/test_m10_trade_server_feed.py:103` | **High** (which is stale: UNKNOWN) |
| 7 | trade-server has no auth | Zero `token\|jwt\|Depends(` matches across its `.py` files | **High** |
| 8 | Event bus not durable | `redis_event_bus.py` pub/sub; `event_store.py` zero callers | **High** |
| 9 | `/ws/stream` drops subscriptions | `api/websockets/endpoints.py` | **High** |
| 10 | `PositionClosed` missing from user socket | `event_bridge.py:126-128` | **High** — confirmed twice |
| 11 | Redis URL logged w/ credentials | `api/main.py:317` | **High** — confirmed twice |
| 12 | `KEYS md:tick:*` | `redis_market_data.py:59` | **High** — confirmed twice |
| 13 | `order_service.py` empty | 0 bytes | **High** |
| 14 | Margin is MT5-faithful | `margin.py` vs `Margin-Calculation-Basic.md` | **High** |
| 15 | Stop-out never fired | `PROJECT-STATE-v4…v8` all state it | **High** — documented, not re-run |
| 16 | 19/25 pre-trade checks missing | `M16-REPORT.md:349-350` | **Medium** — documented |
| 17 | MT5 Web API = 231 commands / 44 families | `Web-API.md` | **High** |
| 18 | mtapi = 124 operations, family counts | `mtapi-docs/swagger.json` | **High** |
| 19 | 93 paths / 116 ops / 34 skeletons | `M18-REPORT.md:7,100,117` | **Medium** — documented |
| 20 | Endpoint catalog dispositions | `docs/ENDPOINT-CATALOG.md` | **Medium** — self-labelled pre-M18 DRAFT |
| 21 | Backend engine patterns | Nautilus / exchange-core / C++ OMS / ULL-FX / otc-rfq source | **High** — code-read |
| 22 | `traderx` doc-vs-code 33× gap | 10,109 claimed vs 304 actual lines | **High** |
| 23 | Deal immutability unresolved | `IMTDeal/ModificationFlags.md` vs `code files/3 oms.md` | **High** — conflict confirmed |
| 24 | Retail Python SDK undocumented in corpus | `symbol_select`/`copy_ticks_*` absent from vendor trees | **High** |
| 25 | Margin call / stop-out are percent | `Groups TCTrader-Live.json`; `Margin.md` | **High** |
| 26 | Volume scaling 10⁴ / 10⁸ | `IMTConSymbol/VolumeMinExt.md`; export (100 → 1,000,000) | **High** |
| 27 | Point ≠ TickSize on 131/362 symbols | `Point.md`, `TickSize.md`; export | **High** |
| 28 | Order states = 10 values | `IMTOrder/Enumerations.md#enorderstate` | **High** |
| 29 | Filling modes / policy table | `Fill-Policy.md`; `#enfillingflags`; `#enorderfilling` | **High** |
| 30 | Stop-out removal order | `Accounts-with-Margin-CallStop-Out.md` | **High** |
| 31 | Group = 47 fields | `Groups TCTrader-Live.json` | **High** |
| 32 | Symbol = 121 fields, 362 symbols | `Symbols TCTrader-Live.json` | **High** |
| 33 | Surfaces/docs/gates stated | `docs/ENDPOINT-CATALOG.md` Part 5 | **Medium** — the rule, not its enforcement |

---

## Scope, Method and Disclosure

### Read-only guarantee

No source code, configuration, migration, test or reference file was modified, created, deleted or renamed.

### Process disclosure

To work around PowerShell quoting limits, one investigator briefly created and then **removed** a temporary helper script (`_tmp_enums.py`) in the reference corpus's parent directory. It was verified absent afterward — no `_tmp*` file exists anywhere outside a vendored `.venv`. Net project state is unchanged, but it should be on record.

### What was NOT done

- **Nothing was executed.** No test suite, no lint, no proof script, no `git status`. Every status above is from reading source. All gate results remain unverified.
- Files not read: `TradePanel.tsx` (930 L), `MarketWatchPage.tsx`, `application/commands/modify_deal.py`, `core/domains/oms/entities/deal.py`, `ledger/models.py`, `application/commands/record_deal.py`, `reconciliation_service.py`, `swap_worker.py` bodies, `evaluate_margin_state()` body, docker-compose service lists, `api/routers/manager/websockets.py`.
- No per-operation enumeration of the 124 mtapi operations.
- UoW coverage was not enumerated across write paths.

### How to read the statuses

| Status | Means |
|---|---|
| **MATCH** | Our implementation appears consistent with the reference |
| **PARTIAL** | Implemented, but incomplete or materially different |
| **GAP** | An expected capability appears missing |
| **UNKNOWN** | Insufficient evidence — stated as such rather than guessed |

---

**Document status:** generated by GLM AutoClaw, 2026-09-29. Analysis only — no recommendations implemented. This document should be updated when the architecture materially changes or when the gates are actually run.
