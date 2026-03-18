<script lang="ts">
	const filters: string[] = ['all', 'info', 'warn', 'error'];
</script>

<ul>
	{#each filters as filter}
		<li>
			{filter}
		</li>
	{/each}
</ul>
