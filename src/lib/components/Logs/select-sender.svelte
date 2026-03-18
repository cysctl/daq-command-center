<script lang="ts">
	import Select from '../ui/select.svelte';

	let selectedOption = $state('All');

	// I will replace with actual satellite data source
	let senderOptions = ['All', 'Satellite 1'];
</script>

<Select
	options={senderOptions}
	bind:selected={selectedOption}
	prefix="Sender:"
	minWidthClass="w-auto min-w-44"
/>
