<script lang="ts">
	import Select from '../ui/select.svelte';

	let selectedOption = $state('ALL');

	// I will replace with actual log level options
	let levelOptions = ['ALL', 'INFO', 'WARNING', 'ERROR'];
</script>

<Select
	options={levelOptions}
	bind:selected={selectedOption}
	prefix="Network Log Level:"
	minWidthClass="w-auto min-w-56"
	capitalize={true}
/>
