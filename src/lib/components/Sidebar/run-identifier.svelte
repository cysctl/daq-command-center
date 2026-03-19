<script lang="ts">
	import { Settings2, X, Save } from '@lucide/svelte';
	import { fade, scale } from 'svelte/transition';

	let isOpen = $state(false);
	let prefix = $state('run');
	let sequence = $state('15');

	function close() {
		isOpen = false;
	}

	function portal(node: HTMLElement) {
		document.body.appendChild(node);
		return {
			destroy() {
				node.remove();
			}
		};
	}
</script>

<div
	class="flex items-center justify-between rounded-md border border-border bg-secondary px-3 py-1"
>
	<div>
		<div>
			<span class="text-sm text-muted-foreground">Run Prefix: </span>
			<span class="font-mono text-sm text-foreground">{prefix}</span>
		</div>
		<div>
			<span class="text-sm text-muted-foreground">Sequence: </span>
			<span class="font-mono text-sm text-foreground">{sequence}</span>
		</div>
	</div>
	<button
		class="h-fit cursor-pointer rounded-lg p-1 text-muted-foreground hover:bg-border active:scale-95"
		onclick={() => (isOpen = true)}
	>
		<Settings2 size={17} />
	</button>
</div>

{#if isOpen}
	<div class="fixed inset-0 z-60 flex items-center justify-center" use:portal>
		<button
			class="absolute inset-0 cursor-default bg-black/60 backdrop-blur-sm"
			transition:fade={{ duration: 200 }}
			onclick={close}
			onkeydown={(e) => e.key === 'Escape' && close()}
			aria-label="Close settings"
		></button>

		<div
			class="relative z-10 max-h-[90vh] w-full max-w-lg overflow-y-auto rounded-2xl border border-border bg-background p-6 md:p-8"
			transition:scale={{ duration: 200, start: 0.95 }}
			role="dialog"
		>
			<div class="mb-8 flex items-start justify-between">
				<div>
					<h2 class="text-2xl font-bold tracking-tight">Run Identifier</h2>
					<p class="mt-1 text-sm text-muted-foreground">
						Configure current run prefix and sequence parameters
					</p>
				</div>
				<button
					class="h-fit cursor-pointer rounded-lg p-1 text-muted-foreground transition-colors hover:bg-border active:scale-95"
					onclick={close}
					aria-label="Close"
				>
					<X size={17} />
				</button>
			</div>

			<div class="space-y-4">
				<h3 class="text-sm font-semibold text-muted-foreground">Configuration</h3>

				<div class="space-y-4 rounded-xl border border-border bg-card p-4">
					<div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
						<div class="flex flex-col gap-1.5">
							<label for="prefix" class="text-xs font-medium text-muted-foreground">Prefix</label>
							<input
								id="prefix"
								type="text"
								bind:value={prefix}
								class="rounded-md border border-border bg-background px-3 py-2 text-sm text-foreground transition-colors focus:border-blue-500 focus:ring-1 focus:ring-blue-500 focus:outline-none"
							/>
						</div>

						<div class="flex flex-col gap-1.5">
							<label for="sequence" class="text-xs font-medium text-muted-foreground"
								>Sequence</label
							>
							<input
								id="sequence"
								type="number"
								bind:value={sequence}
								class="rounded-md border border-border bg-background px-3 py-2 text-sm text-foreground transition-colors focus:border-blue-500 focus:ring-1 focus:ring-blue-500 focus:outline-none"
							/>
						</div>
					</div>

					<div class="pt-2">
						<button
							class="flex cursor-pointer items-center gap-2 rounded-md bg-white px-4 py-2 text-sm font-semibold text-black transition-colors hover:bg-gray-100 focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-background focus:outline-none active:scale-95"
							onclick={close}
						>
							<Save size={17} />
							Save
						</button>
					</div>
				</div>
			</div>
		</div>
	</div>
{/if}
