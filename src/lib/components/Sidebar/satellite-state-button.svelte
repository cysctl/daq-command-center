<script lang="ts">
	import type { StateType } from '../ui/state.svelte';

	let {
		state,
		isActive = false,
		isDisabled = false,
		onclick
	}: {
		state: StateType;
		isActive?: boolean;
		isDisabled?: boolean;
		onclick?: () => void;
	} = $props();

	const activeStyles: Record<StateType, string> = {
		NEW: 'bg-neutral-500 text-white border-neutral-500',
		INIT: 'bg-amber-500 text-amber-950 border-amber-500',
		ORBIT: 'bg-cyan-500 text-cyan-950 border-cyan-500',
		RUN: 'bg-emerald-500 text-emerald-950 border-emerald-500',
		SAFE: 'bg-orange-500 text-orange-950 border-orange-500',
		ERROR: 'bg-red-500 text-white border-red-500',
		DEAD: 'bg-red-900 text-white border-red-900'
	};

	const inactiveStyles: Record<StateType, string> = {
		NEW: 'bg-transparent text-neutral-400 border-neutral-600/50 hover:bg-neutral-500/15',
		INIT: 'bg-transparent text-amber-400 border-amber-500/40 hover:bg-amber-500/15',
		ORBIT: 'bg-transparent text-cyan-400 border-cyan-500/40 hover:bg-cyan-500/15',
		RUN: 'bg-transparent text-emerald-400 border-emerald-500/40 hover:bg-emerald-500/15',
		SAFE: 'bg-transparent text-orange-400 border-orange-500/40 hover:bg-orange-500/15',
		ERROR: 'bg-transparent text-red-400 border-red-500/40 hover:bg-red-500/15',
		DEAD: 'bg-transparent text-red-600 border-red-800/40 hover:bg-red-900/15'
	};
</script>

<button
	{onclick}
	disabled={isDisabled || isActive}
	class="w-full rounded-xl border-2 py-1 font-mono text-[0.8rem] font-semibold transition-colors {isActive
		? activeStyles[state]
		: inactiveStyles[state]} {isDisabled
		? 'cursor-not-allowed opacity-30'
		: 'cursor-pointer active:scale-95'}"
>
	{state}
</button>
