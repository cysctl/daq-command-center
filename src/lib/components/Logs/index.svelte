<script lang="ts">
	import LogMessagesArea from './log-messages-area.svelte';
	import LogsHeader from './logs-header.svelte';
	import OperatorNote from './operator-note.svelte';
</script>

<section class="flex min-h-96 flex-col">
	<LogsHeader />
	<LogMessagesArea />
	<OperatorNote />
</section>
