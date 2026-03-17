<script lang="ts">
	import { Satellite } from '@lucide/svelte';

	type Props = {
		satelliteCount: number;
	};

	let { satelliteCount }: Props = $props();
</script>

<div class="flex items-center gap-2">
	<Satellite size={17} class="text-muted-foreground" />
	<span class="text-sm font-semibold tracking-wider text-muted-foreground uppercase"
		>Satellites ({satelliteCount})</span
	>
</div>
