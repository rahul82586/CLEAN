/**
 * Live WebSocket Market Data & User Events Streaming Service
 *
 * Real-time low-latency WebSocket connection to the backend (/ws/stream and /ws/user).
 * Replaces HTTP polling for live quotes, price flashes, and instant trade/margin updates.
 */
import { getSettings } from '../../store/settingsStore';
import type { Ticks } from './contract';

type TickCallback = (ticks: Ticks) => void;
type UserUpdateCallback = (eventType: string, data: any) => void;

function resolveWsUrl(endpointPath: string): string {
    const { baseUrl } = getSettings();
    if (!baseUrl) {
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        return `${protocol}//${window.location.host}${endpointPath}`;
    }
    if (baseUrl.startsWith('http://') || baseUrl.startsWith('https://')) {
        return baseUrl.replace(/^http/, 'ws').replace(/\/$/, '') + endpointPath;
    }
    if (baseUrl.startsWith('ws://') || baseUrl.startsWith('wss://')) {
        return baseUrl.replace(/\/$/, '') + endpointPath;
    }
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const cleanBase = baseUrl.startsWith('/') ? baseUrl : `/${baseUrl}`;
    return `${protocol}//${window.location.host}${cleanBase.replace(/\/$/, '')}${endpointPath}`;
}

class WebSocketStreamService {
    private ws: WebSocket | null = null;
    private tickListeners: Set<TickCallback> = new Set();
    private isConnecting = false;
    private reconnectTimer: any = null;

    private userWs: WebSocket | null = null;
    private userListeners: Set<UserUpdateCallback> = new Set();
    private userToken: string | null = null;

    /** Subscribe to real-time market data quotes (/ws/stream) */
    subscribeTicks(callback: TickCallback): () => void {
        this.tickListeners.add(callback);
        if (!this.ws && !this.isConnecting) {
            this.connectPublicStream();
        }
        return () => {
            this.tickListeners.delete(callback);
            if (this.tickListeners.size === 0 && this.ws) {
                this.ws.close();
                this.ws = null;
            }
        };
    }

    /** Connect to unauthenticated /ws/stream */
    private connectPublicStream() {
        const wsUrl = resolveWsUrl('/ws/stream');
        this.isConnecting = true;

        try {
            this.ws = new WebSocket(wsUrl);

            this.ws.onopen = () => {
                this.isConnecting = false;
                if (this.reconnectTimer) clearTimeout(this.reconnectTimer);
            };

            this.ws.onmessage = (event) => {
                try {
                    const data = JSON.parse(event.data);
                    const ticksMap: Ticks = {};

                    if (data.type === 'tick' && data.symbol) {
                        ticksMap[data.symbol] = this.parseTick(data);
                    } else if (data.type === 'ticks' && Array.isArray(data.ticks)) {
                        for (const item of data.ticks) {
                            if (item.symbol) {
                                ticksMap[item.symbol] = this.parseTick(item);
                            }
                        }
                    }

                    if (Object.keys(ticksMap).length > 0) {
                        for (const listener of this.tickListeners) {
                            listener(ticksMap);
                        }
                    }
                } catch (err) {
                    console.error('[WS] Failed to parse tick frame:', err);
                }
            };

            this.ws.onerror = (err) => {
                console.warn('[WS] Stream error:', err);
            };

            this.ws.onclose = () => {
                this.ws = null;
                this.isConnecting = false;
                if (this.tickListeners.size > 0) {
                    this.reconnectTimer = setTimeout(() => this.connectPublicStream(), 2000);
                }
            };
        } catch (e) {
            this.isConnecting = false;
            console.error('[WS] Could not instantiate WebSocket:', e);
        }
    }

    private parseTick(raw: any) {
        const bid = raw.bid != null ? Number(raw.bid) : (null as unknown as number);
        const ask = raw.ask != null ? Number(raw.ask) : (null as unknown as number);
        const spread = raw.spread != null ? Number(raw.spread) : (bid && ask ? ask - bid : undefined);
        let age = 0;
        if (raw.ts) {
            age = (Date.now() - Number(raw.ts)) / 1000.0;
        }
        return {
            bid,
            ask,
            spread,
            age: age > 0 ? age : 0,
            marketState: 'open' as const,
            isMarketOpen: true,
            isTickStale: false,
        };
    }

    /** Subscribe to private user trade/margin updates (/ws/user) */
    subscribeUserUpdates(token: string, callback: UserUpdateCallback): () => void {
        this.userToken = token;
        this.userListeners.add(callback);
        if (!this.userWs) {
            this.connectUserStream();
        }
        return () => {
            this.userListeners.delete(callback);
            if (this.userListeners.size === 0 && this.userWs) {
                this.userWs.close();
                this.userWs = null;
            }
        };
    }

    private connectUserStream() {
        if (!this.userToken) return;
        const wsUrl = resolveWsUrl('/ws/user');

        try {
            this.userWs = new WebSocket(wsUrl);

            this.userWs.onopen = () => {
                // Send first-message auth
                if (this.userWs && this.userToken) {
                    this.userWs.send(JSON.stringify({ action: 'auth', token: this.userToken }));
                }
            };

            this.userWs.onmessage = (event) => {
                try {
                    const data = JSON.parse(event.data);
                    if (data.type && data.data) {
                        for (const listener of this.userListeners) {
                            listener(data.type, data.data);
                        }
                    }
                } catch (err) {
                    console.error('[WS] Failed to parse user stream frame:', err);
                }
            };

            this.userWs.onclose = () => {
                this.userWs = null;
                if (this.userListeners.size > 0) {
                    setTimeout(() => this.connectUserStream(), 3000);
                }
            };
        } catch (e) {
            console.error('[WS] Failed to connect user stream:', e);
        }
    }
}

export const wsStreamService = new WebSocketStreamService();
