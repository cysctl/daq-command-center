<script lang="ts">
	import { Power, Rocket, Play } from '@lucide/svelte';
	import type { Component } from 'svelte';

	type ActionButton = {
		label: string;
		icon: Component;
		onClick: () => void;
	};

	function initializeAll() {
		console.log('Initializing all systems...');
	}

	function launchAll() {
		console.log('Launching all orbits...');
	}

	function startAll() {
		console.log('Starting all processes...');
	}

	const buttons: ActionButton[] = [
		{
			label: 'Initialize All',
			icon: Power,
			onClick: initializeAll
		},
		{
			label: 'Launch All',
			icon: Rocket,
			onClick: launchAll
		},
		{
			label: 'Start All',
			icon: Play,
			onClick: startAll
		}
	];
</script>

<div class="flex items-center justify-between gap-5">
	{#each buttons as { label, onClick, icon: Icon }}
		<button
			onclick={onClick}
			class="flex cursor-pointer items-center gap-2 rounded-lg border border-border bg-card px-4 py-2 text-sm font-medium text-card-foreground transition-colors hover:bg-border hover:text-accent-foreground active:scale-95"
		>
			<Icon size={17} />
			{label}
		</button>
	{/each}
</div>
