// Trade-tab field visibility, by MT5 calculation mode.
//
// WHY THIS IS ITS OWN MODULE
//
// The Trade tab shows different fields depending on the Calculation mode, and that
// rule was previously expressed as one inline `isForex` check that gated exactly one
// field. Two of the rules are load-bearing and were wrong or missing:
//
//   * Tick size / Tick value are shown only for NON-Forex modes. Trade.md: the two
//     are "used for calculating profit, margin and swaps for CFD Index and Futures" -
//     and the live export confirms it, carrying TickValue = 0 on every FOREX and
//     FOREX_NO_LEVERAGE symbol.
//   * Convert profit is shown only for Forex. Trade.md: "this option is available
//     only for the Forex type symbols."
//
// Everything else - Contract size, Calculation, Trade mode, GTC, Filling, Expiration,
// Orders, Limit & stop level, Freeze level, Max quote delay and all four volume
// bounds - is shown for every mode.
//
// The mode is carried to the UI as a LABEL ("CFD Leverage"), because that is what the
// draft and the Calculation dropdown use. Matching therefore goes through the label,
// and the enum name is accepted too so a value arriving from the API resolves either
// way.

/** A Calculation mode, as either the dialog label or the MT5 enum member name. */
export type CalcModeLike = string | number | null | undefined;

/** MT5 EnCalcMode values, for when the API sends the integer. */
const CALC_MODE_NUMBERS: Record<string, number> = {
    forex: 0,
    futures: 1,
    cfd: 2,
    cfdindex: 3,
    cfdleverage: 4,
    forexholeverage: 5, // placeholder, replaced below
};

/** The Forex family: mode 0 and mode 5 only. */
const FOREX_MODES = new Set(['FOREX', 'FOREX_NO_LEVERAGE']);

/**
 * Normalise any spelling of a calculation mode to its MT5 enum member name.
 *
 * Accepts "Forex No Leverage", "FOREX_NO_LEVERAGE", "forex no leverage" and the
 * integer 5 - all four reach this function in practice, because the draft holds the
 * label from the dropdown, the API returns the integer, and a schema-derived option
 * can carry the member name.
 */
export function normaliseCalcMode(mode: CalcModeLike): string {
    if (mode === null || mode === undefined) return '';
    if (typeof mode === 'number') {
        switch (mode) {
            case 0: return 'FOREX';
            case 1: return 'FUTURES';
            case 2: return 'CFD';
            case 3: return 'CFD_INDEX';
            case 4: return 'CFD_LEVERAGE';
            case 5: return 'FOREX_NO_LEVERAGE';
            case 32: return 'EXCHANGE_STOCKS';
            case 33: return 'EXCHANGE_FUTURES';
            case 34: return 'EXCHANGE_FUTURES_FORTS';
            case 35: return 'EXCHANGE_OPTIONS';
            case 36: return 'EXCHANGE_OPTIONS_MARGIN';
            case 37: return 'EXCHANGE_BONDS';
            case 38: return 'EXCHANGE_STOCKS_MOEX';
            case 39: return 'EXCHANGE_BONDS_MOEX';
            case 64: return 'SERV_COLLATERAL';
            default: return '';
        }
    }

    const raw = String(mode).trim();
    if (/^-?\d+$/.test(raw)) return normaliseCalcMode(Number(raw));

    // "Exchange MOEX Stocks" -> EXCHANGE_MOEX_STOCKS; "CFD Leverage" -> CFD_LEVERAGE.
    const upper = raw.toUpperCase().replace(/[\s-]+/g, '_');

    // The enum's own spelling wins when it matches exactly.
    if (FOREX_MODES.has(upper)) return upper;

    // Otherwise match on the words, ignoring order and singular/plural, so the
    // dialog label and the enum name resolve to the same mode:
    //   label "Exchange MOEX Bonds"  <-> enum EXCHANGE_BONDS_MOEX
    //   label "Exchange Margin Option" <-> enum EXCHANGE_OPTIONS_MARGIN
    const words = sortWords(upper);
    for (const member of KNOWN_MODES) {
        const memberUpper = member.toUpperCase();
        if (memberUpper === upper) return memberUpper;
        if (sortWords(memberUpper) === words) return memberUpper;
    }
    return upper;
}

function sortWords(value: string): string {
    return value
        .split('_')
        .filter(Boolean)
        .map(w => (w.endsWith('S') && w.length > 1 ? w.slice(0, -1) : w))
        .sort()
        .join('_');
}

/** Every mode MT5 defines, so the word-matching above has a target set. */
const KNOWN_MODES = [
    'FOREX', 'FUTURES', 'CFD', 'CFD_INDEX', 'CFD_LEVERAGE', 'FOREX_NO_LEVERAGE',
    'EXCHANGE_STOCKS', 'EXCHANGE_FUTURES', 'EXCHANGE_FUTURES_FORTS',
    'EXCHANGE_OPTIONS', 'EXCHANGE_OPTIONS_MARGIN', 'EXCHANGE_BONDS',
    'EXCHANGE_STOCKS_MOEX', 'EXCHANGE_BONDS_MOEX', 'SERV_COLLATERAL',
];

/** True for Forex and Forex No Leverage - the only two modes with the Forex rules. */
export function isForexFamily(mode: CalcModeLike): boolean {
    return FOREX_MODES.has(normaliseCalcMode(mode));
}

/**
 * Tick size and Tick value.
 *
 * Hidden for Forex and Forex No Leverage, shown for every other mode. The values are
 * still STORED and still round-trip; MT5 hides the inputs, it does not reject the
 * fields, so hiding here must not clear them.
 */
export function showsTickSizeAndValue(mode: CalcModeLike): boolean {
    return !isForexFamily(mode);
}

/** Convert profit: "available only for the Forex type symbols." */
export function showsConvertProfit(mode: CalcModeLike): boolean {
    return isForexFamily(mode);
}

/**
 * The futures-only price fields (Settlement / Minimum / Maximum).
 *
 * These live on the separate Futures tab, which MT5 shows for the two futures
 * modes; the predicate is here so the two places agree on the rule.
 */
export function showsFuturesPrices(mode: CalcModeLike): boolean {
    const normalised = normaliseCalcMode(mode);
    return normalised === 'EXCHANGE_FUTURES' || normalised === 'EXCHANGE_FUTURES_FORTS';
}

/** The Options tab appears only for the exchange options modes. */
export function showsOptionFields(mode: CalcModeLike): boolean {
    const normalised = normaliseCalcMode(mode);
    return normalised === 'EXCHANGE_OPTIONS' || normalised === 'EXCHANGE_OPTIONS_MARGIN';
}

/** The Bonds tab appears only for the exchange bond modes. */
export function showsBondFields(mode: CalcModeLike): boolean {
    const normalised = normaliseCalcMode(mode);
    return normalised === 'EXCHANGE_BONDS' || normalised === 'EXCHANGE_BONDS_MOEX';
}

/**
 * Collateral instruments are not tradable: MT5 says "the margin and profit are not
 * calculated" for them, so the trading-parameter fields are meaningless.
 */
export function isCollateral(mode: CalcModeLike): boolean {
    return normaliseCalcMode(mode) === 'SERV_COLLATERAL';
}
