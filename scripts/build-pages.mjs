import fs from 'node:fs/promises';
import path from 'node:path';

const output = path.resolve('dist/pages');
const apiBase = (process.env.ATLAS_API_BASE || '').replace(/\/$/, '');
if (apiBase) {
  const url = new URL(apiBase);
  if (url.protocol !== 'https:' || url.username || url.password || url.search || url.hash || url.pathname !== '/') throw Error('ATLAS_API_BASE must be an HTTPS origin.');
}
await fs.rm(output, { recursive: true, force: true });
await fs.mkdir(output, { recursive: true });
await fs.cp('public', output, { recursive: true });
await fs.copyFile('atlas.html', path.join(output, 'index.html'));
await fs.writeFile(path.join(output, 'backend-config.js'), 'window.ATLAS_CONFIG = ' + JSON.stringify({ mode: 'standalone', apiBase }) + ';\n');
await fs.writeFile(path.join(output, '.nojekyll'), '');
console.log('Built GitHub Pages frontend at dist/pages. Cloud accounts: ' + (apiBase ? 'configured' : 'awaiting backend setup'));
