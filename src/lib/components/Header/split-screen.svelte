<script lang="ts">
	import { Columns2, Rows2 } from '@lucide/svelte';
	import { layoutStore } from '$lib/stores/layout.svelte';
</script>

<button
	class="h-fit cursor-pointer rounded-lg p-1 text-muted-foreground transition-colors hover:bg-border active:scale-95"
	onclick={() => layoutStore.toggleSplitDirection()}
>
	{#if layoutStore.splitDirection === 'vertical'}
		<Columns2 size={17} />
	{:else}
		<Rows2 size={17} />
	{/if}
</button>
