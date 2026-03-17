<script lang="ts">
	type Props = {
		connStatus: 'connected' | 'disconnected';
	};

	let { connStatus }: Props = $props();
</script>

<div class="inline-flex items-center gap-2">
	<div
		class="size-2 animate-pulse rounded-full {connStatus === 'connected'
			? 'bg-state-run'
			: 'bg-red-500'}"
	></div>

	<span class="hidden lg:block">
		{connStatus === 'connected' ? 'Connected' : 'Disconnected'}
	</span>
</div>
