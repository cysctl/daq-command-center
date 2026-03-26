<script lang="ts">
	type Log = {
		id: number;
		timestamp: string;
		level: string;
		sender: string;
		message: string;
	};

	let { log }: { log: Log } = $props();

	function getLevelColor(level: string) {
		switch (level) {
			case 'INFO':
				return 'text-blue-500/90 dark:text-blue-400';
			case 'STATUS':
				return 'text-emerald-500/90 dark:text-emerald-400';
			case 'WARNING':
				return 'text-amber-500/90 dark:text-amber-400';
			case 'CRITICAL':
				return 'text-red-500/90 dark:text-red-400';
			case 'TRACE':
				return 'text-purple-500/90 dark:text-purple-400';
			case 'DEBUG':
			default:
				return 'text-muted-foreground';
		}
	}

	function getRowBackground(level: string) {
		switch (level) {
			case 'STATUS':
				return 'bg-emerald-500/10';
			case 'WARNING':
				return 'bg-amber-500/10';
			case 'CRITICAL':
				return 'bg-red-500/10';
			default:
				return '';
		}
	}
</script>

<div
	class="group flex flex-col gap-1 rounded px-2 py-1 transition-colors hover:bg-secondary/40 sm:flex-row sm:items-start sm:gap-3 {getRowBackground(
		log.level
	)}"
>
	<div class="flex w-full shrink-0 items-center gap-2 sm:w-auto sm:shrink-0">
		<span class="shrink-0 text-muted-foreground/70 select-none">[{log.timestamp}]</span>
		<span class="w-18 shrink-0 font-bold select-none {getLevelColor(log.level)}">
			{log.level}
		</span>
		<span class="w-24 shrink-0 truncate text-muted-foreground sm:hidden">
			{log.sender}:
		</span>
	</div>

	<div class="flex flex-1 items-start gap-2">
		<span class="hidden w-24 shrink-0 truncate text-muted-foreground select-none sm:block">
			{log.sender}:
		</span>
		<span class="wrap-break-words flex-1 pl-4 whitespace-pre-wrap text-foreground sm:pl-0">
			{log.message}
		</span>
	</div>
</div>
