<script lang="ts">
	import Logo from './logo.svelte';
	import SystemState from './system-state.svelte';
	import Operator from './operator.svelte';
	import ServerConnStatus from './server-conn-status.svelte';
</script>

<header class="flex w-full justify-between p-5">
	<Logo />
	<div class="flex items-center gap-4">
		<SystemState />
		<ServerConnStatus />
		<Operator />
	</div>
</header>
