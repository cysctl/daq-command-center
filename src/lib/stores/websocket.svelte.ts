import { satellitesStore } from './satellites.svelte.ts';
import { telemetryStore } from './telemetry.svelte.ts';
import { logStore } from './logs.svelte.ts';

export class WebSocketStore {
	ws = $state<WebSocket | null>(null);
	isConnected = $state(false);
	isConnecting = $state(false);
	error = $state<string | null>(null);
	clientId = $state<string>('-');
	heartbeat = $state<string>('-');

	connect(host: string, port: string) {
		if (this.ws) {
			this.ws.close();
		}
		
		this.isConnecting = true;
		this.error = null;

		try {
			const url = `ws://${host}:${port}`;
			this.ws = new WebSocket(url);

			this.ws.onopen = () => {
				this.isConnected = true;
				this.isConnecting = false;
				this.error = null;
				console.log(`Connected to ${url}`);
			};

			this.ws.onmessage = (event) => {
				try {
					const data = JSON.parse(event.data);
					if (data.type === 'sync' && Array.isArray(data.satellites)) {
						if (data.client_id) {
							this.clientId = data.client_id;
						}
						const mappedSatellites = data.satellites.map((s: any) => ({
							id: s.id,
							name: s.name,
							type: s.type,
							state: s.state ? s.state.toUpperCase() : 'INIT',
							lastMessage: s.last_message || s.lastMessage || '-',
							heartbeat: s.heartbeat || '-',
							lives: s.lives?.toString() || '-'
						}));
						satellitesStore.setSatellites(mappedSatellites);

					} else if (data.type === 'SATELLITE_STATE_UPDATE') {
						const newState = data.new_state ? data.new_state.toUpperCase() : 'INIT';
						satellitesStore.updateSatelliteState(data.satellite_id, newState, data.last_message);

					} else if (data.type === 'TELEMETRY' && data.satellite_id && data.metrics) {
						const satellite = satellitesStore.satellites.find((s) => s.id === data.satellite_id);
						const name = satellite ? satellite.name : data.satellite_id;
						telemetryStore.addTelemetry(name, data.metrics);

					} else if (data.type === 'LOG') {
						logStore.addLog(data.sender, data.level, data.message, data.timestamp);
					} else if (data.type === 'HEARTBEAT') {
						this.heartbeat = data.value || '-';
					}
				} catch (err) {
					console.error('Error parsing WebSocket message:', err);
				}
			};

			this.ws.onclose = () => {
				this.isConnected = false;
				this.isConnecting = false;
				this.ws = null;
				satellitesStore.setSatellites([]);
				telemetryStore.clear();
				logStore.clear();
				console.log('WebSocket disconnected');
			};

			this.ws.onerror = (e) => {
				console.error('WebSocket error:', e);
				this.error = 'Failed to connect';
				this.isConnecting = false;
			};
		} catch (err: any) {
			this.error = err.message || 'Invalid WebSocket URL';
			this.isConnecting = false;
		}
	}

	disconnect() {
		if (this.ws) {
			this.ws.close();
		}
	}

    send(data: any) {
        if (this.ws && this.isConnected) {
            this.ws.send(typeof data === 'string' ? data : JSON.stringify(data));
        } else {
            console.warn('Cannot send message, WebSocket is not connected.');
        }
    }
}

export const wsStore = new WebSocketStore();
