const json = (data, status = 200) => Response.json(data, { status, headers: { 'Cache-Control': 'private, no-store' } });
// Canonical records take precedence over retired aliases, including a corrected unsolve.
// GROUP BY ensures repeated appearances can never earn a second point.
const totals = `WITH solved AS (
  SELECT p.user_id, c.canonical_id, MAX(c.difficulty_tenths) AS difficulty
  FROM account_progress p JOIN atlas_question_catalog c ON c.problem_id = p.problem_id
  WHERE p.status = 'solved' AND (p.problem_id = c.canonical_id OR NOT EXISTS (
    SELECT 1 FROM account_progress canonical WHERE canonical.user_id = p.user_id AND canonical.problem_id = c.canonical_id
  )) GROUP BY p.user_id, c.canonical_id
), totals AS (
  SELECT user_id, COUNT(*) AS solved_count, SUM(10 + difficulty) AS weighted_tenths FROM solved GROUP BY user_id
)`;
const ranks = `${totals}, ranked AS (
  SELECT t.user_id, p.display_name, t.solved_count, t.weighted_tenths,
    RANK() OVER (ORDER BY t.solved_count DESC) AS solved_rank,
    RANK() OVER (ORDER BY t.weighted_tenths DESC) AS weighted_rank
  FROM totals t JOIN atlas_leaderboard_profiles p ON p.user_id = t.user_id WHERE p.listed = 1
)`;
const entry = (row, userId, metric) => ({
  displayName: row.display_name, solved: row.solved_count, weighted: row.weighted_tenths / 10,
  rank: row[metric === 'weighted' ? 'weighted_rank' : 'solved_rank'], isYou: row.user_id === userId
});
export async function getLeaderboard(request, db, user) {
  if (!db) return json({ error: 'The leaderboard is temporarily unavailable.' }, 503);
  const params = new URL(request.url).searchParams;
  const metric = params.get('metric') || 'solved';
  const offsetText = params.get('offset') || '0';
  if (!['solved', 'weighted'].includes(metric) || !/^\d{1,7}$/.test(offsetText)) return json({ error: 'Invalid leaderboard selection.' }, 400);
  const offset = Number(offsetText), limit = 50;
  const sort = metric === 'weighted' ? 'weighted_tenths' : 'solved_count';
  const [rows, count, mine] = await Promise.all([
    db.prepare(`${ranks} SELECT * FROM ranked ORDER BY ${sort} DESC, display_name COLLATE NOCASE, user_id LIMIT ? OFFSET ?`).bind(limit + 1, offset).all(),
    db.prepare(`${ranks} SELECT COUNT(*) AS participants FROM ranked`).first(),
    user?.userId ? db.prepare(`${ranks} SELECT p.display_name, p.listed, COALESCE(t.solved_count, 0) AS solved_count, COALESCE(t.weighted_tenths, 0) AS weighted_tenths,
      r.solved_rank, r.weighted_rank FROM (SELECT ? AS user_id) u
      LEFT JOIN atlas_leaderboard_profiles p ON p.user_id = u.user_id
      LEFT JOIN totals t ON t.user_id = u.user_id LEFT JOIN ranked r ON r.user_id = u.user_id`).bind(user.userId).first() : null
  ]);
  return json({ metric, offset, limit, participants: count.participants, hasMore: rows.results.length > limit,
    entries: rows.results.slice(0, limit).map(row => entry(row, user?.userId, metric)),
    me: mine ? { displayName: mine.display_name || '', listed: mine.listed === 1, solved: mine.solved_count,
      weighted: mine.weighted_tenths / 10, rank: mine[metric === 'weighted' ? 'weighted_rank' : 'solved_rank'] ?? null } : null
  });
}
export async function saveLeaderboardProfile(data, db, user) {
  if (!user?.userId) return json({ error: 'Sign in to manage your leaderboard profile.' }, 401);
  if (data?.accountId !== user.userId) return json({ error: 'Your account changed. Reload before saving.' }, 409);
  if (typeof data.listed !== 'boolean' || typeof data.displayName !== 'string') return json({ error: 'Choose a display name and whether to join.' }, 400);
  const name = data.displayName.normalize('NFKC').trim();
  if (name.length > 30 || (data.listed && name.length < 2) || /[\p{C}<>@]/u.test(name)) return json({ error: 'Use a display name of 2–30 characters, without email addresses, markup or hidden characters.' }, 400);
  await db.prepare(`INSERT INTO atlas_leaderboard_profiles (user_id, display_name, listed, updated_at) VALUES (?, ?, ?, ?)
    ON CONFLICT(user_id) DO UPDATE SET display_name=excluded.display_name, listed=excluded.listed, updated_at=excluded.updated_at`)
    .bind(user.userId, name, data.listed ? 1 : 0, Date.now()).run();
  return json({ ok: true });
}
