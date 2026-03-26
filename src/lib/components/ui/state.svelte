<script lang="ts">
	export type StateType =
		| 'NEW'
		| 'INIT'
		| 'ORBIT'
		| 'RUN'
		| 'SAFE'
		| 'ERROR'
		| 'INITIALIZING'
		| 'LAUNCHING'
		| 'LANDING'
		| 'RECONFIGURING'
		| 'STARTING'
		| 'STOPPING';

	type Props = {
		state: StateType;
	};

	let { state }: Props = $props();

	import { LoaderCircle } from '@lucide/svelte';

	const TRANSITION_STATES: Set<string> = new Set([
		'INITIALIZING',
		'LAUNCHING',
		'LANDING',
		'RECONFIGURING',
		'STARTING',
		'STOPPING'
	]);

	const isTransitionState = $derived(TRANSITION_STATES.has(state));

	// transitional states use their target state's style
	const transitionStyleMap: Record<string, string> = {
		INITIALIZING: 'INIT',
		LAUNCHING: 'ORBIT',
		LANDING: 'INIT',
		RECONFIGURING: 'ORBIT',
		STARTING: 'RUN',
		STOPPING: 'ORBIT'
	};

	const stateStyles: Record<string, string> = {
		NEW: 'bg-state-new/20 text-state-new border-state-new/50',
		INIT: 'bg-state-init/20 text-state-init border-state-init/50',
		ORBIT: 'bg-state-orbit/20 text-state-orbit border-state-orbit/50',
		RUN: 'bg-state-run/20 text-state-run border-state-run/50',
		SAFE: 'bg-state-safe/20 text-state-safe border-state-safe/50',
		ERROR: 'bg-state-error/20 text-state-error border-state-error/50'
	};

	const styleKey = $derived(transitionStyleMap[state] ?? state);
</script>

<div
	class="inline-flex items-center rounded-xl border px-3 py-1.5 font-mono text-xs leading-none {stateStyles[
		styleKey
	]}"
>
	{#if isTransitionState}
		<LoaderCircle class="mr-2 h-3 w-3 animate-spin" />
	{/if}

	<span>
		{state}
	</span>
</div>
