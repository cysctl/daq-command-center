<script lang="ts">
	import { Satellite } from '@lucide/svelte';
	import { satellitesStore } from '$lib/stores/satellites.svelte';
</script>

<span
	class="inline-flex items-center gap-2 text-sm font-semibold text-muted-foreground uppercase select-none"
>
	<Satellite size={18} />
	<span>satellites ({satellitesStore.satellites.length})</span>
</span>
