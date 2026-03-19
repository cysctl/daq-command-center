<script lang="ts">
	import type { Component } from 'svelte';
	import { tick } from 'svelte';
	import * as echarts from 'echarts';
	import Select from '../ui/select.svelte';
	import { satellitesStore } from '../../stores/satellites.svelte.ts';
	import { telemetryStore } from '../../stores/telemetry.svelte.ts';

	interface Props {
		title: string;
		icon: Component<{ size: number }>;
		unit: string;
		color: string;
	}

	let { title, icon: Icon, unit, color }: Props = $props();

	let chartContainer: HTMLDivElement;
	let chart: echarts.ECharts | undefined;

	let satelliteOptions = $derived(
		satellitesStore.satellites
			.filter((s) => {
				const t = title.toLowerCase();
				if (t.includes('temperature') || t.includes('pressure')) {
					return s.type === 'EnviroSensor';
				} else if (t.includes('voltage') || t.includes('power')) {
					return s.type === 'PowerSupply';
				}
				return true;
			})
			.map((s) => s.name)
	);

	let selectedOption = $state('');

	$effect(() => {
		if (satelliteOptions.length > 0 && !satelliteOptions.includes(selectedOption)) {
			selectedOption = satelliteOptions[0] || '';
		} else if (satelliteOptions.length === 0) {
			selectedOption = '';
		}
	});

	let chartData = $derived(
		selectedOption && telemetryStore.data[selectedOption]?.[title.toLowerCase()]
			? telemetryStore.data[selectedOption][title.toLowerCase()]
			: []
	);

	let displayValue = $derived(chartData.length > 0 ? chartData[chartData.length - 1] : null);

	function getChartOption(seriesData: number[], seriesColor: string): echarts.EChartsOption {
		return {
			grid: {
				top: 5,
				right: 0,
				bottom: 0,
				left: 0
			},
			xAxis: {
				type: 'category',
				show: false,
				boundaryGap: false,
				data: seriesData.map((_, i) => i)
			},
			yAxis: {
				type: 'value',
				show: false
			},
			series: [
				{
					type: 'line',
					data: seriesData,
					smooth: true,
					symbol: 'none',
					lineStyle: {
						color: seriesColor,
						width: 2
					},
					areaStyle: {
						color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
							{ offset: 0, color: seriesColor + '40' },
							{ offset: 1, color: seriesColor + '05' }
						])
					}
				}
			],
			tooltip: {
				trigger: 'axis',
				backgroundColor: 'hsl(var(--card))',
				borderColor: 'hsl(var(--border))',
				textStyle: {
					color: 'hsl(var(--card-foreground))',
					fontSize: 12
				},
				formatter: (params: any) => {
					const val = params[0]?.value;
					return `<strong>${val}</strong> ${unit}`;
				}
			}
		};
	}

	$effect(() => {
		if (!chartContainer) return;

		chart = echarts.init(chartContainer);
		chart.setOption(getChartOption(chartData, color), true);

		tick().then(() => chart?.resize());

		const resizeObserver = new ResizeObserver(() => {
			chart?.resize();
		});
		resizeObserver.observe(chartContainer);

		return () => {
			resizeObserver.disconnect();
			chart?.dispose();
		};
	});

	$effect(() => {
		chart?.setOption(getChartOption(chartData, color), true);
	});
</script>

<div
	class="flex flex-col gap-6 overflow-hidden rounded-xl border border-border bg-card p-6 text-card-foreground"
>
	<div class="flex items-center justify-between">
		<div class="inline-flex items-center gap-2">
			<span class="text-muted-foreground">
				<Icon size={17} />
			</span>

			<span class="text-muted-foreground">{title}</span>
		</div>

		<Select options={satelliteOptions} bind:selected={selectedOption} />
	</div>

	<div>
		<div class="flex items-baseline gap-1">
			<span class="text-4xl font-semibold tracking-tight tabular-nums">
				{displayValue !== null ? displayValue : '--'}
			</span>
			<span class="text-lg text-muted-foreground">{unit}</span>
		</div>

		<div bind:this={chartContainer} class="mt-5 h-32 w-full overflow-hidden"></div>
	</div>
</div>
