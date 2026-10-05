const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const root = path.resolve(__dirname, '..');
const url = process.env.PREVIEW_URL || 'http://127.0.0.1:8766/';
const context = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(root, 'dist/lessons.js'), 'utf8'), context);
const lessons = context.window.CANON_LESSONS;
const lesson = id => lessons.find(l => l.id === id);
// Pasek „Wróć” po odsyłaczu (D-076): zapamiętanie, brak nadpisania, czyszczenie.
(async () => {
  const browser = await chromium.launch({ headless: true, ...(process.env.CHROME_EXECUTABLE ? { executablePath: process.env.CHROME_EXECUTABLE } : {}) });
  try {
    const page = await browser.newPage({ viewport: { width: 430, height: 932 }, isMobile: true, hasTouch: true });
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    const bar = page.locator('.back-bar');
    const heading = title => page.getByRole('heading', { name: title, exact: true }).waitFor();
    // Przejście bez kliknięcia w odsyłacz (jak Dalej/Wstecz, które nie zapamiętują miejsca).
    const go = async (hash, title) => { await page.evaluate(h => { location.hash = h; }, hash); await heading(title); };
    const xref = text => page.locator('.lesson-text a[data-xref], .check a[data-xref]').filter({ hasText: text }).first().click();
    const help4 = lesson(4).help, step4 = lesson(4).steps[4], step4S04 = lesson(4).steps.find(s => s.id === 'L1-04-S04');
    const intro2 = lesson(2).intro, intro1 = lesson(1).intro;

    // Dalej/Wstecz/Spis lekcji nie zapamiętują miejsca.
    await page.goto(url + '#lekcja-2/cel');
    await heading(intro2.title);
    await page.getByRole('link', { name: 'Dalej', exact: true }).click();
    await page.getByRole('link', { name: '← Wstecz', exact: true }).click();
    await heading(intro2.title);
    assert.equal(await bar.count(), 0, 'Bar without a cross-reference');

    // Zapamiętanie: odsyłacz do innej lekcji.
    await xref('poprzedniej lekcji');
    await heading(intro1.title);
    assert.equal(await bar.innerText(), `← Wróć do lekcji 2 · ${intro2.title}`);
    assert(await page.evaluate(() => document.querySelector('article').firstElementChild.matches('.back-bar')), 'Bar is not at the top');
    // Pasek zostaje po „Dalej”.
    await page.getByRole('link', { name: 'Dalej', exact: true }).click();
    await page.locator('.lesson-meta').getByText('Krok 1', { exact: false }).waitFor();
    assert.equal(await bar.innerText(), `← Wróć do lekcji 2 · ${intro2.title}`);
    // Powrót: pasek prowadzi do pierwotnej strony i znika.
    await bar.click();
    await heading(intro2.title);
    assert.equal(page.url().split('#')[1], 'lekcja-2/cel');
    assert.equal(await bar.count(), 0, 'Bar after return');

    // Odsyłacz w obrębie jednej lekcji.
    await go('lekcja-4/pomoc', help4.title);
    await xref('Ustaw jeden punkt ostrości');
    await heading(step4S04.title);
    assert.equal(await bar.innerText(), `← Wróć do lekcji 4 · ${help4.title}`);
    // Brak nadpisania: kolejny odsyłacz zostawia pierwotne miejsce.
    await go(`lekcja-4/${step4.id}`, step4.title);
    assert.equal(await bar.innerText(), `← Wróć do lekcji 4 · ${help4.title}`);
    await xref('powiększałaś zdjęcie');
    await page.locator('article[data-lesson="L1-02"]').waitFor();
    assert.equal(await bar.innerText(), `← Wróć do lekcji 4 · ${help4.title}`);
    await bar.click();
    await heading(help4.title);
    assert.equal(await bar.count(), 0, 'Bar after return');

    // Czyszczenie: spis lekcji.
    await xref('Ustaw jeden punkt ostrości');
    await heading(step4S04.title);
    await page.getByRole('link', { name: '← Spis lekcji', exact: true }).click();
    await page.locator('.lesson-list').waitFor();
    await go(`lekcja-4/${step4S04.id}`, step4S04.title);
    assert.equal(await bar.count(), 0, 'Bar after the lesson list');

    // Czyszczenie: dojście do zapamiętanej strony inną drogą.
    await go('lekcja-4/pomoc', help4.title);
    await xref('Ustaw jeden punkt ostrości');
    await heading(step4S04.title);
    await go('lekcja-4/pomoc', help4.title);
    assert.equal(await bar.count(), 0, 'Bar on the remembered page');

    // Tylko pamięć otwartej strony: nic w pamięci telefonu, ponowne otwarcie bez paska.
    await xref('Ustaw jeden punkt ostrości');
    await heading(step4S04.title);
    assert.deepEqual(await page.evaluate(() => [localStorage.length, sessionStorage.length]), [0, 0]);
    await page.reload();
    await heading(step4S04.title);
    assert.equal(await bar.count(), 0, 'Bar after reopening');

    assert.equal(errors.length, 0, errors.join('\n'));
    console.log(JSON.stringify({ backBar: 'PASS' }));
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exitCode = 1; });
