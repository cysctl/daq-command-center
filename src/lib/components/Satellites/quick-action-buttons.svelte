<script lang="ts">
	const buttons = ['Initialize', 'Shutdown', 'Launch', 'Land', 'Start', 'Stop'];
</script>

<div class="hidden flex-wrap items-center gap-2 md:flex">
	{#each buttons as label}
		<button
			class="cursor-pointer rounded-lg px-2 py-1 text-sm text-muted-foreground transition-colors select-none hover:bg-border active:scale-95"
		>
			{label}
		</button>
	{/each}
</div>
