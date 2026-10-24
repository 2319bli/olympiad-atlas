import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
const host={innerHTML:''},listeners={},requests=[];
let storedName='',error=null;
const context={
  AtlasAccount:{user:{id:'alice'},mode:'account',nickname:'',profileLoaded:false,paint(){},async request(path,options){requests.push({path,options});if(error)throw Error(error);if(options){const body=JSON.parse(options.body);assert.equal(body.accountId,'alice');assert.equal(body.listed,true);storedName=body.displayName;return {ok:true}}return {me:{displayName:storedName}}}},
  document:{getElementById(id){if(id==='settings-view')return host;return {addEventListener(event,fn){listeners[id+':'+event]=fn}}}},
  state:{view:'settings'},location:{hash:'#settings'},toast(){},esc:s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;')
};
vm.createContext(context);vm.runInContext(fs.readFileSync('public/account-settings.js','utf8')+'\nglobalThis.render=renderAccountSettings;globalThis.save=saveAccountNickname;',context);
await context.render();
assert(host.innerHTML.includes('Choose your nickname'));assert(host.innerHTML.includes('Finish account setup'));
assert(!host.innerHTML.includes('type="checkbox"'),'Account creation must not require separate leaderboard opt-in');
const submit=async nickname=>{const button={disabled:false},message={textContent:''};await context.save({preventDefault(){},currentTarget:{elements:{nickname:{value:nickname}},querySelector:s=>s==='button[type="submit"]'?button:message}});return {button,message}};
await submit('  Chosen nickname  ');
assert.equal(storedName,'Chosen nickname');assert.equal(context.AtlasAccount.nickname,storedName);assert.equal(context.location.hash,'account');
context.state.view='settings';await context.render();assert(host.innerHTML.includes('Save nickname'));assert(host.innerHTML.includes('Chosen nickname'));
await submit('New nickname');assert.equal(storedName,'New nickname');assert.equal(context.AtlasAccount.user.id,'alice');
const before=requests.length;await submit('name@example.com');assert.equal(requests.length,before,'Invalid nicknames must not be submitted');
error='Session expired';const failed=await submit('Another nickname');assert.equal(context.AtlasAccount.nickname,'New nickname');assert.equal(failed.message.textContent,'Session expired');assert(!failed.button.disabled);
error=null;storedName='"><img src=x>';await context.render();assert(!host.innerHTML.includes('<img'));assert(host.innerHTML.includes('&lt;img'));
context.AtlasAccount.user=null;await context.render();assert(host.innerHTML.includes('Sign in or create an account'));assert(!host.innerHTML.includes('<form'));
console.log('Passed nickname account setup: required chosen name, automatic leaderboard participation, persisted renaming, validation, safe rendering, failed saves and signed-out settings.');
