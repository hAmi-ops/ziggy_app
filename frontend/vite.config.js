import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Get the API URL from environment variable or use default
const apiUrl = process.env.VITE_API_URL || 'http://localhost:8000'

export default defineConfig({
  plugins: [vue()],
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    rollupOptions: {
      input: {
        main: '/index.html'
      }
    }
  },
  server: {
    proxy: {
      '/api': {
        target: apiUrl,
        changeOrigin: true,
        secure: false
      }
    }
  },
  define: {
    'process.env.VITE_API_URL': JSON.stringify(apiUrl)
  }
}) 