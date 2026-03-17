<script lang="ts">
	import { ChevronDown } from '@lucide/svelte';
	import type { Component } from 'svelte';
	import { tick } from 'svelte';
	import * as echarts from 'echarts';

	interface Props {
		title: string;
		icon: Component<{ size: number }>;
		value: number;
		unit: string;
		color: string;
		data: number[];
	}

	let { title, icon: Icon, value, unit, color, data }: Props = $props();

	let chartContainer: HTMLDivElement;
	let chart: echarts.ECharts | undefined;

	let isDropdownOpen = $state(false);
	let selectedOption = $state('Overview');

	// I will replace with actual satellite data source
	let satelliteOptions = ['Overview', 'Satellite 1'];

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
		chart.setOption(getChartOption(data, color));

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
		chart?.setOption(getChartOption(data, color));
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

		<div class="relative">
			<button
				onclick={() => (isDropdownOpen = !isDropdownOpen)}
				class="inline-flex cursor-pointer items-center gap-2 rounded-lg border border-border bg-card px-3 py-2 whitespace-nowrap hover:bg-border active:scale-95"
			>
				<span class="text-sm text-card-foreground">{selectedOption}</span>
				<span
					class="text-muted-foreground transition-transform duration-200"
					class:rotate-180={isDropdownOpen}
				>
					<ChevronDown size={17} />
				</span>
			</button>

			{#if isDropdownOpen}
				<div
					class="fixed inset-0 z-40 cursor-default"
					onclick={() => (isDropdownOpen = false)}
					role="button"
					tabindex="-1"
					aria-hidden="true"
				></div>
				<ul
					class="absolute top-[calc(100%+0.5rem)] right-0 z-50 flex min-w-35 flex-col overflow-hidden rounded-lg border border-border bg-card shadow-lg"
				>
					{#each satelliteOptions as option}
						<li class="w-full">
							<button
								class="w-full px-4 py-2 text-left text-sm text-card-foreground transition-colors outline-none hover:bg-border focus:bg-border"
								class:bg-border={selectedOption === option}
								onclick={() => {
									selectedOption = option;
									isDropdownOpen = false;
								}}
							>
								{option}
							</button>
						</li>
					{/each}
				</ul>
			{/if}
		</div>
	</div>

	<div>
		<div class="flex items-baseline gap-1">
			<span class="text-4xl font-semibold tracking-tight tabular-nums">{value}</span>
			<span class="text-lg text-muted-foreground">{unit}</span>
		</div>

		<div bind:this={chartContainer} class="mt-5 h-32 w-full overflow-hidden"></div>
	</div>
</div>
