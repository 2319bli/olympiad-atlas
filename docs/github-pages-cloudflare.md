# GitHub Pages and Cloudflare

The frontend is published to https://2319bli.github.io/olympiad-atlas/ by `.github/workflows/pages.yml`. It serves only `atlas.html` and `public/`; source code, database files and environment values are not copied into the Pages artifact. Asset paths are relative to the project subdirectory.

The public question bank, saved local mocks, practice marks and PDF exports work without a backend. An empty `ATLAS_API_BASE` leaves the Account page in local-only mode. Publishing a new API endpoint never moves data automatically.

## Deploy the backend

Use Node 24 and the dependencies in the root `package.json` (`pnpm install --frozen-lockfile`, using its declared package-manager version). Run the following from the repository root:

```sh
npx wrangler login
npx wrangler d1 create olympiad-atlas
cp cloudflare/wrangler.example.jsonc cloudflare/wrangler.jsonc
```

Paste the returned database ID into the local, ignored `cloudflare/wrangler.jsonc`. Set `account_id` there if the login has multiple Cloudflare accounts. Keep `FRONTEND_ORIGIN` as `https://2319bli.github.io` (an origin has no path). Leave `GOOGLE_CLIENT_ID` empty until Google setup is complete.

```sh
npx wrangler d1 migrations apply DB --remote --config cloudflare/wrangler.jsonc
npx wrangler deploy --config cloudflare/wrangler.jsonc
```

Use the exact HTTPS Worker origin returned by deployment. Check its `/health` endpoint; `googleEnabled` is false until sign-in is configured. In GitHub repository Settings → Secrets and variables → Actions → Variables, set **ATLAS_API_BASE** to that origin, without a trailing slash. It is a public URL, not a secret. Run **Publish GitHub Pages** under Actions to update the frontend.

## Activate Google sign-in

In Google Auth Platform, configure branding and audience and create a **Web application** OAuth client. Add the authorised JavaScript origin:

```text
https://2319bli.github.io
```

Set `GOOGLE_CLIENT_ID` in the local Wrangler configuration to the public client ID and redeploy the Worker. The new integration uses Google's Identity Services button with a JavaScript callback; it needs no redirect URI and no client secret. Add test users if the Google application is in testing mode. Test sign-in and sync from two browsers before declaring live authentication verified.

The frontend obtains a one-use nonce from the backend. The backend verifies Google's token signature, issuer, audience, expiry and nonce, consumes the nonce atomically, and issues a random revocable Atlas session. Session hashes are stored in D1. The frontend keeps its session in app-namespaced browser storage and sends it only to the configured HTTPS API in an Authorization header. Tokens never go in URLs. The API accepts the configured frontend origin and does not rely on third-party cookies or ChatGPT identity headers. Imported question content must continue to be safely rendered; do not introduce untrusted scripts into the frontend.

Free-plan sync batches contain at most 40 records so database queries stay below the Worker free-plan query budget. Normal usage remains subject to Cloudflare's free limits; no paid plan is selected by these instructions.

## Existing progress and papers

Browser storage is separate for the old Site and GitHub Pages. Before moving, export practice progress and mock papers on the old website and import those files on the new one. A combined account backup contains both `papers` and `progress`, and can be imported through the Saved papers and My practice import controls. Then use **Import this browser's data** if signed in to the new account. Original data is preserved; nothing is deleted from the old Site.

The new Cloudflare database starts empty. ChatGPT-backed account IDs are not automatically matched to Google accounts by email. The old Site remains available until migration is checked.

## Verification

```sh
node tests/paper-engine.cjs
node tests/account-service.mjs
node tests/account-client.mjs
node tests/google-auth.mjs
node tests/cloudflare-worker.mjs
node tests/pages-client.mjs
node scripts/build-pages.mjs
npx wrangler deploy --dry-run --config cloudflare/wrangler.example.jsonc
```

The former Site deployment remains supported by the original Vinext build and Google redirect flow. `backend-config.js` defaults to that legacy mode; the Pages build replaces it with the standalone configuration.
