import { defineConfig } from 'cypress'

export default defineConfig({
  e2e: {
    baseUrl: 'http://automationpractice.com/index.php',
    retries: 2,
    defaultCommandTimeout: 30000
  }
})
