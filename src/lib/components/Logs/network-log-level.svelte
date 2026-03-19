<script lang="ts">
	import Select from '../ui/select.svelte';
	import { wsStore } from '../../stores/websocket.svelte.ts';

	let selectedOption = $state('ALL');

	let levelOptions = ['ALL', 'INFO', 'WARN', 'ERROR'];

	$effect(() => {
		if (wsStore.isConnected) {
			wsStore.send({
				type: 'CHANGE_LOG_LEVEL',
				level: selectedOption
			});
		}
	});
</script>

<Select
	options={levelOptions}
	bind:selected={selectedOption}
	prefix="Network Log Level:"
	minWidthClass="w-auto min-w-56"
	capitalize={true}
/>
