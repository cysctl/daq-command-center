<script lang="ts">
	import { tick } from 'svelte';
	import LogMessage from './log-message.svelte';
	import { logsState } from './store.svelte';
	import { logStore } from '../../stores/logs.svelte.ts';

	let filteredLogs = $derived(
		logStore.logs.filter((log) => {
			const matchesLevel =
				logsState.filter === 'all' || log.level.toLowerCase() === logsState.filter;
			const matchesSearch =
				logsState.searchQuery === '' || log.message.includes(logsState.searchQuery);
			const matchesSender = logsState.sender === 'All' || log.sender === logsState.sender;
			return matchesLevel && matchesSearch && matchesSender;
		})
	);

	let container: HTMLDivElement;

	$effect(() => {
		if (filteredLogs.length && container) {
			tick().then(() => {
				container.scrollTo({ top: container.scrollHeight, behavior: 'smooth' });
			});
		}
	});
</script>

<div
	bind:this={container}
	class="custom-scrollbar my-4 flex-1 overflow-y-auto rounded-xl border border-border bg-secondary/10 p-2 font-mono text-sm sm:p-4"
>
	{#if filteredLogs.length === 0}
		<p class="py-8 text-center text-lg text-muted-foreground">No log messages.</p>
	{:else}
		<ul class="flex flex-col gap-1.5 sm:gap-1">
			{#each filteredLogs as log}
				<li>
					<LogMessage {log} />
				</li>
			{/each}
		</ul>
	{/if}
</div>
