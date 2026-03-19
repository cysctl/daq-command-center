<script lang="ts">
	import { Thermometer, Gauge, Zap } from '@lucide/svelte';
	import GraphCard from './graph-card.svelte';

	const cards = [
		{
			title: 'Temperature',
			icon: Thermometer,
			unit: '°C',
			color: '#ef4444'
		},
		{
			title: 'Pressure',
			icon: Gauge,
			unit: 'hPa',
			color: '#3b82f6'
		},
		{
			title: 'Voltage',
			icon: Zap,
			unit: 'V',
			color: '#eab308'
		}
	];
</script>

<section class="grid grid-cols-1 gap-5 lg:grid-cols-3">
	{#each cards as card}
		<GraphCard title={card.title} icon={card.icon} unit={card.unit} color={card.color} />
	{/each}
</section>
