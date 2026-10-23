import { sqliteTable, text, integer, primaryKey } from "drizzle-orm/sqlite-core";
export const papers = sqliteTable("account_papers", {
 userId: text("user_id").notNull(), paperId: text("paper_id").notNull(),
 payload: text("payload").notNull(), createdAt: integer("created_at").notNull()
}, t => [primaryKey({columns:[t.userId,t.paperId]})]);
export const progress = sqliteTable("account_progress", {
 userId: text("user_id").notNull(), problemId: text("problem_id").notNull(),
 saved: integer("saved").notNull(), status: text("status").notNull(), updatedAt: integer("updated_at").notNull()
}, t => [primaryKey({columns:[t.userId,t.problemId]})]);
export const googleIdentities = sqliteTable('google_identities', {
 subject: text('subject').primaryKey(), userId: text('user_id').notNull().unique(),
 email: text('email').notNull(), name: text('name').notNull()
});
export const googleStates = sqliteTable('google_states', {
 stateHash: text('state_hash').primaryKey(), browserHash: text('browser_hash').notNull(),
 verifier: text('verifier').notNull(), nonce: text('nonce').notNull(),
 linkUserId: text('link_user_id'), expiresAt: integer('expires_at').notNull()
});
export const googleSessions = sqliteTable('google_sessions', {
 tokenHash: text('token_hash').primaryKey(), userId: text('user_id').notNull(),
 expiresAt: integer('expires_at').notNull()
});
