CREATE TABLE IF NOT EXISTS atlas_leaderboard_profiles (
  user_id TEXT PRIMARY KEY,
  display_name TEXT NOT NULL,
  listed INTEGER NOT NULL DEFAULT 0 CHECK (listed IN (0, 1)),
  updated_at INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS atlas_question_catalog (
  problem_id TEXT PRIMARY KEY,
  canonical_id TEXT NOT NULL,
  difficulty_tenths INTEGER NOT NULL CHECK (difficulty_tenths BETWEEN 10 AND 100)
);
CREATE INDEX IF NOT EXISTS atlas_progress_status ON account_progress(status, user_id, problem_id);
CREATE INDEX IF NOT EXISTS atlas_profiles_listed ON atlas_leaderboard_profiles(listed, user_id);
