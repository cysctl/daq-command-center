<script lang="ts">
	import State from '../ui/state.svelte';
	import type { StateType } from '../ui/state.svelte';
	import { Ellipsis } from '@lucide/svelte';
	import { layoutStore } from '$lib/stores/layout.svelte';
	import { wsStore } from '$lib/stores/websocket.svelte';
	import { scale } from 'svelte/transition';

	interface SatellitesTableItemProps {
		id: string;
		type: string;
		name: string;
		state: StateType;
		lastMessage: string;
		lastMessageTime: string;
		heartbeat: string;
		lives: string; // I can change this to number later
	}

	let {
		id,
		type,
		name,
		state: currentState,
		lastMessage,
		lastMessageTime,
		heartbeat,
		lives
	}: SatellitesTableItemProps = $props();

	let showPopup = $state(false);

	function togglePopup() {
		showPopup = !showPopup;
	}

	function closePopup() {
		showPopup = false;
	}

	function sendCommand(command: string) {
		wsStore.send({
			type: 'CHANGE_STATE',
			satellite_id: id,
			new_state: command.toUpperCase()
		});
	}

	const validCommands: Record<string, string[]> = {
		NEW: ['Initialize', 'Shutdown'],
		INIT: ['Launch', 'Shutdown'],
		ORBIT: ['Land', 'Start'],
		RUN: ['Stop'],
		SAFE: [],
		ERROR: ['Shutdown']
	};

	function isEnabled(button: string): boolean {
		const allowed = validCommands[currentState];
		if (!allowed) return false; // transitional states — no commands allowed
		return allowed.includes(button);
	}

	let buttons: string[] = ['Initialize', 'Launch', 'Land', 'Start', 'Stop', 'Shutdown'];
</script>

<tr class="transition-colors hover:bg-muted/50">
	<td class="font-mono text-sm text-muted-foreground">{type}</td>
	<td class="text-sm font-medium">{name}</td>
	<td>
		<State state={currentState} />
	</td>
	<td>
		<div class="flex flex-col">
			<span class="text-sm">{lastMessage}</span>
			<span class="text-xs leading-tight text-muted-foreground">{lastMessageTime}</span>
		</div>
	</td>
	<td class="text-sm text-muted-foreground">{heartbeat}</td>
	<td class="text-sm text-muted-foreground">{lives}</td>
	<td class="text-right">
		{#if layoutStore.splitDirection === 'horizontal'}
			<div class="flex items-center justify-end gap-2">
				{#each buttons as button}
					{@const enabled = isEnabled(button)}
					<button
						onclick={() => sendCommand(button)}
						disabled={!enabled}
						class="rounded-lg px-2 py-1 text-sm transition-colors select-none {enabled
							? 'cursor-pointer text-muted-foreground hover:bg-border active:scale-95'
							: 'cursor-not-allowed text-muted-foreground/30'}">{button}</button
					>
				{/each}
			</div>
		{:else}
			<div class="relative inline-block text-left">
				<button
					class="h-fit cursor-pointer rounded-lg p-1 text-muted-foreground transition-colors hover:bg-border active:scale-95"
					onclick={togglePopup}
				>
					<Ellipsis size={17} />
				</button>

				{#if showPopup}
					<div
						class="fixed inset-0 z-40 cursor-default"
						onclick={closePopup}
						role="button"
						tabindex="-1"
						aria-hidden="true"
					></div>
					<ul
						transition:scale={{ duration: 150, start: 0.95 }}
						class="absolute right-0 z-50 mt-1 flex min-w-40 origin-top-right flex-col overflow-hidden rounded-xl border border-border bg-card shadow-lg"
					>
						{#each buttons as button}
							{@const enabled = isEnabled(button)}
							<li class="w-full">
								<button
									disabled={!enabled}
									class="w-full px-4 py-2 text-left text-sm transition-colors outline-none {enabled
										? 'cursor-pointer text-card-foreground hover:bg-border focus:bg-border'
										: 'cursor-not-allowed text-muted-foreground/30'}"
									onclick={() => {
										sendCommand(button);
										closePopup();
									}}>{button}</button
								>
							</li>
						{/each}
					</ul>
				{/if}
			</div>
		{/if}
	</td>
</tr>
