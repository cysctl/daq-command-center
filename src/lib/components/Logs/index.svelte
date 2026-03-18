<script lang="ts">
	import LogMessagesArea from './log-messages-area.svelte';
	import LogsHeader from './logs-header.svelte';
	import OperatorNote from './operator-note.svelte';
</script>

<section class="flex h-full min-h-[500px] flex-col rounded-xl border border-border bg-card p-4 sm:p-6 text-card-foreground">
	<LogsHeader />
	<LogMessagesArea />
	<OperatorNote />
</section>
