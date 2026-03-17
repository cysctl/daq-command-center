<script lang="ts">
	import State from '../ui/state.svelte';
</script>

<div class="inline-flex items-center gap-1">
	<span class="hidden lg:block"> System State: </span>
	<span>
		<State state="INIT" />
	</span>
</div>
