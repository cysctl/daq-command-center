<script lang="ts">
	import QuickActionButtons from './quick-action-buttons.svelte';
	import SatellitesHeader from './satellites-header.svelte';
	import SatellitesTable from './satellites-table.svelte';
</script>

<section class="flex min-h-64 flex-2 flex-col gap-3">
	<div class="flex items-center justify-between">
		<SatellitesHeader />
		<QuickActionButtons />
	</div>

	<div class="relative flex-1 overflow-x-auto">
		<SatellitesTable />
	</div>
</section>
