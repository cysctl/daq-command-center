// i will clean here later

import type { StateType } from '../components/ui/state.svelte';

export interface Satellite {
	id: string;
	name: string;
	state: StateType;
	type: string;
	lastMessage: string;
	lastMessageTime: string;
	heartbeat: string;
	lives: string;
}

class SatellitesStore {
	satellites = $state<Satellite[]>([]);

	setSatellites(satellites: Satellite[]) {
		this.satellites = satellites;
	}

	updateSatelliteState(id: string, newState: StateType, newLastMessage?: string) {
		this.satellites = this.satellites.map((satellite) =>
			satellite.id === id
				? { ...satellite, state: newState, lastMessage: newLastMessage ?? satellite.lastMessage }
				: satellite
		);
	}
}

export const satellitesStore = new SatellitesStore();
