<template>
  <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-md p-6">
    <h2 class="text-2xl font-bold text-indigo-600 mb-6">Hashtag Wizard</h2>
    
    <div class="mb-6">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="hashtag-platform">
        Select Platform
      </label>
      <select v-model="platform" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500">
        <option value="instagram">Instagram</option>
        <option value="twitter">Twitter</option>
        <option value="facebook">Facebook</option>
        <option value="linkedin">LinkedIn</option>
      </select>
    </div>

    <div class="mb-6">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="hashtag-topic">
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
      @click="generateHashtags" 
      class="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition duration-200"
    >
      Generate Hashtags
    </button>

    <div v-if="result" class="mt-6">
      <h3 class="text-lg font-semibold mb-2">Recommended Hashtags</h3>
      <div class="bg-gray-50 p-4 rounded-lg">{{ result.hashtags.join('\n') }}</div>
      <div class="mt-4 text-sm text-gray-600">{{ result.explanation }}</div>
      <button 
        @click="copyHashtags" 
        class="mt-4 w-full bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition duration-200"
      >
        Copy Hashtags
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const platform = ref('instagram')
const topic = ref('')
const result = ref(null)

async function generateHashtags() {
  try {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/api/generate-hashtags`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ platform: platform.value, topic: topic.value }),
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const data = await response.json()
    result.value = data
  } catch (error) {
    console.error('Error:', error)
    alert(`Failed to generate hashtags: ${error.message}. Please try again.`)
  }
}

async function copyHashtags() {
  try {
    await navigator.clipboard.writeText(result.value.hashtags.join('\n'))
    alert('Hashtags copied to clipboard!')
  } catch (err) {
    console.error('Failed to copy hashtags:', err)
    alert('Failed to copy hashtags. Please try again.')
  }
}
</script> 