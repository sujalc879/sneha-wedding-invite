# Match report

## Research

- Visual reference: [InviteFlare printed botanical arch invitation](https://www.inviteflare.com/invitations/wedding/tree-indian-wedding-invitation-template). Saved in reference/ for study only, never deployed. No personal wording or artwork is reused.
- Public venue address: [official Taj Hotels Rambagh Palace fact sheet](https://assets.tajhotels.com/en-in/hotels/rambagh-palace-jaipur/documents/rambagh-palace-jaipur-factsheet.pdf). A real public venue is used for working sample directions only; no actual wedding booking is implied.
- Read the full nine-page local master-prompt PDF. It is a written brief, not a visual invitation reference. AGENTS.md remains the governing project specification.

## Reference match

- Warm ivory paper and palette sampled from reference pixels.
- Burgundy display typography, gold architectural borders and a central invitation arch.
- Original botanical and pavilion illustrations recreate the garden mood without copying the artwork.
- Portrait and gallery frames use arches and fine rules instead of generic rounded cards.
- Required extra sections follow the same print-inspired hierarchy, restrained palette and ornament.

## Approved assumptions and limitations

- The user approved a temporary fictional demonstration on 25 November 2026, then intends to supply real photos. DETAILS.md records every sample detail explicitly.
- No personal telephone number is fabricated; optional RSVP is omitted.
- No photos were supplied. Original fictional SVG portraits and three original illustrated gallery scenes temporarily replace photographic content. No resemblance to actual people is claimed. Photo preparation, likeness study, skin sampling and face-crop validation await real originals.
- No photographic og.jpg is fabricated. Site URL is blank, so og:url and og:image are omitted as required.
- The reference is static. Opening, entrances, hover, parallax and particles are original interpretations, not measured animation.
- Event venue fields inherit Rambagh Palace; the blank Wedding dress code inherits Indian festive; all directions inherit the main exact link.
- Calendar end times use one hidden three-hour constant; those derived end times are never displayed.
- Delivery is local only; no Git remote, push, hosted Site or upload.

## Visual review: ten largest reference differences and their resolution

Reviewed every section at 390px and 1440px; section screenshots are in work/screenshots/ and overview sheets in work/sheets/.

| Difference from the printed reference | Resolution / recreation |
|---|---|
| 1. Physical paper versus a flat display | Exact sampled paper colours, subtle original rosette tessellation, and inset paper panels restore the printed feel. |
| 2. Gold arch definition | Nested original pointed/scalloped arch strokes were strengthened after screenshot review; no reference contour was traced. |
| 3. Dense painted garden borders | Original layered vector stems, shaded leaves and rose-toned flowers frame both edges; secondary stems were added after review. Painted texture remains an acknowledged medium difference. |
| 4. Domed pavilions along the foot | Original architectural vignettes anchor the lower hero, with higher visibility after review. They are not reproductions of the source art. |
| 5. Hand-lettered names | Cormorant Garamond italic supplies an accessible free-font equivalent in character; the source's exact lettering is not used. |
| 6. Print has only one content panel | All required extra sections carry its palette, serif hierarchy, gold rules and restrained spacing; fixed content remains in DETAILS.md order. |
| 7. No supplied people or photographs | User-approved fictional SVG portraits and illustrated gallery scenes are clearly identified. Real likeness and skin sampling are deferred, not simulated. |
| 8. No source portrait/gallery card system | Arched double-line portrait plates and fine album frames extend the central architectural motif; no generic grey shadow cards. |
| 9. Static reference has no opening or scroll recording | An original 1.9-second envelope reveal, gentle entrances, parallax and slow petals supply the required motion. No measured source timing is claimed. |
| 10. Gold ornament versus interactive readability | Burgundy text is used for the hero ampersand for contrast; a burgundy venue panel uses the source's ink colour while the overall site stays light. Plane layering was corrected so its trail remains visible through the venue panel. |

The reference is a visual direction, not a website with equivalent sections to reproduce pixel for pixel. Its personal text and artwork never enter public/.

## Verification

- Static: **PASS**, 21 checks. All populated DETAILS.md cells match exactly in source and CHECKLIST.md; forbidden strings absent; fixed-offset dates and actual weekdays agree; URLs, SVG references, palette, file list and size budgets pass.
- Browser: **PASS**, 19 check groups using installed Playwright 1.62.1 / cached headless Chromium. Layout checked at 360×800, 390×844, 430×932, 768×1024 and 1440×900: no horizontal overflow, no controls below 44px, no computed fonts below 14px, no hero-name/plane overlap.
- Opening: locked wheel scroll and inert page, initial seal focus, click/Enter/Space activation, scroll unlock, top reset and hero focus all passed.
- Countdown: mocked clocks gave identical results in America/New_York and Asia/Kolkata; second ticks, hidden pause/resync and post-target Just Married all passed.
- Calendar: an actual .ics download contains exactly four VEVENT entries, correct UTC starts/three-hour ends, comma escaping, CRLF and 75-octet folding. Simulated iPhone in-app data-URL fallback contains all four events. Test download: work/invitation-test.ics.
- Gallery: next/previous, both arrow keys, wrapping, touch-pointer swipe, counter, Escape, scroll lock, focus trap and focus return passed. Verification waits for the asynchronous native dialog close event before checking restored body scrolling.
- Effects: all six layers ignore pointer events; exact phone/desktop particle counts pass; three lanterns are created and removed. Reduced motion bypasses the opening, reveals all content, disables running animations and retains a static plane.
- Performance: whole-page scroll at 4× CPU throttle completed without script errors. 143 sampled frames; median 11.5ms, 95th percentile 26.1ms. These are local Chromium observations, not a real Android benchmark.
- Errors/resources: no console errors and no failed requests in the final headless run; the final in-app-browser preview also reported no console errors. Google Fonts loaded during this run; each has an explicit fallback stack.
- Visual: all seven sections captured and reviewed on phone and desktop; the above refinements were applied and the browser suite rerun. Latest result JSON: work/STATIC_RESULTS.json and work/BROWSER_RESULTS.json.
- Size: public/index.html and the entire public/ folder are **78,746 bytes**, below both budgets. No original, reference or scratch assets are deployed.

## Checks deferred or skipped

- Lighthouse is absent from PATH and the bundled Node runtime: Performance/Accessibility scores were not run or claimed.
- Real photographs were not provided. EXIF/orientation/dimension checks, skin-tone sampling, recognisable likeness, face-safe crop review and og.jpg creation await the real originals. This is the user-approved temporary exception; no stock or fabricated photos were substituted.
- Real-device iPhone import, Android scroll feel and WhatsApp preview still need the user's phone. The iOS fallback path was exercised with a simulated user agent, not an actual iPhone calendar app.
- RSVP is blank, so its optional WhatsApp control is omitted. Site URL is blank, so publishing metadata stays omitted. The site has not been published.
- System ffmpeg and ImageMagick are unavailable. No video extraction was needed; the reference is a still image. Bundled Pillow, pypdf and Poppler supplied image study and PDF extraction/rendering instead.

## Handoff / next steps

- Open public/index.html directly, or run `python3 -m http.server 8080 --directory public` from the project root and visit http://localhost:8080.
- Supply real data in DETAILS.md and original photos in originals/ before an actual invitation is shared. work/scripts/prepare_photos.py provides orientation, metadata stripping and compression using Pillow in the bundled Python runtime, but every final crop and portrait still needs visual review.
- Test opening, complete scroll, directions, calendar import and lightbox on a real phone. Then publish public/ only and supply the final Site URL for absolute Open Graph tags.
- Local Git checkpoints preserve phases. No remote was added and nothing was pushed or uploaded.
