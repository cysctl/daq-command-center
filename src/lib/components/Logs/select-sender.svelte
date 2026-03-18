<script lang="ts">
	import Select from '../ui/select.svelte';
	import { satellitesStore } from '../../stores/satellites.svelte.ts';

	let selectedOption = $state('All');

	let senderOptions = $derived(['All', ...satellitesStore.satellites.map((s) => s.name)]);
</script>

<Select
	options={senderOptions}
	bind:selected={selectedOption}
	prefix="Sender:"
	minWidthClass="w-auto min-w-44"
/>
