<script lang="ts">
	import LogMessage from './log-message.svelte';

	const logs: string[] = ['msg 1', 'msg 2', 'msg 3'];
</script>

<ul>
	{#each logs as log}
		<li>
			<LogMessage {log} />
		</li>
	{/each}
</ul>
