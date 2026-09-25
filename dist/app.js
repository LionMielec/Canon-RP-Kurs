(() => {
  'use strict';

  const app = document.getElementById('app');
  const home = app.innerHTML;

  const escape = value => String(value).replace(/[&<>"']/g, character => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  })[character]);
  const inline = value => escape(value).replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

  function markdown(value) {
    return value.trim().split(/\n\s*\n/).map(block => {
      const lines = block.split('\n');
      const parts = [];
      let group = [];
      let kind = 'p';
      const flush = () => {
        if (!group.length) return;
        parts.push(kind === 'p'
          ? `<p>${inline(group.join(' '))}</p>`
          : `<${kind}>${group.map(line => `<li>${inline(line)}</li>`).join('')}</${kind}>`);
        group = [];
      };
      for (const line of lines) {
        const nextKind = /^- /.test(line) ? 'ul' : /^\d+\. /.test(line) ? 'ol' : 'p';
        if (nextKind !== kind) flush();
        kind = nextKind;
        group.push(nextKind === 'ul' ? line.slice(2) : nextKind === 'ol' ? line.replace(/^\d+\. /, '') : line);
      }
      flush();
      return parts.join('');
    }).join('');
  }

  function pagesFor(lesson) {
    return [
      { key: 'cel', kind: 'intro', ...lesson.intro },
      ...lesson.steps.map(step => ({ key: step.id, kind: 'step', ...step })),
      { key: 'cwiczenie', kind: 'exercise', ...lesson.exercise },
      ...(lesson.help ? [{ key: 'pomoc', kind: 'help', ...lesson.help }] : []),
      ...lesson.summary.map((section, index) => ({ key: `podsumowanie-${index + 1}`, kind: 'summary', ...section }))
    ];
  }

  function assetMarkup(asset) {
    if (asset.target) {
      return `<figure class="asset-photo" data-asset-id="${escape(asset.id)}">
        <div class="asset-image"><img src="${escape(asset.target)}" alt="${escape(asset.title)} na rzeczywistym aparacie Canon EOS RP" width="${asset.id === 'L1-02-V03' ? '500' : '640'}" height="${asset.id === 'L1-02-V03' ? '500' : '480'}">
          <span class="asset-marker marker-${escape(asset.id.toLowerCase())}" aria-hidden="true"></span></div>
        <figcaption><strong>${escape(asset.title)}</strong><span>Kadr roboczy · do zatwierdzenia</span></figcaption>
      </figure>`;
    }
    return `<figure class="asset-placeholder" data-asset-id="${asset.id}">
      <figcaption><span class="asset-status">Materiał produkcyjny do przygotowania</span>
        <strong>${escape(asset.title)}</strong><span class="asset-code">${escape(asset.id)} · ${escape(asset.status)}</span>
        <p>${escape(asset.note)}</p></figcaption>
    </figure>`;
  }

  function render() {
    const match = location.hash.match(/^#lekcja-([12])(?:\/([\w-]+))?$/);
    if (!match) {
      app.innerHTML = home;
      document.title = 'Canon RP — Kurs';
      if (window.matchMedia('(display-mode: standalone)').matches || navigator.standalone) {
        app.querySelector('.install').hidden = true;
      }
      window.scrollTo(0, 0);
      return;
    }

    const lesson = window.CANON_LESSONS.find(item => item.id === Number(match[1]));
    const pages = pagesFor(lesson);
    const requested = match[2];
    const index = requested && /^\d+$/.test(requested)
      ? Math.min(Number(requested), pages.length - 1)
      : Math.max(0, pages.findIndex(page => page.key === requested));
    const page = pages[index];
    const assets = lesson.assets.filter(asset => asset.step === page.id);
    const assetHtml = assets.map(assetMarkup).join('');
    const exampleFirst = lesson.id === 2 && ['L1-02-S01', 'L1-02-S02'].includes(page.id);
    const previous = pages[index - 1];
    const next = pages[index + 1];
    const link = item => `#lekcja-${lesson.id}/${item.key}`;
    const position = page.kind === 'step'
      ? `Krok ${lesson.steps.findIndex(step => step.id === page.id) + 1} z ${lesson.steps.length}`
      : ({ intro: 'Cel', exercise: 'Ćwiczenie', help: 'Pomoc', summary: 'Podsumowanie' })[page.kind];

    app.innerHTML = `<article data-lesson="${lesson.code}" data-section-id="${escape(page.id || page.key)}">
      <a class="crumb" href="#">← Spis lekcji</a>
      <p class="lesson-name">${escape(lesson.title)}</p>
      <div class="lesson-meta"><span>Lekcja 0${lesson.id} · ${escape(lesson.duration)}</span><span>${position}</span></div>
      <div class="track" role="progressbar" aria-label="Miejsce w lekcji" aria-valuemin="0" aria-valuemax="${pages.length}" aria-valuenow="${index + 1}"><span style="width:${(index + 1) / pages.length * 100}%"></span></div>
      <p class="eyebrow">${escape(lesson.category.toUpperCase())}</p>
      <h1 class="step-title step-heading" tabindex="-1">${escape(page.title)}</h1>
      ${exampleFirst ? assetHtml : ''}
      <div class="lesson-text">${markdown(page.body)}</div>
      ${exampleFirst ? '' : assetHtml}
      <nav class="footer-actions" aria-label="Przechodzenie przez lekcję">
        ${previous ? `<a class="secondary" href="${link(previous)}">← Wstecz</a>` : ''}
        <a class="primary" href="${next ? link(next) : '#'}">${next ? 'Dalej' : 'Spis lekcji'} <span aria-hidden="true">→</span></a>
      </nav>
      ${!next && lesson.id === 1 ? '<a class="end-nav subtle-link" href="#lekcja-2">Przejdź do lekcji 2</a>' : ''}
    </article>`;
    document.title = `${lesson.title} · Canon RP`;
    window.scrollTo(0, 0);
    app.querySelector('h1').focus({ preventScroll: true });
  }

  window.addEventListener('hashchange', render);
  render();
})();
