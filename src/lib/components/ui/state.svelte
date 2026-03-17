<script lang="ts">
	// I can edit here later
	// I can remove some states or add new states
	export type State = 'NEW' | 'INIT' | 'ORBIT' | 'RUN' | 'SAFE' | 'ERROR' | 'DEAD';

	let { state }: { state: State } = $props();

	const stateStyles: Record<State, string> = {
		NEW: 'bg-neutral-800 text-neutral-200 border-neutral-600',
		INIT: 'bg-amber-500/20 text-amber-300 border-amber-500/50',
		ORBIT: 'bg-cyan-500/20 text-cyan-300 border-cyan-500/50',
		RUN: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/50',
		SAFE: 'bg-orange-500/20 text-orange-300 border-orange-500/50',
		ERROR: 'bg-red-500/20 text-red-300 border-red-500/50',
		DEAD: 'bg-red-950 text-red-600 border-red-800 opacity-80'
	};
</script>

<div
	class="inline-flex items-center rounded-lg px-2 py-1.5 font-mono text-sm leading-none {stateStyles[
		state
	]}"
>
	{state}
</div>
