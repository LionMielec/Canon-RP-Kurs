(() => {
  'use strict';

  const app = document.getElementById('app');
  const home = app.innerHTML;

  const escape = value => String(value).replace(/[&<>"']/g, character => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  })[character]);
  // Odsyłacz [[ID|tekst]] jest linkiem do lekcji, kroku albo części lekcji (D-060).
  const inline = value => escape(value)
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\[\[(L1-(\d+)(-[\w-]+)?)\|(.+?)\]\]/g, (match, id, lesson, section, text) =>
      `<a class="subtle-link" href="#lekcja-${Number(lesson)}${section ? `/${id}` : ''}">${text}</a>`);

  function markdown(value) {
    return value.trim().split(/\n\s*\n/).map(block => {
      const lines = block.split('\n');
      const parts = [];
      let group = [];
      let kind = 'p';
      let start = 1;
      const flush = () => {
        if (!group.length) return;
        // Dwie spacje na końcu wiersza akapitu oraz wcięty wiersz pod punktem listy to nowa linia.
        parts.push(kind === 'p'
          ? `<p>${group.map((line, i) => inline(line.trimEnd()) + (i < group.length - 1 ? (/ {2}$/.test(line) ? '<br>' : ' ') : '')).join('')}</p>`
          : `<${kind}${kind === 'ol' && start > 1 ? ` start="${start}"` : ''}>${group.map(line => `<li>${inline(line).replace(/\n/g, '<br>')}</li>`).join('')}</${kind}>`);
        group = [];
      };
      for (const line of lines) {
        if (kind !== 'p' && group.length && /^\s+\S/.test(line)) {
          group[group.length - 1] += '\n' + line.trim();
          continue;
        }
        const nextKind = /^- /.test(line) ? 'ul' : /^\d+\. /.test(line) ? 'ol' : 'p';
        if (nextKind !== kind) flush();
        kind = nextKind;
        // Lista zaczęta od innego numeru niż 1 kontynuuje numerację listy przerwanej obrazem.
        if (kind === 'ol' && !group.length) start = Number(line.match(/^\d+/)[0]);
        group.push(nextKind === 'ul' ? line.slice(2) : nextKind === 'ol' ? line.replace(/^\d+\. /, '') : line);
      }
      flush();
      return parts.join('');
    }).join('');
  }

  function pagesFor(lesson) {
    return [
      { key: 'cel', kind: 'intro', ...lesson.intro },
      ...lesson.steps.flatMap(step => step.screens
        ? step.screens.map(screen => ({ ...step, ...screen, kind: 'step' }))
        : [{ key: step.id, kind: 'step', ...step }]),
      { key: 'cwiczenie', kind: 'exercise', ...lesson.exercise },
      ...(lesson.afterExercise || []).map(section => ({ key: section.id, kind: 'reflection', ...section })),
      ...(lesson.help ? [{ key: 'pomoc', kind: 'help', ...lesson.help }] : []),
      ...lesson.summary.map((section, index) => ({ key: `podsumowanie-${index + 1}`, kind: 'summary', ...section }))
    ];
  }

  function markerMarkup(marker) {
    const values = ['x', 'y', 'width', 'height'].map(key => Number(marker[key]));
    if (values.some(value => !Number.isFinite(value) || value < 0 || value > 100)) return '';
    const [x, y, width, height] = values;
    const style = `--marker-x:${x}%;--marker-y:${y}%;--marker-width:${width}%;--marker-height:${height}%`;
    const direction = marker.kind === 'direction';
    return `<span class="camera-marker${direction ? ' camera-marker--direction' : ''}" style="${style}" aria-hidden="true">${direction ? escape(marker.label || '') : ''}</span>`;
  }

  function photoMarkup(asset, frame) {
    return `<figure class="asset-photo" data-asset-id="${escape(asset.id)}">
      <div class="asset-image"><img${asset.localOnly ? ' data-local-only' : ''} src="${escape(frame.target)}" alt="${escape(frame.alt || `${frame.title} na rzeczywistym aparacie Canon EOS RP`)}" width="${frame.width}" height="${frame.height}">
        ${(frame.markers || []).map(markerMarkup).join('')}</div>
      <figcaption><strong>${escape(frame.title)}</strong></figcaption>
    </figure>`;
  }

  function placeholderMarkup(asset, message = 'Ten materiał nie jest jeszcze gotowy.') {
    return `<figure class="asset-placeholder" data-asset-id="${escape(asset.id)}">
      <figcaption><span class="asset-status">Materiał w przygotowaniu</span>
        <strong>${escape(asset.title)}</strong><p>${escape(message)}</p></figcaption>
    </figure>`;
  }

  function assetMarkup(asset, frameIndex) {
    if (!asset) return '';
    if (asset.kind === 'card') return `<aside class="check" data-asset-id="${escape(asset.id)}">${markdown(asset.body)}</aside>`;
    if (!asset.frames) return placeholderMarkup(asset);
    if (frameIndex !== undefined) {
      return asset.frames[frameIndex] ? photoMarkup(asset, asset.frames[frameIndex]) : placeholderMarkup(asset);
    }
    const photos = asset.frames.map(frame => photoMarkup(asset, frame)).join('');
    return (asset.layout === 'grid' ? `<div class="asset-grid">${photos}</div>` : photos)
      + (asset.pendingMessage ? placeholderMarkup(asset, asset.pendingMessage) : '');
  }

  function contentMarkup(lesson, page) {
    if (page.blocks) {
      return page.blocks.map(block => block.text !== undefined
        ? `<div class="lesson-text">${markdown(block.text)}</div>`
        : assetMarkup(lesson.assets.find(asset => asset.id === block.asset), block.frame)).join('');
    }
    const assets = lesson.assets.filter(asset => asset.step === page.id).map(asset => assetMarkup(asset)).join('');
    const text = `<div class="lesson-text">${markdown(page.body)}</div>`;
    return page.mediaPlacement === 'before' ? assets + text : text + assets;
  }

  function render() {
    const match = location.hash.match(/^#lekcja-(\d+)(?:\/([\w-]+))?$/);
    const lesson = match && window.CANON_LESSONS.find(item => item.id === Number(match[1]));
    if (!lesson) {
      app.innerHTML = home;
      document.title = 'Canon RP — Kurs';
      if (window.matchMedia('(display-mode: standalone)').matches || navigator.standalone) {
        app.querySelector('.install').hidden = true;
      }
      window.scrollTo(0, 0);
      return;
    }

    const pages = pagesFor(lesson);
    const requested = match[2];
    const index = requested && /^\d+$/.test(requested)
      ? Math.min(Number(requested), pages.length - 1)
      : Math.max(0, pages.findIndex(page => page.key === requested || page.id === requested));
    const page = pages[index];
    const previous = pages[index - 1];
    const next = pages[index + 1];
    const link = item => `#lekcja-${lesson.id}/${item.key}`;
    const position = page.kind === 'step'
      ? `Krok ${lesson.steps.findIndex(step => step.id === page.id) + 1} z ${lesson.steps.length}`
      : ({ intro: 'Cel', exercise: 'Ćwiczenie', reflection: 'Porównanie', help: 'Pomoc', summary: 'Podsumowanie' })[page.kind];

    app.innerHTML = `<article data-lesson="${lesson.code}" data-section-id="${escape(page.id || page.key)}">
      <a class="crumb" href="#">← Spis lekcji</a>
      <p class="lesson-name">${escape(lesson.title)}</p>
      <div class="lesson-meta"><span>Lekcja ${lesson.id} · ${escape(lesson.duration)}</span><span>${position}</span></div>
      <div class="track" role="progressbar" aria-label="Miejsce w lekcji" aria-valuemin="0" aria-valuemax="${pages.length}" aria-valuenow="${index + 1}"><span style="width:${(index + 1) / pages.length * 100}%"></span></div>
      <p class="eyebrow">${escape(lesson.category.toUpperCase())}</p>
      <h1 class="step-title step-heading" tabindex="-1">${escape(page.title)}</h1>
      ${contentMarkup(lesson, page)}
      <nav class="footer-actions" aria-label="Przechodzenie przez lekcję">
        ${previous ? `<a class="secondary" href="${link(previous)}">← Wstecz</a>` : ''}
        <a class="primary" href="${next ? link(next) : '#'}">${next ? (next.kind === 'exercise' ? 'Przejdź do ćwiczenia' : 'Dalej') : 'Spis lekcji'} <span aria-hidden="true">→</span></a>
      </nav>
      ${!next && lesson.id === 1 ? '<a class="end-nav subtle-link" href="#lekcja-2">Przejdź do lekcji 2</a>' : ''}
    </article>`;
    // Plik tylko lokalny (rysunek Canon, D-056) nie trafia do wersji publicznej;
    // gdy go brak, w jego miejscu stoi jawne miejsce na brakujący materiał.
    app.querySelectorAll('img[data-local-only]').forEach(img => img.addEventListener('error', () => {
      const figure = img.closest('figure');
      const asset = lesson.assets.find(item => item.id === figure.dataset.assetId);
      figure.outerHTML = placeholderMarkup(asset);
    }, { once: true }));
    document.title = `${lesson.title} · Canon RP`;
    window.scrollTo(0, 0);
    app.querySelector('h1').focus({ preventScroll: true });
  }

  window.addEventListener('hashchange', render);
  render();
})();
