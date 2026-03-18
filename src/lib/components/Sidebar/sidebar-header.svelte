<script lang="ts">
	import { Satellite, X, RefreshCw } from '@lucide/svelte';

	type Props = {
		satelliteCount: number;
		onclose?: () => void;
	};

	let { satelliteCount, onclose }: Props = $props();
</script>

<div class="flex items-center justify-between">
	<div class="flex items-center gap-2">
		<Satellite size={17} class="text-muted-foreground" />
		<span class="text-sm font-semibold tracking-wider text-muted-foreground uppercase"
			>Satellites ({satelliteCount})</span
		>
	</div>

	<div class="flex items-center gap-1">
		<button
			class="h-fit cursor-pointer rounded-lg p-1 text-muted-foreground transition-colors hover:bg-border active:scale-95"
		>
			<RefreshCw size={17} class="cursor-pointer text-muted-foreground" />
		</button>

		<button
			onclick={onclose}
			class="block h-fit cursor-pointer rounded-lg p-1 text-muted-foreground transition-colors hover:bg-border active:scale-95 lg:hidden"
			aria-label="Close sidebar"
		>
			<X size={17} />
		</button>
	</div>
</div>
