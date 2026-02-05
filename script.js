// Smooth scroll for navigasjonslenker
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();
    const id = this.getAttribute('href').slice(1);
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

// Søkefunksjon – søker i teksten på siden og markerer treff
(function () {
  const searchInput = document.getElementById('site-search');
  const searchCountEl = document.getElementById('search-result-count');
  const main = document.querySelector('main');
  const topics = document.querySelectorAll('.topic');

  if (!searchInput || !main) return;

  function escapeRegex(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  function clearHighlights() {
    main.querySelectorAll('mark.search-highlight').forEach(function (mark) {
      const parent = mark.parentNode;
      parent.replaceChild(document.createTextNode(mark.textContent), mark);
      parent.normalize();
    });
    topics.forEach(function (section) {
      section.classList.remove('search-no-match');
    });
  }

  function highlightTextNodes(parent, query) {
    const regex = new RegExp(escapeRegex(query), 'gi');
    const walker = document.createTreeWalker(parent, NodeFilter.SHOW_TEXT, null, false);
    const textNodes = [];
    while (walker.nextNode()) textNodes.push(walker.currentNode);

    textNodes.forEach(function (node) {
      const text = node.textContent;
      if (!text.trim()) return;
      const parts = text.split(regex);
      if (parts.length <= 1) return;

      const fragment = document.createDocumentFragment();
      let lastIndex = 0;
      let match;
      regex.lastIndex = 0;
      while ((match = regex.exec(text)) !== null) {
        fragment.appendChild(document.createTextNode(text.slice(lastIndex, match.index)));
        const mark = document.createElement('mark');
        mark.className = 'search-highlight';
        mark.textContent = match[0];
        fragment.appendChild(mark);
        lastIndex = match.index + match[0].length;
      }
      fragment.appendChild(document.createTextNode(text.slice(lastIndex)));
      node.parentNode.replaceChild(fragment, node);
    });
  }

  function runSearch() {
    const query = searchInput.value.trim();
    clearHighlights();

    if (!query) {
      searchCountEl.textContent = '';
      return;
    }

    let totalMatches = 0;
    const regex = new RegExp(escapeRegex(query), 'gi');

    topics.forEach(function (section) {
      const text = section.textContent || '';
      const matchCount = (text.match(regex) || []).length;
      if (matchCount > 0) {
        totalMatches += matchCount;
        highlightTextNodes(section, query);
        section.classList.remove('search-no-match');
      } else {
        section.classList.add('search-no-match');
      }
    });

    if (totalMatches > 0) {
      searchCountEl.textContent = totalMatches + ' treff';
    } else {
      searchCountEl.textContent = 'Ingen treff';
    }
  }

  searchInput.addEventListener('input', runSearch);
  searchInput.addEventListener('search', function () {
    if (!this.value.trim()) runSearch();
  });
})();
