<script lang="ts">
	// I can edit here later
	// I can remove some states or add new states
	export type StateType = 'NEW' | 'INIT' | 'ORBIT' | 'RUN' | 'SAFE' | 'ERROR' | 'DEAD';

	type Props = {
		state: StateType;
		isTransitionState: boolean;
	};

	let { state, isTransitionState }: Props = $props();

	import { LoaderCircle } from '@lucide/svelte';

	const stateStyles: Record<StateType, string> = {
		NEW: 'bg-state-new/20 text-state-new border-state-new/50',
		INIT: 'bg-state-init/20 text-state-init border-state-init/50',
		ORBIT: 'bg-state-orbit/20 text-state-orbit border-state-orbit/50',
		RUN: 'bg-state-run/20 text-state-run border-state-run/50',
		SAFE: 'bg-state-safe/20 text-state-safe border-state-safe/50',
		ERROR: 'bg-state-error/20 text-state-error border-state-error/50',
		DEAD: 'bg-state-dead/20 text-state-dead border-state-dead/50 opacity-80'
	};
</script>

<div
	class="inline-flex items-center rounded-xl border px-3 py-1.5 font-mono text-xs leading-none {stateStyles[
		state
	]}"
>
	{#if isTransitionState}
		<LoaderCircle class="mr-2 h-3 w-3 animate-spin" />
	{/if}

	<span>
		{state}
	</span>
</div>
