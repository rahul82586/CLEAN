"""Account entity - Trading state & financials (IMTAccount)."""
from dataclasses import InitVar, dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict, List, Optional

from core.domains.common.value_objects import Money
from core.domains.identity.rights import (
    MT5_USER_RIGHT_DEFAULT,
    UserRight,
)

#: Margin level used when an account has no margin in use. Percent scale, matching
#: MT5's own "no margin" display. Comparisons against real thresholds must treat this
#: as "unlimited", never as a number to be exceeded.
MARGIN_LEVEL_UNLIMITED = Decimal('999999')
#: MT5's own margin thresholds, in PERCENT, from the live export
#: (`MarginCall "50.00"`, `MarginStopOut "30.00"`).
#:
#: R11: these existed as FIVE different literals - the dataclass defaulted to 80/50 while the
#: loader, the mapper and the live export all said 50/30. An account whose group failed to load
#: was therefore stopped out at 50% instead of 30%, keeping it trading 20 percentage points past
#: the configured floor. Falling back to a MORE PERMISSIVE number is the wrong direction for a
#: risk system, so there is now exactly one definition and every site reads it.
from .enums import AccountType, SOActivation, FreeMarginMode
from .thresholds import (
    DEFAULT_MARGIN_CALL_LEVEL,
    DEFAULT_STOP_OUT_LEVEL,
)
from .value_objects import StopOutSnapshot
from .group import Group


@dataclass
class Account:
    """
    Account Entity - Trading State & Financials (IMTAccount)
    
    Represents a trading account linked to a Client and Group.
    """
    # Identity
    login: int = 0
    client_id: str = ""
    group_id: str = ""
    group_name: str = ""
    group: Optional[Group] = None
    
    # Type
    account_type: AccountType = AccountType.REAL
    currency: str = "USD"
    currency_digits: int = 2
    
    # Leverage (can override Group's leverage)
    leverage: Optional[int] = None
    
    # Financial state (Money value objects)
    balance: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    credit: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    equity: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    margin_used: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    margin_free: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    #: M6: margin held for in-flight (approved, not yet filled) orders. Counts
    #: against free margin in the pre-trade check; released exactly on fill or
    #: rejection via orders.reserved_margin.
    margin_reserved: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    margin_level: Decimal = field(default_factory=lambda: Decimal('0'))
    
    # Floating values
    profit: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    storage: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    commission: Money = field(default_factory=lambda: Money(Decimal('0'), "USD"))
    
    # Stop-out state machine
    so_activation: SOActivation = SOActivation.NONE
    so_time: Optional[datetime] = None
    so_level: Optional[Decimal] = None
    so_equity: Optional[Money] = None
    so_margin: Optional[Money] = None
    
    # Flags
    #: IMTUser::Rights - the account's own 18-bit permission mask. This is the
    #: SINGLE AUTHORITY for "may this account connect / trade / use EAs / ...".
    #: `is_enabled` below is a derived view of the ENABLED bit, not a second
    #: stored fact: two independent booleans for one MT5 bit is exactly the
    #: D1/D8b/D13/D16 class (a value written in one place, read from another).
    rights: UserRight = field(default_factory=lambda: MT5_USER_RIGHT_DEFAULT)
    #: Constructor-only mirror of the ENABLED bit, so `Account(is_enabled=False)`
    #: keeps working. It is NOT a stored field: see __post_init__. When both
    #: `rights` and `is_enabled` are supplied, the explicit `is_enabled` wins for
    #: that one bit and the rest of the mask is kept as given.
    is_enabled: InitVar[Optional[bool]] = None
    is_online: bool = False
    last_login: Optional[datetime] = None
    #: Argon2 hash of the trading password (MT5 IMTAccount::m_password main).
    #: The domain stores ONLY the hash - never the plaintext. Empty means
    #: "not yet provisioned": login refuses it rather than allowing it, because
    #: before M6 there was no password check at all and any caller who named an
    #: existing login_id was issued a token for that account.
    password_hash: str = ""
    
    # UI
    color_tag: Optional[str] = None
    dealer_notes: str = ""

    # ------------------------------------------------------------------
    # IMTUser identity surface (plan step 5). Every field below has a column
    # added by migration 009_identity_plane AND a mapper in both directions -
    # declared together, never one without the other, because a model column
    # with no mapper support is a full-row save() waiting to blank it (D8b).
    # Names in comments are the SDK accessors, which are also the MT5 export
    # wire names.
    # ------------------------------------------------------------------
    #: IMTUser::FirstName / LastName / MiddleName. MT5 stores the three parts
    #: separately; `Name()` is the composed display name, not a fourth field.
    first_name: str = ""
    last_name: str = ""
    middle_name: str = ""
    #: IMTUser::Company
    company: str = ""
    #: IMTUser::Country / State / City / ZIPCode / Address
    country: str = ""
    state: str = ""
    city: str = ""
    zip_code: str = ""
    address: str = ""
    #: IMTUser::Phone / EMail. The guide: EMail is comma-separated, 63 chars total.
    phone: str = ""
    email: str = ""
    #: IMTUser::Language - a WinAPI LANGID on the wire. Stored as the language
    #: tag string ("en") because that is what the rest of the platform and the
    #: UI speak; the codec owns any LANGID translation.
    language: str = "en"
    #: IMTUser::Status - the Account tab's RE (resident) / NR (non-resident).
    #: A STRING on the wire (LPCWSTR), not an int. See ResidencyStatus.
    residency_status: str = ""
    #: IMTUser::ID - "additional ID": passport / TIN / national id.
    id_number: str = ""
    #: IMTUser::LeadSource / LeadCampaign
    lead_source: str = ""
    lead_campaign: str = ""
    #: IMTUser::MQID - the MetaQuotes ID push notifications are addressed to.
    mqid: str = ""
    #: Finteza Visitor ID (guide, Overview tab). Not an IMTUser member; it is
    #: carried by the platform when a Finteza subscription is active.
    visitor_id: str = ""
    #: IMTUser::Comment
    comment: str = ""
    #: IMTUser::Color - COLORREF, exported by MT5 as AABBGGRR. 0xFF000000 means
    #: "transparent"/no colour, 0x00xxxxxx is opaque. Stored as the raw int; the
    #: UI formats it. Kept SEPARATE from the dealer's free-form `color_tag`.
    color: Optional[int] = None
    #: IMTUser::Agent - the agent (IB) account that earns agent commission on
    #: this account's deals.
    agent_login: Optional[int] = None
    #: IMTUser::Account - "external system account (exchange, ECN, etc)". The
    #: Account tab labels it "Bank account"; migration 009's column is
    #: `bank_account`, so that name is kept and this comment is the mapping.
    bank_account: str = ""
    #: IMTUser::InterestRate - accumulated interest on the account.
    interest_rate: Decimal = field(default_factory=lambda: Decimal("0"))
    #: IMTUser::LimitOrders - open-orders limit. NULL means INHERIT THE GROUP;
    #: 0 means "no orders allowed", which is a different thing. The guide: when
    #: both account and group set a limit, THE STRICTER ONE WINS.
    limit_orders: Optional[int] = None
    #: IMTUser::LimitPositionsValue - see ACCOUNT-GROUP-CREATION-SPEC §2c for
    #: the exact per-symbol buy-vs-sell difference algorithm. NULL = inherit.
    limit_positions_value: Optional[Decimal] = None
    #: IMTUser::PhonePassword / the investor and Web-API passwords. MT5 puts all
    #: per-account password material on IMTUser, NOT on the person - one client
    #: with a demo and a real account has two investor passwords. These three
    #: therefore live here, and the copies on Client are legacy (step 5 makes
    #: this side the writer; see client.py).
    investor_password_hash: str = ""
    phone_password_hash: str = ""
    webapi_password_hash: str = ""
    #: IMTUser::OTPSecret - 16 chars, binds exactly one generator.
    otp_secret: Optional[str] = None
    #: IMTUser::CertSerialNumber
    cert_serial_number: Optional[int] = None
    #: IMTUser::LastIP - "last access time and address data is updated once per
    #: hour" (guide, Overview tab).
    last_ip: str = ""
    #: IMTUser::LastPassChange. Changing a password RESETS the account's
    #: connection to the trade server, so this is also "when were they dropped".
    last_pass_change: Optional[datetime] = None
    
    # Dates
    registration_date: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    
    def __post_init__(self, is_enabled: Optional[bool]) -> None:
        """Reconcile the InitVar `is_enabled` into the rights mask.

        `rights` is the only stored fact. A caller that passes `is_enabled`
        gets that one bit set or cleared on the mask; everything else in the
        mask is left exactly as supplied. Coercing an int/str through
        UserRight.from_flags keeps a raw bigint read off the wire honest - and
        from_flags REFUSES bits outside IMTUser::EnUsersRights rather than
        silently masking them, which is the project's design law.
        """
        if not isinstance(self.rights, UserRight):
            self.rights = UserRight.from_flags(self.rights)
        if is_enabled is None:
            return
        if is_enabled:
            self.rights = self.rights | UserRight.ENABLED
        else:
            self.rights = self.rights & ~UserRight.ENABLED

    # --- derived views of the rights mask -----------------------------------
    #
    # These are PROPERTIES, not fields: the mask is the one writer. Before step 5
    # `is_enabled` was an independent bool column, so an account could be
    # "enabled" while its rights said otherwise, and nothing reconciled them.

    @property
    def is_enabled(self) -> bool:
        """USER_RIGHT_ENABLED - may this account connect at all."""
        return bool(self.rights & UserRight.ENABLED)

    @is_enabled.setter
    def is_enabled(self, value: bool) -> None:
        self.rights = (
            self.rights | UserRight.ENABLED
            if value
            else self.rights & ~UserRight.ENABLED
        )

    @property
    def trading_disabled(self) -> bool:
        """USER_RIGHT_TRADE_DISABLED - INVERTED sense, straight from the SDK.

        The guide is explicit that disabling an account or its trading does NOT
        cancel pending orders or SL/TP (they may already be at an external
        system), but Stop Out IS skipped for a disabled account, because
        stop-out is the broker's own internal risk tool.
        """
        return bool(self.rights & UserRight.TRADE_DISABLED)

    @property
    def may_trade(self) -> bool:
        """The mask's own answer to "can this account place an order".

        Distinct from can_trade(), which additionally consults the group and
        the session. Both must pass; this one is the per-account bit.
        """
        return self.is_enabled and not self.trading_disabled

    @property
    def must_change_password(self) -> bool:
        """USER_RIGHT_RESET_PASS - "change password at next login"."""
        return bool(self.rights & UserRight.RESET_PASS)

    @must_change_password.setter
    def must_change_password(self, value: bool) -> None:
        self.rights = (
            self.rights | UserRight.RESET_PASS
            if value
            else self.rights & ~UserRight.RESET_PASS
        )

    @property
    def is_technical(self) -> bool:
        """USER_RIGHT_TECHNICAL - hidden from regular managers.

        This is the bit migration 009's partial index exposes:
        `idx_accounts_rights_technical ... WHERE (rights & 65536) <> 0`.
        """
        return bool(self.rights & UserRight.TECHNICAL)

    @property
    def is_investor_session(self) -> bool:
        """USER_RIGHT_INVESTOR - set on a session logged in with the investor
        password; such a session cannot trade."""
        return bool(self.rights & UserRight.INVESTOR)

    def has_right(self, right: UserRight) -> bool:
        return bool(self.rights & right)

    def display_name(self) -> str:
        """IMTUser::Name - MT5 composes it from the three name parts."""
        parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(p for p in (str(x).strip() for x in parts) if p)

    def effective_limit_orders(self, group_limit: Optional[int]) -> Optional[int]:
        """The stricter of the account and group limits wins; NULL = unlimited.

        Guide, Limits tab: "Limit number of active orders" falls back to the
        group when unset, and when both are set the stricter one applies.
        0 is a real limit meaning "none allowed" - it is NOT the same as NULL,
        which is why both stay Optional all the way down.
        """
        mine, theirs = self.limit_orders, group_limit
        candidates = [int(v) for v in (mine, theirs) if v is not None]
        return min(candidates) if candidates else None

    def effective_leverage(self, symbol: Any = None) -> int:
        """THE effective leverage for this account. One resolver, for every caller.

        Semantics: the account's own leverage is the BASE, the group's
        ``leverage_default`` is the FALLBACK when the account has none, and the group's
        ``leverage_max`` is a CAP applied on top. The cap is the part that was missing.

        ``leverage_default`` is NOT a cap. Folding it into the same ``min()`` as the
        maximum gives ``min(1000, 100, 500) = 100`` where MT5 gives 500, and would silently
        charge five times the intended margin on every account whose leverage sits above
        the group default.

        The previous version ignored ``leverage_max`` entirely while the pre-trade gate
        applied it, so the gate and the book disagreed by 10x: ``margin_used`` understated,
        ``margin_level`` overstated, and stop-out late or never. Group
        ``leverage_max = 500`` is the seeded default, so this was the ordinary case.

        Two resolvers will always eventually disagree, so this is the ONLY one:
        ``PreTradeRiskService._resolve_leverage`` delegates here.

        ``symbol`` is accepted for a future per-symbol cap and is deliberately NOT read
        from a ``leverage_max`` attribute today - ``Symbol`` has no such field, and the old
        code's read of it could never fire. A branch that looks like protection it does not
        provide is worse than no branch at all.
        """
        margin = getattr(self.group, "margin", None)

        base = 0
        if self.leverage is not None and self.leverage > 0:
            base = int(self.leverage)
        else:
            default = getattr(margin, "leverage_default", 0) or 0
            if default > 0:
                base = int(default)

        if base <= 0:
            base = 100

        maximum = getattr(margin, "leverage_max", 0) or 0
        if maximum > 0:
            return min(base, int(maximum))
        return base
    
    def recompute_margin_level(self) -> Decimal:
        """Recompute margin level as a PERCENT, and store it.

        This is the ONLY place the margin level formula lives. It used to be written
        out by hand in seven different modules, five of which computed a ratio
        (equity / margin) and two of which computed a percent (ratio * 100), while the
        thresholds they were compared against were stored both ways. That is how an
        account at 40% margin level came to report no margin call and no stop-out.

        MT5's convention is percent: the live server export carries
        ``MarginCall: "50.00"`` and ``MarginStopOut: "30.00"``, and ``MarginSOMode: 0``
        is ``STOPOUT_PERCENT``. Group thresholds are therefore percent too.

        With no margin used there is no meaningful level, so we return the sentinel
        ``MARGIN_LEVEL_UNLIMITED`` rather than zero - zero would read as "fully
        exhausted" and trigger an immediate stop-out on an account with no positions.
        """
        if self.margin_used.amount <= Decimal('0'):
            self.margin_level = MARGIN_LEVEL_UNLIMITED
        else:
            self.margin_level = (self.equity.amount / self.margin_used.amount) * Decimal('100')
        return self.margin_level

    def recompute_free_margin(self, unrealized_pnl: Optional[Money] = None) -> None:
        """THE free-margin rule. ONE home, honouring the group's FreeMarginMode.

        R15/R19 consolidation. This ladder existed in `update_equity`, while the rest
        of the codebase wrote `equity - margin_used` by hand at more than a dozen call
        sites - each ignoring the group's mode. A broker that bills margin differently
        per group cannot have two answers for the same account, so every caller now
        points here.

        `unrealized_pnl` is consulted only by the PROFIT and LOSS modes; a caller
        without one passes None, which those modes read as zero.
        """
        pnl_amount = unrealized_pnl.amount if unrealized_pnl is not None else Decimal("0")
        used = self.margin_used.amount

    # Update free margin based on Group's free_margin_mode
        if self.group:
            mode = self.group.margin.free_margin_mode
            if mode == FreeMarginMode.USE_PL:
                self.margin_free = Money(
                    self.equity.amount - self.margin_used.amount,
                    self.currency
                )
            elif mode == FreeMarginMode.NOT_USE_PL:
                self.margin_free = Money(
                    self.balance.amount + self.credit.amount - self.margin_used.amount,
                    self.currency
                )
            elif mode == FreeMarginMode.PROFIT:
                pnl_amount = max(pnl_amount, Decimal('0'))
                self.margin_free = Money(
                    self.balance.amount + self.credit.amount + pnl_amount - self.margin_used.amount,
                    self.currency
                )
            elif mode == FreeMarginMode.LOSS:
                loss_amount = min(pnl_amount, Decimal('0'))
                self.margin_free = Money(
                    self.balance.amount + self.credit.amount + loss_amount - self.margin_used.amount,
                    self.currency
                )
        else:
            self.margin_free = Money(
                self.equity.amount - self.margin_used.amount,
                self.currency
            )

    # R19: delegate. This inlined the SAME formula as `recompute_margin_level`,
    # contradicting that method's own docstring ("This is the ONLY place the margin
    # level formula lives"). Two copies inside one entity is how they drift.

    def update_equity(self, unrealized_pnl: Money) -> None:
        """Update equity, free margin and margin level from an unrealised PnL.

        NOTE ON `margin_reserved` (audit R19): this deliberately does NOT subtract the
        reserved hold. `PreTradeRiskService` computes `available = margin_free -
        margin_reserved` when it gates an order, so subtracting it here as well would
        count the SAME hold twice and refuse orders the account can actually afford. The
        entity keeps `margin_free` free of the hold; the GATE applies it once, and
        `reserve_margin`'s SQL applies it again atomically at the database.

        The MARGIN LEVEL is delegated to `recompute_margin_level()` rather than re-derived
        here, so the formula has exactly one home.
        """
        self.profit = unrealized_pnl
        self.equity = Money(
            self.balance.amount + self.credit.amount + unrealized_pnl.amount,
            self.currency
        )
        
        # R19: the FreeMarginMode ladder has ONE home.
        self.recompute_free_margin(unrealized_pnl)
        self.recompute_margin_level()
    
    def evaluate_margin_state(self) -> List[Dict[str, Any]]:
        """
        Evaluate margin state and return list of events to emit.
        Implements the MT5 Stop-Out state machine.
        """
        events = []
        
        if not self.group:
            return events
        
        margin_call_level = self.group.margin.margin_call_level
        stop_out_level = self.group.margin.stop_out_level
        
        # Check if we should enter margin call
        if self.so_activation == SOActivation.NONE:
            if self.margin_level < margin_call_level:
                self.so_activation = SOActivation.MARGIN_CALL
                events.append({
                    "event_type": "MarginCallEntered",
                    "account_login": self.login,
                    "margin_level": str(self.margin_level),
                    "timestamp": datetime.now(timezone.utc).isoformat()
                })
        
        # Check if we should exit margin call
        elif self.so_activation == SOActivation.MARGIN_CALL:
            if self.margin_level >= margin_call_level:
                self.so_activation = SOActivation.NONE
                events.append({
                    "event_type": "MarginCallExited",
                    "account_login": self.login,
                    "margin_level": str(self.margin_level),
                    "timestamp": datetime.now(timezone.utc).isoformat()
                })
            
            # Check if we should enter stop-out
            elif self.margin_level < stop_out_level:
                self.so_activation = SOActivation.STOP_OUT
                self.so_time = datetime.now(timezone.utc)
                self.so_level = self.margin_level
                self.so_equity = self.equity
                self.so_margin = self.margin_used
                
                events.append({
                    "event_type": "StopOutEntered",
                    "account_login": self.login,
                    "margin_level": str(self.margin_level),
                    "equity": str(self.equity.amount),
                    "margin": str(self.margin_used.amount),
                    "timestamp": self.so_time.isoformat()
                })
        
        # Check if we should exit stop-out
        elif self.so_activation == SOActivation.STOP_OUT:
            if self.margin_level >= stop_out_level:
                self.so_activation = SOActivation.NONE
                events.append({
                    "event_type": "StopOutExited",
                    "account_login": self.login,
                    "margin_level": str(self.margin_level),
                    "timestamp": datetime.now(timezone.utc).isoformat()
                })
        
        return events
    
    def can_trade(self) -> bool:
        """Check if account is enabled and group allows trading.

        Reads the RIGHTS MASK, not a separate bool: USER_RIGHT_ENABLED must be
        set and USER_RIGHT_TRADE_DISABLED must not be. An investor-password
        session (USER_RIGHT_INVESTOR) can never trade either.
        """
        if not self.may_trade:
            return False
        if self.is_investor_session:
            return False
        if self.group and not self.group.can_trade():
            return False
        return True
    
    def can_open_position(
        self,
        symbol: str,
        volume: Decimal,
        required_margin: Money
    ) -> tuple:
        """Check if account can open a position."""
        if not self.is_enabled:
            return False, "Account is disabled"
        
        if not self.group:
            return False, "No group assigned"
        
        if not self.group.can_trade():
            return False, "Trading not allowed for this account"
        
        if not self.group.is_symbol_allowed(symbol):
            return False, f"Symbol {symbol} not allowed for this account"
        
        if required_margin.amount > self.margin_free.amount:
            return False, "Insufficient free margin"
        
        return True, "OK"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert account to dictionary."""
        return {
            "login": self.login,
            "client_id": self.client_id,
            "group_id": self.group_id,
            "group_name": self.group.name if self.group else None,
            "account_type": self.account_type.value,
            "currency": self.currency,
            "currency_digits": self.currency_digits,
            "leverage": self.effective_leverage(),
            "balance": str(self.balance.amount),
            "credit": str(self.credit.amount),
            "equity": str(self.equity.amount),
            "margin_used": str(self.margin_used.amount),
            "margin_free": str(self.margin_free.amount),
            "margin_level": str(self.margin_level),
            "profit": str(self.profit.amount),
            "storage": str(self.storage.amount),
            "commission": str(self.commission.amount),
            "so_activation": self.so_activation.name,
            "so_time": self.so_time.isoformat() if self.so_time else None,
            "so_level": str(self.so_level) if self.so_level else None,
            "is_enabled": self.is_enabled,
            "rights": int(self.rights),
            "rights_names": sorted(
                m.name for m in UserRight if m.value and m in self.rights
            ),
            "trading_disabled": self.trading_disabled,
            "must_change_password": self.must_change_password,
            "is_technical": self.is_technical,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "middle_name": self.middle_name,
            "display_name": self.display_name(),
            "company": self.company,
            "country": self.country,
            "state": self.state,
            "city": self.city,
            "zip_code": self.zip_code,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "language": self.language,
            "residency_status": self.residency_status,
            "id_number": self.id_number,
            "lead_source": self.lead_source,
            "lead_campaign": self.lead_campaign,
            "mqid": self.mqid,
            "visitor_id": self.visitor_id,
            "comment": self.comment,
            "color": self.color,
            "agent_login": self.agent_login,
            "bank_account": self.bank_account,
            "interest_rate": str(self.interest_rate),
            # NULL is meaningful here (inherit the group) so it is NOT coerced.
            "limit_orders": self.limit_orders,
            "limit_positions_value": (
                str(self.limit_positions_value)
                if self.limit_positions_value is not None
                else None
            ),
            "cert_serial_number": self.cert_serial_number,
            "last_ip": self.last_ip,
            "last_pass_change": (
                self.last_pass_change.isoformat() if self.last_pass_change else None
            ),
            "is_online": self.is_online,
            "color_tag": self.color_tag,
            "dealer_notes": self.dealer_notes,
            "registration_date": self.registration_date.isoformat(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }