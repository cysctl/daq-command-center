<script lang="ts">
	import Select from '../ui/select.svelte';
	import { Send } from '@lucide/svelte';

	let note = $state('');
	let selectedLevel = $state('INFO');

	let levelOptions = ['INFO', 'WARN', 'ERROR'];
</script>

<div class="mt-4 flex flex-col gap-3 border-t border-border pt-4 sm:flex-row sm:items-stretch">
	<input
		type="text"
		bind:value={note}
		placeholder="Enter operator note..."
		class="min-w-0 flex-1 rounded-lg border border-border bg-card px-4 py-2 text-sm text-foreground shadow-sm transition-[color,box-shadow] outline-none placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-2 focus-visible:ring-ring"
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
			class="inline-flex flex-1 cursor-pointer items-center justify-center gap-2 rounded-lg bg-primary px-4 py-2 text-sm font-medium text-primary-foreground shadow-sm transition-colors hover:bg-primary/90 focus-visible:ring-2 focus-visible:ring-ring active:scale-95 disabled:pointer-events-none disabled:opacity-50 sm:flex-none"
		>
			<Send size={16} />
			<span>Send</span>
		</button>
	</div>
</div>
