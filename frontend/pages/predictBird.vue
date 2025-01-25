
<script setup>
const isOpen = ref(false);
const route = useRoute();
const links = [
  {
    label: 'Home',
    icon: 'ic:baseline-home',
    to: '/',
  },
  {
    label: 'Login/Register',
    icon: 'ic:baseline-login',
    to: '/login',
  },
];

watch(route, () => {
  isOpen.value = false
})


const router = useRouter()
  const {loggedIn, clear} = useUserSession()

  if(!loggedIn.value) {
    router.push('/login')
  }

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
    //if the type of the file is not an image, reset the value
    if (!imageFile.value.type.startsWith('image/')) {
      imageFile.value = null
      alert('Please upload an image file')
    }
    previewImage(event)
  }

  async function handleLogout(){
    await clear()
    router.push('/login')
  }
</script>
<template>
  <div>
    <nav class="relative text-white shadow-lg bg-gradient-to-r from-[#142001] to-[#243302] border-b-2 border-black">
      <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">

        <div class="text-2xl font-semibold flex items-center">
          <span>Bird Detection System</span>
        </div>

        <!-- Desktop Navigation Links -->
        <div class="hidden md:flex space-x-8">
          <NuxtLink to="/" class="text-white hover:bg-blue-700 px-4 py-2 rounded-md transition duration-300">Home
          </NuxtLink>
          <UButton v-if="!loggedIn" to="/login"
            class="text-white bg-yellow-400 hover:bg-yellow-500 px-6 py-2 rounded-md transition duration-300 font-semibold">
            Login</UButton>
            <UButton v-if="loggedIn" @click="handleLogout" class="text-white bg-yellow-400 hover:bg-yellow-500 px-6 py-2 rounded-md transition duration-300 font-semibold">LogOut</UButton>
        </div>

        <USlideover v-model="isOpen" class="xl:hidden">
          <UCard class="h-full bg-white rounded-none">
            <template #header>
              <h1 class="text-2xl font-semibold">
                Awe-WorkLogs
              </h1>
              <UButton size="sm" icon="ic:baseline-close" class="flex absolute end-5 top-5 z-10" variant="link"
                @click="isOpen = false" />
            </template>
            <UVerticalNavigation :links="links" />
          </UCard>
        </USlideover>

        <div class="md:hidden">
          <UIcon name="ic:baseline-menu" class="md:hidden w-10 h-10 cursor-pointer" @click="isOpen = true" />
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section
      class="relative bg-blue-600 text-white h-screen flex items-center justify-center  bg-[url('/public/heroBird.jpg')] bg-cover bg-right">
      <div class="absolute inset-0 bg-black opacity-40"></div>

      <!-- Content -->
      <div class="relative z-10 text-center space-y-6 px-6 md:px-12 max-w-4xl mx-auto">
        <h1 class="text-5xl font-semibold leading-tight md:text-6xl">
          Discover and Identify Birds with AI
        </h1>
        <p class="text-lg md:text-2xl">
          Our Bird Detection System uses cutting-edge technology to recognize bird species from images. Empowering bird
          watchers, researchers, and enthusiasts to explore the avian world like never before.
        </p>
      </div>
    </section>

    <div class="min-h-screen flex flex-col items-center text-xl text-slate-600 font-semibold p-20 bg-slate-100 space-y-10" id="detect-bird">
      <h1>Upload an Image for Bird Detection</h1>
  
      <!-- File upload input -->
      <div class="border-2 border-slate-600">
        <input
          type="file"
          class="text-gray-500 h-full font-medium text-sm bg-slate-100 file:cursor-pointer cursor-pointer file:border-0 file:py-2 file:px-4 file:mr-4 file:bg-gray-800 file:hover:bg-gray-700 file:text-white"
          id="imageInput"
          accept=".jpg, .jpeg, .png"
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
        <div class="result flex space-x-2">
          <img :src="previewImageUrl" width="500" alt="Preview" v-if="imageFile" />
          <img :src="resultImage" width="500" alt="Result" v-if="resultImage" />
        </div>
      <p v-if="resultText" v-html="resultText"></p>
    </div>

    <!-- Footer Section -->
    <footer id="contact" class="py-8 bg-slate-600 text-white text-center">
      <p>&copy; 2025 Bird Detection System. All rights reserved.</p>
    </footer>
  </div>
</template>
