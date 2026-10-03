# Match-Trade Technologies — Bridge & RMS Feature Summary
> Scraped from: https://docs.match-trade.com/docs/crm-prop-features-admin-guide/
> Date: 2026-08-18
> Purpose: Reference for designing our own broker backend, particularly A/B-Book routing, RMS, and bridge connectivity.

---

## 1. What Match-Trade Provides (as a Third-Party Bridge)

Match-Trade is a **white-label broker technology provider** that offers:

| Product | Description |
|---|---|
| **MT5/MT4 Bridge** | Connects MT5 server to external LPs. Handles A/B-book routing. No MT5 plugin needed. |
| **RMS (Risk Management System)** | Real-time exposure monitoring, hedge rules, coverage ratios |
| **Match-Trader Platform** | Proprietary trading terminal (alternative to MT5 client) |
| **Client Office / CRM** | Back-office: KYC, deposits, IB commissions, prop challenge management |
| **Admin API** | REST API for brokers to programmatically manage accounts, groups, positions |

---

## 2. A-Book / B-Book Routing (What Their Bridge Does)

### A-Book Configuration:
- Broker defines rules per: **Group**, **Account**, **Symbol**
- Coverage ratio: 1:1 (full hedge) or partial (e.g., 50%)
- Coverage weight: priority order across multiple LPs
- Can hedge selectively per instrument or volume threshold

### B-Book Configuration:
- Broker acts as **market-maker / counterparty**
- Internal trade processor: fills orders at broker's own price
- No LP involvement

### Hybrid (most common):
- Small retail traders → B-Book
- Profitable traders / large volume → switch to A-Book
- Rules engine triggers the switch automatically

---

## 3. RMS Features (What Their RMS Does)

| Feature | Description |
|---|---|
| Real-time exposure monitoring | Shows broker's net delta per symbol across all B-book accounts |
| Hedge threshold alerts | Notify when net exposure exceeds configured limit |
| Auto-hedging | Automatically routes excess exposure to LP (partial A-book) |
| P&L simulation | "A-Book simulation" report: what would P&L have been if everything was A-booked |
| Multiple LP management | Route to different LPs based on symbol/rules |
| Bridge Manager UI | Web UI for managing data feeds, spreads, routing rules |

---

## 4. CRM / Client Office Features

| Feature | Description |
|---|---|
| KYC onboarding | Document upload, approval workflow |
| Deposit/Withdrawal | Multiple payment gateways, automated processing |
| IB (Introducing Broker) | Multi-level commission structures |
| Prop Trading Challenges | Challenge configuration, daily loss limits, profit targets |
| Automated phase progression | Challenge pass/fail triggers automatically |
| Trader dashboard | Real-time account targets, drawdown monitoring |

---

## 5. What We Can Use vs. What We Build Ourselves

| Component | Use Match-Trade (3rd party)? | Build ourselves? |
|---|---|---|
| MT5 Bridge connectivity | ✅ YES (if connected to MT5) | Later: build our own FIX gateway |
| A/B-book routing engine | Build ourselves (we understand the logic) | ✅ YES — simple rule table |
| RMS basic (margin/stop-out) | Build ourselves | ✅ YES |
| RMS advanced (auto-hedging, exposure) | Use Match-Trade or OnceZero bridge | As addon later |
| CRM / Client Portal | 3rd party initially (or VFI_Backend) | Build later |
| Prop trading features | Match-Trade or standalone prop system | Future |

---

## 6. Key Takeaway for Our Architecture

The Match-Trade bridge model teaches us:
1. **The bridge is a SEPARATE service** — it sits between MT5 (trade server) and LPs. We replicate this as our **Gateway Service**.
2. **RMS is not IN the trade server** — it runs separately, reads trades, and sends hedge orders. We replicate this as our **RMS Service**.
3. **Admin API is first-class** — everything configurable via API. We must build our Admin REST API from day 1.
4. **The bridge manager is a web UI** — we will build an Admin Dashboard on top of our Admin API.

---

## 7. Related Third-Party Bridge Providers for Reference

| Provider | Key Feature |
|---|---|
| **Match-Trade** | Bridge + RMS + CRM, MT4/MT5 |
| **B2Broker / B2Core** | Liquidity aggregation, white-label |
| **OnceZero** | AI-driven B-book risk management |
| **Condroid** | Hedge management, analytics |
| **Your Bourse** | MT4/MT5 bridge, cloud-based RMS |
| **Tools for Brokers** | Bridge + reporting, plugin-based |

> All of these do essentially what we are building: they sit between the MT5/trade server and the LPs, and apply routing/risk rules. Our backend IS the trade server + bridge combined.
