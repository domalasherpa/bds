<script setup>
import { LoginSchema } from '~/shared';
const {loggedIn} = useUserSession()

if (loggedIn.value) {
  navigateTo('/predictBird')
}

const router = useRouter()
const user = ref({
  username: '',
  password: '',
})

const toast = useToast()
async function handleLogin(){
  try {
      const res = await $fetch('/loginApi', {
        method: 'POST',
        body: JSON.stringify({
          username: user.value.username,
          password: user.value.password
        })
      })
      toast.add({
        title: 'Success',
        description: 'successfully logged in',
      })
      window.location.href = '/predictBird#detect-bird'
    }
    catch (err) {
      toast.add({
        title: 'Error',
        description: err.data.statusMessage || err.data.message || 'Something went wrong',
      })
      throw err
    }
}

</script>

<template>

  <div class="h-screen flex justify-center items-center text-center bg-slate-100">
    <div class="px-6 pt-16 pb-10 space-y-8 bg-white shadow-xl rounded-lg text-slate-600">
      <div class="space-y-2">
        <h1 class="text-4xl font-semibold">
          Welcome back
        </h1>
        <p>Please sign in to continue</p>
      </div>

      <UForm :schema="LoginSchema" :state="user" @submit.prevent="handleLogin" class="space-y-4 text-2xl">
        <UFormGroup label="Username" name="username" type="username">
          <UInput v-model="user.username" color="white" placeholder="Enter your Username" required />
        </UFormGroup>

        <UFormGroup label="Password" name="password">
          <UInput v-model="user.password" type="password" placeholder="Enter your password" required/>
        </UFormGroup>
        <UButton label="Sign in" type="submit"/>
      </UForm>
      <div class="flex justify-between text-slate-600 text-sm ">
        <p>Don't have an account? <span class="text-blue-600 ">
            <ULink to="/register">Sign Up</ULink>
          </span></p>
      </div>
    </div>
  </div>
</template>
