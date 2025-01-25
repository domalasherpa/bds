export default defineEventHandler(async (event) => {
    const {pathname} = getRequestURL(event)

    if(pathname.startsWith('/api')){
        const user = await requireUserSession(event)
        event.context.user = user
    }
    
})