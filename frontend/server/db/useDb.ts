import { drizzle } from "drizzle-orm/better-sqlite3"
import * as tables from '@/server/db/schema'
import Database from "better-sqlite3"

export function useDb(){
    let _db = null
    
    try{
        const dbDir = './server/db/db.sqlite'
        const sqlite = new Database(dbDir)
        _db = drizzle(sqlite, {schema: tables})
    }
    catch(e){
        console.error('Failed to connect to database', e)
        throw new Error('Failed to connect to database')
    }

    return _db
}
