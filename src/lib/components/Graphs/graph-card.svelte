<!-- Mock Card -->

<script lang="ts">
	import { ChevronDown, Thermometer } from '@lucide/svelte';
</script>

<div
	class="flex flex-col gap-6 overflow-hidden rounded-xl border border-border bg-card p-6 text-card-foreground"
>
	<div class="flex items-center justify-between">
		<div class="inline-flex items-center gap-2">
			<span class="text-muted-foreground">
				<Thermometer size={17} />
			</span>

			<span class="text-muted-foreground"> Temperature </span>
		</div>

		<button
			class="bg- inline-flex cursor-pointer items-center gap-2 rounded-lg border border-border bg-card px-3 py-2 whitespace-nowrap hover:bg-border active:scale-95"
		>
			<span class="text-sm text-card-foreground">Overview</span>
			<span class="text-muted-foreground">
				<ChevronDown size={17} />
			</span>
		</button>
	</div>

	<div>
		<div class="flex items-baseline gap-1">
			<span class="text-4xl font-semibold tracking-tight tabular-nums">25.6</span>
			<span class="text-lg text-muted-foreground">°C</span>
		</div>

		<div class="mt-5">
			<span>Graph</span>
		</div>
	</div>
</div>
