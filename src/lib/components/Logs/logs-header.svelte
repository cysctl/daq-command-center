<script lang="ts">
	import FrontEndFilters from './front-end-filters.svelte';
	import NetworkLogLevel from './network-log-level.svelte';
	import Search from './search.svelte';
	import SelectSender from './select-sender.svelte';
	import { logStore } from '../../stores/logs.svelte.ts';

	import { Terminal, Trash2 } from '@lucide/svelte';
</script>

<div
	class="flex flex-col gap-4 border-b border-border pb-4 md:flex-row md:items-start md:justify-between xl:items-center"
>
	<div class="flex items-center gap-2 md:mt-2 xl:mt-0">
		<Terminal size={20} class="text-muted-foreground" />
		<span class="font-medium tracking-wider text-muted-foreground uppercase">system logs</span>
	</div>
	<div class="relative flex flex-wrap items-center gap-3 md:justify-end">
		<Search />
		<FrontEndFilters />
		<div class="hidden h-6 w-px self-center bg-border sm:block"></div>
		<SelectSender />
		<NetworkLogLevel />
		<button
			onclick={() => logStore.clear()}
			class="flex cursor-pointer items-center justify-center rounded-md border border-border p-2 text-muted-foreground hover:bg-border"
			title="Clear Logs"
		>
			<Trash2 size={16} />
		</button>
	</div>
</div>
