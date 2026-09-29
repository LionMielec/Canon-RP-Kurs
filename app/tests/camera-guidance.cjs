const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const root = path.resolve(__dirname, '..');
const output = process.env.QA_OUTPUT || '/private/tmp/canon-camera-guidance-qa';
const url = process.env.PREVIEW_URL || 'http://127.0.0.1:8766/';
const context = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(root, 'dist/lessons.js'), 'utf8'), context);
const lessons = context.window.CANON_LESSONS;
const keys = lesson => ['cel', ...lesson.steps.flatMap(s => s.screens ? s.screens.map(p => p.key) : [s.id]), 'cwiczenie', ...(lesson.help ? ['pomoc'] : []), ...lesson.summary.map((s, i) => `podsumowanie-${i + 1}`)];
fs.mkdirSync(output, { recursive: true });
(async () => {
  const browser = await chromium.launch({ headless: true, ...(process.env.CHROME_EXECUTABLE ? { executablePath: process.env.CHROME_EXECUTABLE } : {}) });
  const results = [];
  try {
    for (const viewport of [{ width: 430, height: 932 }, { width: 440, height: 956 }, { width: 1440, height: 1000 }]) {
      for (const motion of ['no-preference', 'reduce']) {
        const ctx = await browser.newContext({ viewport, reducedMotion: motion, ...(viewport.width < 500 ? { isMobile: true, hasTouch: true } : {}) });
        const page = await ctx.newPage();
        const errors = [];
        page.on('pageerror', e => errors.push(e.message));
        page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
        page.on('response', r => { if (r.status() >= 400) errors.push(`${r.status()} ${r.url()}`); });
        let screens = 0;
        for (const lesson of [null, ...lessons]) {
          for (const key of lesson ? keys(lesson) : ['']) {
            await page.goto(url + '?preview=camera-guidance#' + (lesson ? `lekcja-${lesson.id}/${key}` : ''));
            await page.locator('h1').waitFor();
            const text = await page.locator('body').innerText();
            assert(!/L1-\d|\b[SV]\d{2}\b/.test(text), `Internal label: ${key}`);
            assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `Overflow: ${key}`);
            await page.locator('img').evaluateAll(async imgs => Promise.all(imgs.map(i => i.decode())));
            const geometry = await page.locator('.camera-marker').evaluateAll(markers => markers.map(m => {
              const image = m.parentElement.querySelector('img').getBoundingClientRect();
              const r = m.getBoundingClientRect();
              const s = getComputedStyle(m);
              const glow = getComputedStyle(m, '::before');
              return { x: (r.x + r.width / 2 - image.x) / image.width * 100, y: (r.y + r.height / 2 - image.y) / image.height * 100, width: r.width / image.width * 100, height: r.height / image.height * 100,
                expected: ['x', 'y', 'width', 'height'].map(k => parseFloat(s.getPropertyValue('--marker-' + k))), animation: glow.animationName, duration: glow.animationDuration, iterations: glow.animationIterationCount, opacity: parseFloat(glow.opacity), border: s.borderWidth };
            }));
            for (const m of geometry) {
              ['x', 'y', 'width', 'height'].forEach((k, i) => assert(Math.abs(m[k] - m.expected[i]) < .08, `Misaligned ${key} ${k}`));
              assert.equal(m.border, '0px');
              assert.equal(m.opacity, 1);
              assert.equal(m.duration, motion === 'reduce' ? '0s' : '6s');
              assert.equal(m.iterations, motion === 'reduce' ? '1' : '2');
              assert.equal(m.animation, motion === 'reduce' ? 'none' : 'camera-glow');
            }
            if (key === 'odtwarzanie' || key === 'wybierak') {
              assert.equal(await page.locator('.asset-photo').count(), 1);
              const expected = key === 'odtwarzanie' ? 'Odtwarzanie — naciśnij przycisk ▶' : 'Tylny wybierak — lewo / prawo';
              assert.equal(await page.locator('.asset-photo strong').innerText(), expected);
              assert(await page.evaluate(() => document.querySelector('.lesson-text').nextElementSibling.matches('.asset-photo')));
              assert.equal(await page.locator('.camera-marker--direction').count(), key === 'wybierak' ? 2 : 0);
              await page.screenshot({ path: path.join(output, `${viewport.width}-${motion}-${key}.png`), fullPage: true });
            }
            if (key === 'L1-02-S04') {
              assert.equal(await page.locator('.asset-photo').count(), 3);
              assert(await page.locator('.asset-photo').evaluateAll(figures => figures.every(f => f.previousElementSibling.matches('.lesson-text'))));
            }
            screens++;
          }
        }
        await page.goto(url + '#lekcja-2/odtwarzanie');
        await page.getByRole('link', { name: 'Dalej', exact: true }).click();
        await page.getByRole('heading', { name: 'Użyj tylnego wybieraka' }).waitFor();
        await page.getByRole('link', { name: '← Wstecz', exact: true }).click();
        await page.getByRole('heading', { name: 'Otwórz zdjęcie na Canon EOS RP' }).waitFor();
        await page.goto(url + '#lekcja-2/L1-02-S03');
        await page.getByRole('heading', { name: 'Otwórz zdjęcie na Canon EOS RP' }).waitFor();
        await page.goto(url + '#lekcja-1/L1-01-S07');
        await page.getByRole('link', { name: 'Przejdź do ćwiczenia', exact: true }).click();
        await page.getByRole('heading', { name: 'Zrób jeszcze dwa zdjęcia' }).waitFor();
        assert.equal(errors.length, 0, errors.join('\n'));
        results.push({ viewport, motion, screens, errors: 0, status: 'PASS' });
        await ctx.close();
      }
    }
    // Resize the same loaded image: the normalized coordinates must remain constant.
    const page = await browser.newPage({ reducedMotion: 'reduce' });
    await page.goto(url + '#lekcja-2/wybierak');
    let reference;
    for (const width of [320, 430, 440, 768, 1440, 430]) {
      await page.setViewportSize({ width, height: 1000 });
      const coords = await page.locator('.camera-marker').evaluateAll(ms => ms.map(m => {
        const i = m.parentElement.querySelector('img').getBoundingClientRect(), r = m.getBoundingClientRect();
        return [(r.x+r.width/2-i.x)/i.width, (r.y+r.height/2-i.y)/i.height, r.width/i.width, r.height/i.height];
      }));
      if (!reference) reference = coords;
      coords.forEach((c, i) => c.forEach((v, j) => assert(Math.abs(v-reference[i][j]) < .001)));
    }
    await page.emulateMedia({ reducedMotion: 'no-preference' });
    await page.reload();
    await page.waitForTimeout(12500);
    assert(await page.locator('.camera-marker').evaluateAll(ms => ms.every(m => getComputedStyle(m, '::before').transform === 'none' && getComputedStyle(m, '::before').opacity === '1' && m.getAnimations({subtree:true}).every(a => a.playState === 'finished'))));
    fs.writeFileSync(path.join(output, 'results.json'), JSON.stringify({ results, resize: 'PASS' }, null, 2));
    console.log(JSON.stringify({ results, resize: 'PASS' }, null, 2));
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exitCode = 1; });
