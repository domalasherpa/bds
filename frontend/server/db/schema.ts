import { relations, type InferSelectModel, sql } from "drizzle-orm";
import { sqliteTable, integer, text } from "drizzle-orm/sqlite-core";

export const users = sqliteTable('users', {
    id: integer().primaryKey(),
    username: text().unique().notNull(),
    password: text().notNull(),
    email: text().unique().notNull(),
    createdAt: text().notNull().default(sql`CURRENT_TIMESTAMP`),
    updatedAt: text().notNull().default(sql`CURRENT_TIMESTAMP`),
});

export const images = sqliteTable('userImages', {
    id: integer().primaryKey(),
    userId: integer().references(()=>users.id, { onDelete: 'cascade' }).notNull(),
    path: text().unique().notNull(),
    detectedBird: text(),
    createdAt: text().notNull().default(sql`CURRENT_TIMESTAMP`),
    updatedAt: text().notNull().default(sql`CURRENT_TIMESTAMP`),
});

// Explicitly define the relation for better clarity
export const userImages = relations(images, ({ one }) => ({
    user: one(users, {
        fields: [images.userId], // Explicitly specify the foreign key
        references: [users.id],   // Reference the primary key in the users table
    })
}));

export type Users = InferSelectModel<typeof users>;
export type Images = InferSelectModel<typeof images>;
