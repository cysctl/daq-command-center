<script lang="ts">
	import FrontEndFilters from './front-end-filters.svelte';
	import NetworkLogLevel from './network-log-level.svelte';
	import Search from './search.svelte';
	import SelectSender from './select-sender.svelte';
</script>

<div>
	<span>system logs</span>
	<div>
		<FrontEndFilters />
		<SelectSender />
		<Search />
		<NetworkLogLevel />
	</div>
</div>
