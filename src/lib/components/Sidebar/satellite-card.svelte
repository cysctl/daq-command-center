<script lang="ts">
	import State from '../ui/state.svelte';
	import SatelliteStateButton from './satellite-state-button.svelte';

	import type { StateType } from '../ui/state.svelte';

	let currentState: StateType = $state('INIT');

	let availableStates: StateType[] = ['INIT', 'ORBIT', 'RUN', 'ERROR'];
</script>

<div class="flex flex-col gap-2 rounded-lg border border-border p-3">
	<div class="flex justify-between">
		<span class="font-mono text-sm font-semibold uppercase">Satellite 1</span>
		<State state={currentState} />
	</div>

	<span class="font-mono text-sm text-muted-foreground uppercase">Type: -</span>
	<span class="font-mono text-sm text-muted-foreground uppercase">Last Message: -</span>
	<span class="font-mono text-sm text-muted-foreground uppercase">Heartbeat: -</span>
	<span class="font-mono text-sm text-muted-foreground uppercase">Lives: -</span>

	<div class="grid grid-cols-4 gap-2">
		{#each availableStates as state}
			<SatelliteStateButton
				{state}
				isActive={state === currentState}
				onclick={() => {
					currentState = state;
				}}
			/>
		{/each}
	</div>
</div>
