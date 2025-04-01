<template>
  <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-md p-6">
    <h2 class="text-2xl font-bold text-indigo-600 mb-6">Comment Assistant</h2>
    
    <div class="mb-6">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="comment-platform">
        Select Platform
      </label>
      <select v-model="platform" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500">
        <option value="general">General</option>
        <option value="instagram">Instagram</option>
        <option value="twitter">Twitter</option>
        <option value="facebook">Facebook</option>
        <option value="linkedin">LinkedIn</option>
      </select>
    </div>

    <div class="mb-6">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="comment-tone">
        Select Response Tone
      </label>
      <select v-model="tone" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500">
        <option value="professional">Professional</option>
        <option value="friendly">Friendly</option>
        <option value="empathetic">Empathetic</option>
        <option value="humorous">Humorous</option>
        <option value="formal">Formal</option>
        <option value="casual">Casual</option>
      </select>
    </div>

    <div class="mb-6">
      <label class="block text-gray-700 text-sm font-bold mb-2" for="comment-input">
        Enter the Comment
      </label>
      <textarea 
        v-model="comment" 
        rows="4" 
        class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500" 
        placeholder="Paste the comment you want to respond to..."
      ></textarea>
    </div>

    <button 
      @click="generateCommentResponse" 
      class="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition duration-200"
    >
      Generate Response
    </button>

    <div v-if="result" class="mt-6">
      <h3 class="text-lg font-semibold mb-2">Suggested Response</h3>
      <div class="bg-gray-50 p-4 rounded-lg">{{ result.response }}</div>
      <div class="mt-4 text-sm text-gray-600">{{ result.explanation }}</div>
      <button 
        @click="copyCommentResponse" 
        class="mt-4 w-full bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition duration-200"
      >
        Copy Response
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const platform = ref('general')
const tone = ref('professional')
const comment = ref('')
const result = ref(null)

async function generateCommentResponse() {
  try {
    const response = await fetch('/api/generate-comment-response', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ 
        platform: platform.value, 
        tone: tone.value, 
        comment: comment.value 
      }),
    })

    const data = await response.json()
    result.value = data
  } catch (error) {
    console.error('Error:', error)
    alert('Failed to generate comment response. Please try again.')
  }
}

async function copyCommentResponse() {
  try {
    await navigator.clipboard.writeText(result.value.response)
    alert('Response copied to clipboard!')
  } catch (err) {
    console.error('Failed to copy response:', err)
    alert('Failed to copy response. Please try again.')
  }
}
</script> 