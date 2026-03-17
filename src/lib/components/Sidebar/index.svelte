<script lang="ts">
	import SidebarHeader from './sidebar-header.svelte';
	import SatelliteCard from './satellite-card.svelte';
	import QuickActionButtons from './quick-action-buttons.svelte';
	import RunIdentifier from './run-identifier.svelte';
</script>

<aside class="flex h-full flex-col justify-between border-r border-border p-5">
	<div class="flex flex-col gap-5">
		<SidebarHeader satelliteCount={5} />
		<QuickActionButtons />
		<div class="flex flex-col gap-7">
			<SatelliteCard />
		</div>
	</div>
	<RunIdentifier />
</aside>
