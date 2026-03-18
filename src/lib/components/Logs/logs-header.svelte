<script lang="ts">
	import FrontEndFilters from './front-end-filters.svelte';
	import NetworkLogLevel from './network-log-level.svelte';
	import Search from './search.svelte';
	import SelectSender from './select-sender.svelte';

	import { Terminal } from '@lucide/svelte';
</script>

<div class="flex items-center justify-between border-b border-border pb-4">
	<div class="flex items-center gap-2">
		<Terminal size={20} class="text-muted-foreground" />
		<span class="font-medium tracking-wider text-muted-foreground uppercase">system logs</span>
	</div>
	<div class="flex flex-wrap items-stretch gap-3 relative">
		<Search />
		<FrontEndFilters />
		<div class="h-6 w-px self-center bg-border mx-1"></div>
		<SelectSender />
		<NetworkLogLevel />
	</div>
</div>
