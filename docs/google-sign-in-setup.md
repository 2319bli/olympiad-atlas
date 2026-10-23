# Activate Google sign-in

The Google sign-in implementation is deployed behind a configuration check. It stays disabled until both production values below are set. Existing ChatGPT sign-in and all account data remain usable.

1. In Google Cloud / Google Auth Platform, select the project that will own Olympiad Atlas. Configure the app's branding, support email and audience. For initial testing, add the Google accounts that should be allowed to sign in. Follow Google's publishing requirements before making the OAuth application generally available.
2. Create an OAuth client of type **Web application**.
3. Add this exact authorised redirect URI:

   `https://olympiad-atlas.pr141.chatgpt.site/auth/google/callback`

4. Configure these production runtime values through Sites' environment-variable tool (never commit them or paste a client secret into a chat message):

   - `GOOGLE_CLIENT_ID`: the web application's client ID.
   - `GOOGLE_CLIENT_SECRET`: the matching secret, marked `is_secret: true`.

5. Redeploy the saved Site version so the new environment revision takes effect. The button enables automatically when both values and the database are available.
6. Test a real Google login, cloud save, sign-out, and login from a second browser. OAuth requests use only `openid email profile`.

## Preserve an existing account

First sign into the existing Atlas account using ChatGPT. Choose **Link Google to this account**. Complete Google's login for the account to link. Subsequent Google logins resolve to the existing Atlas user ID and retain its papers/progress. Email matching is never used to merge accounts. A Google identity already linked elsewhere cannot be reassigned through this flow. Guest data still requires the explicit browser import.

## Implementation and validation

The platform's reserved sign-in/sign-out/callback routes remain untouched. Google endpoints are under `/auth/google/`; `/auth/chatgpt/start` clears a Google browser session before entering the existing platform sign-in flow. `/auth/logout` revokes the current Google session and clears both sign-in paths.

Google's authorization-code flow uses PKCE S256, a browser-bound, single-use ten-minute state record, and a nonce. ID tokens are verified with Google's public keys, RS256, issuer, audience, authorised-party, issue/expiry times, and nonce. Atlas sessions last 30 days, use Secure/HttpOnly/SameSite=Lax host cookies, and store only token hashes. OAuth access/refresh/ID tokens are not retained.

`node tests/google-auth.mjs` tests signature/audience/nonce/expiry rejection, state replay, account isolation despite matching email, explicit linking, collision/session-switch protection, sign-out and disabled configuration. Live Google consent and token exchange remain unverified until real credentials are configured.

Official reference: https://developers.google.com/identity/openid-connect/openid-connect
