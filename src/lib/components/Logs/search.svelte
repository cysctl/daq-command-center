<script lang="ts">
	import { Search as SearchIcon } from '@lucide/svelte';
</script>

<div class="relative flex items-center">
	<SearchIcon size={17} class="absolute left-3 text-muted-foreground" />
	<input
		type="text"
		class="w-48 min-w-0 rounded-lg border border-border bg-card py-2 pr-3 pl-9 text-sm text-foreground shadow-sm transition-[color,box-shadow] outline-none placeholder:text-muted-foreground focus-visible:border-ring focus-visible:ring-2 focus-visible:ring-ring"
		placeholder="Search in logs"
	/>
</div>
