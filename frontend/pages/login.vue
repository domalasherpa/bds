<script setup>
// import { signInWithPopup, GoogleAuthProvider } from 'firebase/auth'

// const auth = useFirebaseAuth()
// const router = useRouter()

// function signInWithGoogle() {
//   signInWithPopup(auth, new GoogleAuthProvider()).then(()=>router.replace('/'))
// }
const loggedIn = ref(false)
</script>

<template>
  <div class="h-screen flex justify-center items-center text-center bg-slate-100">
    <div v-if="!loggedIn" class="px-6 pt-16 pb-10 space-y-8 bg-white shadow-xl rounded-lg text-slate-600">
      <div class="space-y-2">
        <h1 class="text-4xl font-semibold">
          Welcome back
        </h1>
        <p>Please sign in to continue</p>
      </div>
      
      <UForm class="space-y-4 text-2xl">
        <UFormGroup label="Email" name="email" type="email" >
          <UInput v-model="email" color="white" placeholder="Enter your Email"/>
        </UFormGroup>

          <UFormGroup label="Password" name="password" >
          <UInput v-model="email" type="password" placeholder="Enter your password"/>
          </UFormGroup>
        <UButton label="Sign in" />

          
      </UForm>  
      <div class="flex justify-between text-slate-600 text-sm ">
          <p>Don't have an account? <span class="text-blue-600 "><ULink>Sign Up</ULink></span></p>
      </div>
    </div>

    <div v-else class="px-6 pt-16 pb-10 space-y-8 bg-white shadow-xl rounded-lg text-slate-600">
  <div class="space-y-2">
    <h1 class="text-4xl font-semibold">
      Create your account
    </h1>
      <p>Sign up to get started</p>
    </div>
    
    <UForm class="space-y-4 text-2xl">
      <UFormGroup label="Email" name="email" type="email">
        <UInput v-model="email" color="white" placeholder="Enter your Email"/>
      </UFormGroup>

      <UFormGroup label="Username" name="username">
        <UInput v-model="username" color="white" placeholder="Enter your username"/> 
      </UFormGroup>

      <UFormGroup label="Password" name="password">
        <UInput v-model="password" type="password" placeholder="Create a password"/>
      </UFormGroup>

      <UFormGroup label="Confirm Password" name="confirmPassword">
        <UInput v-model="confirmPassword" type="password" placeholder="Confirm your password"/>
      </UFormGroup>
      
      <UButton label="Sign up" />
    </UForm>  
    
    <div class="flex justify-between text-slate-600 text-sm ">
      <p>Already have an account? <span class="text-blue-600 "><ULink>Sign In</ULink></span></p>
    </div>
  </div>

  </div>
</template>
