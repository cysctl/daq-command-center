<script lang="ts">
	import Logs from '$lib/components/Logs/index.svelte';
	import Satellites from '$lib/components/Satellites/index.svelte';
	import { layoutStore } from '$lib/stores/layout.svelte';
</script>

<main
	class="flex flex-1 justify-between gap-10 overflow-hidden p-5 {layoutStore.splitDirection ===
	'vertical'
		? 'flex-row'
		: 'flex-col'}"
>
	<Satellites />
	{#if layoutStore.splitDirection === 'vertical'}
		<div class="border-r border-border"></div>
	{/if}
	<Logs />
</main>
