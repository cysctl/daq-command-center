<script lang="ts">
	import { Settings } from '@lucide/svelte';
	import { fade, scale } from 'svelte/transition';

	let isOpen = $state(false);

	function close() {
		isOpen = false;
	}
</script>

<button
	class="h-fit cursor-pointer rounded-lg p-1 text-muted-foreground transition-colors hover:bg-border active:scale-95"
	onclick={() => (isOpen = true)}
>
	<Settings size={17} />
</button>

{#if isOpen}
	<div class="fixed inset-0 z-60 flex items-center justify-center">
		<button
			class="absolute inset-0 cursor-default bg-black/60 backdrop-blur-sm"
			transition:fade={{ duration: 200 }}
			onclick={close}
			onkeydown={(e) => e.key === 'Escape' && close()}
			aria-label="Close settings"
		></button>

		<div
			class="relative z-10 rounded-2xl border border-border bg-background px-7 py-5"
			transition:scale={{ duration: 200, start: 0.95 }}
			role="dialog"
		>
			Settings
		</div>
	</div>
{/if}
