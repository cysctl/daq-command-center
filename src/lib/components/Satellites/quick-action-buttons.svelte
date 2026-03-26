<script lang="ts">
	import { wsStore } from '$lib/stores/websocket.svelte';
	import { satellitesStore } from '$lib/stores/satellites.svelte';

	const buttons = ['Initialize', 'Shutdown', 'Launch', 'Land', 'Start', 'Stop'];

	function sendCommandToAll(command: string) {
		for (const satellite of satellitesStore.satellites) {
			wsStore.send({
				type: 'CHANGE_STATE',
				satellite_id: satellite.id,
				new_state: command.toUpperCase()
			});
		}
	}
</script>

<div class="hidden flex-wrap items-center gap-2 md:flex">
	<span class="text-sm text-muted-foreground select-none">All:</span>
	{#each buttons as label}
		<button
			onclick={() => sendCommandToAll(label)}
			class="cursor-pointer rounded-lg px-2 py-1 text-sm text-muted-foreground transition-colors select-none hover:bg-border active:scale-95"
		>
			{label}
		</button>
	{/each}
</div>
