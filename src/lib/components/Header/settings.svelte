<script lang="ts">
	import { Settings, X, Plug, Unplug, CircleCheck, CircleX, LoaderCircle } from '@lucide/svelte';
	import { fade, scale } from 'svelte/transition';
	import { wsStore } from '$lib/stores/websocket.svelte';

	let isOpen = $state(false);
	let host = $state('localhost');
	let port = $state('8765');

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
			class="relative z-10 max-h-[90vh] w-full max-w-4xl overflow-y-auto rounded-2xl border border-border bg-background p-6 md:p-8"
			transition:scale={{ duration: 200, start: 0.95 }}
			role="dialog"
		>
			<div class="mb-8 flex items-start justify-between">
				<div>
					<h2 class="text-2xl font-bold tracking-tight">Settings</h2>
					<p class="mt-1 text-sm text-muted-foreground">
						Configure WebSocket connection parameters
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
				<h3 class="text-sm font-semibold text-muted-foreground">Connection</h3>

				<div class="space-y-4 rounded-xl border border-border bg-card p-4">
					<div class="grid grid-cols-1 gap-4 md:grid-cols-[1fr_2fr_1fr]">
						<div class="flex flex-col gap-1.5">
							<label for="protocol" class="text-xs font-medium text-muted-foreground"
								>Protocol</label
							>
							<input
								id="protocol"
								type="text"
								value="ws://"
								class="cursor-not-allowed rounded-md border border-border bg-border px-3 py-2 text-sm text-foreground transition-colors focus:border-blue-500 focus:ring-1 focus:ring-blue-500 focus:outline-none"
								disabled
							/>
						</div>

						<div class="flex flex-col gap-1.5">
							<label for="host" class="text-xs font-medium text-muted-foreground">Host</label>
							<input
								id="host"
								type="text"
								bind:value={host}
								disabled={wsStore.isConnected || wsStore.isConnecting}
								class="rounded-md border border-border bg-background px-3 py-2 text-sm text-foreground transition-colors focus:border-blue-500 focus:ring-1 focus:ring-blue-500 focus:outline-none disabled:cursor-not-allowed disabled:opacity-50"
							/>
						</div>

						<div class="flex flex-col gap-1.5">
							<label for="port" class="text-xs font-medium text-muted-foreground">Port</label>
							<input
								id="port"
								type="text"
								bind:value={port}
								disabled={wsStore.isConnected || wsStore.isConnecting}
								class="rounded-md border border-border bg-background px-3 py-2 text-sm text-foreground transition-colors focus:border-blue-500 focus:ring-1 focus:ring-blue-500 focus:outline-none disabled:cursor-not-allowed disabled:opacity-50"
							/>
						</div>
					</div>

					<div class="rounded-md border border-border bg-background/50 px-4 py-3">
						<p class="mb-1 text-[10px] font-medium tracking-wider text-muted-foreground uppercase">
							Full URL
						</p>
						<code class="text-sm font-semibold text-blue-500">ws://{host}:{port}</code>
					</div>

					<div class="flex items-center gap-3 pt-2">
						{#if !wsStore.isConnected}
							<button
								class="flex cursor-pointer items-center gap-2 rounded-md bg-white px-4 py-2 text-sm font-semibold text-black transition-colors hover:bg-gray-100 focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-background focus:outline-none active:scale-95 disabled:cursor-not-allowed disabled:opacity-50"
								onclick={() => wsStore.connect(host, port)}
								disabled={wsStore.isConnecting}
							>
								{#if wsStore.isConnecting}
									<LoaderCircle class="animate-spin" size={17} />
									Testing...
								{:else}
									<Plug size={17} />
									Connect
								{/if}
							</button>
							{#if wsStore.error && !wsStore.isConnecting}
								<span class="flex items-center gap-1.5 text-sm font-medium text-red-500">
									<CircleX size={17} />
									Failed to connect to ws://{host}:{port}
								</span>
							{/if}
						{:else}
							<button
								class="flex cursor-pointer items-center gap-2 rounded-md bg-red-500 px-4 py-2 text-sm font-semibold text-white transition-colors hover:bg-red-600 focus:ring-2 focus:ring-red-500 focus:ring-offset-2 focus:ring-offset-background focus:outline-none active:scale-95"
								onclick={() => wsStore.disconnect()}
							>
								<Unplug size={17} />
								Disconnect
							</button>
							<span class="flex items-center gap-1.5 text-sm font-medium text-green-500">
								<CircleCheck size={17} />
								Successfully connected to ws://{host}:{port}
							</span>
						{/if}
					</div>
				</div>
			</div>
		</div>
	</div>
{/if}
