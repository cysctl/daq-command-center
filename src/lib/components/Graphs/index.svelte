<script lang="ts">
	import { Thermometer, Gauge, Zap } from '@lucide/svelte';
	import GraphCard from './graph-card.svelte';

	const cards = [
		{
			title: 'Temperature',
			icon: Thermometer,
			value: 25.6,
			unit: '°C',
			color: '#ef4444',
			data: [22.1, 23.4, 24.0, 23.8, 25.1, 24.6, 25.6]
		},
		{
			title: 'Pressure',
			icon: Gauge,
			value: 1013.2,
			unit: 'hPa',
			color: '#3b82f6',
			data: [1010.5, 1011.2, 1012.0, 1011.8, 1012.5, 1013.0, 1013.2]
		},
		{
			title: 'Voltage',
			icon: Zap,
			value: 3.31,
			unit: 'V',
			color: '#eab308',
			data: [3.28, 3.3, 3.29, 3.32, 3.3, 3.31, 3.31]
		}
	];
</script>

<section class="grid grid-cols-1 gap-5 lg:grid-cols-3">
	{#each cards as card}
		<GraphCard
			title={card.title}
			icon={card.icon}
			value={card.value}
			unit={card.unit}
			color={card.color}
			data={card.data}
		/>
	{/each}
</section>
