<script setup>
import { signInWithPopup, GoogleAuthProvider } from 'firebase/auth'

const auth = useFirebaseAuth()
const router = useRouter()

function signInWithGoogle() {
  signInWithPopup(auth, new GoogleAuthProvider()).then(()=>router.replace('/'))
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
      <UButton
        class="text-xl text-center py-3 w-full font-semibold flex justify-center items-center gap-2"
        label="Sign in with Google"
        icon="codicon:google"
        @click="signInWithGoogle"
      />
      <p>
        By signing in, you agree to our
        <ULink class="text-primary">
          Terms Of Service
        </ULink> and <ULink class="text-primary">
          Privacy Policy
        </ULink>
      </p>
    </div>
  </div>
</template>
