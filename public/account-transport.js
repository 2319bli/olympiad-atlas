'use strict';
const AtlasTransport = {
  get standalone() { return window.ATLAS_CONFIG?.mode === 'standalone'; },
  get apiBase() { return (window.ATLAS_CONFIG?.apiBase || '').replace(/\/$/, ''); },
  get tokenKey() { return 'olympiad-atlas-session-v1:' + this.apiBase; },
  token() { try { return localStorage.getItem(this.tokenKey) || ''; } catch { return ''; } },
  async request(path, options = {}) {
    if (!this.apiBase) {
      if (path === '/api/account') return { user: null, googleEnabled: false, signInUrl: null, signOutUrl: null };
      throw Error('Cloud accounts are being connected. You can keep using Atlas in this browser.');
    }
    if (!path.startsWith('/') || path.startsWith('//')) throw Error('Invalid API path.');
    const base = new URL(this.apiBase);
    if (base.protocol !== 'https:') throw Error('Account connections require HTTPS.');
    const headers = new Headers(options.headers), token = this.token();
    if (token) headers.set('Authorization', 'Bearer ' + token);
    const controller = new AbortController(), timer = setTimeout(() => controller.abort(), 20000);
    try {
      const response = await fetch(this.apiBase + path, { ...options, headers, credentials: 'omit', cache: 'no-store', redirect: 'error', signal: controller.signal });
      const data = await response.json();
      if (!response.ok) {
        if (response.status === 401 && token) { AtlasAccount.mode = 'expired'; AtlasAccount.paint(); }
        throw Error(data.error || 'Account request failed.');
      }
      return data;
    } finally { clearTimeout(timer); }
  },
  async googleLibrary() {
    if (window.google?.accounts?.id) return;
    if (!this.loading) this.loading = new Promise((resolve, reject) => {
      const script = document.createElement('script'); script.src = 'https://accounts.google.com/gsi/client'; script.async = true;
      const timer = setTimeout(() => { script.remove(); reject(Error('Google sign-in took too long to load. Please try again.')); }, 15000);
      script.onload = () => { clearTimeout(timer); resolve(); };
      script.onerror = () => { clearTimeout(timer); script.remove(); reject(Error('Google sign-in could not load. Please try again.')); };
      document.head.append(script);
    }).catch(error => { this.loading = null; throw error; });
    await this.loading;
  },
  async mountGoogle(element) {
    if (!element || !AtlasAccount.googleEnabled) return;
    try {
      const [challenge] = await Promise.all([this.request('/auth/challenge', { method: 'POST' }), this.googleLibrary()]);
      if (!element.isConnected) return;
      window.google.accounts.id.initialize({ client_id: challenge.clientId, nonce: challenge.nonce, auto_select: false,
        callback: async response => {
          try {
            if ((AtlasAccount.user || this.token()) && !['expired','unknown'].includes(AtlasAccount.mode)) throw Error('Sign out before choosing another account.');
            const session = await this.request('/auth/google/session', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ credential: response.credential, nonce: challenge.nonce }) });
            localStorage.setItem(this.tokenKey, session.token);
            location.reload();
          } catch (error) { AtlasAccount.error = error.message; renderAccount(); }
        }
      });
      element.textContent = '';
      window.google.accounts.id.renderButton(element, { theme: 'outline', size: 'large', text: 'signin_with' });
    } catch (error) { if (element.isConnected) element.textContent = error.message; }
  },
  async signOut() {
    const a = AtlasAccount;
    if (a.busy) throw Error('Please wait for syncing to finish.');
    if (a.user && (Object.keys(a.pending.papers).length || Object.keys(a.pending.progress).length)) {
      await a.sync(false);
      if (a.error) throw Error('Sync your pending changes or export an account backup before signing out.');
    }
    await this.request('/auth/logout', { method: 'POST' });
    localStorage.removeItem(this.tokenKey);
    window.google?.accounts?.id?.disableAutoSelect();
    location.reload();
  }
};
window.addEventListener('storage', event => {
  if (AtlasTransport.standalone && event.key === AtlasTransport.tokenKey && event.oldValue !== event.newValue) {
    AtlasAccount.mode = 'expired'; AtlasAccount.error = 'Your signed-in account changed in another tab. Reload to continue safely.'; AtlasAccount.paint();
    if (typeof state !== 'undefined' && state.view === 'account') renderAccount();
  }
});
