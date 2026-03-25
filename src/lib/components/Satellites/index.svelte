<script lang="ts">
	import { Satellite } from '@lucide/svelte';
	import { satellitesStore } from '$lib/stores/satellites.svelte';
	import SatellitesTable from './satellites-table.svelte';
</script>

<section class="flex min-h-64 flex-2 flex-col gap-3">
	<span
		class="inline-flex items-center gap-2 text-sm font-semibold text-muted-foreground uppercase select-none"
	>
		<Satellite size={18} />
		<span>satellites ({satellitesStore.satellites.length})</span>
	</span>

	<div class="flex-1">
		<SatellitesTable />
	</div>
</section>
