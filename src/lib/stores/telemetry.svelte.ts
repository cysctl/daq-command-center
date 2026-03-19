class TelemetryStore {
	data = $state<Record<string, Record<string, number[]>>>({});

	addTelemetry(satelliteId: string, metrics: Record<string, number>) {
		if (!this.data[satelliteId]) {
			this.data[satelliteId] = {};
		}
		for (const [key, value] of Object.entries(metrics)) {
			if (!this.data[satelliteId][key]) {
				this.data[satelliteId][key] = [];
			}
			this.data[satelliteId][key].push(value);
			// remove old data if array length > 30
			if (this.data[satelliteId][key].length > 30) {
				this.data[satelliteId][key].shift();
			}
		}
	}

	clear() {
		this.data = {};
	}
}

export const telemetryStore = new TelemetryStore();
