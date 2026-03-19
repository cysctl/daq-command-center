<script lang="ts">
	import Logo from './logo.svelte';
	import Settings from './settings.svelte';
	import ServerConnStatus from './server-conn-status.svelte';
	import Divider from '../ui/divider.svelte';
</script>

<header class="flex w-full justify-between border-b border-border p-5">
	<Logo />
	<div class="flex items-center gap-4">
		<ServerConnStatus />
		<Divider />
		<Settings />
	</div>
</header>
