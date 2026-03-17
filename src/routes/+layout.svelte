<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';

	import Header from '$lib/components/Header/index.svelte';

	let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>
<div class="flex h-screen w-full flex-col">
	<Header />
	{@render children()}
</div>
