<script lang="ts">
	import Select from '../ui/select.svelte';

	let selectedLevel = $state('INFO');

	let levelOptions = ['INFO', 'WARN', 'ERROR'];
</script>

<div>
	<input type="text" placeholder="Enter operator note..." />
	<Select
		options={levelOptions}
		bind:selected={selectedLevel}
		minWidthClass="w-32"
		capitalize={true}
	/>
	<button>Send</button>
</div>
