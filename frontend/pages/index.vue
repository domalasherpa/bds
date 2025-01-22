<!-- <script setup lang="ts">
</script>

<template>
  <div class="space-y-20">
    <div class="flex">
      <div class="flex-1 flex flex-col justify-center px-4 space-y-4 bg-gradient-to-r from-green-300">
        <h1 class="text-8xl">Bird Vision <br />Tech:</h1>
        <p class="text-3xl italic">
          Our mission is to provide a platform for birdwatchers to identify birds in real-time using machine learning.
        </p>
      </div>
      <div class="flex-1">
        <img src="/public/heroBird.jpg" alt="" class="h-full w-full">
      </div>
    </div>

    <div class="min-h-screen">
      <div class="flex flex-col items-center space-y-10 bg-white px-10">
        <h1>Experience the magic of learning by cutting-edge Ai technology</h1>
        <p>
          Bird Vision tech allows bird enthusiasta to identify birds in real-time using machine learning.
          Just take a picture of a bird and our Ai will identify the bird for you.
        </p>
      </div>
      <div>
        <div>

        </div>
        <div>

        </div>
        <div>

        </div>
      </div>

    </div>

    <div class="min-h-screen">
      <h1>How it works</h1>
      <p>
        Bird Vision tech uses a machine learning model to identify birds in real-time.
        The model is trained on a dataset of 1000+ bird species and can identify birds with an accuracy of 90%.
      </p>
    </div>

    <div>
      <h1>Get started</h1>
      <p>
        Experience the joy of bird-watching and let Bird Vision tech help you identify birds in real-time.
        Get started by signing up for an account and start using our platform today.
      </p>
      <ULink href="/signup" class="bg-blue-500 text-white p-4 rounded-md">Sign up</ULink>
    </div>
  </div>
</template>

<style scoped>

.customGradient{
  /* background-color: linear-gradient(to right bottom, #3e5703, #577905, #719e08, #8cc40d, #a8eb12); */
  background-color: yellow;
}
</style> -->

<template>
  <div>
    <!-- Navigation Bar -->
    <!-- <nav class="bg-blue-600 text-white shadow-md">
      <div class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex justify-between items-center">
          <div class="text-2xl font-semibold flex items-center space-x-2">
            <img src="/public/logo.png" alt="Bird Detection System" class="h-24"/>
            Bird Detection System
          </div>
          <div class="hidden md:flex space-x-6">
            <NuxtLink to="/" class="text-white hover:bg-blue-700 px-4 py-2 rounded-md">Home</NuxtLink>
            <NuxtLink to="#try-system" class="text-white hover:bg-blue-700 px-4 py-2 rounded-md">How It Works</NuxtLink>
            <NuxtLink to="#team" class="text-white hover:bg-blue-700 px-4 py-2 rounded-md">Team</NuxtLink>
            <UButton to="/login" class="text-white hover:bg-blue-700 px-4 py-2 rounded-md" :color="yellow">Login/Register</UButton>
          </div>
          <div class="md:hidden">
            <button @click="toggleMenu" class="text-white">Menu</button>
          </div>
        </div>
      </div> -->

      <!-- Mobile Menu
      <div v-if="isMenuOpen" class="md:hidden bg-blue-600 text-white px-6 py-4">
        <NuxtLink to="/" class="block py-2">Home</NuxtLink>
        <NuxtLink to="#try-system" class="block py-2">How It Works</NuxtLink>
        <NuxtLink to="#team" class="block py-2">Team</NuxtLink>
        <NuxtLink to="#contact" class="block py-2">Contact</NuxtLink>
        <NuxtLink to="/login" class="block py-2">Login/Register</NuxtLink>
      </div>
    </nav> -->

    <nav class="relative text-white shadow-lg bg-gradient-to-r from-[#142001] to-[#243302] border-b-2 border-black">
  <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
    <!-- Logo and Brand Name -->
    <div class="text-2xl font-semibold flex items-center">
      <span>Bird Detection System</span>
    </div>

    <!-- Desktop Navigation Links -->
    <div class="hidden md:flex space-x-8">
      <NuxtLink to="/" class="text-white hover:bg-blue-700 px-4 py-2 rounded-md transition duration-300">Home</NuxtLink>
      <NuxtLink to="#try-system" class="text-white hover:bg-blue-700 px-4 py-2 rounded-md transition duration-300">How It Works</NuxtLink>
      <NuxtLink to="#team" class="text-white hover:bg-blue-700 px-4 py-2 rounded-md transition duration-300">Team</NuxtLink>
      <!-- Login/Register Button -->
      <UButton to="/login" class="text-white bg-yellow-400 hover:bg-yellow-500 px-6 py-2 rounded-md transition duration-300 font-semibold">Login/Register</UButton>
    </div>

    <!-- Mobile Menu Button -->
    <div class="md:hidden">
      <button @click="toggleMenu" class="text-white text-xl focus:outline-none">
        <i class="fas fa-bars"></i> <!-- Hamburger Icon -->
      </button>
    </div>
  </div>

  <!-- Mobile Menu -->
  <div v-if="isMenuOpen" class="md:hidden bg-blue-600 text-white px-6 py-4 space-y-4">
    <NuxtLink to="/" class="block py-2 text-lg">Home</NuxtLink>
    <NuxtLink to="#try-system" class="block py-2 text-lg">How It Works</NuxtLink>
    <NuxtLink to="#team" class="block py-2 text-lg">Team</NuxtLink>
    <NuxtLink to="/login" class="block py-2 text-lg">Login/Register</NuxtLink>
  </div>
</nav>


    <!-- Hero Section -->
    <section class="relative bg-blue-600 text-white h-screen flex items-center justify-center  bg-[url('/public/heroBird.jpg')] bg-cover bg-right"
    >
      <!-- Background Image with opacity -->
      <div class="absolute inset-0 bg-black opacity-40"></div>
      <!-- <div class="absolute inset-0 bg-cover bg-center" :style="`background-image: url('${backgroundImage}')`"></div> -->
      
      <!-- Content -->
      <div class="relative z-10 text-center space-y-6 px-6 md:px-12 max-w-4xl mx-auto">
        <h1 class="text-5xl font-semibold leading-tight md:text-6xl">
          Discover and Identify Birds with AI
        </h1>
        <p class="text-lg md:text-2xl">
          Our Bird Detection System uses cutting-edge technology to recognize bird species from images or videos. Empowering bird watchers, researchers, and enthusiasts to explore the avian world like never before.
        </p>

        <!-- Call to Action Buttons -->
        <div class="flex justify-center space-x-4 mt-8">
          <NuxtLink to="#try-system" class="bg-yellow-400 text-blue-600 font-semibold py-3 px-6 rounded-lg text-xl hover:bg-yellow-500 transition duration-300">
            Try It Now
          </NuxtLink>
          <NuxtLink to="#learn-more" class="bg-transparent border-2 border-white text-white font-semibold py-3 px-6 rounded-lg text-xl hover:bg-white hover:text-blue-600 transition duration-300">
            Learn More
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Try System Section -->
    <div class="bg-gray-50 min-h-screen ">
    <!-- How It Works Section -->
    <section class="py-16 px-8 text-center text-slate-600">
      <h2 class="text-4xl font-semibold mb-8">How It Works</h2>
      <p class="text-lg mb-12">
        Our Bird Detection System uses AI to identify bird species from images. Here’s a simple step-by-step guide to using the system.
      </p>

      <!-- Steps Section -->
      <div class="space-y-12 flex flex-col items-center">
        <!-- Step 1: Login -->
        <div class="flex items-center justify-center space-x-6 w-4/5">
          <div class="bg-slate-400 text-white p-6 rounded-lg shadow-lg ">
            <h3 class="text-xl font-semibold mb-4">Step 1: Login to Your Account</h3>
            <p>
              To get started, please sign in to your account. If you don't have an account, you can easily sign up and join the community.
            </p>
          </div>
        </div>

        <!-- Step 2: Upload Image or Video -->
        <div class="flex items-center justify-center space-x-6 w-4/5">
          <div class="bg-slate-400 text-white p-6 rounded-lg shadow-lg ">
            <h3 class="text-xl font-semibold mb-4">Step 2: Upload Image or Video</h3>
            <p>
              After logging in, you can upload an image or a video of a bird. Our system supports multiple file formats for easy use.
            </p>
          </div>
        </div>

        <!-- Step 3: AI Analysis -->
        <div class="flex items-center justify-center space-x-6 w-4/5">
          <div class="bg-slate-400 text-white p-6 rounded-lg shadow-lg ">
            <h3 class="text-xl font-semibold mb-4">Step 3: AI Analysis</h3>
            <p>
              The system uses AI to analyze the uploaded image or video. It recognizes key features of the bird to determine its species.
            </p>
          </div>
        </div>

        <!-- Step 4: Bird Identification -->
        <div class="flex items-center justify-center space-x-6 w-4/5">
          <div class="bg-slate-400 text-white p-6 rounded-lg shadow-lg ">
            <h3 class="text-xl font-semibold mb-4">Step 4: Bird Identification</h3>
            <p>
              Once the analysis is complete, the system will identify the species of the bird and display detailed information about it.
            </p>
          </div>
        </div>
      </div>
    </section>
    </div>

    <!-- Team Section -->
    <section id="team" class="h-screen py-16 px-8 text-center text-slate-600 space-y-24">
      <h2 class="text-3xl font-semibold mb-8">Meet the Team</h2>
      <div class="flex justify-evenly gap-10 w-3/5 items-center mx-auto">
        <div class="bg-white p-6 rounded-lg shadow-lg space-y-4">
          <img src="/public/avatar.png" alt="Team Member" class="h-52 w-full">
          <h3 class="text-xl font-semibold">Domala Sherpa</h3>
          <p class="text-lg text-gray-600">TU Roll No.(26713)</p>
          <p class="text-lg text-gray-600">Bsc.Csit 7th semester</p>
          <p class="text-lg text-gray-600">Asian College Of Higher Studies</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-lg space-y-4">
          <img src="/public/avatar.png" alt="Team Member" class="h-52 w-full">
          <h3 class="text-xl font-semibold">Ronisha oli</h3>
          <p class="text-lg text-gray-600">TU Roll No.(26729)</p>
          <p class="text-lg text-gray-600">Bsc.Csit 7th semester</p>
          <p class="text-lg text-gray-600">Asian College Of Higher Studies</p>
        </div>
      </div>
    </section>

    <!-- Footer Section -->
    <footer id="contact" class="py-8 bg-slate-600 text-white text-center">
      <p>&copy; 2025 Bird Detection System. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backgroundImage: '/public/heroBird.jpg', // Replace with actual image URL
      isMenuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    }
  }
};
</script>

<style scoped>
/* Add custom styles here if necessary */
</style>
