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
    label: 'How It Works',
    icon: 'ic:baseline-info',
    to: '#try-system',
  },
  {
    label: 'Team',
    icon: 'ic:baseline-group',
    to: '#team',
  },
  {
    label: 'Contact',
    icon: 'ic:baseline-email',
    to: '#contact',
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
          <NuxtLink to="#try-system" class="text-white hover:bg-blue-700 px-4 py-2 rounded-md transition duration-300">
            How It Works</NuxtLink>
          <NuxtLink to="#team" class="text-white hover:bg-blue-700 px-4 py-2 rounded-md transition duration-300">Team
          </NuxtLink>
          <UButton to="/login"
            class="text-white bg-yellow-400 hover:bg-yellow-500 px-6 py-2 rounded-md transition duration-300 font-semibold">
            Login</UButton>
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

        <!-- Call to Action Buttons -->
        <div class="flex justify-center space-x-4 mt-8">
          <NuxtLink to="/register"
            class="bg-yellow-400 text-blue-600 font-semibold py-3 px-6 rounded-lg text-xl hover:bg-yellow-500 transition duration-300">
            Try It Now
          </NuxtLink>
          <NuxtLink to="#learn-more"
            class="bg-transparent border-2 border-white text-white font-semibold py-3 px-6 rounded-lg text-xl hover:bg-white hover:text-blue-600 transition duration-300">
            Learn More
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Try System Section -->
    <div class="bg-gray-50 min-h-screen" id="try-system">
      <!-- How It Works Section -->
      <section class="py-16 px-8 text-center text-slate-600">
        <h2 class="text-4xl font-semibold mb-8">How It Works</h2>
        <p class="text-lg mb-12">
          Our Bird Detection System uses AI to identify bird species from images. Here’s a simple step-by-step guide to
          using the system.
        </p>

        <!-- Steps Section -->
        <div class="space-y-12 flex flex-col items-center">
          <!-- Step 1: Login -->
          <div class="flex items-center justify-center space-x-6 w-4/5">
            <div class="bg-slate-400 text-white p-6 rounded-lg shadow-lg ">
              <h3 class="text-xl font-semibold mb-4">Step 1: Login to Your Account</h3>
              <p>
                To get started, please sign in to your account. If you don't have an account, you can easily sign up and
                join the community.
              </p>
            </div>
          </div>

          <!-- Step 2: Upload Image or Video -->
          <div class="flex items-center justify-center space-x-6 w-4/5">
            <div class="bg-slate-400 text-white p-6 rounded-lg shadow-lg ">
              <h3 class="text-xl font-semibold mb-4">Step 2: Upload Image or Video</h3>
              <p>
                After logging in, you can upload an image or a video of a bird. Our system supports multiple file
                formats
                for easy use.
              </p>
            </div>
          </div>

          <!-- Step 3: AI Analysis -->
          <div class="flex items-center justify-center space-x-6 w-4/5">
            <div class="bg-slate-400 text-white p-6 rounded-lg shadow-lg ">
              <h3 class="text-xl font-semibold mb-4">Step 3: AI Analysis</h3>
              <p>
                The system uses AI to analyze the uploaded image or video. It recognizes key features of the bird to
                determine its species.
              </p>
            </div>
          </div>

          <!-- Step 4: Bird Identification -->
          <div class="flex items-center justify-center space-x-6 w-4/5">
            <div class="bg-slate-400 text-white p-6 rounded-lg shadow-lg ">
              <h3 class="text-xl font-semibold mb-4">Step 4: Bird Identification</h3>
              <p>
                Once the analysis is complete, the system will identify the species of the bird and display detailed
                information about it.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- Team Section -->
    <section id="team" class="min-h-screen py-16 px-8 text-center text-slate-600 space-y-24">
      <h2 class="text-3xl font-semibold mb-8">Meet the Team</h2>
      <div class="space-y-10 md:space-y-0 md:flex md:justify-evenly md:gap-10 w-3/5 md:items-center mx-auto">
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
