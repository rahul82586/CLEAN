// MT5 symbol session model — shared by the Sessions tab and its day editor.
//
// WHY THIS FILE EXISTS
//
// The draft model used `{ start: string, end: string }` with `'24:00'` as the
// end-of-day seed, and bound both ends straight to `<input type="time">`.
//
// HTML time inputs accept 00:00–23:59. `24:00` is not a legal value, so the
// browser DISCARDS it and the field falls back to showing 12:00 AM — the
// reported "it always goes to 12:00". And because MT5 genuinely represents
// end-of-day as 1440 minutes, clamping to 23:59 would silently shorten every
// full-day session by one minute.
//
// So the model keeps MINUTES (0..1440, the same unit MT5 stores), which makes
// 1440 fully representable, and the DOM conversion happens only at the two edges
// where a native time input is involved.

/** One session range, in the same unit MT5 stores: minutes from midnight. */
export interface SessionRange {
    /** Minutes from midnight, 0..1440. */
    open: number;
    /**
     * Minutes from midnight, 0..1440.
     * 1440 is END OF DAY and is a real, distinct value — not 23:59.
     */
    close: number;
}

/** Minutes in a day. MT5's own end-of-day sentinel. */
export const END_OF_DAY = 1440;

/** MT5's weekday order is SUNDAY-FIRST (index 0 = Sunday). */
export const MT5_DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                         'Thursday', 'Friday', 'Saturday'] as const;

/** The order the Sessions tab lists them in, which is Monday-first. */
export const DISPLAY_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                             'Friday', 'Saturday', 'Sunday'] as const;

export type DayName = typeof DISPLAY_DAYS[number];

/** Display day name -> MT5's index. */
export function mt5DayIndex(day: DayName): number {
    return MT5_DAYS.indexOf(day as any);
}

/** Minutes -> "HH:MM", where 1440 renders as the literal "24:00". */
export function minutesToLabel(minutes: number): string {
    const clamped = Math.max(0, Math.min(END_OF_DAY, Math.round(minutes)));
    const h = Math.floor(clamped / 60);
    const m = clamped % 60;
    return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}`;
}

/** "HH:MM" (or "24:00") -> minutes. Returns null when it is not a time. */
export function labelToMinutes(label: string): number | null {
    const match = /^(\d{1,2}):(\d{2})$/.exec((label || '').trim());
    if (!match) return null;
    const h = Number(match[1]);
    const m = Number(match[2]);
    if (m > 59 || h > 24) return null;
    const total = h * 60 + m;
    return total > END_OF_DAY ? null : total;
}

/**
 * Minutes -> the value a native `<input type="time">` can actually hold.
 *
 * 1440 has no legal representation, so it renders as 23:59. This is a DISPLAY
 * ONLY conversion: the model keeps 1440, and the "= end of day" hint beside the
 * field tells the operator what 23:59 means here. Writing the picker's value
 * back to the model would be the bug this whole module exists to prevent.
 */
export function minutesToTimeInput(minutes: number): string {
    const clamped = Math.max(0, Math.min(1439, Math.round(minutes)));
    return minutesToLabel(clamped);
}

/** True when this range spans the whole day (used to label the hint). */
export function isFullDay(range: SessionRange): boolean {
    return range.open === 0 && range.close === END_OF_DAY;
}

/**
 * The `session_hours` string the backend accepts:
 *   "MON,00:00-24:00;TUE,08:00-17:00"
 *
 * Only days with at least one range are emitted; an omitted day is closed, which
 * is exactly how MT5 reads an empty session array.
 */
export function toSessionHours(
    schedules: Record<string, { quotes: SessionRange[]; trade: SessionRange[]; separateTrade: boolean }>,
): string {
    const parts: string[] = [];
    for (const day of DISPLAY_DAYS) {
        const sched = schedules[day];
        if (!sched) continue;
        const ranges = sched.separateTrade ? sched.trade : sched.quotes;
        if (!ranges || ranges.length === 0) continue;
        const rendered = ranges
            .map(r => `${minutesToLabel(r.open)}-${minutesToLabel(r.close)}`)
            .join(',');
        parts.push(`${day.substring(0, 3).toUpperCase()},${rendered}`);
    }
    return parts.join(';');
}

/** Parse the backend's `session_hours` string back into per-day ranges. */
export function fromSessionHours(
    hours: string,
): Record<string, SessionRange[]> {
    const out: Record<string, SessionRange[]> = {};
    for (const chunk of (hours || '').split(';')) {
        const [dayPart, rangesPart] = chunk.split(',');
        if (!dayPart || !rangesPart) continue;
        const key = dayPart.trim().toUpperCase();
        const day = DISPLAY_DAYS.find(d => d.substring(0, 3).toUpperCase() === key);
        if (!day) continue;
        const ranges: SessionRange[] = [];
        for (const pair of rangesPart.split(',')) {
            const [start, end] = pair.split('-');
            const open = labelToMinutes(start || '');
            const close = labelToMinutes(end || '');
            if (open === null || close === null) continue;
            ranges.push({ open, close });
        }
        out[day] = ranges;
    }
    return out;
}

/** A full trading week — the default a new symbol starts from, as MT5 does. */
export function defaultWeek(): Record<string, SessionRange[]> {
    const out: Record<string, SessionRange[]> = {};
    for (const day of DISPLAY_DAYS) {
        // The weekend is closed, as on every real FX server.
        out[day] = (day === 'Saturday' || day === 'Sunday')
            ? []
            : [{ open: 0, close: END_OF_DAY }];
    }
    return out;
}
