import {z} from 'zod'
import { useDb } from '@/server/db/useDb'
import { users } from '@/server/db/schema'
import { and, eq } from 'drizzle-orm'
import { LoginSchema } from '~/shared'

export default defineEventHandler(async(event)=>{
    const body = await readValidatedBody(event, LoginSchema.parse)

    const userExists = await useDb().query.users.findFirst({
        where: (eq(users.username, body.username))
    })

    const hashPassoword = await hashPassword(body.password)
    if(!userExists?.username || await verifyPassword(hashPassoword, userExists.password)){
        throw createError({
            statusCode: 401,
            statusMessage: 'Invalid login',
            message: 'Username or password is incorrect',
        })
    }
    
    console.log('userExists', userExists)

    await setUserSession(event, {
        user:{
            id: userExists.id, 
            username: userExists.username
        }})

})