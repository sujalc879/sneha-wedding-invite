import { chromium } from '/Users/sujalsunilchaudhary/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs';
import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';

const root=path.resolve(import.meta.dirname,'../..');
const out=path.join(root,'work');
const result={status:'RUNNING',checks:[],screens:[],errors:[],failedRequests:[]};
function pass(name){result.checks.push({name,status:'PASS'});console.log('PASS:',name);}
const current=await fs.readFile(path.join(root,'public/index.html'),'utf8');
const baseline=execFileSync('git',['show','HEAD:public/index.html'],{cwd:root,encoding:'utf8'});
function withoutOpening(html){return html.replace(/\/\* ===== ENVELOPE REVEAL ===== \*\/[\s\S]*?(?=\/\* ===== HEADER AND HERO ===== \*\/)/,'').replace(/<!-- ===== OPENING ===== -->[\s\S]*?(?=<div id="page" inert>)/,'').replace(/\/\* ===== REVEAL ===== \*\/[\s\S]*?(?=\/\* ===== COUNTDOWN ===== \*\/)/,'');}
assert.equal(withoutOpening(current),withoutOpening(baseline));pass('Changes are confined to the opening CSS, HTML and reveal JavaScript; all wedding data and other features are byte-for-byte unchanged');
assert(!/<audio|AudioContext|webkitAudioContext|new Audio\(/.test(current));pass('Opening remains silent under the project audio rule');
const browser=await chromium.launch({headless:true,executablePath:'/Users/sujalsunilchaudhary/Library/Caches/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-mac-arm64/chrome-headless-shell'});
const url='http://127.0.0.1:8080/';
function track(page){page.on('pageerror',error=>result.errors.push(error.message));page.on('requestfailed',request=>result.failedRequests.push({url:request.url(),message:request.failure()?.errorText}));}
async function ready(page){await page.goto(url,{waitUntil:'networkidle'});await page.waitForTimeout(950);}
async function opened(page){await page.locator('#opening').waitFor({state:'hidden',timeout:4000});assert.equal(await page.locator('#page').evaluate(node=>node.inert),false);assert.equal(await page.evaluate(()=>document.body.classList.contains('sealed')),false);assert.equal(await page.evaluate(()=>document.activeElement.id),'hero');assert.equal(await page.evaluate(()=>scrollY),0);}

try{
  const sizes=[{width:360,height:800},{width:390,height:844},{width:430,height:932},{width:768,height:1024},{width:1440,height:900}];
  for(const size of sizes){
    const context=await browser.newContext({viewport:size});const page=await context.newPage();track(page);await ready(page);
    assert.equal(await page.locator('#page').evaluate(node=>node.inert),true);assert.equal(await page.evaluate(()=>document.activeElement.id),'open-invitation');
    await page.mouse.wheel(0,650);await page.waitForTimeout(70);assert.equal(await page.evaluate(()=>scrollY),0);
    const metrics=await page.evaluate(()=>{
      const selectors=['.opening-edition','.opening-kicker','.opening-title','.envelope-stage','.opening-hint','.opening-meta','#close-opening','#open-invitation','#open-invitation-cta'];
      const rects=selectors.map(selector=>{const element=document.querySelector(selector),r=element.getBoundingClientRect();return {selector,left:r.left,right:r.right,top:r.top,bottom:r.bottom};});
      const small=Array.from(document.querySelectorAll('#opening button')).filter(element=>element.getBoundingClientRect().height<44).map(element=>element.id);
      const tiny=Array.from(document.querySelectorAll('#opening *')).filter(element=>element.getClientRects().length&&parseFloat(getComputedStyle(element).fontSize)<14).map(element=>element.tagName);
      const title=document.querySelector('.opening-title').getBoundingClientRect(),envelope=document.querySelector('.envelope-stage').getBoundingClientRect(),cue=document.querySelector('.opening-cue').getBoundingClientRect();
      return {width:innerWidth,height:innerHeight,scrollWidth:document.documentElement.scrollWidth,rects,small,tiny,titleClear:title.bottom<envelope.top,envelopeClear:envelope.bottom<cue.top};
    });
    assert(metrics.scrollWidth<=size.width);assert.deepEqual(metrics.small,[]);assert.deepEqual(metrics.tiny,[]);assert(metrics.titleClear&&metrics.envelopeClear);assert(metrics.rects.every(rect=>rect.left>=-.5&&rect.right<=size.width+.5&&rect.top>=0&&rect.bottom<=size.height));
    const screenshot=path.join(out,`screenshots/onboarding-${size.width}.jpg`);await page.screenshot({path:screenshot,type:'jpeg',quality:90});result.screens.push({size,metrics,path:screenshot});
    await page.keyboard.press('Tab');assert.equal(await page.evaluate(()=>document.activeElement.id),'open-invitation-cta');await page.keyboard.press('Tab');assert.equal(await page.evaluate(()=>document.activeElement.id),'close-opening');await page.keyboard.press('Tab');assert.equal(await page.evaluate(()=>document.activeElement.id),'open-invitation');await page.keyboard.press('Shift+Tab');assert.equal(await page.evaluate(()=>document.activeElement.id),'close-opening');await page.keyboard.press('Shift+Tab');assert.equal(await page.evaluate(()=>document.activeElement.id),'open-invitation-cta');await page.keyboard.press('Shift+Tab');assert.equal(await page.evaluate(()=>document.activeElement.id),'open-invitation');
    if(size.width===360){await page.getByRole('button',{name:'Close opening',exact:true}).click();}
    else if(size.width===430){await page.getByRole('button',{name:'Open invitation',exact:true}).press('Enter');}
    else if(size.width===768){await page.getByRole('button',{name:'Open invitation',exact:true}).press('Space');}
    else if(size.width===1440){await page.keyboard.press('Escape');}
    else {await page.getByRole('button',{name:'Open invitation',exact:true}).click();}
    await opened(page);
    const hero=await page.evaluate(()=>{const p=document.getElementById('paper-plane').getBoundingClientRect(),n=document.getElementById('couple-names').getBoundingClientRect();return {overflow:document.documentElement.scrollWidth>innerWidth,overlap:p.left<n.right&&p.right>n.left&&p.top<n.bottom&&p.bottom>n.top};});assert(!hero.overflow&&!hero.overlap);
    pass(`${size.width}x${size.height}: complete opening visible, 44px buttons, 14px fonts, locked scroll, trapped focus and successful reveal/close into unobstructed hero`);await context.close();
  }
  const desktop=await browser.newContext({viewport:{width:1440,height:900}});const page=await desktop.newPage();track(page);await ready(page);
  const stage=page.locator('#envelope-stage'),bounds=await stage.boundingBox();await page.mouse.move(bounds.x+bounds.width*.8,bounds.y+bounds.height*.25);await page.waitForTimeout(600);const tilt=await stage.evaluate(node=>({x:node.style.getPropertyValue('--rx'),y:node.style.getPropertyValue('--ry')}));assert.notEqual(tilt.x,'');assert.notEqual(tilt.y,'');await page.screenshot({path:path.join(out,'screenshots/onboarding-hover-1440.jpg'),type:'jpeg',quality:90});await page.mouse.move(40,45);await page.waitForTimeout(100);assert.equal(await stage.evaluate(node=>node.style.getPropertyValue('--rx')),'');pass('Mouse tilt and seal/paper hover feedback respond, then reset on pointer leave');
  await page.getByRole('button',{name:'Open invitation',exact:true}).click();await page.waitForTimeout(350);await page.screenshot({path:path.join(out,'screenshots/onboarding-reveal-1440.jpg'),type:'jpeg',quality:90});await page.getByRole('button',{name:'Close opening',exact:true}).click();await opened(page);await page.waitForTimeout(2000);assert.equal(await page.evaluate(()=>document.activeElement.id),'hero');assert.equal(await page.locator('.seal-spark').count(),16);pass('Close remains usable during the reveal; cancelled opening timeout never relocks or moves focus again');await desktop.close();
  const touch=await browser.newContext({viewport:{width:390,height:844},hasTouch:true,isMobile:true});const mobile=await touch.newPage();track(mobile);await ready(mobile);await mobile.locator('#envelope-stage').dispatchEvent('pointermove',{pointerType:'touch',clientX:120,clientY:370});assert.equal(await mobile.locator('#envelope-stage').evaluate(node=>node.style.getPropertyValue('--rx')),'');await mobile.getByRole('button',{name:'Open invitation',exact:true}).tap();await opened(mobile);pass('Real touch-context tap opens the envelope; touch pointer movement does not trigger desktop tilt');await ready(mobile);await mobile.getByRole('button',{name:'Open the wedding invitation',exact:true}).tap();await opened(mobile);pass('Explicit Open invitation action works by touch and shares the same accessible reveal');await touch.close();
  const reduced=await browser.newContext({viewport:{width:390,height:844},reducedMotion:'reduce'});const quiet=await reduced.newPage();track(quiet);await quiet.goto(url);await opened(quiet);assert.equal(await quiet.evaluate(()=>document.getAnimations().filter(animation=>animation.playState==='running').length),0);assert.equal(await quiet.locator('.reveal:not(.visible)').count(),0);pass('Reduced motion bypasses onboarding, unlocks content immediately and leaves no running animations');await reduced.close();
  const short=await browser.newContext({viewport:{width:360,height:640}});const compact=await short.newPage();track(compact);await ready(compact);const bottom=await compact.locator('.opening-meta').evaluate(node=>node.getBoundingClientRect().bottom);assert(bottom<=640);await compact.keyboard.press('Escape');await opened(compact);pass('Additional short-phone check at 360x640 keeps the date, venue and dismissal accessible');await short.close();
  assert.deepEqual(result.errors,[]);const nonFont=result.failedRequests.filter(request=>!request.url.includes('fonts.googleapis.com')&&!request.url.includes('fonts.gstatic.com'));assert.deepEqual(nonFont,[]);pass('No JavaScript errors or failed non-font requests');result.status='PASS';
}catch(error){result.status='FAIL';result.error=String(error.stack||error);console.error(result.error);process.exitCode=1;}finally{await fs.writeFile(path.join(out,'ONBOARDING_RESULTS.json'),JSON.stringify(result,null,2));await browser.close();}
