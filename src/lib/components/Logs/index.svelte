<script lang="ts">
	import LogMessagesArea from './log-messages-area.svelte';
	import LogsHeader from './logs-header.svelte';
	import OperatorNote from './operator-note.svelte';
</script>

<section
	class="flex min-h-96 flex-3 flex-col rounded-xl border border-border bg-card p-4 text-card-foreground sm:p-6"
>
	<LogsHeader />
	<LogMessagesArea />
	<OperatorNote />
</section>
