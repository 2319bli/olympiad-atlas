import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
const store = new Map(); let calls = [], storageListener;
const context = { URL, Headers, AbortController, Blob, structuredClone, console, setTimeout: () => 1, clearTimeout: () => {},
  localStorage: { getItem: k => store.get(k) || null, setItem: (k, v) => store.set(k, v), removeItem: k => store.delete(k), get length() { return store.size; }, key: i => [...store.keys()][i] },
  window: { ATLAS_CONFIG: { mode: 'standalone', apiBase: '' }, addEventListener: (event, cb) => { if (event === 'storage') storageListener = cb; } },
  document: { getElementById: () => null, addEventListener: () => {} },
  fetch: async (url, options) => { calls.push({ url, options }); return { ok: true, json: async () => ({ user: null, googleEnabled: false }) }; },
  module: { exports: {} }
};
vm.createContext(context);
vm.runInContext(fs.readFileSync('public/paper-engine.js', 'utf8'), context); context.PaperEngine = context.module.exports;
vm.runInContext(fs.readFileSync('public/account-transport.js', 'utf8') + '\nglobalThis.transport=AtlasTransport;', context);
vm.runInContext(fs.readFileSync('public/account.js', 'utf8') + '\nglobalThis.account=AtlasAccount;', context);
const a = context.account, t = context.transport;
await a.init(); assert.equal(a.mode, 'guest'); a.saveProgress({ p: { saved: true, status: 'solved' } });
assert.equal(calls.length, 0); assert(store.has('olympiad-atlas-progress'));
context.window.ATLAS_CONFIG.apiBase = 'https://atlas-api.example';
store.set(t.tokenKey, 'a'.repeat(64));
await a.request('/api/account');
assert.equal(calls[0].url, 'https://atlas-api.example/api/account');
assert.equal(calls[0].options.credentials, 'omit');
assert.equal(calls[0].options.headers.get('Authorization'), 'Bearer ' + 'a'.repeat(64));
assert.equal(calls[0].options.redirect, 'error');
await assert.rejects(() => t.request('//evil.example/'), /Invalid/);
a.user = { id: 'alice' }; a.mode = 'account';
storageListener({ key: t.tokenKey, oldValue: 'a', newValue: 'b' }); assert.equal(a.mode, 'expired');
assert.throws(() => a.saveProgress({}), /Sign-in/);
context.fetch = async () => ({ ok: false, status: 401, json: async () => ({ error: 'Session expired' }) });
await assert.rejects(() => a.request('/api/sync'), /Session expired/); assert.equal(a.mode, 'expired');
assert.equal(t.token(), 'a'.repeat(64)); // Do not silently turn expired account writes into guest writes.
store.delete(t.tokenKey); a.user = null;
context.fetch = async () => { throw Error('offline'); };
await a.init(); assert.equal(a.mode, 'guest'); a.saveProgress({ offline: { saved: true, status: 'attempted' } });
console.log('Passed Pages client: local-only saves, token scoping, cookie-free API calls, account-switch protection, expired sessions and guest offline mode.');
