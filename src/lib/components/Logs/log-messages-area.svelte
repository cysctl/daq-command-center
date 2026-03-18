<script lang="ts">
	import LogMessage from './log-message.svelte';
	import { logsState } from './store.svelte';

	// mock data
	const logs = [
		{
			id: 1,
			timestamp: '14:23:45.123',
			level: 'INFO',
			sender: 'System',
			message: 'Initialization started.'
		},
		{
			id: 2,
			timestamp: '14:23:50.000',
			level: 'ERROR',
			sender: 'Telemetry',
			message: 'Failed to parse incoming packet.'
		},
		{
			id: 3,
			timestamp: '14:23:55.333',
			level: 'INFO',
			sender: 'Operator',
			message: 'Adjusting antenna position.'
		}
	];

	let filteredLogs = $derived(
		logsState.filter === 'all'
			? logs
			: logs.filter((log) => log.level.toLowerCase() === logsState.filter)
	);
</script>

<div
	class="my-4 flex-1 overflow-y-auto rounded-md border border-border bg-secondary/10 p-2 font-mono text-sm sm:p-4"
>
	<ul class="flex flex-col gap-1.5 sm:gap-1">
		{#each filteredLogs as log}
			<li>
				<LogMessage {log} />
			</li>
		{/each}
	</ul>
</div>
