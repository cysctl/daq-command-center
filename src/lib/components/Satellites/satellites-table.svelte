<script>
	import State from '../ui/state.svelte';
</script>

<table class="w-full caption-bottom text-sm whitespace-nowrap">
	<thead class="border-b border-border">
		<tr
			class="text-left text-xs font-medium tracking-wider text-muted-foreground uppercase [&_th]:px-3 [&_th]:py-2"
		>
			<th>Type</th>
			<th>Name</th>
			<th class="w-[10%]">State</th>
			<th class="w-[35%]">Last Message</th>
			<th>Heartbeat</th>
			<th class="w-[8%]">Lives</th>
			<th class="w-[20%] text-right">Actions</th>
		</tr>
	</thead>
	<tbody class="divide-y divide-border [&_td]:px-3 [&_td]:py-2">
		<tr class="transition-colors hover:bg-muted/50">
			<td class="font-mono text-sm text-muted-foreground">Sputnik</td>
			<td class="text-sm font-medium">TestSatellite1</td>
			<td>
				<State state="NEW" />
			</td>
			<td>
				<div class="flex flex-col">
					<span class="text-sm">Waiting..</span>
					<span class="text-xs leading-tight text-muted-foreground">Just now</span>
				</div>
			</td>
			<td class="text-sm text-muted-foreground">500ms</td>
			<td class="text-sm text-muted-foreground">3</td>
			<td class="text-right"> Test </td>
		</tr>
	</tbody>
</table>
