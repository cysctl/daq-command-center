<script lang="ts">
	import Sidebar from '$lib/components/Sidebar/index.svelte';
	import Graphs from '$lib/components/Graphs/index.svelte';
	import Logs from '$lib/components/Logs/index.svelte';
</script>

<main class="flex flex-1">
	<Sidebar />

	<div class="flex flex-col">
		<Graphs />
		<Logs />
	</div>
</main>
