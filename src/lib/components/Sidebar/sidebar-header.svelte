<script lang="ts">
	import { Satellite, Plus } from '@lucide/svelte';

	type Props = {
		satelliteCount: number;
	};

	let { satelliteCount }: Props = $props();
</script>

<div class="flex items-center justify-between">
	<div class="flex items-center gap-2">
		<Satellite size={17} class="text-muted-foreground" />
		<span class="text-sm font-semibold tracking-wider text-muted-foreground uppercase"
			>Satellites ({satelliteCount})</span
		>
	</div>

	<Plus size={17} class="cursor-pointer text-muted-foreground" />
</div>
