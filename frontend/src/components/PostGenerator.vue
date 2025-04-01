<template>
  <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-md p-6">
    <div class="mb-6">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="platform">
        Select Platform
      </label>
      <select v-model="platform" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500">
        <option value="twitter">Twitter</option>
        <option value="facebook">Facebook</option>
        <option value="instagram">Instagram</option>
        <option value="linkedin">LinkedIn</option>
      </select>
    </div>

    <div class="mb-6">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="topic">
        Topic or Theme
      </label>
      <input 
        v-model="topic" 
        type="text" 
        class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500" 
        placeholder="Enter your topic..."
      >
    </div>

    <button 
      @click="generatePost" 
      class="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition duration-200"
    >
      Generate Post
    </button>

    <div v-if="result" class="mt-6">
      <h3 class="text-lg font-semibold mb-2">Generated Post</h3>
      <div class="bg-gray-50 p-4 rounded-lg">{{ result }}</div>
      <button 
        @click="schedulePost" 
        class="mt-4 w-full bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition duration-200"
      >
        Schedule Post
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const platform = ref('twitter')
const topic = ref('')
const result = ref('')

async function generatePost() {
  try {
    const response = await fetch('/api/generate-post', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ platform: platform.value, topic: topic.value }),
    })

    const data = await response.json()
    result.value = data.content
  } catch (error) {
    console.error('Error:', error)
    alert('Failed to generate post. Please try again.')
  }
}

async function schedulePost() {
  try {
    const response = await fetch('/api/schedule-post', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        platform: platform.value,
        content: result.value,
        scheduled_time: new Date().toISOString(),
      }),
    })

    const data = await response.json()
    alert('Post scheduled successfully!')
  } catch (error) {
    console.error('Error:', error)
    alert('Failed to schedule post. Please try again.')
  }
}
</script> 