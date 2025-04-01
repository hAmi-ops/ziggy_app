<template>
  <div class="min-h-screen bg-gray-100">
    <nav class="bg-white shadow-lg">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex justify-between h-16">
          <div class="flex">
            <div class="flex-shrink-0 flex items-center">
              <h1 class="text-xl font-bold text-gray-800">Ziggy</h1>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="container mx-auto px-4 py-8">
      <header class="text-center mb-12">
        <h1 class="text-4xl font-bold text-indigo-600 mb-2">Ziggy</h1>
        <p class="text-gray-600">Your AI Social Media Assistant</p>
      </header>

      <!-- Main Content Tabs -->
      <div class="max-w-2xl mx-auto mb-8">
        <div class="flex space-x-4 justify-center">
          <button 
            v-for="tab in tabs" 
            :key="tab.id"
            @click="currentTab = tab.id"
            :class="['tab-button px-4 py-2 rounded-lg', currentTab === tab.id ? 'bg-indigo-700' : 'bg-indigo-600', 'text-white']"
          >
            {{ tab.name }}
          </button>
        </div>
      </div>

      <!-- Tab Contents -->
      <div v-for="tab in tabs" :key="tab.id" :id="tab.id" :class="['tab-content', currentTab !== tab.id ? 'hidden' : '']">
        <component :is="tab.component"></component>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import PostGenerator from './components/PostGenerator.vue'
import HashtagWizard from './components/HashtagWizard.vue'
import CommentAssistant from './components/CommentAssistant.vue'

const currentTab = ref('post-generator')

const tabs = [
  { id: 'post-generator', name: 'Post Generator', component: PostGenerator },
  { id: 'hashtag-wizard', name: 'Hashtag Wizard', component: HashtagWizard },
  { id: 'comment-assistant', name: 'Comment Assistant', component: CommentAssistant }
]
</script> 