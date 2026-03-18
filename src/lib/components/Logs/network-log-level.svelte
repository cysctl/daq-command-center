<script lang="ts">
	import { ChevronDown } from '@lucide/svelte';

	let isDropdownOpen = $state(false);
	let selectedOption = $state('All');

	// I will replace with actual log level options
	let levelOptions = ['All', 'Info', 'Warning', 'Error'];
</script>

<div class="relative">
	<button
		onclick={() => (isDropdownOpen = !isDropdownOpen)}
		class="inline-flex w-auto min-w-56 cursor-pointer items-center justify-between gap-2 rounded-lg border border-border bg-card px-3 py-2 whitespace-nowrap outline-none hover:bg-border active:scale-95"
	>
		<span class="text-sm text-card-foreground"
			><span class="mr-1 text-muted-foreground">Network Log Level:</span><span class="capitalize"
				>{selectedOption}</span
			></span
		>
		<span
			class="text-muted-foreground transition-transform duration-200"
			class:rotate-180={isDropdownOpen}
		>
			<ChevronDown size={17} />
		</span>
	</button>

	{#if isDropdownOpen}
		<div
			class="fixed inset-0 z-40 cursor-default"
			onclick={() => (isDropdownOpen = false)}
			role="button"
			tabindex="-1"
			aria-hidden="true"
		></div>
		<ul
			class="absolute top-[calc(100%+0.5rem)] right-0 z-50 flex min-w-full flex-col overflow-hidden rounded-lg border border-border bg-card shadow-lg"
		>
			{#each levelOptions as option}
				<li class="w-full">
					<button
						class="w-full px-4 py-2 text-left text-sm text-card-foreground capitalize transition-colors outline-none hover:bg-border focus:bg-border"
						class:bg-border={selectedOption === option}
						onclick={() => {
							selectedOption = option;
							isDropdownOpen = false;
						}}
					>
						{option}
					</button>
				</li>
			{/each}
		</ul>
	{/if}
</div>
