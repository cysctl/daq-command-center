<script lang="ts">
	import Divider from '../ui/divider.svelte';
	import FrontEndFilters from './front-end-filters.svelte';
	import NetworkLogLevel from './network-log-level.svelte';
	import Search from './search.svelte';
	import SelectSender from './select-sender.svelte';
	// import { logStore } from '../../stores/logs.svelte.ts';

	import { Terminal } from '@lucide/svelte';

	import { layoutStore } from '$lib/stores/layout.svelte';

	// I will add the Trash icon later
	// import { Trash2 } from '@lucide/svelte';
</script>

<div
	class="flex justify-between gap-4 {layoutStore.splitDirection === 'vertical'
		? 'w-full flex-col items-start'
		: 'items-center'}"
>
	<span
		class="inline-flex items-center gap-2 text-sm font-semibold text-muted-foreground uppercase select-none"
	>
		<Terminal size={18} />
		<span>system logs</span>
	</span>

	<div
		class="relative flex gap-3 {layoutStore.splitDirection === 'vertical'
			? 'w-full flex-col items-stretch'
			: 'items-center'}"
	>
		<div>
			<Search />
		</div>
		<div class="flex flex-wrap items-center gap-3">
			<FrontEndFilters />
			<Divider />
			<SelectSender />
			<NetworkLogLevel />
			<!--
		<button
			onclick={() => logStore.clear()}
			class="flex cursor-pointer items-center justify-center rounded-md border border-border p-2 text-muted-foreground hover:bg-border"
			title="Clear Logs"
			>
			<Trash2 size={16} />
		</button>
		-->
		</div>
	</div>
</div>
