// Luke Combs UK: small progressive enhancements. The site works without JS.

// Header goes solid once you scroll
const header = document.querySelector('.site-header');
if (header && !header.classList.contains('solid')) {
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 40);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}

// Mobile nav
const navToggle = document.querySelector('.nav-toggle');
const mobileNav = document.querySelector('.mobile-nav');
if (navToggle && mobileNav) {
  const setOpen = open => {
    mobileNav.classList.toggle('open', open);
    navToggle.setAttribute('aria-expanded', String(open));
    navToggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    document.documentElement.classList.toggle('nav-open', open);
    if (open) mobileNav.querySelector('a')?.focus();
  };
  navToggle.addEventListener('click', () => setOpen(!mobileNav.classList.contains('open')));
  mobileNav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && mobileNav.classList.contains('open')) { setOpen(false); navToggle.focus(); }
  });
}

// Tour lists: hide dates that have passed, keep the "next show" strip current
const todayISO = (() => {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
})();
const fmt = iso => new Date(`${iso}T12:00:00`).toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' });

document.querySelectorAll('[data-tour]').forEach(list => {
  list.querySelectorAll('.tour-row').forEach(row => {
    if (row.dataset.date < todayISO) { row.remove(); }
  });
  list.querySelectorAll('.tour-month').forEach(m => { if (!m.querySelector('.tour-row')) m.remove(); });
  if (!list.querySelector('.tour-row')) {
    list.parentElement.querySelector('.tour-empty')?.removeAttribute('hidden');
  }
});

const nextShow = (() => {
  const row = document.querySelector('[data-tour] .tour-row');
  if (row) return row.dataset;
  const json = document.getElementById('tour-data');
  if (!json) return null;
  try {
    return JSON.parse(json.textContent).filter(s => s.date >= todayISO).sort((a, b) => a.date.localeCompare(b.date))[0] || null;
  } catch { return null; }
})();
document.querySelectorAll('[data-next-show]').forEach(el => {
  if (!nextShow) {
    if (el.classList.contains('hero-next')) el.hidden = true;
    else el.innerHTML = '<p>New dates coming soon. Follow us on socials for announcements.</p>';
    return;
  }
  const { date, city, venue, url } = nextShow;
  const t = el.querySelector('[data-next-date]');
  const v = el.querySelector('[data-next-venue]');
  if (t) { t.textContent = fmt(date); t.setAttribute('datetime', date); }
  if (v) v.textContent = `${city}, ${venue}`;
  const link = el.querySelector('a[data-next-link]');
  if (link && url) link.href = url;
});

// Tour region filter
const filterButtons = document.querySelectorAll('.tour-filter button');
filterButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    filterButtons.forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
    const region = btn.dataset.region;
    document.querySelectorAll('[data-tour] .tour-row').forEach(row => {
      row.hidden = !(region === 'all' || row.dataset.region === region);
    });
    document.querySelectorAll('[data-tour] .tour-month').forEach(m => {
      m.hidden = !m.querySelector('.tour-row:not([hidden])');
    });
  });
});

// Gallery lightbox
const lightbox = document.querySelector('.lightbox');
if (lightbox) {
  const lbImg = lightbox.querySelector('img');
  const lbCounter = lightbox.querySelector('.lightbox-counter');
  const seen = new Set();
  const imgs = [...document.querySelectorAll('.gallery-collage img, .gallery-featured img')]
    .filter(i => !seen.has(i.dataset.full) && seen.add(i.dataset.full));
  let idx = 0;
  let lastFocus = null;
  const show = i => {
    idx = (i + imgs.length) % imgs.length;
    lbImg.src = imgs[idx].dataset.full || imgs[idx].currentSrc;
    lbImg.alt = imgs[idx].alt;
    lbCounter.textContent = `${idx + 1} / ${imgs.length}`;
  };
  const open = i => {
    lastFocus = document.activeElement;
    show(i);
    lightbox.hidden = false;
    document.documentElement.classList.add('nav-open');
    lightbox.querySelector('.lightbox-close').focus();
  };
  const close = () => {
    lightbox.hidden = true;
    document.documentElement.classList.remove('nav-open');
    lastFocus?.focus();
  };
  // featured carousel items open the matching photo in the collage set
  document.querySelectorAll('.gallery-photo .zoom').forEach(btn => {
    btn.addEventListener('click', () => {
      const img = btn.querySelector('img');
      let i = imgs.indexOf(img);
      if (i < 0) i = imgs.findIndex(x => x.dataset.full === img.dataset.full);
      open(Math.max(0, i));
    });
  });
  lightbox.querySelector('.lightbox-close').addEventListener('click', close);
  lightbox.querySelector('.lightbox-prev').addEventListener('click', () => show(idx - 1));
  lightbox.querySelector('.lightbox-next').addEventListener('click', () => show(idx + 1));
  lightbox.addEventListener('click', e => { if (e.target === lightbox) close(); });
  document.addEventListener('keydown', e => {
    if (lightbox.hidden) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(idx - 1);
    if (e.key === 'ArrowRight') show(idx + 1);
    if (e.key === 'Tab') {
      const f = [...lightbox.querySelectorAll('button')];
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
}

// Featured carousel
document.querySelectorAll('[data-carousel]').forEach(btn => {
  btn.addEventListener('click', () => {
    const track = document.getElementById(btn.dataset.carousel);
    if (track) track.scrollBy({ left: track.clientWidth * Number(btn.dataset.dir), behavior: 'smooth' });
  });
});
const heroTrack = document.getElementById('heroTrack');
const heroDots = document.getElementById('heroDots');
if (heroTrack && heroDots) {
  [...heroTrack.children].forEach((_, i) => {
    const dot = document.createElement('button');
    dot.type = 'button';
    dot.setAttribute('aria-label', `Go to photo ${i + 1}`);
    if (i === 0) dot.setAttribute('aria-current', 'true');
    dot.addEventListener('click', () => heroTrack.scrollTo({ left: heroTrack.clientWidth * i, behavior: 'smooth' }));
    heroDots.appendChild(dot);
  });
  const dots = [...heroDots.children];
  let t;
  heroTrack.addEventListener('scroll', () => {
    clearTimeout(t);
    t = setTimeout(() => {
      const i = Math.round(heroTrack.scrollLeft / heroTrack.clientWidth);
      dots.forEach((d, j) => d.toggleAttribute('aria-current', i === j));
    }, 80);
  }, { passive: true });
}
