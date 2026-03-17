<script lang="ts">
	import SidebarHeader from './sidebar-header.svelte';
	import SatelliteCard from './satellite-card.svelte';
	import QuickActionButtons from './quick-action-buttons.svelte';
	import RunIdentifier from './run-identifier.svelte';

	let { open = $bindable(false) } = $props();

	function closeSidebar() {
		open = false;
	}
</script>

<aside
	class="fixed inset-y-0 left-0 z-50 flex w-80 flex-col justify-between border-r border-border bg-background p-5 transition-transform duration-300 ease-in-out lg:static lg:z-auto lg:w-auto lg:translate-x-0"
	class:max-lg:-translate-x-full={!open}
	class:max-lg:translate-x-0={open}
>
	<div class="flex flex-col gap-5">
		<SidebarHeader satelliteCount={5} onclose={closeSidebar} />
		<QuickActionButtons />
		<div class="flex flex-col gap-7">
			<SatelliteCard />
		</div>
	</div>
	<RunIdentifier />
</aside>
