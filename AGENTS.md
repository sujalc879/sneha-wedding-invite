# AGENTS.md: Wedding Invitation Website Builder

You are a senior front-end developer, a motion designer and a luxury Indian wedding invitation designer.
Build ONE self-contained `public/index.html` that LOOKS and MOVES like a reference invitation, says ONLY what `DETAILS.md` says, and always contains the fixed features in section 6.

Read this file and `DETAILS.md` completely before any work. Re-read sections 4 and 11 before every build and every fix.
Keep replies short. Work is delivered as files on disk. Never paste the site's code into chat.

---

## 1. Two layers (never mix them) and priority

| Layer | Decided by | Covers |
|---|---|---|
| STYLE | the reference in `reference/` | colours, fonts, backgrounds, textures, layout, spacing, card shapes, borders, frames, ornaments, icon and imagery style, opening animation, transitions, section naming style, mood |
| CONTENT + FEATURES | `DETAILS.md` and this file | names, dates, days, times, venues, links, events, photos, the fixed features |

The reference can never add, remove, rename or reorder anything in the second layer.

If instructions conflict, the order is: section 11 hard rules > `DETAILS.md` (content) > reference (style) > defaults in this file > the user's latest chat message.
The user may change style or feature defaults in chat. If a chat message would break a section 4 or section 11 rule, say so in one sentence and confirm once before doing it.

---

## 2. Project layout

```
AGENTS.md      this file: rules, same for every wedding
DETAILS.md     the couple's details: single source of truth, filled by the user
reference/     the reference invite (video and/or screenshots). Never deployed.
originals/     raw couple photos. Never modified, never deployed.
public/        DEPLOY FOLDER: index.html, photo1.jpg..photo5.jpg, og.jpg. Nothing else.
work/          scratch: frames/, sheets/, screenshots/, scripts, PLAN.md,
               STYLE_DNA.md, CHECKLIST.md, MATCH_REPORT.md
```

- Create missing folders. If this is not a git repo, run `git init` and commit after each phase (`phase-N: summary`) so any step can be undone.
- Never add a remote or push. The repo holds personal photos, addresses and phone numbers.
- Only `public/` is ever uploaded to a host.

---

## 3. Workflow (follow in order)

Keep `work/PLAN.md` as a checkbox list of these phases and tick items as you finish them. Re-read it whenever you resume.

**Phase 0. Intake and validate.**
Treat `[ ]`, blank, `skip` and anything inside `<!-- -->` as EMPTY. An empty optional field means that element is left out of the site completely.
Stop and ask ONLY if: `reference/` has no usable files; or Bride, Groom, Name order, Main date and time, or all functions are missing; or `originals/` has no photos.
For anything else, make a sensible assumption, log it in `work/MATCH_REPORT.md`, and continue.

**Phase 1. Prepare photos** (section 9).

**Phase 2. Study the reference** and write `work/STYLE_DNA.md` (section 5).
If the user's prompt says to stop after the Style DNA, print a summary of at most 12 lines and wait for "go".

**Phase 3. Plan.** In `PLAN.md`, map every reference section to a site section and to the fixed features, and list what cannot be matched exactly and how you will recreate its feel (CSS gradients, inline SVG, the couple's photos).

**Phase 4. Build** `public/index.html`.
Order: head and meta, CSS tokens, HTML sections, SVG symbols (caricatures), then JS (CONFIG, reveal, countdown, ICS, lightbox, plane, petals, glitter, glow, scroll reveal, reduced motion).
Use `/* ===== NAME ===== */` section markers so later fixes are small patches.
The file on disk must be complete and runnable at every save. No "rest of code", ellipses, TODOs or placeholder text, ever.

**Phase 5. Verify** (section 10). Fix everything found, then re-run until green.

**Phase 6. Reports** (section 12).

**Phase 7. Handoff** (section 13).

---

## 4. Data rules: data is sacred

- Every name, date, day, time, venue, address, phone number, link and line from `DETAILS.md` appears EXACTLY as typed. Copy, never retype. Do not translate, transliterate, reformat, round, abbreviate, change case, reorder or "correct" anything.
- `7:30 PM` stays `7:30 PM`. Never write "onwards" or "around".
- Do not invent anything: no extra functions, venues, family names, phone numbers, hashtags, dress codes, quotes, bios, love stories, dates or end times shown on screen.
- Empty field means the element is omitted. Never fill it with sample text or anything from the reference. No lorem ipsum, no "Your Name Here".
- UI labels and section titles ("Save the Date", "Countdown", "Venue", "The Couple") are allowed, in neutral wording and the reference's naming style. Do not write sentences about the couple that the user did not provide. Replace anything in the reference's wording that is personal to its couple with neutral wording.
- Day and date mismatch: keep the user's text, compute the real weekday with a script (never from memory), and flag the mismatch in `CHECKLIST.md`.
- Main date vs the "Wedding" function: keep both exactly as typed. The countdown uses the main date. Flag any disagreement.

Where a technical format differs from the displayed text, the DISPLAY stays exact and only the internal value is derived:
- Phone: shown exactly as typed. The `wa.me` link uses digits only (strip `+`, spaces, dashes, brackets, the name).
- Time zone: the countdown and the .ics use the fixed UTC offset from `DETAILS.md` (default `+05:30`, IST). Never use the visitor's local zone.
- Maps links: used byte for byte as `href` (HTML-escaping `&` as `&amp;` is encoding, not editing). Open with `target="_blank" rel="noopener noreferrer"`.
- .ics needs an end time but functions only have a start. Use start + 3 hours via one constant in CONFIG, never display it, and flag it in the report.

---

## 5. Reference study and STYLE DNA

**Read the reference first, before any code.**

Images: open each one at full size, in order.
If you cannot view images in this environment, say so and ask the user to attach key frames (`codex -i frame.png`, or paste into the composer). Do not guess a style.

Video: you cannot watch video, so extract frames and study them.
```
ffprobe -v error -show_entries format=duration -of csv=p=0 reference/<video>
ffmpeg -i reference/<video> -t 10 -vf "fps=8,scale=720:-1" work/frames/open_%03d.png      # opening animation; frame n is at (n-1)/8 s
ffmpeg -ss 10 -i reference/<video> -vf "fps=1,scale=720:-1" work/frames/scroll_%03d.png   # rest of the scroll
ffmpeg -i reference/<video> -vf "fps=1,scale=360:-1,tile=4x3" work/sheets/sheet_%02d.png  # contact sheets for overview
```
Use frame numbers to measure timings (opening steps, transitions). Hover and scroll-linked effects are inferred from neighbouring frames; state that they are inferred.
If `ffmpeg` is missing, try `pip install imageio-ffmpeg opencv-python-headless`. If that fails, ask for 6 to 10 screenshots (one per section) plus 2 or 3 of the opening animation.

**Sample colours from pixels** (Pillow or ImageMagick), do not eyeball them.

**Write `work/STYLE_DNA.md`** (25 lines max) and follow it exactly in code:
a. Mood in five words.
b. Palette: 6 to 10 hex codes, each with its role (page bg, section tints, cards, headings, body text, accent, buttons, borders).
c. Typography: closest free Google Fonts for display/names, headings, subtitle or script, body/labels, with sizes, weights, letter-spacing, where capitals are used.
d. Backgrounds and textures (flat, gradient, paper, watercolour, photographic, pattern; light or dark).
e. Layout rhythm: content width, alignment, section spacing, columns on desktop and phone.
f. Components: card shape and radius, borders, shadows, photo frames, dividers, ornaments, buttons, icons.
g. Imagery: photographic, painted, illustrated or line art; how photos are framed and cropped.
h. Section order and naming style (eyebrow labels, titles, subtitles).
i. Motion: opening reveal (envelope, door, curtain, scroll, card) with steps and timing; section entrances; parallax; particles; hover.
j. What cannot be reproduced exactly and how the feel will be recreated.
Also add a final block `FORBIDDEN STRINGS`: every name, date, venue, hashtag and personal line visible in the reference. The verifier greps for these.

Where the reference is silent, make a deliberate choice that fits it. Avoid generic template tells: identical rounded cards with the same grey shadow, emoji icons, clip-art, Bootstrap-style boxes, tracked all-caps eyebrow labels on every heading (unless the reference does it). Never switch a light reference to dark or the reverse.

---

## 6. Fixed features (all required, styled with the STYLE DNA)

Match each feature to the closest section in the reference and keep the reference's section order where it has an equivalent. Place any feature the reference lacks where it fits naturally.
If the reference has an extra section fillable from `DETAILS.md` (for example a dress-code palette), include it. If it needs content that was not given (love story, menu, hotel info, registry), leave it out.

**6.1 Opening reveal.** Full screen. Page scroll locked and the rest of the page `inert` until opened. Copy the reference's opening style and timing. If it has none: sealed envelope, wax seal with the initials; tap the seal, it glows, a ring of light sweeps out, the flap opens with a burst of sparkling particles, a soft flash, then fade into the hero (about 2 s). Opens by tap, click, Enter or Space (a real focused `<button>`). On open: unlock scroll, scroll to top, move focus to the hero.

**6.2 Hero.** Blessing line, couple names (largest text on the site, in the given name order), subtitle, main wedding date as given, a "Save the Date" button that scrolls to the countdown, and a scroll hint. Background in the reference's style with parallax at about 35% of scroll speed (transform only).

**6.3 The couple.** One card each for bride and groom: label, name, portrait (caricature, section 7), and the bio only if given.

**6.4 Countdown.** Days, hours, minutes, seconds to the main date, updating every second, computed from the fixed-offset timestamp (for example `Date.parse('2026-12-04T20:00:00+05:30')`). After the moment passes show "Just Married". Pause when the tab is hidden and resync on return. `role="timer"` with `aria-live="off"` plus a visually hidden static sentence with the date.

**6.5 Venue details.** Cards for date, time, venue, dress code. "Add to Calendar" downloads one .ics with EVERY function. "Get Directions" opens the exact Maps link in a new tab. A map card drawn in inline SVG in the reference's style (roads, a pin, the venue name) that also opens the link.
.ics rules: CRLF line endings, lines folded at 75 octets, `BEGIN:VCALENDAR` / `VERSION:2.0` / `PRODID`, one `VEVENT` per function with `UID`, `DTSTAMP`, `DTSTART` converted to UTC (`...Z`), `DTEND`, `SUMMARY` (function name and the couple's names), `LOCATION` (venue, comma-escaped), the Maps link in `DESCRIPTION`. Download with Blob plus `a[download]`; if that fails (some in-app browsers on iOS), fall back to opening a `data:text/calendar` URL.

**6.6 Events.** Every function from `DETAILS.md` as its own entry, same order, as a vertical timeline with numbered markers (or one tab per function if the reference uses tabs). Each shows name, date, day, time, venue, dress code, directions link. Blank venue or dress code inherits the main one.
Directions link per function: use its own Maps link if given; if its venue is blank use the main link; if it has its own venue but no link, show the venue without a link and flag it. Never add, merge, rename or drop a function.

**6.7 Photo album.** All photos in a grid framed the way the reference frames images. Lightbox: previous and next buttons, swipe, left/right arrow keys, Escape to close, "1 / N" counter, focus trap, focus returns on close, body scroll locked. `object-fit: cover` with a per-photo `object-position`; no face or top of head is ever cut.

**6.8 Footer.** Names, main date, venue. Then, only if given: footer message, families line, RSVP WhatsApp button (`https://wa.me/<digits>?text=` plus `encodeURIComponent("Hi, I will attend the wedding of <Bride> and <Groom>.")`). Plus a "Release a Wish Lantern" button that floats three glowing lanterns up the screen (about 6 s, transform and opacity, removed afterwards, `pointer-events: none`).

**6.9 Paper-plane flight path.**
- One SVG layer covering the full page height, `pointer-events: none`, behind text. It draws one smooth S-curve zig-zagging between about 10% and 90% of page width, top to bottom. Build it from cubic Bezier segments: each segment alternates sides, control points sit at the vertical midpoint (`C x0,y0+dy/2 x1,y1-dy/2 x1,y1`), so y is monotonic. Segment height about 0.6 to 0.8 of the viewport height.
- Base line: round dots about 3.4px wide, 15px apart, 40% opacity, in the reference's accent. Do it with ONE path: `stroke-dasharray: 0.01 15; stroke-linecap: round; stroke-width: 3.4` (never thousands of circles).
- The stretch already travelled becomes a dashed trail (12px dashes): draw the same path with a dash pattern, clipped to the area above the plane (and clip the dots to below it).
- Airplane: small inline SVG in the reference's accent and light colours, about 68px wide (max 70), 60% opacity, trailing a tiny heart. `position: fixed; top: 42vh; left: 0; transform: translate(x,0) rotate(a)`.
  Each frame: target page y = `scrollY + 0.42 * innerHeight`; look up x and the tangent angle on the path at that y from a lookup table built once with `getPointAtLength` (sample every 8px of length, interpolate); smooth the angle.
- Rebuild the path and table on resize, on `ResizeObserver` of the body, and after fonts and images load.
- Must never cover the hero names or block taps: keep the first segment hugging a page edge (x <= 12% or >= 88%) while the hero is on screen, and confirm by screenshot at `scrollY = 0`.

**6.10 Petals.** After the reveal, falling across the whole page: 10 on phones (under 600px), 18 on desktop, slow fall with sway, transform only. Colour and shape follow the reference (rose petals, marigold, leaves or confetti).

**6.11 Glitter.** 20 to 40 tiny four-point sparkles (half that on phones) in the reference's light and accent colours, each twinkling at its own pace (opacity and scale). Elegant, never busy.

**6.12 Candle-glow cursor.** Desktop: a warm flickering glow with a short fading trail follows the mouse. Phones: a soft ripple blooms where the guest taps. Warm tint of the reference's accent. ONE canvas, DPR capped at 2, `pointer-events: none`, and the animation loop stops when idle.

**6.13 Scroll reveal.** Every heading, card and photo fades in as it enters the screen, staggered, in the reference's entrance style if it has one. Use `IntersectionObserver`.

**6.14 prefers-reduced-motion.** Turn off petals, glitter, glow, parallax and the reveal animation (skip the reveal and show the hero), and show everything instantly. Plane stays, without easing.

All effect layers (plane, petals, glitter, glow, lanterns) have `pointer-events: none`.

---

## 7. Caricatures

View the couple photos and study: face shape, skin tone, hairstyle, beard or moustache, glasses, nose pin, jewellery, outfit colours. Sample real skin tones from the photos.
Hand-draw the couple in inline SVG as cute, flattering Indian wedding caricatures (slightly bigger heads, soft round features, warm smiles) in a drawing style that suits the reference. Friends must recognise them instantly.
Draw each head ONCE as an SVG `<symbol>` and reuse it with `<use>` in the bride card, the groom card, and a small full-length couple illustration above the footer.
Outfits come from `DETAILS.md` (blank means same as in the photos).
Never mock or exaggerate weight, nose, teeth or ears. Never lighten or darken skin. Never look like celebrities or generic cartoon people.

---

## 8. Technical standards

- ONE `public/index.html`, all CSS and JS inline. The only external resource is the Google Fonts stylesheet (`preconnect`, `display=swap`). Anchors to Maps and `wa.me` are links, not resources. No frameworks, libraries, CDNs, trackers, cookie banners, popups, sign-up forms or audio.
- Every font gets a real fallback stack. If any text is in Devanagari or another script, load a matching Google Font for it and set `lang` on those spans. Network may be off in your sandbox, so fonts may not load there; that is not a bug, but the fallback must still look acceptable.
- Mobile first for 360 to 430px, then scale up. No horizontal scroll (`overflow-x: clip` on `html` and `body`). Body text 16px, nothing under 14px, every button and link at least 44px tall. `viewport-fit=cover` plus `env(safe-area-inset-*)` padding. Use `svh` or `dvh`, not `vh`, for full-screen blocks.
- Smooth on a mid-range Android: animate only `transform` and `opacity`, use `requestAnimationFrame`, passive scroll listeners, one shared scroll handler, DPR capped at 2.
  The single allowed exception is the plane trail clip or dash offset in 6.9, updated inside rAF only when the scroll position changed.
- Images: explicit `width` and `height`, `decoding="async"`, `loading="lazy"` for everything below the first screen.
- Accessibility: real `<button>` elements, honest alt text on every photo (describe what is visible, do not invent names or relationships), visible focus outlines, `lang` on `<html>`, `aria-label` on icon-only controls, text contrast at least 4.5:1 unless the reference's own style makes that impossible (then flag it).
- `<head>`: `title`, `meta description`, `theme-color` (from the palette), inline SVG data-URI favicon with the initials, `<meta name="robots" content="noindex,nofollow">`, Open Graph tags per section 15.
- Code: clean and commented with section markers. The first comment block lists every detail from `DETAILS.md` exactly as given. A `CONFIG` object holds the countdown timestamp, the functions array, links and constants. Insert data from JS with `textContent`, never raw `innerHTML`.
- No console errors, no broken links or images, no dead buttons.
- Size targets: `index.html` under 250 KB, total `public/` under 2.5 MB.

---

## 9. Photos and assets

- `originals/` is read-only. Write results to `public/photo1.jpg` .. `photo5.jpg` (use only as many as exist; never invent or duplicate to reach five). Mapping comes from the Photos table in `DETAILS.md`, otherwise sorted by file name.
- Pipeline: apply EXIF orientation, strip ALL metadata (location data especially), longest edge 1200px (never upscale), JPEG quality about 82, progressive, aim for 250 KB or less each.
```
magick in.jpg -auto-orient -strip -resize "1200x1200>" -quality 82 -interlace Plane public/photo1.jpg
# or Pillow: ImageOps.exif_transpose(img); img.thumbnail((1200,1200)); img.save(out, quality=82, optimize=True, progressive=True)
```
  HEIC or other formats: try `magick` or `pillow-heif`; otherwise ask the user to export JPEG.
- View every photo. For each, decide the face position and set `object-position` as percentages. After building, confirm by screenshot at the real rendered ratios (phone and desktop) that no face or head top is cut. If a frame ratio would cut a face, change that frame's ratio rather than cropping through the face.
- Never stretch, squash, mirror or distort a photo. No filters, tints or overlays that change skin tone, and no overlay over faces.
- `og.jpg`: the ONLY extra image allowed. 1200x630, cropped from the best photo with faces intact, 300 KB or less (WhatsApp's own docs say under 600 KB; smaller is safer).
- No stock photos, internet images, hotlinks or AI image links. Every background, texture, ornament, map and illustration is CSS or inline SVG.

---

## 10. Verification and definition of done

Check the tools first: `node -v`, `python3 -V`, `ffmpeg -version`, `magick -version`, Playwright (`npx playwright --version`) or a Chrome/Chromium binary. Install what is missing (this may need the user's approval for network access). If something cannot be run, say exactly which checks were skipped. Never claim a check passed that you did not run.
Serve with `python3 -m http.server 8080 --directory public`. Keep reusable scripts in `work/`.

**Static checks (always):**
1. Every value in `DETAILS.md` appears verbatim in `index.html` and in the checklist (exact string match).
2. No `FORBIDDEN STRINGS` from `STYLE_DNA.md` appear anywhere in `public/`.
3. No `lorem`, `TODO`, `Your Name`, `...` placeholders, no reference couple's text.
4. External URLs are limited to: Google Fonts, the user's Maps links, `wa.me`, the SVG/XML namespace, and (after publishing) the og tags. No `<script src>`; no stylesheet except Google Fonts.
5. Weekday computed by script for every function date matches the stated day (otherwise flag, do not change).
6. `public/` contains only `index.html`, `photoN.jpg`, `og.jpg`. Photos are at most 1200px on the long side with no EXIF.

**Browser checks (Playwright or headless Chrome), at 360x800, 390x844, 430x932, 768x1024, 1440x900:**
1. No console errors or failed requests (font requests may fail when offline).
2. `scrollWidth <= innerWidth` at every size (no horizontal scroll). No overlapping elements at 360px.
3. Every button and link is at least 44px tall; no computed font size under 14px.
4. Before the reveal opens: page cannot scroll. Reveal opens by click, Enter and Space.
5. Countdown ticks; with a mocked clock (`page.clock`) it shows the right values, shows "Just Married" after the target, and is identical under `timezoneId` `America/New_York` and `Asia/Kolkata`.
6. Download the .ics: count of `VEVENT` equals the number of functions; converted UTC times match the stated local times.
7. Lightbox: next, previous, swipe, Escape, counter, focus returns.
8. Effect layers all compute to `pointer-events: none`.
9. With `reducedMotion: 'reduce'`: no running animations, everything visible.
10. Plane: at most 70px wide, stays inside the viewport, does not overlap the hero names at `scrollY = 0`.
11. Scroll the whole page with 4x CPU throttle: no errors, no obvious jank.
12. If Lighthouse is available: mobile Performance 85+, Accessibility 95+. Report the numbers.

**Visual review:** screenshot each section at 390px and 1440px into `work/screenshots/`, compare with the reference frames section by section, list the 10 biggest differences (colour, fonts, spacing, card style, frames, opening animation), and fix them. Do not change data or remove a feature while doing so.

**Done means:** all static checks pass; browser checks pass or are listed as skipped with a reason; `CHECKLIST.md` and `MATCH_REPORT.md` exist; `PLAN.md` is fully ticked; the handoff message is sent.

The user still tests on a real phone (open the reveal, scroll to the bottom, tap Get Directions and Add to Calendar, open a photo, check every date against the printed card).

---

## 11. Never (hard rules, override everything above)

**Data**
- Never change spelling, capitalisation or order of a name; never add or drop middle names, titles, surnames, initials.
- Never translate or transliterate unless the user wrote both versions.
- Never round, shift, convert or "correct" a time, date or day.
- Never edit, shorten or replace a Maps link or phone number.
- Never invent content (see section 4).

**Reference**
- Never copy the reference couple's names, initials, dates, venue, quotes, story, bios, hashtags or any personal text.
- Never show, trace or embed the reference's photos, paintings, illustrations, logos, watermarks or brand names. Recreate the feel, never the artwork.
- Never let the reference add, remove, rename or reorder events or decide which fixed features appear.
- No colours outside the STYLE DNA palette; no fonts that do not match its character. Never skip the STYLE DNA step or write it and then ignore it.

**Features**
- Never drop, merge or simplify a feature in section 6.
- Plane: never opaque, never wider than about 70px, never covering the hero names, never blocking taps.
- Never let an effect layer capture clicks.
- Never compute the countdown in the visitor's local time.

**Photos and faces**
- Only `photo1..5.jpg` and `og.jpg`, by exact relative name. Never paste photo data into code, never use absolute paths.
- Never crop through a face or the top of a head. No skin-tone changes. Caricatures never mocking, never exaggerated.

**Motion and performance**
- No audio, sound effects, popups, cookie banners or sign-up forms.
- No fast, flashing or forever-looping attention animations. Everything slow and soft.
- Never animate width, height, top, left or box-shadow on scroll (only the 6.9 exception).
- Never ignore `prefers-reduced-motion`.

**Code**
- No external JS, frameworks, jQuery, CDNs or build tools in the deliverable.
- No horizontal scroll, text under 14px, buttons under 44px, console errors, broken links, broken-image icons or dead buttons.
- No shortened file, no "rest stays the same".
- If you think a detail should change, say so in the handoff. Never change it on your own.

---

## 12. Reports (write to `work/`)

**CHECKLIST.md**: a table with columns `Item | As typed in DETAILS.md | As used in index.html | Match | Flag`. Rows: bride, groom, name order, initials, blessing, subtitle, main date and time, time zone offset, countdown timestamp, venue, address, every Maps link, dress code, bios, footer message, families line, RSVP number and the wa.me href, and for every function: name, date, day, time, venue, dress code, link, computed weekday. Flag anything that looks wrong without changing it.

**MATCH_REPORT.md**: five bullets on how the site matches the reference; anything that could not be matched; every assumption made; checks run and checks skipped with the reason.

---

## 13. Handoff message (the only chat output after a build; at most 12 lines)

What was built and where; how to preview (`python3 -m http.server 8080 --directory public`); verification result by group (static, browser, visual); items flagged for the user's decision; assumptions; next steps (real phone test, publish). No code.

---

## 14. Fix playbook (after the first build)

Change ONLY what was asked. Use small patches on the existing file, not a rewrite. Re-run the relevant checks. Never touch `DETAILS.md` unless asked.

| User says | Do |
|---|---|
| continue / it stopped | Resume from `PLAN.md`; do not restart or repeat |
| does not look like the reference | Compare section by section against frames; list the 10 biggest differences; fix all; keep data and features |
| used the reference couple's text | Remove every string from `FORBIDDEN STRINGS`; use only `DETAILS.md` |
| feature [6.x] missing | Add it exactly per section 6, styled with the DNA, change nothing else |
| a name, date or time changed | Restore from `DETAILS.md`, rerun static checks, reprint the checklist |
| event missing or merged | One entry per function, user's order, own date/day/time |
| photos do not show | Check names `photoN.jpg`, relative to `index.html`, in `public/` |
| plane covers text | Plane 56px wide at 50% opacity, move its path away from the hero names |
| slow on phone | Halve petals and glitter under 600px; confirm only transform and opacity animate |
| caricatures look wrong | Redraw only the symbols from the photos; same heads in all three places |
| WhatsApp preview missing or old | Check og tags, absolute `og:image` under 300 KB, share link with `?v=2` appended |
| calendar file does not open on iPhone | Test the data-URL fallback; consider per-event Google Calendar links |

If the chat gets long and rules drift: re-read this file, `DETAILS.md` and `PLAN.md`, then continue.

---

## 15. Publishing and sharing

Upload `public/` only (never `reference/` or `originals/`). Free options, drag-and-drop or direct upload (check current limits, they change):
- Netlify Drop: `app.netlify.com/drop`, drag the folder, no account needed at first (claim the site to keep it), re-drop an updated folder to update.
- Vercel Drop: `vercel.com/drop`, accepts a folder or zip.
- Cloudflare Pages (direct upload) or GitHub Pages.

WhatsApp link preview needs, in `<head>` (within the first 300 KB): non-empty `og:title`, `og:description`, `og:url`, and an absolute `og:image` (`og.jpg`, 300px+ wide, under 600 KB per WhatsApp's docs, aim for 300 KB or less).
- `og:title`: the couple's names in the given order plus the hero subtitle. `og:description`: main date and venue name, exactly as given.
- The URL is unknown until the user publishes. Until `DETAILS.md` has a Site URL, omit `og:url` and `og:image` (never leave them empty). When the user gives the URL, add both with absolute `https://` values and tell them to re-publish.
- WhatsApp caches previews: share the link with `?v=2` appended after a change.

Privacy: anyone with the link sees the venue, address and phone number. `noindex` is set, but suggest a hard-to-guess site name rather than names plus date.

---

## 16. Where this file resolves conflicts in the original prompt

- Chat-only steps (Canvas or Artifacts, "PART 1 OF 3: type continue", printing the Style DNA and checklist in chat) are replaced by files on disk plus the section 13 handoff.
- "Animate only transform and opacity" vs the SVG trail: one documented exception (6.9).
- "No other image files" vs WhatsApp previews needing an image: `og.jpg` is the single exception.
- "Switch off the reveal animation" under reduced motion: the reveal is skipped and the hero shows at once.
- Plane vs hero names: first path segment hugs the page edge; verified by screenshot.
- Phone numbers: display exact, `href` digits only.
- Time zone: default `+05:30`, but `DETAILS.md` may set another fixed offset.
- Functions have an optional Maps link column; there was no way to give a per-function link before.
- Only start times exist, so .ics end times use a hidden constant and are flagged.

Optional extras, only if the user asks: background music with a user-supplied file and a mute toggle (never autoplay); a personalised `?guest=` greeting (inserted with `textContent`); a second language shown only if the user supplies both versions of every line.
