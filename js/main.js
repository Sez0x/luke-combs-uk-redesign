// Header solid-on-scroll
const header = document.querySelector('.site-header');
const onScroll = () => {
  if (window.scrollY > 40) header.classList.add('solid');
  else header.classList.remove('solid');
};
onScroll();
window.addEventListener('scroll', onScroll, { passive: true });

// Mobile nav
const navToggle = document.querySelector('.nav-toggle');
const mobileNav = document.querySelector('.mobile-nav');
if (navToggle && mobileNav) {
  const setOpen = open => {
    mobileNav.classList.toggle('open', open);
    navToggle.setAttribute('aria-expanded', String(open));
    document.documentElement.classList.toggle('nav-open', open);
  };
  navToggle.addEventListener('click', () => {
    setOpen(!mobileNav.classList.contains('open'));
  });
  mobileNav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && mobileNav.classList.contains('open')) setOpen(false);
  });
}

// Tour filter (index teaser has none; tour page uses this)
const filterButtons = document.querySelectorAll('.tour-filter button');
const tourRows = document.querySelectorAll('.tour-row');
filterButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    filterButtons.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const region = btn.dataset.region;
    tourRows.forEach(row => {
      row.style.display = (region === 'all' || row.dataset.region === region) ? 'grid' : 'none';
    });
  });
});

// Click-to-load video facade (avoids broken/oversized embed, no cookie prompt until user opts in)
document.querySelectorAll('.watch-media[data-video]').forEach(media => {
  media.addEventListener('click', () => {
    const id = media.dataset.video;
    const wrap = document.createElement('div');
    wrap.className = 'video-embed-wrap';
    wrap.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0" title="Luke Combs UK video" allow="accelerated-video; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>`;
    media.replaceWith(wrap);
  });
});

// Gallery lightbox
const lightbox = document.querySelector('.lightbox');
if (lightbox) {
  const lbImg = lightbox.querySelector('img');
  const lbCounter = lightbox.querySelector('.lightbox-counter');
  const figures = [...document.querySelectorAll('.gallery-photo img, .masonry figure img')];
  let idx = 0;
  const show = i => {
    idx = (i + figures.length) % figures.length;
    lbImg.src = figures[idx].src.replace(/-\d+x\d+(?=\.\w+$)/, '');
    if (lbCounter) lbCounter.textContent = `${idx + 1} / ${figures.length}`;
  };
  figures.forEach((img, i) => {
    img.parentElement.addEventListener('click', () => {
      show(i);
      lightbox.classList.add('open');
    });
  });
  lightbox.querySelector('.lightbox-close').addEventListener('click', () => lightbox.classList.remove('open'));
  lightbox.querySelector('.lightbox-prev').addEventListener('click', () => show(idx - 1));
  lightbox.querySelector('.lightbox-next').addEventListener('click', () => show(idx + 1));
  lightbox.addEventListener('click', e => { if (e.target === lightbox) lightbox.classList.remove('open'); });
  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape') lightbox.classList.remove('open');
    if (e.key === 'ArrowLeft') show(idx - 1);
    if (e.key === 'ArrowRight') show(idx + 1);
  });
}

// Generic horizontal carousels (gallery rows + featured hero)
document.querySelectorAll('[data-carousel]').forEach(btn => {
  btn.addEventListener('click', () => {
    const track = document.getElementById(btn.dataset.carousel);
    if (!track) return;
    const amount = track.clientWidth * 0.85 * Number(btn.dataset.dir);
    track.scrollBy({ left: amount, behavior: 'smooth' });
  });
});

const heroTrack = document.getElementById('heroTrack');
const heroDots = document.getElementById('heroDots');
if (heroTrack && heroDots) {
  const slideCount = heroTrack.children.length;
  for (let i = 0; i < slideCount; i++) {
    const dot = document.createElement('button');
    dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
    if (i === 0) dot.classList.add('active');
    dot.addEventListener('click', () => {
      heroTrack.scrollTo({ left: heroTrack.clientWidth * i, behavior: 'smooth' });
    });
    heroDots.appendChild(dot);
  }
  const dotEls = [...heroDots.children];
  let scrollTimer;
  heroTrack.addEventListener('scroll', () => {
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(() => {
      const idx = Math.round(heroTrack.scrollLeft / heroTrack.clientWidth);
      dotEls.forEach((d, i) => d.classList.toggle('active', i === idx));
    }, 80);
  }, { passive: true });
}

// Honeypot-protected form submit (no captcha)
document.querySelectorAll('form[data-honeypot]').forEach(form => {
  form.addEventListener('submit', e => {
    e.preventDefault();
    const hp = form.querySelector('.hp-field');
    if (hp && hp.value) return; // silently drop bots
    const btn = form.querySelector('button[type="submit"]');
    btn.textContent = 'Sending…';
    btn.disabled = true;
    setTimeout(() => {
      window.location.href = '/thank-you';
    }, 500);
  });
});
