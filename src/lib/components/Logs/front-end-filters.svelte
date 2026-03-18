<script lang="ts">
	const filters: string[] = ['all', 'info', 'warn', 'error'];
	let selectedFilter = $state('all');
</script>

<ul class="inline-flex items-center gap-1 rounded-lg border border-border bg-card p-1 shadow-sm">
	{#each filters as filter}
		<li>
			<button
				class="cursor-pointer rounded-md px-3 py-1 text-sm capitalize transition-colors outline-none hover:bg-border focus:bg-border"
				class:bg-border={selectedFilter === filter}
				class:text-card-foreground={selectedFilter === filter}
				class:text-muted-foreground={selectedFilter !== filter}
				onclick={() => {
					selectedFilter = filter;
				}}
			>
				{filter}
			</button>
		</li>
	{/each}
</ul>
