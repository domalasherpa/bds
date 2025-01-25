<script setup>
import { registerSchema } from '~/shared';
const {loggedIn} = useUserSession()
if (loggedIn.value) {
  navigateTo('/predictBird')
}

const toast = useToast()
const body = ref({
  email: '',
  username: '',
  password: '',
  confirmPassword: ''
})

async function handleRegister(){
  try {
    const res = await $fetch('/registerApi', {
      method: 'POST',
      body: JSON.stringify({
        email: body.value.email,
        username: body.value.username,
        password: body.value.password,
        confirmPassword: body.value.confirmPassword
      })
    })
    toast.add({
      title: 'Success',
      description: 'successfully registered',
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
          Create your account
        </h1>
        <p>Sign up to get started</p>
      </div>

      <UForm :schema="registerSchema" :state="body" class="space-y-4 text-2xl" @submit.prevent="handleRegister">
        <UFormGroup label="Email" name="email" type="email">
          <UInput v-model="body.email" color="white" placeholder="Enter your Email" required />
        </UFormGroup>

        <UFormGroup label="Username" name="username">
          <UInput v-model="body.username" color="white" placeholder="Enter your username" required />
        </UFormGroup>

        <UFormGroup label="Password" name="password">
          <UInput v-model="body.password" type="password" placeholder="Create a password"  required/>
        </UFormGroup>

        <UFormGroup label="Confirm Password" name="password">
          <UInput v-model="body.confirmPassword" type="password" placeholder="Confirm your password" required />
        </UFormGroup>

        <UButton label="Sign up" type="submit"/>
      </UForm>

      <div class="flex justify-between text-slate-600 text-sm ">
        <p>Already have an account? <span class="text-blue-600 ">
            <ULink to="/login">Sign In</ULink>
          </span></p>
      </div>
    </div>
  </div>
</template>
