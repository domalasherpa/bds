export default defineNuxtRouteMiddleware(async(to)=>{
    const {loggedIn}= useUserSession()
    
    if(!loggedIn.value && to.path !== '/register' && to.path !== '/login'){
        console.log("not authorized")
        return navigateTo('/login')
    }
})