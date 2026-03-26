<script lang="ts">
	import { logsState } from './store.svelte';

	const filters: string[] = ['all', 'info', 'warning', 'status', 'critical', 'trace', 'debug'];
</script>

<ul class="inline-flex items-center gap-1 rounded-xl border border-border bg-card p-1">
	{#each filters as filter}
		<li>
			<button
				class="cursor-pointer rounded-lg px-3 py-1 text-sm capitalize transition-colors outline-none hover:bg-border focus:bg-border"
				class:bg-border={logsState.filter === filter}
				class:text-card-foreground={logsState.filter === filter}
				class:text-muted-foreground={logsState.filter !== filter}
				onclick={() => {
					logsState.filter = filter;
				}}
			>
				{filter}
			</button>
		</li>
	{/each}
</ul>
