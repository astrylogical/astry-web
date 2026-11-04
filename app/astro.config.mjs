import { defineConfig } from 'astro/config';

export default defineConfig({
	site: 'https://info.astry.app',
	devToolbar: { enabled: false },
	// The site policy allows same-origin image files, not embedded data URLs.
	vite: { build: { assetsInlineLimit: 0 } }
});
