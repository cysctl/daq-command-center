<script lang="ts">
	import State from '../ui/state.svelte';
	import SatelliteStateButton from './satellite-state-button.svelte';
</script>

<div class="flex flex-col gap-1">
	<div>
		<span>Satellite Name</span>
		<State state="NEW" />
	</div>
	<span>Uptime: -</span>
	<div>
		<SatelliteStateButton />
	</div>
</div>
