/* A chosen account nickname is the public identity on both leaderboards. */
'use strict';
let accountSettingsRequest = 0, accountSettingsSaving = false;
async function renderAccountSettings() {
  const a = AtlasAccount, host = document.getElementById('settings-view'), requestId = ++accountSettingsRequest;
  if (!a.user || ['expired','unknown'].includes(a.mode)) {
    host.innerHTML = '<div class="account-page"><p class="eyebrow">YOUR ATLAS PROFILE</p><h1>Account settings</h1><section class="account-card"><p>Sign in with Google to create or manage your Atlas account and choose your nickname.</p><a class="button primary" href="#account">Sign in or create an account →</a></section></div>';
    return;
  }
  host.innerHTML = '<div class="account-page"><p role="status">Loading account settings…</p></div>';
  try {
    const profile = await a.request('/api/leaderboard');
    if (requestId !== accountSettingsRequest || state.view !== 'settings') return;
    if (!profile.me) throw Error('Your session expired. Sign in again to manage your account.');
    a.nickname = profile.me.displayName || ''; a.profileLoaded = true;
    const creating = !a.nickname;
    host.innerHTML = `<div class="account-page"><p class="eyebrow">${creating ? 'FINISH CREATING YOUR ACCOUNT' : 'YOUR ATLAS PROFILE'}</p><h1>${creating ? 'Choose your nickname' : 'Account settings'}</h1><p class="account-intro">${creating ? 'You’re signed in with Google. Choose the name you want to use on Atlas.' : 'Manage the nickname people see on Atlas.'}</p><section class="account-card"><form id="account-settings-form"><label class="account-nickname-label" for="account-nickname">Nickname</label><input class="account-nickname-input" id="account-nickname" name="nickname" type="text" required minlength="2" maxlength="30" autocomplete="nickname" value="${esc(a.nickname)}" placeholder="Your chosen nickname" aria-describedby="account-nickname-help"><p class="small-note" id="account-nickname-help">2–30 characters. This is public, so choose a name you’re happy for others to see. Don’t enter an email address.</p><p class="account-settings-info">Your distinct solved-question count and difficulty-weighted total appear automatically under this nickname on the all-time leaderboards. Your Google name, email, saved papers and individual practice records stay private.</p><div class="paper-actions"><button class="button primary" type="submit">${creating ? 'Finish account setup' : 'Save nickname'}</button><a class="text-button" href="#account">Back to account</a></div><p id="account-settings-message" role="status"></p></form></section><p class="small-note">You can change your nickname here later. Your account, saved papers, solved totals and ranks stay attached to the same Google sign-in.</p><p class="small-note"><a href="privacy.html">Privacy policy</a> · <a href="terms.html">Terms of use</a></p></div>`;
    document.getElementById('account-settings-form').addEventListener('submit', saveAccountNickname);
  } catch(error) {
    if (requestId !== accountSettingsRequest || state.view !== 'settings') return;
    host.innerHTML = `<div class="account-page"><h1>Account settings</h1><section class="account-card"><p role="alert">${esc(error.message)}</p><button class="button secondary" id="account-settings-retry">Try again</button><a class="text-button" href="#account">Back to account</a></section></div>`;
    document.getElementById('account-settings-retry').onclick = renderAccountSettings;
  }
}
async function saveAccountNickname(event) {
  event.preventDefault();
  if (accountSettingsSaving) return;
  const a = AtlasAccount, form = event.currentTarget, button = form.querySelector('button[type="submit"]'), message = form.querySelector('[role="status"]');
  const nickname = form.elements.nickname.value.normalize('NFKC').trim();
  if (nickname.length < 2 || nickname.length > 30 || /[\p{C}<>@]/u.test(nickname)) { message.textContent = 'Use 2–30 characters without email addresses, markup or hidden characters.'; return; }
  const accountId = a.user?.id, creating = !a.nickname;
  accountSettingsSaving = true; button.disabled = true; message.textContent = 'Saving your nickname…';
  try {
    await a.request('/api/leaderboard/profile', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({accountId, displayName:nickname, listed:true}) });
    if (a.user?.id !== accountId) throw Error('Your account changed. Reload to continue.');
    a.nickname = nickname; a.profileLoaded = true; a.paint();
    if (creating && state.view === 'settings') location.hash = 'account';
    else if (state.view === 'settings') await renderAccountSettings();
    toast(creating ? 'Your Atlas account is ready.' : 'Nickname updated. Your progress is unchanged.');
  } catch(error) { message.textContent = error.message; }
  finally { accountSettingsSaving = false; button.disabled = false; }
}
