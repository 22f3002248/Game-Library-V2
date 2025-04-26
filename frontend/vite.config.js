import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: true, // 👈 allows external access
    hmr: {
      protocol: 'wss', // or 'ws' if not using https
      host: 'localhost',
    },
    allowedHosts: ['all'], // 👈 works in older Vite
    // Fallback if that fails, use 'originIsAllowed' in connect middleware
    originIsAllowed: () => true, // 👈 hacky workaround for new Vite
  },
})
