<script lang="ts">
	import { ChevronDown } from '@lucide/svelte';

	type Props = {
		options: string[];
		selected?: string;
		prefix?: string;
		minWidthClass?: string;
		capitalize?: boolean;
		onSelect?: (option: string) => void;
	};

	let {
		options,
		selected = $bindable(options[0]),
		prefix = '',
		minWidthClass = '',
		capitalize = false,
		onSelect
	}: Props = $props();

	let isDropdownOpen = $state(false);
</script>

<div class="relative">
	<button
		onclick={() => (isDropdownOpen = !isDropdownOpen)}
		class="inline-flex {minWidthClass} cursor-pointer items-center justify-between gap-2 rounded-lg border border-border bg-card px-3 py-2 whitespace-nowrap outline-none hover:bg-border active:scale-95"
	>
		<span class="text-sm text-card-foreground">
			{#if prefix}
				<span class="mr-1 text-muted-foreground">{prefix}</span>
			{/if}
			<span class={capitalize ? 'capitalize' : ''}>{selected}</span>
		</span>
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
			class:min-w-35={!minWidthClass}
		>
			{#each options as option}
				<li class="w-full">
					<button
						class="w-full px-4 py-2 text-left text-sm text-card-foreground transition-colors outline-none hover:bg-border focus:bg-border {capitalize
							? 'capitalize'
							: ''}"
						class:bg-border={selected === option}
						onclick={() => {
							selected = option;
							isDropdownOpen = false;
							onSelect?.(option);
						}}
					>
						{option}
					</button>
				</li>
			{/each}
		</ul>
	{/if}
</div>
