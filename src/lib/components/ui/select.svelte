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
	let buttonRef = $state<HTMLButtonElement | null>(null);
	let openUpwards = $state(false);

	function toggleDropdown() {
		if (!isDropdownOpen && buttonRef) {
			const rect = buttonRef.getBoundingClientRect();
			const spaceBelow = window.innerHeight - rect.bottom;
			const estimatedDropdownHeight = options.length * 40;

			if (spaceBelow < estimatedDropdownHeight && rect.top > estimatedDropdownHeight) {
				openUpwards = true;
			} else {
				openUpwards = false;
			}
		}
		isDropdownOpen = !isDropdownOpen;
	}
</script>

<div class="relative">
	<button
		bind:this={buttonRef}
		onclick={toggleDropdown}
		class="inline-flex {minWidthClass} cursor-pointer items-center justify-between gap-2 rounded-xl border border-border bg-card px-3 py-2 whitespace-nowrap outline-none hover:bg-border active:scale-95"
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
			onclick={() => {
				isDropdownOpen = false;
				openUpwards = false;
			}}
			role="button"
			tabindex="-1"
			aria-hidden="true"
		></div>
		<ul
			class="absolute right-0 z-50 flex min-w-full flex-col overflow-hidden rounded-xl border border-border bg-card shadow-lg"
			class:top-[calc(100%+0.5rem)]={!openUpwards}
			class:bottom-[calc(100%+0.5rem)]={openUpwards}
			class:min-w-35={!minWidthClass}
		>
			{#each options as option}
				<li class="w-full">
					<button
						class="w-full cursor-pointer px-4 py-2 text-left text-sm text-card-foreground transition-colors outline-none hover:bg-border focus:bg-border {capitalize
							? 'capitalize'
							: ''}"
						class:bg-border={selected === option}
						onclick={() => {
							selected = option;
							isDropdownOpen = false;
							openUpwards = false;
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
