"""Generate the static pages from one set of data (tour dates, nav, images).

Run from the repo root:  python3 _build/build.py
Edit TOUR_2026 / CANDLELIGHT below when dates change, then re-run and commit the HTML.
Past dates are also hidden automatically in the browser by js/main.js.
"""
from pathlib import Path
from datetime import date
from html import escape
import json

ROOT = Path(__file__).resolve().parent.parent
IMG = json.loads((ROOT / "_build" / "images.json").read_text())
SITE = "https://sez0x.github.io/luke-combs-uk-redesign/"
YEAR = 2026

SOCIAL = {
    "instagram": "https://www.instagram.com/lukecombsuktribute/",
    "facebook": "https://www.facebook.com/lukecombsuktribute/",
    "youtube": "https://www.youtube.com/@LukeCombsUK",
    "tiktok": "https://www.tiktok.com/@lukecombstribute",
}
NEWSLETTER_ACTION = "https://lukecombsuk.us13.list-manage.com/subscribe/post?u=2b78be43e5334d1675575d823&amp;id=075c43957e&amp;f_id=002ef7e7f0"
NEWSLETTER_HP = "b_2b78be43e5334d1675575d823_075c43957e"
BOOKING_FORM = "https://lukecombsuk.com/contact-us/"

# Source: https://lukecombsuk.com/uk-tour-2026/ (official site, page last modified 3 Nov 2026), read 4 Nov 2026.
# (iso date, city, venue, ticket url or None, region, status)
TOUR_2026 = [
    ("2026-11-06", "Chesterfield", "Winding Wheel", "https://chesterfieldtheatres.co.uk/events/luke-combs-uk/", "uk", ""),
    ("2026-11-07", "Burnley", "Penny Blacks", "https://www.skiddle.com/whats-on/Burnley/Penny-Blacks/Luke-Combs-UK-tribute-in-BURNLEY/42172501/", "uk", ""),
    ("2026-11-17", "Munich", "Tonhalle", "https://www.eventim.de/en/event/luke-combs-uk-the-worlds-leading-tribute-to-luke-combs-tonhalle-eventfabrik-21544190/", "eu", ""),
    ("2026-11-18", "Frankfurt", "Batschkapp", "https://www.batschkapp.net/events/luke-combs-uk-frankfurt-batschkapp-2026-11-18-200000", "eu", ""),
    ("2026-11-19", "Cologne", "Live Music Hall", "https://www.eventim.de/en/event/luke-combs-uk-tribute-luke-combs-uk-the-worlds-leading-tribute-to-luke-combs-live-music-hall-21523172/", "eu", ""),
    ("2026-11-20", "Berlin", "Metropol", "https://www.eventim.de/en/event/luke-combs-uk-the-worlds-leading-tribute-to-luke-combs-metropol-21650075/", "eu", ""),
    ("2026-11-21", "Hamburg", "Docks Hamburg", "https://www.eventim.de/en/event/luke-combs-uk-tribute-luke-combs-uk-the-worlds-leading-tribute-to-luke-combs-docks-hamburg-21606230/", "eu", ""),
    ("2026-11-26", "Birmingham", "Rodeos", "https://rodeosbbq.co.uk/event/luke-combs-uk-5/", "uk", ""),
    ("2026-11-28", "Lincoln", "The Engine Shed", "https://www.skiddle.com/whats-on/Lincoln/The-Engine-Shed/LINCOLN-GOES-COUNTRY---Luke-Combs--Morgan-Wallen-Tribute/42406721/", "uk", ""),
    ("2026-11-29", "Shrewsbury", "The Buttermarket", "https://www.thebuttermarket.co.uk/event/%F0%9F%A4%A0-luke-combs-uk-tribute-in-concert-special-guest-%E2%AD%90%EF%B8%8F%E2%AD%90%EF%B8%8F%E2%AD%90%EF%B8%8F%E2%AD%90%EF%B8%8F%E2%AD%90%EF%B8%8F-5/", "uk", ""),
    ("2026-12-06", "Birmingham", "Rodeos Country Christmas Market", "https://www.skiddle.com/whats-on/Birmingham/Rodeos-Bbq/Rodeos-Country-Christmas-Market-with-Luke-Combs-UK/42667148/", "uk", ""),
    ("2026-12-11", "Huddersfield", "Smile Bar and Venue", "https://www.skiddle.com/whats-on/Huddersfield/Smile-Bar-And-Venue/Luke-Combs-UK-tribute-in-HUDDERSFIELD/42271868/", "uk", ""),
    ("2026-12-12", "Nottingham", "The Nest · Road To Nashville", "https://www.skiddle.com/whats-on/Nottingham/The-Nest-%28%40-Notts-County-FC%29/Road-to-Nashville-Indoor-Rodeo-Show--The-Nest/42649447/", "uk", ""),
    ("2026-12-13", "Edinburgh", "Edinburgh Corn Exchange", "https://www.edinburghcornexchange.co.uk/all-events/luke-combs-uk-tickets-ae1447611", "uk", ""),
    ("2026-12-19", "Sheffield", "Network Sheffield", "https://www.skiddle.com/whats-on/Sheffield/Network-Sheffield-14-16-Matilda-Street-S14qd/Sheffield-Goes-Country---Luke-Combs-and-Morgan-Wallen-Tribute/42124392/", "uk", ""),
    ("2026-12-20", "Wolverhampton", "Rodeos", None, "uk", "Sold out"),
]

# Source: https://lukecombsuk.com/luke-combs-by-candlelight/ (official site), read 4 Nov 2026.
CANDLELIGHT = [
    ("2027-01-16", "Hull", "Hull City Hall", "https://www.hulltheatres.co.uk/theatre-events/luke-combs-uk-by-candlelight-with-string-orchestra"),
    ("2027-01-23", "Hoddesdon", "The Spotlight", "https://www.thespotlightvenue.com/whats-on/luke-combs-by-candlelight/515/book/1687"),
    ("2027-01-29", "Warrington", "Culture Warrington", "https://culturewarrington.org/whats-on/luke-combs-uk-by-candlelight-with-string-orchestra/"),
    ("2027-01-30", "Crewe", "Lyceum Theatre", "https://trafalgartickets.com/lyceum-theatre-crewe/en-GB/event/music/luke-combs-uk-tickets"),
    ("2027-02-04", "Swindon", "Wyvern Theatre", "https://trafalgartickets.com/swindon-theatres/en-GB/event/music/luke-combs-uk-by-candlelight-tickets"),
    ("2027-02-05", "Birmingham", "Symphony Hall", "https://bmusic.co.uk/events/luke-combs-uk-by-candlelight-with-string-orchestra"),
    ("2027-02-12", "Stockport", "The Plaza", "https://www.quaytickets.com/stockport/en-GB/shows/luke%20combs%20by%20candlelight%20with%20string%20orchestra/events"),
    ("2027-02-20", "Cheltenham", "Cheltenham Town Hall", "https://cheltenhamtownhall.org.uk/event/luke-combs-uk-by-candlelight/"),
    ("2027-03-17", "Chelmsford", "Chelmsford Theatre", "https://www.chelmsfordtheatre.co.uk/events/luke-combs-uk-by-candlelight"),
    ("2027-03-18", "Bath", "Bath Forum", "https://bathforum.ticketline.co.uk/order/tickets/13380726/luke-combs-uk-by-candlelight-with-string-orchestra-bath-forum-2027-03-18-19-30-00"),
]

ALT = {
    "Gallery-1": "Two Luke Combs UK band members playing under red stage lights and haze",
    "Gallery-2": "Luke Combs UK drummer at the kit under green stage light",
    "Gallery-3": "The Luke Combs UK band lined up on stage in front of the crowd",
    "Gallery-4": "Two Luke Combs UK guitarists playing side by side on stage",
    "Gallery-5": "The band posing on stage with a packed theatre crowd behind them",
    "Gallery6": "Fans in cowboy hats watching the stage at a Luke Combs UK show",
    "Gallery7": "Black and white shot of the drummer mid-song",
    "Gallery8": "Hazy black and white wide shot of the singer and the crowd",
    "Gallery9": "The band on stage with guitars under green light",
    "Gallery10": "Black and white shot of the singer at the microphone",
    "Gallery11": "Dark stage with the Luke Combs UK logo on the backdrop",
    "Gallery12": "Guitarist in a cap singing into the microphone under warm light",
    "Gallery13": "Crowd with hands raised as the singer performs",
    "Gallery14": "The singer with an acoustic guitar centre stage under purple lights",
    "Gallery15": "Stage bathed in amber light, seen over the crowd",
    "Gallery16": "The singer alone centre stage under blue light with the logo behind him",
    "Gallery17": "The singer leaning towards the crowd under bright stage lights",
    "Gallery18": "The singer seen from behind, facing a packed theatre",
    "Gallery19": "The singer with arms spread wide in front of the Luke Combs UK logo",
    "Gallery20": "The singer pointing skywards under red light",
    "Gallery21": "The singer pointing upwards under green light",
    "Gallery22": "Close-up of the singer singing into the microphone",
    "Gallery23": "Black and white close-up portrait of the singer",
    "Gallery24": "The singer on stage in front of the illuminated Luke Combs UK logo",
    "Gallery25": "Black and white shot of the singer playing acoustic guitar",
}

SVG = {
 "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M7 2C4.243 2 2 4.243 2 7v10c0 2.757 2.243 5 5 5h10c2.757 0 5-2.243 5-5V7c0-2.757-2.243-5-5-5H7zm10 2c1.654 0 3 1.346 3 3v10c0 1.654-1.346 3-3 3H7c-1.654 0-3-1.346-3-3V7c0-1.654 1.346-3 3-3h10zM12 7a5 5 0 100 10 5 5 0 000-10zm0 2a3 3 0 110 6 3 3 0 010-6zm4.5-3a1 1 0 100 2 1 1 0 000-2z"/></svg>',
 "facebook": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M13.5 21v-7.6h2.6l.4-3h-3V8.5c0-.9.3-1.5 1.5-1.5h1.6V4.3c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6V21h3.1z"/></svg>',
 "youtube": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M21.6 7.2a2.5 2.5 0 00-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 002.4 7.2C2 8.8 2 12 2 12s0 3.2.4 4.8a2.5 2.5 0 001.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 001.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3L10 15z"/></svg>',
 "tiktok": '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M16.6 5.82A4.278 4.278 0 0 1 15.54 3h-3.09v12.4a2.592 2.592 0 0 1-2.59 2.5c-1.42 0-2.6-1.16-2.6-2.6 0-1.72 1.66-3.01 3.37-2.48V9.66c-3.45-.46-6.47 2.22-6.47 5.64 0 3.33 2.76 5.7 5.69 5.7 3.14 0 5.69-2.55 5.69-5.7V9.01a7.35 7.35 0 0 0 4.3 1.38V7.3s-1.88.09-3.24-1.48z"/></svg>',
}
LABEL = {"instagram": "Instagram", "facebook": "Facebook", "youtube": "YouTube", "tiktok": "TikTok"}


def d(iso):
    return date.fromisoformat(iso)


def srcset(name, ext="webp", p=""):
    m = IMG[name]
    return ", ".join(f"{p}img/{name}-{w}.{ext} {w}w" for w in m["widths"])


def pic(name, alt, sizes, p="", lazy=True, priority=False, cls="", full=False):
    m = IMG[name]
    fb = m["fallback"]
    attrs = f'loading="lazy" decoding="async"' if lazy else 'decoding="async"'
    if priority:
        attrs += ' fetchpriority="high"'
    data = f' data-full="{p}img/{name}-{max(m["widths"])}.webp"' if full else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<picture><source type="image/webp" srcset="{srcset(name, p=p)}" sizes="{sizes}">'
            f'<img{c} src="{p}img/{name}-{fb}.jpg" width="{m["w"]}" height="{m["h"]}" alt="{escape(alt)}" {attrs}{data}></picture>')


def social_links(p, cls):
    return "\n".join(
        f'<li><a class="{cls}" href="{SOCIAL[k]}" target="_blank" rel="noopener"><span class="sr-only">{LABEL[k]}</span>{SVG[k]}</a></li>'
        for k in SOCIAL)


def head(p, title, desc, path, og_img="Gallery16-1920.webp", noindex=False, extra=""):
    url = SITE + path
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
{robots}<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Luke Combs UK">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="{SITE}img/{og_img}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="{p}img/icon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{p}img/icon-192.png">
<link rel="apple-touch-icon" href="{p}img/icon-180.png">
<meta name="theme-color" content="#0c0a08">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&amp;family=Inter:wght@400;600;700&amp;display=swap">
<link rel="stylesheet" href="{p}css/style.css">
{extra}</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
'''


NAV = [("tour/", "Tour"), ("candlelight/", "Candlelight"), ("gallery/", "Gallery"), ("contact/", "Bookings")]


def header(p, active="", solid=True):
    def li(href, label):
        cur = ' aria-current="page"' if href == active else ""
        return f'<li><a href="{p}{href}"{cur}>{label}</a></li>'
    desktop = "".join(li(h, l) for h, l in NAV)
    mobile = "".join(
        f'<li style="--i:{i}"><a href="{p}{h}"{" aria-current=\"page\"" if h == active else ""}><span class="num" aria-hidden="true">0{i+1}</span>{l}</a></li>'
        for i, (h, l) in enumerate(NAV))
    return f'''<header class="site-header{' solid' if solid else ''}">
  <div class="wrap">
    <nav class="main-nav" aria-label="Main">
      <ul>{desktop}</ul>
    </nav>
    <a href="{p or './'}" class="brand"><img src="{p}img/lcuk-logo.png" width="558" height="415" alt="Luke Combs UK, home"></a>
    <div class="header-cta"><a href="{p}tour/" class="btn btn-primary">Get Tickets</a></div>
    <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav"><span class="hamburger" aria-hidden="true"><span></span><span></span><span></span></span></button>
  </div>
</header>

<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
  <ol class="mobile-nav-links">{mobile}</ol>
  <a href="{p}tour/" class="btn btn-primary btn-block mobile-nav-cta">Get Tickets</a>
  <ul class="mobile-nav-social">
{social_links(p, "social-icon")}
  </ul>
</nav>
'''


def footer(p, sticky=None):
    st = ""
    if sticky:
        st = f'\n<div class="sticky-mobile-cta"><a href="{sticky[0]}" class="btn btn-primary btn-block">{sticky[1]}</a></div>'
    return f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <div class="footer-brand">
          <img src="{p}img/lcuk-logo.png" width="558" height="415" alt="" loading="lazy">
          <span class="brand-text display">Luke Combs UK</span>
        </div>
        <p class="footer-tagline">The world's leading tribute to Luke Combs, endorsed by the man himself.</p>
      </div>
      <div class="footer-links">
        <nav class="footer-col" aria-label="Footer">
          <h2 class="footer-h">Explore</h2>
          <a href="{p}tour/">Tour Dates</a>
          <a href="{p}candlelight/">Candlelight Tour</a>
          <a href="{p}gallery/">Gallery</a>
          <a href="{p}contact/">Bookings</a>
        </nav>
        <div class="footer-col">
          <h2 class="footer-h">Follow</h2>
          <ul class="footer-social-row">
{social_links(p, "social-icon")}
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <small>Luke Combs UK &copy; {YEAR}. All rights reserved.</small>
      <small>Photos: Luke Combs UK.</small>
    </div>
  </div>
</footer>{st}

<script src="{p}js/main.js" defer></script>
</body>
</html>
'''


def breadcrumbs(p, items):
    lis = []
    for href, label in items:
        if href is None:
            lis.append(f'<li aria-current="page">{label}</li>')
        else:
            lis.append(f'<li><a href="{p}{href}">{label}</a></li>')
    return f'''<nav class="breadcrumbs" aria-label="Breadcrumb">
  <div class="wrap"><ol>{"".join(lis)}</ol></div>
</nav>
'''


def date_block(iso):
    x = d(iso)
    return (f'<time class="dateblock" datetime="{iso}"><span class="dow">{x:%a}</span>'
            f'<span class="day">{x.day}</span><span class="mon">{x:%b}</span></time>')


def tour_rows(rows, show_region=True):
    out, month = [], None
    for r in rows:
        iso, city, venue, url = r[0], r[1], r[2], r[3]
        region = r[4] if len(r) > 4 else "uk"
        status = r[5] if len(r) > 5 else ""
        x = d(iso)
        if (x.year, x.month) != month:
            if month:
                out.append("</ol></div>")
            month = (x.year, x.month)
            out.append(f'<div class="tour-month" data-month="{x:%Y-%m}"><h3 class="tour-month-h">{x:%B %Y}</h3><ol class="tour-list">')
        if url:
            cta = (f'<a href="{url}" class="btn btn-outline" target="_blank" rel="noopener">Tickets'
                   f'<span class="sr-only"> for {escape(city)}, {escape(venue)} (opens in new tab)</span></a>')
        else:
            cta = f'<span class="badge">{escape(status or "Tickets soon")}</span>'
        reg = f' data-region="{region}"' if show_region else ""
        country = ' <span class="country">Germany</span>' if region == "eu" else ""
        out.append(f'<li class="tour-row" data-date="{iso}"{reg} data-city="{escape(city)}" data-venue="{escape(venue)}" data-url="{url or ""}">'
                   f'{date_block(iso)}<div class="place"><b>{escape(city)}{country}</b><span>{escape(venue)}</span></div>{cta}</li>')
    out.append("</ol></div>")
    return "\n".join(out)


def upcoming(rows, today):
    return [r for r in rows if d(r[0]) >= today]


def next_show_strip(rows, today, label="Next show"):
    nxt = upcoming(rows, today)
    if not nxt:
        return '<div class="next-show" id="next" data-next-show><p>New dates coming soon. Follow us on socials for announcements.</p></div>'
    r = nxt[0]
    x = d(r[0])
    url = r[3]
    btn = (f'<a href="{url}" class="btn btn-primary" target="_blank" rel="noopener" data-next-link>Get Tickets</a>'
           if url else '<span class="badge" data-next-link>Tickets soon</span>')
    return f'''<div class="next-show" id="next" data-next-show>
  <div>
    <span class="label">{label}</span>
    <p class="info"><time class="date display" datetime="{r[0]}" data-next-date>{x:%a %-d %b}</time>
    <span class="venue" data-next-venue>{escape(r[1])}, {escape(r[2])}</span></p>
  </div>
  {btn}
</div>'''


TODAY = date(2026, 11, 4)


def page_home():
    p = ""
    nxt = upcoming(TOUR_2026, TODAY)[0]
    x = d(nxt[0])
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "MusicGroup", "name": "Luke Combs UK",
        "url": SITE, "logo": SITE + "img/lcuk-logo.png", "genre": "Country",
        "description": "The world's leading tribute to Luke Combs, endorsed by the man himself.",
        "sameAs": list(SOCIAL.values()),
        "member": [{"@type": "Person", "name": "Liam Price", "roleName": "Lead vocals"}],
    }, indent=1)
    h = head(p, "Luke Combs UK | The World's Leading Luke Combs Tribute",
             "Luke Combs UK, the world's leading tribute to Luke Combs, endorsed by the man himself. Full band, authentic sound, on tour across the UK and Europe.",
             "", extra=f'<script type="application/ld+json">\n{ld}\n</script>\n')
    m19, m16 = IMG["Gallery19"], IMG["Gallery16"]
    hero_pic = (f'<picture>'
                f'<source media="(max-width: 720px)" type="image/webp" srcset="{srcset("Gallery19")}" sizes="100vw">'
                f'<source type="image/webp" srcset="{srcset("Gallery16")}" sizes="100vw">'
                f'<img src="img/Gallery16-960.jpg" width="{m16["w"]}" height="{m16["h"]}" alt="" decoding="async" fetchpriority="high"></picture>')
    body = f'''{header(p, solid=False)}
<main id="main">
<section class="hero" aria-labelledby="hero-title">
  <div class="hero-media">{hero_pic}</div>
  <div class="wrap hero-content">
    <p class="eyebrow">Endorsed by Luke Combs himself</p>
    <h1 class="hero-title display" id="hero-title">The world's leading tribute to <em>Luke Combs</em></h1>
    <p class="hero-sub">Dust off your hats and boots. Luke Combs UK brings the look, the voice and the full band for an unforgettable night of country music, note for note.</p>
    <div class="hero-actions">
      <a href="tour/" class="btn btn-primary">See Tour Dates</a>
      <a href="contact/" class="btn btn-outline">Book For Your Event</a>
    </div>
    <p class="hero-next" data-next-show>
      <span class="label">Next show</span>
      <a href="tour/#next"><time datetime="{nxt[0]}" data-next-date>{x:%a %-d %b}</time> <span data-next-venue>{escape(nxt[1])}, {escape(nxt[2])}</span></a>
    </p>
  </div>
</section>

<section class="about" aria-labelledby="about-title">
  <div class="wrap about-grid">
    <div class="about-copy">
      <p class="eyebrow">The Tribute</p>
      <h2 class="section-title display" id="about-title">As close as you'll get<br>to the real deal</h2>
      <p>Luke Combs UK delivers the look and the authentic sound of the GRAMMY-nominated country megastar: full band, full production, every stadium-sized hit.</p>
      <p>Fronted by Wolverhampton singer Liam Price, the band has been on the road since 2023, and was invited to play the opening of Luke's own Nashville bar, Category 10.</p>
      <ul class="stat-row">
        <li class="stat"><b>2023</b><span>On the road since</span></li>
        <li class="stat"><b>UK &amp; EU</b><span>Touring</span></li>
        <li class="stat"><b>Full Band</b><span>Live on stage</span></li>
      </ul>
    </div>
    <figure class="about-media">
      {pic("Luke-Combs-UK-With-Luke-Comb", "Luke Combs UK frontman Liam Price with Luke Combs", "(max-width: 920px) 90vw, 514px", p)}
    </figure>
  </div>
</section>

<section class="tour-teaser" aria-labelledby="tour-title">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">On The Road</p>
        <h2 class="section-title display" id="tour-title">Tour Dates</h2>
      </div>
      <a href="tour/" class="section-link">Full schedule <span aria-hidden="true">→</span></a>
    </div>
    <div class="tour-teaser-grid">
      <a class="tour-card" href="tour/">
        {pic("2026-Tour-Poster-4", "", "(max-width: 920px) 92vw, 560px", p)}
        <div class="tour-card-body">
          <p class="eyebrow">2026</p>
          <h3>UK Tour 2026</h3>
          <p>Winter dates across the UK &amp; Germany</p>
          <span class="btn btn-outline" aria-hidden="true">View Dates</span>
        </div>
      </a>
      <a class="tour-card" href="candlelight/">
        {pic("Candlelight-Square-Tour-Dates-Web", "", "(max-width: 920px) 92vw, 560px", p)}
        <div class="tour-card-body">
          <p class="eyebrow">2027</p>
          <h3>Candlelight Tour</h3>
          <p>An intimate evening with string orchestra</p>
          <span class="btn btn-outline" aria-hidden="true">View Dates</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="watch" aria-labelledby="watch-title">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">Watch</p>
        <h2 class="section-title display" id="watch-title">See It Live</h2>
      </div>
      <a href="{SOCIAL['youtube']}" class="section-link" target="_blank" rel="noopener">More on YouTube <span aria-hidden="true">→</span></a>
    </div>
    <div class="watch-panel">
      <a class="watch-media" href="{SOCIAL['youtube']}/videos" target="_blank" rel="noopener">
        {pic("Gallery-5", "The band on stage with a packed theatre crowd behind them", "(max-width: 920px) 92vw, 700px", p)}
        <span class="play" aria-hidden="true"><span class="play-btn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span></span>
        <span class="sr-only">Watch Luke Combs UK videos on YouTube (opens in new tab)</span>
      </a>
      <div class="watch-info">
        <p class="eyebrow">Full Band, Full Sound</p>
        <h3>Straight From The Stage</h3>
        <p>Live clips from shows across the UK. Head to the channel for the full library.</p>
        <a href="{SOCIAL['youtube']}/videos" class="btn btn-primary" target="_blank" rel="noopener">Watch On YouTube</a>
      </div>
    </div>
  </div>
</section>

<section class="gallery-teaser" aria-labelledby="gallery-title">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">In Pictures</p>
        <h2 class="section-title display" id="gallery-title">Gallery</h2>
      </div>
      <a href="gallery/" class="section-link">See full gallery <span aria-hidden="true">→</span></a>
    </div>
    <a class="gallery-bento" href="gallery/" aria-label="Open the full gallery">
      <figure>{pic("Gallery18", ALT["Gallery18"], "(max-width: 560px) 46vw, 280px", p)}</figure>
      <figure>{pic("Gallery-4", ALT["Gallery-4"], "(max-width: 560px) 46vw, 560px", p)}</figure>
      <figure>{pic("Gallery17", ALT["Gallery17"], "(max-width: 560px) 46vw, 560px", p)}</figure>
      <figure>{pic("Gallery23", ALT["Gallery23"], "280px", p)}</figure>
    </a>
  </div>
</section>

{newsletter_band(p)}
</main>
'''
    data = json.dumps([{"date": r[0], "city": r[1], "venue": r[2], "url": r[3] or ""} for r in TOUR_2026 + [(a, b, c, u) for a, b, c, u in CANDLELIGHT]])
    body = body.replace("</main>", f'<script type="application/json" id="tour-data">{data}</script>\n</main>', 1)
    (ROOT / "index.html").write_text(h + body + footer(p))


def newsletter_form(p, uid, outline=False):
    return f'''<form class="nl-form" action="{NEWSLETTER_ACTION}" method="post" target="_blank">
        <div class="field-row">
          <div class="field"><label for="{uid}-fname">First name</label><input id="{uid}-fname" type="text" name="FNAME" autocomplete="given-name" required></div>
          <div class="field"><label for="{uid}-lname">Last name</label><input id="{uid}-lname" type="text" name="LNAME" autocomplete="family-name" required></div>
        </div>
        <div class="field"><label for="{uid}-email">Email address</label><input id="{uid}-email" type="email" name="EMAIL" autocomplete="email" required></div>
        <div class="hp-field" aria-hidden="true"><input type="text" name="{NEWSLETTER_HP}" tabindex="-1" value="" autocomplete="off"></div>
        <button type="submit" class="btn {'btn-outline' if outline else 'btn-primary'} btn-block">Subscribe</button>
        <p class="form-note">Sign-ups are handled by Mailchimp and open in a new tab to confirm.</p>
      </form>'''


def newsletter_band(p):
    return f'''<section class="cta-band" aria-labelledby="nl-title">
  <div class="wrap cta-grid">
    <div class="cta-copy">
      <p class="eyebrow">Stay In The Loop</p>
      <h2 class="section-title display" id="nl-title">Sign Up For Tour News</h2>
      <p>New dates, ticket presales and behind-the-scenes updates, straight to your inbox.</p>
    </div>
    <div class="form-card">
      {newsletter_form(p, "nl")}
    </div>
  </div>
</section>'''


def page_tour():
    p = "../"
    h = head(p, "Tour Dates 2026 & Candlelight Tour 2027 | Luke Combs UK",
             "Upcoming Luke Combs UK tour dates across the UK and Germany, plus the Candlelight Tour with string orchestra in 2027. Get tickets.",
             "tour/", og_img="2026-Tour-Poster-4-1080.webp")
    body = f'''{header(p, active="tour/")}
{breadcrumbs(p, [("", "Home"), (None, "Tour Dates")])}
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">2026 &amp; 2027</p>
    <h1 class="display">Tour Dates</h1>
    <p>The rest of the 2026 tour across the UK and Germany, plus the intimate Candlelight Tour in 2027. Full band, full production, every night.</p>
    <div class="hero-actions">
      <a href="#next" class="btn btn-primary">See Next Show</a>
      <a href="../contact/" class="btn btn-outline">Book For Your Event</a>
    </div>
  </div>
</section>

<section class="tour-section" aria-labelledby="t26">
  <div class="wrap">
    {next_show_strip(TOUR_2026, TODAY)}
    <div class="section-head">
      <div>
        <p class="eyebrow">UK &amp; Europe</p>
        <h2 class="section-title display" id="t26">2026</h2>
      </div>
      <div class="tour-filter" role="group" aria-label="Filter dates by region">
        <button type="button" aria-pressed="true" data-region="all">All</button>
        <button type="button" aria-pressed="false" data-region="uk">UK</button>
        <button type="button" aria-pressed="false" data-region="eu">Europe</button>
      </div>
    </div>
    <div class="tour-months" data-tour>
{tour_rows(TOUR_2026)}
    </div>
    <p class="tour-empty" hidden>New dates coming soon. Follow us on socials for announcements.</p>
  </div>
</section>

<section id="candlelight" class="tour-section" aria-labelledby="cl">
  <div class="wrap">
    <div class="watch-panel watch-panel-wide">
      <div class="watch-media">{pic("Candlelight-Square-Tour-Dates-Web", "Luke Combs UK By Candlelight 2027 tour poster listing ten UK theatre dates", "(max-width: 920px) 92vw, 520px", p)}</div>
      <div class="watch-info">
        <p class="eyebrow">2027</p>
        <h2 class="display" id="cl">Luke Combs By Candlelight</h2>
        <p>Stripped back and up close: ten UK theatre dates from January to March 2027, with a string orchestra.</p>
        <a href="../candlelight/" class="btn btn-primary">See Candlelight Dates</a>
      </div>
    </div>
  </div>
</section>
</main>
'''
    (ROOT / "tour" / "index.html").write_text(h + body + footer(p, ("#next", "Tickets for the next show")))


def page_candlelight():
    p = "../"
    h = head(p, "Luke Combs By Candlelight 2027 | Luke Combs UK",
             "Luke Combs UK By Candlelight: an intimate evening with string orchestra, touring UK theatres from January to March 2027. See all dates and get tickets.",
             "candlelight/", og_img="Candlelight-Square-Tour-Dates-Web-1080.webp")
    rows = [(a, b, c, u, "uk", "") for a, b, c, u in CANDLELIGHT]
    body = f'''{header(p, active="candlelight/")}
{breadcrumbs(p, [("", "Home"), ("tour/", "Tour"), (None, "Candlelight")])}
<main id="main">
<section class="page-hero page-hero-warm">
  <div class="wrap">
    <p class="eyebrow">2027</p>
    <h1 class="display">Luke Combs By Candlelight</h1>
    <p>Stripped back and up close. Ten UK theatre dates from January to March 2027 with a string orchestra, for the most intimate Luke Combs UK show there is.</p>
    <div class="hero-actions">
      <a href="#next" class="btn btn-primary">See Next Show</a>
      <a href="../tour/" class="btn btn-outline">Full Band Tour Dates</a>
    </div>
  </div>
</section>

<section class="tour-section" aria-labelledby="cl27">
  <div class="wrap">
    {next_show_strip(rows, TODAY)}
    <div class="section-head">
      <div>
        <p class="eyebrow">2027 Dates</p>
        <h2 class="section-title display" id="cl27">Candlelight Tour</h2>
      </div>
    </div>
    <div class="tour-months" data-tour>
{tour_rows(rows, show_region=False)}
    </div>
    <p class="tour-empty" hidden>New dates coming soon. Follow us on socials for announcements.</p>
  </div>
</section>

<section class="tour-section">
  <div class="wrap">
    <div class="watch-panel watch-panel-wide">
      <div class="watch-media">{pic("Candlelight-Square-Tour-Dates-Web", "Luke Combs UK By Candlelight 2027 tour poster", "(max-width: 920px) 92vw, 520px", p)}</div>
      <div class="watch-info">
        <h2 class="display">An Intimate Evening</h2>
        <p>The Candlelight Tour brings the songs to some of the UK's finest theatres, backed by a string orchestra, for a completely different side of Luke Combs UK.</p>
        <a href="../tour/" class="btn btn-primary">See The Full Band Tour</a>
      </div>
    </div>
  </div>
</section>
</main>
'''
    (ROOT / "candlelight" / "index.html").write_text(h + body + footer(p, ("#next", "Tickets for the next show")))


FEATURED = ["Gallery16", "Gallery-1", "Gallery9", "Gallery14", "Gallery-5", "Gallery15"]
COLLAGE = [("Gallery-1", ""), ("Gallery21", ""), ("Gallery-2", ""), ("Gallery18", ""), ("Gallery9", "big"),
           ("Gallery-3", ""), ("Gallery22", ""), ("Gallery6", ""), ("Gallery19", ""), ("Gallery13", ""),
           ("Gallery-4", "big"), ("Gallery23", ""), ("Gallery10", ""), ("Gallery20", ""), ("Gallery17", "big"),
           ("Gallery7", ""), ("Gallery24", ""), ("Gallery11", ""), ("Gallery14", ""), ("Gallery25", "big"),
           ("Gallery8", ""), ("Gallery12", ""), ("Gallery15", ""), ("Gallery16", "")]


def page_gallery():
    p = "../"
    h = head(p, "Gallery | Luke Combs UK",
             "Photos from Luke Combs UK shows: the band, the lights and the crowds.", "gallery/")
    feat = "\n".join(f'<figure class="gallery-photo"><button type="button" class="zoom">{pic(n, ALT[n], "(max-width: 1180px) 100vw, 1132px", p, lazy=i > 0, full=True)}<span class="sr-only">Enlarge photo</span></button></figure>'
                     for i, n in enumerate(FEATURED))
    col = "\n".join(f'<figure class="gallery-photo {c}"><button type="button" class="zoom">{pic(n, ALT[n], "(max-width: 560px) 50vw, (max-width: 920px) 25vw, " + ("380px" if c else "190px"), p, full=True)}<span class="sr-only">Enlarge photo</span></button></figure>'
                    for n, c in COLLAGE)
    body = f'''{header(p, active="gallery/")}
{breadcrumbs(p, [("", "Home"), (None, "Gallery")])}
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">On Stage &amp; Behind It</p>
    <h1 class="display">Gallery</h1>
    <p>Moments from the road: lights, boots and a packed house. Tap any photo for a closer look.</p>
    <div class="hero-actions">
      <a href="../tour/" class="btn btn-primary">See Tour Dates</a>
      <a href="../contact/" class="btn btn-outline">Book For Your Event</a>
    </div>
  </div>
</section>

<section class="gallery-featured" aria-label="Featured photos">
  <div class="wrap">
    <div class="carousel-hero">
      <div class="carousel-hero-track" id="heroTrack" tabindex="0" aria-label="Featured photos, scroll sideways">
{feat}
      </div>
      <button type="button" class="carousel-arrow prev" data-carousel="heroTrack" data-dir="-1" aria-label="Previous photo"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" d="M15 5l-7 7 7 7"/></svg></button>
      <button type="button" class="carousel-arrow next" data-carousel="heroTrack" data-dir="1" aria-label="Next photo"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" d="M9 5l7 7-7 7"/></svg></button>
    </div>
    <div class="carousel-dots" id="heroDots"></div>
  </div>
</section>

<section class="gallery-collage-section" aria-labelledby="every">
  <div class="wrap">
    <div class="section-head">
      <div>
        <p class="eyebrow">The Full Collection</p>
        <h2 class="section-title display" id="every">Every Show, Every Angle</h2>
      </div>
    </div>
    <div class="gallery-collage">
{col}
    </div>
  </div>
</section>
</main>

<div class="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden>
  <button type="button" class="lightbox-close" aria-label="Close">&#x2715;</button>
  <button type="button" class="lightbox-nav lightbox-prev" aria-label="Previous photo">&#x2039;</button>
  <img alt="">
  <button type="button" class="lightbox-nav lightbox-next" aria-label="Next photo">&#x203A;</button>
  <span class="lightbox-counter" aria-live="polite"></span>
</div>
'''
    (ROOT / "gallery" / "index.html").write_text(h + body + footer(p, ("../tour/", "See tour dates &amp; get tickets")))


def page_contact():
    p = "../"
    h = head(p, "Book Luke Combs UK: Weddings, Festivals & Private Events",
             "Book Luke Combs UK for your wedding, festival, corporate event or private party.", "contact/")
    body = f'''{header(p, active="contact/")}
{breadcrumbs(p, [("", "Home"), (None, "Bookings")])}
<main id="main">
<section class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Make It A Night To Remember</p>
    <h1 class="display">Book Luke Combs UK</h1>
    <p>Weddings, festivals, private parties, corporate nights. Send us the details and we'll be in touch. See y'all at the show.</p>
    <div class="hero-actions"><a href="#booking" class="btn btn-primary">Start Your Enquiry</a></div>
  </div>
</section>

<section id="booking" class="tour-section">
  <div class="wrap cta-grid cta-grid-top">
    <div class="form-card booking-card">
      <h2 class="display card-title">Booking enquiries</h2>
      <p>All bookings go through the official enquiry form. To get a quick answer, include:</p>
      <ul class="checklist">
        <li>The date of your event</li>
        <li>The venue and town</li>
        <li>The type of event (wedding, festival, corporate, private party)</li>
        <li>Rough audience size and any timings</li>
      </ul>
      <a href="{BOOKING_FORM}" class="btn btn-primary btn-block" target="_blank" rel="noopener">Open the enquiry form<span class="sr-only"> (opens lukecombsuk.com in a new tab)</span></a>
      <p class="form-note">You can also message us on <a href="{SOCIAL['facebook']}" target="_blank" rel="noopener">Facebook</a> or <a href="{SOCIAL['instagram']}" target="_blank" rel="noopener">Instagram</a>.</p>
    </div>
    <div>
      <p class="eyebrow">Newsletter</p>
      <h2 class="section-title display">Want tour news first?</h2>
      <p class="muted">Sign up for presales, new dates and behind-the-scenes updates.</p>
      {newsletter_form(p, "nl2", outline=True)}
    </div>
  </div>
</section>
</main>
'''
    (ROOT / "contact" / "index.html").write_text(h + body + footer(p, ("../tour/", "See tour dates &amp; get tickets")))


def page_404():
    base = "/luke-combs-uk-redesign/"
    h = head(base, "Page Not Found | Luke Combs UK", "This page couldn't be found.", "404.html", noindex=True)
    body = f'''<main id="main">
<section class="page-hero page-404">
  <div class="wrap">
    <a href="{base}" class="brand-404"><img src="{base}img/lcuk-logo.png" width="558" height="415" alt="Luke Combs UK, home"></a>
    <p class="eyebrow">404</p>
    <h1 class="display">This one's not on the setlist</h1>
    <p>The page you're looking for has moved on, or never existed. Let's get you back to the show.</p>
    <div class="hero-actions">
      <a href="{base}" class="btn btn-primary">Back To Home</a>
      <a href="{base}tour/" class="btn btn-outline">See Tour Dates</a>
    </div>
  </div>
</section>
</main>
</body>
</html>
'''
    (ROOT / "404.html").write_text(h + body)


def sitemap():
    urls = ["", "tour/", "candlelight/", "gallery/", "contact/"]
    items = "\n".join(f"  <url><loc>{SITE}{u}</loc></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}\n</urlset>\n')
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n")


if __name__ == "__main__":
    page_home(); page_tour(); page_candlelight(); page_gallery(); page_contact(); page_404(); sitemap()
    print("built")
