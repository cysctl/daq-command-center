<script lang="ts">
	import State from '../ui/state.svelte';
	import SatelliteStateButton from './satellite-state-button.svelte';
	import { type Satellite } from '../../stores/satellites.svelte.ts';
	import { wsStore } from '../../stores/websocket.svelte.ts';

	import type { StateType } from '../ui/state.svelte';

	let { satellite }: { satellite: Satellite } = $props();

	let currentState: StateType = $derived(satellite.state);

	let availableStates: StateType[] = ['INIT', 'ORBIT', 'RUN', 'SAFE'];

	const allowedTransitions: Record<StateType, StateType[]> = {
		NEW: ['INIT'],
		INIT: ['ORBIT', 'SAFE'],
		ORBIT: ['INIT', 'RUN', 'SAFE'],
		RUN: ['ORBIT', 'SAFE'],
		SAFE: ['INIT'],
		ERROR: ['INIT'],
		DEAD: []
	};
</script>

<div class="flex flex-col gap-2 rounded-lg border border-border p-3">
	<div class="flex justify-between">
		<span class="font-mono text-sm font-semibold uppercase">{satellite.name}</span>
		<State state={currentState} />
	</div>

	<span class="font-mono text-sm text-muted-foreground uppercase">Type: {satellite.type}</span>
	<span class="font-mono text-sm text-muted-foreground uppercase">ID: {satellite.id}</span>

	<!-- the reason for this format is prettier :/ -->
	<span class="font-mono text-sm text-muted-foreground uppercase"
		>Last Message: {satellite.lastMessage}</span
	>

	<!-- the reason for this format is prettier :/ -->
	<span class="font-mono text-sm text-muted-foreground uppercase"
		>Heartbeat: {satellite.heartbeat}</span
	>

	<span class="font-mono text-sm text-muted-foreground uppercase">Lives: {satellite.lives}</span>

	<div class="grid grid-cols-4 gap-2">
		{#each availableStates as state}
			<SatelliteStateButton
				{state}
				isActive={state === currentState}
				isDisabled={!allowedTransitions[currentState].includes(state) && state !== currentState}
				onclick={() => {
					wsStore.send({
						type: 'CHANGE_STATE',
						satellite_id: satellite.id,
						new_state: state
					});
				}}
			/>
		{/each}
	</div>
</div>
