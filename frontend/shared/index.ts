import {z} from 'zod'

const username = z.string().trim().min(3, 'Username must be at least 3 characters')
const password = z.string().trim().min(6, 'Password must be at least 6 characters')

export const registerSchema = z.object({
    username,
    password,
    email: z.string().email({message: 'please enter a valid email'}),
})

export const LoginSchema = z.object({
    username,
    password
})

export const ImageSchema = z.object({
    image: z.string(),
})


export type RegisterBody = z.infer<typeof registerSchema>
export type LoginBody = z.infer<typeof LoginSchema>

