export type SplitDirection = 'vertical' | 'horizontal';

class LayoutStore {
	splitDirection = $state<SplitDirection>('vertical');

	toggleSplitDirection() {
		this.splitDirection = this.splitDirection === 'vertical' ? 'horizontal' : 'vertical';
	}
}

export const layoutStore = new LayoutStore();
