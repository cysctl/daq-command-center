export type LogEntry = {
	id: number;
	timestamp: string;
	level: string;
	sender: string;
	message: string;
};

class LogStore {
	logs = $state<LogEntry[]>([]);
	private nextId = 1;

	addLog(sender: string, level: string, message: string, timestamp: string) {
		this.logs.push({
			id: this.nextId++,
			timestamp,
			level,
			sender,
			message
		});
		
		// store max 1000 logs
		if (this.logs.length > 1000) {
			this.logs.shift();
		}
	}

	clear() {
		this.logs = [];
		this.nextId = 1;
	}
}

export const logStore = new LogStore();
