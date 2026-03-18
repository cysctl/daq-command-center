<script lang="ts">
	import Sidebar from '$lib/components/Sidebar/index.svelte';
	import Graphs from '$lib/components/Graphs/index.svelte';
	import Logs from '$lib/components/Logs/index.svelte';
	import { PanelLeft } from '@lucide/svelte';

	let sidebarOpen = $state(false);
</script>

<main class="flex flex-1 overflow-hidden">
	<button
		onclick={() => (sidebarOpen = true)}
		class="fixed bottom-5 left-5 z-50 flex size-12 items-center justify-center rounded-full bg-primary text-primary-foreground shadow-lg active:scale-95 lg:hidden"
		aria-label="Open sidebar"
	>
		<PanelLeft size={22} />
	</button>

	{#if sidebarOpen}
		<div
			class="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm transition-opacity lg:hidden"
			onclick={() => (sidebarOpen = false)}
			onkeydown={(e) => e.key === 'Escape' && (sidebarOpen = false)}
			role="button"
			tabindex="-1"
		></div>
	{/if}

	<Sidebar bind:open={sidebarOpen} />

	<div class="flex flex-1 flex-col gap-5 overflow-auto p-5">
		<Graphs />
		<Logs />
	</div>
</main>
