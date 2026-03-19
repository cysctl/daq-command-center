<script lang="ts">
	import Select from '../ui/select.svelte';
	import { satellitesStore } from '../../stores/satellites.svelte.ts';
	import { logsState } from './store.svelte.ts';

	let senderOptions = $derived([
		'All',
		'Operator',
		...satellitesStore.satellites.map((s) => s.name)
	]);
</script>

<Select
	options={senderOptions}
	bind:selected={logsState.sender}
	prefix="Sender:"
	minWidthClass="w-auto min-w-44"
/>
