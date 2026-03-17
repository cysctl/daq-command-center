<script lang="ts">
	import { Settings2 } from '@lucide/svelte';
</script>

<div class="flex justify-between rounded-md border border-border bg-secondary px-3 py-1">
	<div>
		<div>
			<span class="text-sm text-muted-foreground">Run Prefix: </span>
			<span class="font-mono text-sm text-foreground">run</span>
		</div>
		<div>
			<span class="text-sm text-muted-foreground">Sequence: </span>
			<span class="font-mono text-sm text-foreground">15</span>
		</div>
	</div>
	<button class="text-muted-foreground">
		<Settings2 size={17} />
	</button>
</div>
