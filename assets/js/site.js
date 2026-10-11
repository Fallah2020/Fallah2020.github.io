/* Publication filtering: progressive enhancement; cards remain available without JS. */
(function () {
  'use strict';
  const input = document.getElementById('pub-search');
  const grid = document.getElementById('publication-grid');
  if (!input || !grid) return;

  const cards = Array.from(grid.querySelectorAll('.publication-card'));
  const buttons = Array.from(document.querySelectorAll('.filter-button'));
  const count = document.getElementById('pub-count');
  const empty = document.getElementById('pub-empty');
  let active = 'all';

  function update() {
    const term = input.value.trim().toLocaleLowerCase();
    let visible = 0;
    cards.forEach((card) => {
      const searchable = (card.dataset.search || '').toLocaleLowerCase();
      const status = (card.dataset.status || '').toLocaleLowerCase();
      const kind = (card.dataset.kind || '').toLocaleLowerCase();
      const matchesStage = active === 'all' ||
        (active === 'published' ? (status.includes('published') || kind.startsWith('published')) : status === active);
      const show = matchesStage && searchable.includes(term);
      card.hidden = !show;
      if (show) visible += 1;
    });
    if (count) count.textContent = `${visible} ${visible === 1 ? 'result' : 'results'} shown`;
    if (empty) empty.hidden = visible !== 0;
  }

  buttons.forEach((button) => button.addEventListener('click', () => {
    active = button.dataset.filter || 'all';
    buttons.forEach((b) => {
      const selected = b === button;
      b.classList.toggle('is-active', selected);
      b.setAttribute('aria-pressed', String(selected));
    });
    update();
  }));
  input.addEventListener('input', update);
  update();
})();
