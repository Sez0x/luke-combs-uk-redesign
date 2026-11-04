# Build sources

Not published (Jekyll skips `_`-prefixed folders on GitHub Pages).

- `originals/`: full-size photos and posters from the band's official site, lukecombsuk.com.
- `images.py`: makes the responsive WebP/JPEG set in `/img` (`python3 _build/images.py`, needs Pillow).
- `build.py`: generates every HTML page, `sitemap.xml` and `robots.txt` from the tour data at the top of the file. Edit the dates there, then run `python3 _build/build.py`.

Past dates are also hidden in the browser by `js/main.js`, and the "Next show" line updates automatically.
