<script lang="ts">
	import Select from '../ui/select.svelte';
	import { Send } from '@lucide/svelte';
	import { wsStore } from '../../stores/websocket.svelte.ts';

	let note = $state('');
	let selectedLevel = $state('INFO');

	let levelOptions = ['INFO', 'WARN'];

	function sendNote() {
		if (!note.trim() || !wsStore.isConnected) return;

		wsStore.send({
			type: 'OPERATOR_LOG',
			level: selectedLevel,
			message: note.trim()
		});

		note = '';
	}

	function handleKeydown(event: KeyboardEvent) {
		if (event.key === 'Enter') {
			sendNote();
		}
	}
</script>

<div class="flex flex-col gap-4 sm:flex-row sm:items-stretch">
	<input
		type="text"
		bind:value={note}
		onkeydown={handleKeydown}
		placeholder="Enter operator note..."
		class="flex-1 rounded-xl border border-border bg-card px-4 py-2 text-sm text-foreground shadow-sm transition-[color,box-shadow] outline-none placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-2 focus-visible:ring-ring"
	/>
	<div class="flex items-stretch gap-3">
		<div class="flex-1 sm:flex-none">
			<Select
				options={levelOptions}
				bind:selected={selectedLevel}
				minWidthClass="w-full sm:w-32 h-full"
				capitalize={true}
			/>
		</div>
		<button
			onclick={sendNote}
			disabled={!note.trim() || !wsStore.isConnected}
			class="inline-flex flex-1 cursor-pointer items-center justify-center gap-2 rounded-xl bg-primary px-4 py-2 text-sm font-medium text-primary-foreground shadow-sm transition-colors hover:bg-primary/90 focus-visible:ring-2 focus-visible:ring-ring active:scale-95 disabled:pointer-events-none disabled:opacity-50 sm:flex-none"
		>
			<Send size={16} />
			<span>Send</span>
		</button>
	</div>
</div>
