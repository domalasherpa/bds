<template>
    <div class="min-h-screen flex flex-col items-center text-xl text-slate-600 font-semibold p-20 bg-slate-100 space-y-10">
      <h1 class="text-3xl">Bird Detection</h1>
      <h1>Upload an Image for Bird Detection</h1>
  
      <!-- File upload input -->
      <div class="border-2 border-slate-600">
        <input
          type="file"
          class="text-gray-500 h-full font-medium text-sm bg-slate-100 file:cursor-pointer cursor-pointer file:border-0 file:py-2 file:px-4 file:mr-4 file:bg-gray-800 file:hover:bg-gray-700 file:text-white"
          id="imageInput"
          accept="image/*"
          @change="handleFileChange"
          required
        />
        <button @click="uploadImage(imageFile)" class="bg-green-400 px-10 py-2">Detect</button>
      </div>

      <!-- Loading Spinner -->
      <div v-if="loading" class="text-center mt-4">
        <div class="w-12 h-12 border-4 border-t-4 border-gray-400 border-t-transparent rounded-full animate-spin mx-auto"></div>
        <p>Processing...</p>
      </div>
  
      <!-- Result Images and Text -->
      <div class="result flex space-x-2" v-if="resultImage">
        <img :src="previewImageUrl" width="500" alt="Preview" />
        <img :src="resultImage" width="500" alt="Result" />
      </div>
  
      <p v-if="resultText" v-html="resultText"></p>
    </div>
  </template>
  
  <script setup>
  // Importing the composable
  import useBirdDetection from '~/composables/useBirdDetection'
  
  // Using the composable API
  const {
    previewImageUrl,
    resultImage,
    resultText,
    loading,
    previewImage,
    uploadImage
  } = useBirdDetection()
  
  // To store the selected file for the upload action
  const imageFile = ref()
  
  const handleFileChange = (event) => {
    imageFile.value = event.target.files[0]
    previewImage(event)
  }
  </script>
  
  <style scoped>
  /* Add your custom styles here */
  </style>
  