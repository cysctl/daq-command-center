<script lang="ts">
	import Logs from '$lib/components/Logs/index.svelte';
	import Satellites from '$lib/components/Satellites/index.svelte';
</script>

<main class="flex flex-1 flex-col justify-between gap-5 overflow-hidden p-5">
	<Satellites />
	<Logs />
</main>
