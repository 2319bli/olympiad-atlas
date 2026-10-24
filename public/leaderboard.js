/* Public all-time totals; participation is explicitly opt-in. */
'use strict';
const AtlasLeaderboard = { metric: 'solved', offset: 0, sequence: 0, saving: false };
async function renderLeaderboard() {
  const b = AtlasLeaderboard, host = document.getElementById('leaderboard-view'), requestId = ++b.sequence;
  const metric = b.metric, offset = b.offset;
  host.innerHTML = '<div class="leaderboard-page"><p role="status">Loading the all-time leaderboard…</p></div>';
  try {
    const data = await AtlasAccount.request('/api/leaderboard?metric=' + metric + '&offset=' + offset);
    if (requestId !== b.sequence || state.view !== 'leaderboard') return;
    const me = data.me, signedIn = AtlasAccount.user && !['expired', 'unknown'].includes(AtlasAccount.mode);
    const pending = AtlasAccount.busy || Object.keys(AtlasAccount.pending.progress).length;
    host.innerHTML = `<div class="leaderboard-page">
      <header class="leaderboard-heading"><p class="eyebrow">ONE QUESTION. ONE CONTRIBUTION.</p><h1>The all-time leaderboard</h1><p>Every distinct question marked solved counts once, wherever you encountered it.</p></header>
      <div class="leaderboard-toolbar"><div class="leaderboard-switch" role="group" aria-label="Rank users by"><button type="button" data-rank="solved" aria-pressed="${metric === 'solved'}">Questions solved</button><button type="button" data-rank="weighted" aria-pressed="${metric === 'weighted'}">Difficulty weighted</button></div><button class="text-button" id="leaderboard-refresh">Refresh</button></div>
      <p class="leaderboard-formula">${metric === 'solved' ? '<strong>1 point per distinct solved question.</strong> Attempts and repeated solves add nothing extra.' : '<strong>Weighted score = sum of (1 + difficulty)</strong> across distinct solved questions. A difficulty 5.5 question earns 6.5 points.'}</p>
      ${me ? `<section class="leaderboard-personal" aria-label="Your all-time totals"><div><span>Your rank</span><strong>${me.rank ? '#' + me.rank : '—'}</strong><small>${me.listed ? me.solved ? 'All-time · ' + (metric === 'solved' ? 'questions solved' : 'weighted score') : 'Solve a question to enter the rankings' : 'Your profile is private'}</small></div><div><span>Questions solved</span><strong>${me.solved.toLocaleString()}</strong></div><div><span>Weighted score</span><strong>${me.weighted.toLocaleString('en-GB', { maximumFractionDigits: 1 })}</strong></div></section>` : ''}
      ${pending ? '<p class="leaderboard-note" role="status">Your latest practice changes are syncing. Rankings use your synced progress.</p>' : AtlasAccount.error && signedIn ? '<p class="leaderboard-note">Some changes may still be waiting to sync. <a href="#account">Check your account</a>.</p>' : ''}
      <div class="leaderboard-table-wrap"><table class="leaderboard-table"><caption>${data.participants.toLocaleString()} ${data.participants === 1 ? 'participant' : 'participants'} · all time · equal scores share a rank</caption><thead><tr><th scope="col">Rank</th><th scope="col">User</th><th scope="col" aria-sort="${metric === 'solved' ? 'descending' : 'none'}">Solved</th><th scope="col" aria-sort="${metric === 'weighted' ? 'descending' : 'none'}">Weighted score</th></tr></thead><tbody>${data.entries.length ? data.entries.map(row => `<tr class="${row.isYou ? 'leaderboard-you' : ''}"><td>${row.rank}</td><th scope="row">${esc(row.displayName)}${row.isYou ? '<span class="leaderboard-you-label">You</span>' : ''}</th><td>${row.solved.toLocaleString()}</td><td>${row.weighted.toLocaleString('en-GB', { maximumFractionDigits: 1 })}</td></tr>`).join('') : '<tr><td colspan="4" class="leaderboard-empty">' + (offset ? 'No more participants on this page.' : 'No ranked users yet. Join below and mark your first question solved.') + '</td></tr>'}</tbody></table></div>
      ${offset || data.hasMore ? `<nav class="leaderboard-pagination" aria-label="Leaderboard pages"><button class="button secondary" id="leaderboard-prev" ${offset === 0 ? 'disabled' : ''}>← Previous</button><span>Page ${Math.floor(offset / data.limit) + 1}</span><button class="button secondary" id="leaderboard-next" ${!data.hasMore ? 'disabled' : ''}>Next →</button></nav>` : ''}
      <section class="leaderboard-profile"><h2>${me?.listed ? 'Your public profile' : 'Join the leaderboard'}</h2>${signedIn ? `<p>Choose a public name. Joining publishes this name and your solved and weighted totals. Your Google name, email, saved papers and individual practice records stay private.</p><form id="leaderboard-profile-form"><label for="leaderboard-name">Public display name</label><input id="leaderboard-name" name="displayName" minlength="2" maxlength="30" autocomplete="off" placeholder="Choose a name or nickname" value="${esc(me?.displayName || '')}" aria-describedby="leaderboard-name-help"><p class="small-note" id="leaderboard-name-help">2–30 characters. A nickname is fine; don’t enter an email address.</p><label class="leaderboard-check"><input type="checkbox" name="listed" id="leaderboard-listed" ${me?.listed ? 'checked' : ''}> Show me on both public leaderboards</label><button class="button primary" type="submit">${me?.listed ? 'Save profile' : 'Save preferences'}</button><p id="leaderboard-profile-message" role="status"></p></form>` : '<p>Sign in to join under a display name and count your synced solves.</p><a class="button primary" href="#account">Go to account →</a>'}</section>
      <details class="leaderboard-rules"><summary>How the rankings work</summary><p>These are self-reported practice totals, not verified competition results. Mark a question <strong>Solved</strong> after completing it. Bookmarks, attempts and repeated appearances do not add points. Questions in generated papers count when you mark the corresponding bank question solved.</p><p>Only known questions in the Atlas bank count. Known duplicates are combined. The weighted score uses the bank’s current difficulty ratings; it may change when ratings are corrected. Changing a question back to attempted or not started removes its contribution after syncing. All-time means there is no weekly or monthly reset.</p><p>Users with the same total share a rank (1, 1, 3). Tied rows are ordered by display name. You can leave at any time by clearing the public leaderboard checkbox and saving; your private practice remains. Existing synced solves count as soon as you join.</p></details>
    </div>`;
    host.querySelectorAll('[data-rank]').forEach(button => button.onclick = () => { b.metric = button.dataset.rank; b.offset = 0; renderLeaderboard(); });
    document.getElementById('leaderboard-refresh').onclick = async () => { if (signedIn) await AtlasAccount.sync(false); renderLeaderboard(); };
    document.getElementById('leaderboard-prev')?.addEventListener('click', () => { b.offset = Math.max(0, offset - data.limit); renderLeaderboard(); });
    document.getElementById('leaderboard-next')?.addEventListener('click', () => { b.offset = offset + data.limit; renderLeaderboard(); });
    document.getElementById('leaderboard-profile-form')?.addEventListener('submit', saveLeaderboardPreferences);
  } catch (error) {
    if (requestId !== b.sequence || state.view !== 'leaderboard') return;
    host.innerHTML = `<div class="leaderboard-page"><h1>The all-time leaderboard</h1><p role="alert">${esc(error.message || 'The leaderboard could not load.')}</p><button class="button secondary" id="leaderboard-retry">Try again</button><p class="small-note">Your saved papers and practice progress are unaffected.</p></div>`;
    document.getElementById('leaderboard-retry').onclick = renderLeaderboard;
  }
}
async function saveLeaderboardPreferences(event) {
  event.preventDefault();
  if (AtlasLeaderboard.saving) return;
  const form = event.currentTarget, button = form.querySelector('button'), message = form.querySelector('[role="status"]');
  const data = { accountId: AtlasAccount.user?.id, displayName: form.elements.displayName.value.trim(), listed: form.elements.listed.checked };
  if (data.listed && data.displayName.length < 2) { message.textContent = 'Choose a display name of 2–30 characters.'; return; }
  AtlasLeaderboard.saving = true; button.disabled = true; message.textContent = 'Saving…';
  try {
    await AtlasAccount.request('/api/leaderboard/profile', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
    AtlasLeaderboard.offset = 0;
    if (state.view === 'leaderboard') await renderLeaderboard();
    toast(data.listed ? 'Your public leaderboard profile is saved.' : 'Your leaderboard profile is private.');
  } catch (error) { message.textContent = error.message; }
  finally { AtlasLeaderboard.saving = false; button.disabled = false; }
}
