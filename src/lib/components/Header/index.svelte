<script lang="ts">
	import Logo from './logo.svelte';
	import Settings from './settings.svelte';
	import ServerConnStatus from './server-conn-status.svelte';
	import Divider from '../ui/divider.svelte';
	import ToggleTheme from './toggle-theme.svelte';
</script>

<header class="flex w-full justify-between border-b border-border px-5 py-3">
	<Logo />
	<div class="flex items-center gap-4">
		<ServerConnStatus />
		<Divider />
		<ToggleTheme />
		<Divider />
		<Settings />
	</div>
</header>
