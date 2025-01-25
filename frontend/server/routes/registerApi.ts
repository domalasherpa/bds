import {z} from 'zod'
import { useDb } from '../db/useDb'
import { users } from '../db/schema';
import { registerSchema } from '~/shared';

export default defineEventHandler(async(event)=>{
    let body = await readValidatedBody(event, registerSchema.parse)

    body.password = await hashPassword(body.password)

    try{
        const user = await useDb().insert(users).values({
            username: body.username,
            password: body.password,
            email: body.email,
        }).returning()
        
        await setUserSession(event, {
            user:{
                id: user[0].id, 
                username: user[0].username
            }})
    }
    catch(e:any){
        if (e.message.includes('UNIQUE constraint failed')) {
            throw createError({
              statusCode: 409,
              statusMessage: 'User with given credentials already exists.',
            })
        }
        throw createError({
            statusCode: 500,
            statusMessage: 'Internal Server Error',
            message: 'Failed to create user',
        })
    }

})
