CREATE TABLE atlas_login_challenges (
  nonce_hash TEXT PRIMARY KEY NOT NULL,
  expires_at INTEGER NOT NULL
);
CREATE INDEX atlas_login_challenges_expiry ON atlas_login_challenges(expires_at);
CREATE INDEX google_sessions_expiry ON google_sessions(expires_at);
