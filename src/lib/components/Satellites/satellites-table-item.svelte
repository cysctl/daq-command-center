<script lang="ts">
	import State from '../ui/state.svelte';
	import type { StateType } from '../ui/state.svelte';

	interface SatellitesTableItemProps {
		type: string;
		name: string;
		state: StateType;
		lastMessage: string;
		lastMessageTime: string;
		heartbeat: string;
		lives: string; // I can change this to number later
	}

	let {
		type,
		name,
		state,
		lastMessage,
		lastMessageTime,
		heartbeat,
		lives
	}: SatellitesTableItemProps = $props();
</script>

<tr class="transition-colors hover:bg-muted/50">
	<td class="font-mono text-sm text-muted-foreground">{type}</td>
	<td class="text-sm font-medium">{name}</td>
	<td>
		<State {state} isTransitionState={false} />
	</td>
	<td>
		<div class="flex flex-col">
			<span class="text-sm">{lastMessage}</span>
			<span class="text-xs leading-tight text-muted-foreground">{lastMessageTime}</span>
		</div>
	</td>
	<td class="text-sm text-muted-foreground">{heartbeat}</td>
	<td class="text-sm text-muted-foreground">{lives}</td>
	<td class="text-right"> Test </td>
</tr>
