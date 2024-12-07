<script setup>
import { signOut } from 'firebase/auth'

const auth = useFirebaseAuth()
function handleSignOut() {
    signOut(auth)
}
</script>
<template>
    <nav class="flex justify-between pb-20 pt-10">
        <div>
            <h1>Bird Detection App</h1>
        </div>
        <div class="md:space-x-4">
            <router-link to="/">Home</router-link>
            <router-link to="/predict">Predict</router-link>
            <router-link to="/history">History</router-link>
            <router-link to="/result">Result</router-link>
        </div>
        <UButton label="sign out" @click="handleSignOut" />
    </nav>
</template>