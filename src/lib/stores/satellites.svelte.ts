// i will clean here later

import type { StateType } from '../components/ui/state.svelte';

export interface Satellite {
	id: string;
	name: string;
	state: StateType;
	type: string;
	lastMessage: string;
	heartbeat: string;
	lives: string;
}

class SatellitesStore {
	satellites = $state<Satellite[]>([]);

	addSatellite(satellite: Satellite) {
		this.satellites.push(satellite);
	}

	setSatellites(satellites: Satellite[]) {
		this.satellites = satellites;
	}

	updateSatelliteState(id: string, newState: StateType) {
		const satellite = this.satellites.find((s) => s.id === id);
		if (satellite) {
			satellite.state = newState;
		}
	}
}

export const satellitesStore = new SatellitesStore();
