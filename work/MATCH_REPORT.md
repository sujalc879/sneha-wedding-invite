# Match report

## Latest details correction

Confirmed names sneha and sanghpal and wedding date 1 January 2027 reapplied after the source returned to the old demo values. The Wedding entry matches the confirmed date; Friday computed with Python. Wedding time is pending, so countdown shows a pending status and calendar export is disabled with an explanation. Other event dates and venue remain demo content; February demo events now follow the January wedding and need replacement. Existing opening artwork preserved. Earlier full-suite results below refer to the demo version. Focused syntax/source checks and browser tests at five widths are run for this correction; full countdown/ICS tests await the real time. No publication or Git changes.


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

## Initial full-build verification

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
- Size: The initial build was **78,746 bytes**, below both budgets. No original, reference or scratch assets are deployed.

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

## Opening refinement — 25 November 2026

- Scope: only the opening CSS, opening markup and reveal JavaScript were patched. The test compares the rest of index.html byte for byte against the previous committed build. DETAILS.md, wedding content, event order and every other feature are unchanged.
- Design: the same sampled ivory/burgundy/gold palette now frames a layered paper envelope with a static soft shadow, embossed wax seal, fine botanical wreath, original architectural backdrop, serif introduction and date/venue sign-off.
- Microinteractions: restrained pointer tilt uses one scheduled rAF update; paper sheen, seal radiance, a small seal rotation/press and close-icon rotation animate only transform and opacity. Mouse leave/blur clears tilt. No continuous attention animation was added.
- Dismissal: a 48px Close opening button and Escape key skip to the hero through a 240ms fade. Both restore scrolling, remove inert and place focus on the hero. Close remains available during the normal 1.9-second reveal and cancels its pending timer. Tab and Shift+Tab cycle between the seal and close button.
- Sound: the user's conditional sound suggestion was not needed for the refinement. The existing section 11 no-audio rule remains respected; no audio, autoplay, external sound file or inactive sound control was added.
- Verification: **PASS**, 13 focused browser groups in work/ONBOARDING_RESULTS.json, plus all 21 static checks. The five required sizes pass complete-viewport visibility, 44px control size, 14px font size, scroll lock, keyboard focus, reveal/dismissal and hero plane clearance.
- Additional checks: desktop hover/tilt reset, touch-context tap without mouse tilt, close during reveal, Escape, timer cancellation, reduced motion with zero running animations, and a short 360×640 screen all passed. No script errors or failed non-font requests.
- Visual review: fresh opening screenshots at all five required widths, plus hover and mid-reveal frames, are saved as work/screenshots/onboarding-*.jpg. Phone and desktop opening views were reviewed. Prior section screenshots describe the unchanged remainder of the invitation.
- Size after the first opening refinement: **89,510 bytes** in one public/index.html; no added deployed assets.
- Checks not repeated: unchanged calendar/gallery/time-zone/whole-page CPU tests retain the initial full-build results. Lighthouse and real-phone checks remain deferred for the reasons recorded above.
- Preview: `python3 -m http.server 8080 --directory public`; refresh the preview to replay the opening.

## Further opening polish — 25 November 2026

- Limited the second pass to the same opening CSS, markup and reveal JavaScript. The automated comparison confirms all other HTML, wedding content and features remain byte-for-byte unchanged. The existing working-tree deletion of AGENTS.md is left untouched and will not be included in the change commit; its last committed rules and the chat instructions informed this pass.
- Added a narrow satin gold ribbon which releases before the flap opens, hand-authored irregular wax-rim artwork, low-contrast embossed corner rosettes, and warm pointer-following light. All movement remains transform/opacity only. Eight tiny opening sparkles play once and fade out; no continuous attention animation was added.
- Added a clear Open invitation action below the seal. It uses the same reveal handler, duplicate-click guard, scroll unlock and hero focus as the seal. Keyboard focus cycles through Close, the seal and the new action. Close and Escape remain available, including during the reveal.
- Sound remains omitted because it was conditional and the supplied project instructions prohibit audio. No sound resource, silent toggle or autoplay was added.
- Verification: **PASS**, 14 focused browser groups plus all 21 static checks. The five required viewport sizes and an additional 360×640 phone pass; desktop pointer feedback, touch for both opening controls, focus trapping, Close/Escape, cancellation and reduced motion all pass. No JavaScript errors or failed non-font requests.
- Visual review: updated opening screenshots for all five sizes, hover, and mid-reveal are in work/screenshots/onboarding-*.jpg; phone and desktop views were reviewed. Unchanged sections retain the prior full-build results. Lighthouse and physical-device testing remain deferred as documented above.
- Current deploy size: **94,984 bytes**, entirely in public/index.html. DETAILS.md and the originals remain untouched.
- Preview with `python3 -m http.server 8080 --directory public`; refresh to replay the opening.

## Confirmed screenshot details — 28 November 2026

- Source: the user-supplied WhatsApp screenshot plus the replies confirming wedding time `1:35 pm`, Sangeet on `31 December 2026` at the Haldi address, and removal of unconfirmed demo content. The existing confirmed wedding date `1 January 2027` is retained.
- Latest name instruction: the user explicitly requested first names only. The site, metadata, opening card, portrait labels, footer, calendar summaries and download filename use **Sneha** and **Sanghpal**. Middle names and surnames are absent even from the deployed HTML source. Original screenshot names are retained only in work/CONFIRMED_DETAILS.json, outside public/. This explicit request supersedes the earlier full-name preservation default.
- Exact venue wording, punctuation and case are preserved in DETAILS.md and on the page. Main venue: `Tirupati mangal karyalay`; complete provided venue/address line: `Tirupati mangal karyalay, itke corner,Tharmal rode , Parli vaijnath,Beed 431515`.
- Haldi: `31st Dec`, `8.00pm.`, `near om caching classes, new shivaji nagar, parli vaijnath,Beed 431515`. The displayed date is not reformatted; its internal year is 2026, consistent with the saved wedding date and confirmed Sangeet date.
- Sangeet: `31 December 2026`, `6.00 pm`, at the same exact Haldi address as confirmed by the user. Weekdays not supplied for these functions are omitted from the page; both compute to Thursday.
- The timeline retains the screenshot order Haldi, Sangeet, then Wedding. Sangeet starts earlier in the day; no silent chronological reordering was made.
- Demo Mehndi, Jaipur/Rambagh content, bios, dress codes, blessing, family lines and quotes were removed with explicit approval. Neutral interface headings remain. Optional RSVP is absent because no number was provided. Previously approved illustrations remain pending real photos.
- Maps links are technical address-search URLs derived from the exact supplied strings; no provided URL was modified. They are not verified place-pin links. The main map/wedding links use the wedding venue address; Haldi and Sangeet use their own address. Check the selected place on a real phone before publishing.
- Initials `s&s` and the fixed offset `+05:30` are retained from the prior details. The new main timestamp is `2027-01-01T13:35:00+05:30`, equivalent to `2027-01-01T08:05:00Z`.
- Calendar export is enabled again and includes exactly three events. UTC starts, in source order: Haldi `20261231T143000Z`, Sangeet `20261231T123000Z`, Wedding `20270101T080500Z`. The existing hidden three-hour end-time constant is retained; end times are never displayed.
- Static verification: **PASS**, 24 checks. Exact DETAILS.md data, source comments, CONFIG, event count/order, derived local/UTC values, actual weekdays, links, palette, permitted files and size budgets pass. Data checklist regenerated in work/CHECKLIST.md.
- Browser verification: **PASS**, 16 groups in work/DETAILS_BROWSER_RESULTS.json. All five required sizes have no horizontal overflow, undersized controls/fonts or actual name-text/plane overlap. Calendar download, CRLF/75-octet folding, both time zones, hidden-tab pause/resync, Just Married, reduced motion, opening keyboard support, gallery smoke test and simulated iOS calendar fallback pass. No script errors or failed non-font requests.
- Visual verification: reviewed the opening and all six changed sections on phone and desktop. Updated section screenshots are work/screenshots/details-*.jpg, with overview sheets in work/sheets/details-review-390.jpg and details-review-1440.jpg. Layout accommodates the confirmed names and long venue text without shortening the supplied venue/address.
- Deploy folder size: **98,891 bytes**, one self-contained index.html. No new external resources. Nothing published or uploaded.
- Deferred checks: real-photo likeness/crops/EXIF await originals; Lighthouse is not installed; actual iPhone calendar import, real-phone scrolling and selected Maps places still need device review. The prior full-build performance and unaffected-effect checks are retained as historical results, not rerun claims.
- Preview: `python3 -m http.server 8080 --directory public`. Publish public/ only after the real-phone check.

## Sequenced envelope reveal — 28 November 2026

- Scope: the explicit latest request replaces the former silent opening and reduced-motion skip defaults. Wedding data, event order, Maps links, gallery configuration and DETAILS.md remain unchanged; the browser suite compares them against commit 2c225b3. The deliverable remains a single public/index.html with inline CSS/JS and no new external resources.
- Sequence: the seal becomes three jagged, matching wax fragments that fall 145–205px and rotate −27°/+24°/−10°, fading out by 620ms and removed at 760ms. Cloned SVG gradients receive unique IDs. The flap rotates from 0° to −178° around its top edge at 180–680ms, with 1000px perspective. The card rises out at 680–1140ms; the page crossfades at 1200–1600ms. The initial satin ribbon and typography release quietly; Close and Escape still bypass the intro in 240ms.
- Haptic: one feature-detected navigator.vibrate(15) call per activation, safely ignored when absent, denied or throwing. Actual vibration depends on browser/device support.
- Chime: opt-in and muted initially, synthesized locally with three softly decaying sine tones; no audio asset, network request or autoplay. Peak master gain is 0.08 and the tail lasts 1.9s. The 46px corner toggle is available inside the opening, then the same button moves outside it and remains fixed after completion. It can mute mid-sequence, previews the chime when enabled after opening, and saves the guest's preference in localStorage. Saved enabled state still waits for interaction. Muting, dismissal and tab hiding silence voices; idle audio contexts suspend. Unsupported Web Audio hides the control; blocked storage leaves interactions functional.
- Reduced motion: the envelope is static until activation, followed only by a 300ms crossfade. No wax split, flap/card animation, tilt, petals, glitter, glow or parallax runs. Switching preference during the sequence cancels the normal timers/fragments and uses the short fade. This is the user's requested replacement for the historical automatic skip behavior.
- Accessibility: real seal/CTA buttons support click, touch, Enter and Space. Focus cycles through available opening controls, page content remains inert and scroll locked until completion, duplicate activation is guarded, and focus moves to the hero. Muting exposes a stable accessible toggle label, pressed state and current status.
- Static verification: **PASS**, 24 checks plus JavaScript syntax. Exact DETAILS.md data, forbidden strings, palette, URLs, unique IDs, single-file constraints and size budgets pass; CHECKLIST.md remains current. Deploy size: **108,673 bytes**.
- Focused browser verification: **PASS**, 14 groups in work/INTRO_SEQUENCE_RESULTS.json. Five required viewports, plus 360×640; actual ~1600ms timing, three fragments/unique IDs, CSS sequencing, 15ms haptic invocation, native Web Audio scheduling/decay/suspension, persisted preference without autoplay, keyboard/touch, Close/Escape cancellation, reduced fade, live preference changes, and unsupported APIs/blocked storage pass. No script errors or failed non-font requests. work/scripts/verify_onboarding.mjs now runs the current suite; obsolete silent/automatic-skip assertions remain in Git history.
- Regression verification: **PASS**, 16 groups in work/DETAILS_BROWSER_RESULTS.json, including exact wedding data and first names, calendar UTC conversion/CRLF/75-octet folding, both time zones, hidden-tab countdown pause/resync, Just Married, calendar fallback and gallery. The viewport-resize test waits for the existing plane angle easing to settle before checking bounds; no plane implementation change was made.
- Visual verification: reviewed sealed, split, flap-open, extracted-card and crossfade states on phone and desktop. Current frames are work/screenshots/intro-*.jpg. Screenshot timelines freeze both animations and opacity transitions for repeatable phase inspection; production timing is verified separately. The existing botanical paper/gold/burgundy styling is preserved. The visible in-app preview was also opened to the hero, confirmed to retain its muted control, then reset ready to replay.
- Remaining device checks: a physical phone is needed to judge real speaker loudness, haptic support, native calendar import and touch feel. Lighthouse is unavailable; a new CPU-throttled full-page performance run was not performed for this scoped intro patch. Prior full-build performance checks are historical. Real-photo/likeness/crop/EXIF review awaits originals; existing approved illustrations remain. No publishing or upload was performed.
- Preview: `python3 -m http.server 8080 --directory public`, then open http://localhost:8080; refresh to replay. The temporary QA server is stopped at handoff. Publish public/ only.
