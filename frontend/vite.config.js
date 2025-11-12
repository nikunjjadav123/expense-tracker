import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
 
// ✅ only import devtools conditionally
const plugins = [vue()]

if (process.env.NODE_ENV === 'development') {
  try {
    const vueDevTools = (await import('vite-plugin-vue-devtools')).default
    plugins.push(vueDevTools())
  } catch (err) {
    console.warn('⚠️ Devtools not loaded:', err.message)
  }
}

// https://vitejs.dev/config/
export default defineConfig({
  plugins,
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
