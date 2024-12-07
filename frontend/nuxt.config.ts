// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  ssr: false,
  modules: ['@nuxt/ui',  'nuxt-vuefire',],
  vuefire: {
    auth: {
      enabled: true,
      sessionCookie: false
    },
    config: {
      apiKey: "AIzaSyCQUNv-m8GllR9IaSzcm68OEAIJVJoW1BM",
      authDomain: "first-firebase-482ad.firebaseapp.com",
      projectId: "first-firebase-482ad",
      storageBucket: "first-firebase-482ad.firebasestorage.app",
      messagingSenderId: "479112328700",
      appId: "1:479112328700:web:20e4043d6c3642f64fae79",
      measurementId: "G-84FXWMRRGN"
    }
  }
})