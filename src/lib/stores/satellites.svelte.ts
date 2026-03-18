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
	satellites = $state<Satellite[]>([
		{
			id: 'sat-1',
			name: 'Satellite 1',
			state: 'INIT',
			type: '-',
			lastMessage: '-',
			heartbeat: '-',
			lives: '-'
		}
	]);

	addSatellite(satellite: Satellite) {
		this.satellites.push(satellite);
	}

	updateSatelliteState(id: string, newState: StateType) {
		const satellite = this.satellites.find((s) => s.id === id);
		if (satellite) {
			satellite.state = newState;
		}
	}
}

export const satellitesStore = new SatellitesStore();
