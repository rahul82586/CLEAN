// Symbol field schema — the single source of truth for the Symbol editor's forms.
//
// WHY THIS EXISTS
//
// Every symbol tab previously declared its own field list and its own dropdown
// options in TypeScript:
//
//     TradeTab.tsx      const CALC_MODES = ['Forex', 'Forex No Leverage', ...]
//     ExecutionTab.tsx  four execution modes inline
//     SwapsTab.tsx      const SWAP_TYPES = [...]; const DAYS_IN_YEAR = [360,365,366]
//     CommonTab.tsx     digits 0-5 and DOM depth as literal <option> elements
//
// So a backend change was always a two-repo change, and the option lists could
// drift from what the API actually accepts. Worse, the Quotes tab had no list at
// all and rendered a stale default object.
//
// The backend now serves the descriptors (GET /admin/symbols/schema, generated
// from the MT5 fieldmap so it cannot drift), and this module is the only place the
// UI reads them from.
import { useEffect, useState } from 'react';
import { API } from '../../../services/api';

/** One field descriptor, exactly as the backend serves it. */
export interface SymbolFieldSchema {
    /** JSON key on GET /admin/symbols/{name}. */
    field: string;
    /** The exact MT5 wire name, or null for our own additions. */
    mt5?: string | null;
    type: 'string' | 'int' | 'decimal' | 'flags' | 'enum' | 'bool' | 'sessions' | 'nested' | 'datetime';
    /** The MT5 Administrator symbol-dialog tab this field sits on. */
    tab?: string;
    /** points | seconds | minutes | lots | days | percent ... */
    unit?: string;
    /** Domain enum name, expanded into enum_values below. */
    enum?: string;
    /** The members of `enum`, expanded server-side from the domain code. */
    enum_values?: Array<{ name: string; value: number | string }>;
    /** SymbolModel column, or null when the value lives in mt5_extra. */
    column?: string | null;
    /** Key inside mt5_extra, for a column-less field. */
    json_key?: string | null;
    /** True when the domain entity exposes the value. */
    modelled?: boolean;
    /** True when PUT /admin/symbols/{name} accepts it today. */
    writable?: boolean;
    /** True when the value is computed and never stored (e.g. Multiply). */
    derived?: boolean;
    right?: string;
    description?: string;
}

export interface SymbolSchema {
    object: string;
    wire_section?: string;
    fields: SymbolFieldSchema[];
}

interface SchemaState {
    schema: SymbolSchema | null;
    loading: boolean;
    error: string | null;
}

// Module-level cache: the schema is identical for every symbol and every mount, so
// the editor fetches it once per session instead of on each tab switch.
let cached: SymbolSchema | null = null;
let inflight: Promise<SymbolSchema> | null = null;

function loadSchema(): Promise<SymbolSchema> {
    if (cached) return Promise.resolve(cached);
    if (!inflight) {
        const pending: Promise<SymbolSchema> = API.getSymbolSchema()
            .then((raw: any) => {
                cached = raw as SymbolSchema;
                inflight = null;
                return cached;
            })
            .catch((err: unknown) => {
                inflight = null;
                throw err;
            });
        inflight = pending;
    }
    return inflight;
}

/** Test/reset hook — lets a screen force a re-read after a backend change. */
export function resetSymbolSchemaCache(): void {
    cached = null;
    inflight = null;
}

export function useSymbolSchema(): SchemaState {
    const [state, setState] = useState<SchemaState>(() =>
        cached ? { schema: cached, loading: false, error: null }
               : { schema: null, loading: true, error: null });

    useEffect(() => {
        if (cached) return;
        let cancelled = false;
        loadSchema()
            .then(schema => { if (!cancelled) setState({ schema, loading: false, error: null }); })
            .catch(err => {
                if (!cancelled) {
                    setState({
                        schema: null,
                        loading: false,
                        error: err?.message ?? String(err),
                    });
                }
            });
        return () => { cancelled = true; };
    }, []);

    return state;
}

/** The fields on one tab, in declaration order. */
export function fieldsForTab(schema: SymbolSchema | null, tab: string): SymbolFieldSchema[] {
    if (!schema?.fields) return [];
    return schema.fields.filter(f => f.tab === tab);
}

/**
 * A dropdown's options for an enum-backed field, straight from the server.
 *
 * Returns [] when the field has no enum, which is the honest answer — the caller
 * then renders a plain input rather than an empty select.
 *
 * Note the labels come from the MT5 member names (FOREX, CFD_LEVERAGE, ...) rather
 * than a hand-written friendly string. That is deliberate: a friendly label is
 * exactly the kind of thing that drifts from the value it claims to describe, and
 * the member name at least matches the wire. A local label map is layered on top
 * in `labelFor` below where a human-readable form genuinely helps.
 */
export function enumOptions(field: SymbolFieldSchema): Array<{ value: number | string; label: string }> {
    const values = field.enum_values;
    if (!values || values.length === 0) return [];
    return values.map(v => ({ value: v.value, label: labelFor(field, v.name) }));
}

// Human-readable labels for the MT5 enum members an operator actually sees. Kept
// as a lookup rather than as a list of options, so a member added to the domain
// enum still appears (under its raw name) instead of vanishing.
const ENUM_LABELS: Record<string, string> = {
    // CalculationMode — MT5's Trade tab wording.
    FOREX: 'Forex',
    FOREX_NO_LEVERAGE: 'Forex No Leverage',
    CFD: 'CFD',
    CFD_INDEX: 'CFD Index',
    CFD_LEVERAGE: 'CFD Leverage',
    FUTURES: 'Futures',
    EXCHANGE_STOCKS: 'Exchange Stocks',
    EXCHANGE_STOCKS_MOEX: 'Exchange MOEX Stocks',
    EXCHANGE_BONDS: 'Exchange Bonds',
    EXCHANGE_BONDS_MOEX: 'Exchange MOEX Bonds',
    EXCHANGE_FUTURES: 'Exchange Futures',
    EXCHANGE_FUTURES_FORTS: 'Exchange FORTS Futures',
    EXCHANGE_OPTIONS: 'Exchange Option',
    EXCHANGE_OPTIONS_MARGIN: 'Exchange Margin Option',
    SERV_COLLATERAL: 'Collateral',
    // TradeMode.
    DISABLED: 'Disabled (no trading)',
    LONGONLY: 'Long only (buys allowed)',
    SHORTONLY: 'Short only (sells allowed)',
    CLOSEONLY: 'Close only (liquidation only)',
    FULL: 'Full access (long & short)',
    // ExecutionMode.
    REQUEST: 'Request Execution',
    INSTANT: 'Instant Execution',
    MARKET: 'Market Execution',
    EXCHANGE: 'Exchange Execution',
    // GTCMode.
    GTC: 'Good till canceled',
    DAILY: 'Good till today including SL/TP',
    DAILY_NO_STOPS: 'Good till today excluding SL/TP',
    // TickFlags.
    REALTIME: 'Allow real-time quotes from data feeds',
    COLLECTRAW: 'Save raw, unfiltered ticks',
    FEED_STATS: 'Receive market statistics from data feeds',
    NEGATIVE_PRICES: 'Allow negative prices (futures only)',
    // MarginFlags.
    CHECK_PROCESS: 'Check before executing orders',
    CHECK_SLTP: 'Check on SL-TP trigger',
    // SwapFlags / RequestFlags / InstantFlags / TradeFlags.
    CONSIDER_HOLIDAYS: 'Automatically consider holidays',
    ORDER: 'Additional confirmation mode',
    FAST_CONFIRMATION: 'Fast confirmation of requotes',
    PROFIT_BY_MARKET: 'Convert profit by market',
    ALLOW_SIGNALS: 'Enable trading signals',
    // SymbolSwapDays.
    SUNDAY: 'Sunday', MONDAY: 'Monday', TUESDAY: 'Tuesday', WEDNESDAY: 'Wednesday',
    THURSDAY: 'Thursday', FRIDAY: 'Friday', SATURDAY: 'Saturday',
    // SymbolChartMode.
    BID_PRICE: 'By bid price', LAST_PRICE: 'By last price', OLD: 'Legacy (bid)',
    // SymbolSpliceType.
    NONE: 'No splicing', UNADJUSTED: 'Unadjusted', ADJUSTED: 'Adjusted',
    // SwapMode — MT5's Swaps tab wording.
    POINTS: 'In points',
    SYMBOL_CURRENCY: 'In money, base currency',
    MARGIN_CURRENCY: 'In money, margin currency',
    GROUP_CURRENCY: 'In money, group currency',
    INTEREST_CURRENT: 'In percent, using current price',
    INTEREST_OPEN: 'In percent, using open price',
    REOPEN_CLOSE_PRICE: 'By reopening positions, close price',
    REOPEN_BID: 'By reopening positions, bid price',
    PROFIT_CURRENCY: 'In money, profit currency',
};

/** A display label for an enum member, falling back to the member name. */
export function labelFor(field: SymbolFieldSchema, memberName: string): string {
    if (field.enum === 'CalculationMode') return ENUM_LABELS[memberName] ?? memberName;
    return ENUM_LABELS[memberName] ?? memberName;
}

/** Fallback label map for enum members that are shared across several enums. */
export function labelForValue(memberName: string): string {
    return ENUM_LABELS[memberName] ?? memberName;
}

/**
 * Read a field's value from a symbol-detail payload.
 *
 * The API spreads modelled fields across the top level and the column-less ones
 * under `fields` / `extra`, so a getter has to look in both. Centralised here so
 * each tab does not reinvent the fallback order.
 */
export function readField(detail: any, field: SymbolFieldSchema): unknown {
    if (!detail) return undefined;
    if (field.field in detail) return detail[field.field];
    const fromFields = detail.fields?.[field.field];
    if (fromFields !== undefined) return fromFields;
    // Column-less fields are also exposed under the raw MT5 wire name in `extra`.
    if (field.mt5 && detail.extra?.[field.mt5] !== undefined) return detail.extra[field.mt5];
    return undefined;
}

/** Flags as a set of set-bit names, for checkbox rendering. */
export function flagsToNames(field: SymbolFieldSchema, value: unknown): Set<string> {
    const mask = Number(value ?? 0);
    const out = new Set<string>();
    for (const member of field.enum_values ?? []) {
        const bit = Number(member.value);
        // A zero-valued member (NONE) is not a "set bit" and must not be ticked.
        if (bit !== 0 && (mask & bit) === bit) out.add(member.name);
    }
    return out;
}

/** Set-bit names back to the integer mask the API stores. */
export function namesToFlags(field: SymbolFieldSchema, names: Set<string>): number {
    let mask = 0;
    for (const member of field.enum_values ?? []) {
        if (names.has(member.name)) mask |= Number(member.value);
    }
    return mask;
}
