<script setup>
  const user = useCurrentUser()  
  const router = useRouter()

  onMounted(() => {
    watch(user, (currentUser, prevUser)=>{
      if(prevUser && !currentUser){
        return router.replace('/login')
      }
    })
  })
</script>
<template>
  <div class="bg-green-100 min-h-screen p-10">
    <NavBar/>
    <NuxtPage />
    <Footer/>
  </div>
</template>
