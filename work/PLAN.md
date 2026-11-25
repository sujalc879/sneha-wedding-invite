# Wedding invitation build

- [x] Phase 0: Read AGENTS.md and the nine-page master-prompt PDF; validate available inputs. User explicitly approved a temporary fictional demo and original SVG illustrations in place of missing photos. Create DETAILS.md as the single source of demo content.
- [x] Phase 1: No original photos exist; the user-approved illustration substitution applies. Keep originals/ untouched. Provide a metadata-stripping photo preparation script for future real photos. No fabricated photo files or OG photograph.
- [x] Phase 2: Research a usable invitation reference, view it at full resolution, sample its palette, and write STYLE_DNA.md.
- [x] Phase 3: Map reference design to all fixed features; document deliberate interpretations.
- [x] Phase 4: Build complete, standalone public/index.html.
- [x] Phase 5: Run static, browser and visual checks; patch observed failures and recheck.
- [x] Phase 6: Complete CHECKLIST.md and MATCH_REPORT.md.
- [x] Phase 7: Deliver local file, preview command, verification summary and replacement guidance.

## Section and feature map

| Reference element | Site section | Fixed features |
|---|---|---|
| Printed paper, gilded border, invitation motif | Sealed envelope reveal | 6.1; real button, inert content, focus transfer |
| Cream central Mughal arch, burgundy names, botanical sides | Hero | 6.2; main details, save-the-date, parallax |
| Botanical vignette framing | Two arch portrait plates | 6.3; original fictional SVG heads reused at footer |
| Formal printed date | Inset countdown panel | 6.4; fixed-offset live countdown |
| Vertical invitation hierarchy | Vertical numbered celebration timeline | 6.6; four separate functions in DETAILS order |
| Domed pavilion, cream and gold architectural framing | Venue and abstract map | 6.5; date/time/venue/dress cards, ICS, Maps |
| Garden vignettes and pale arch frame | Three illustrated gallery panels | 6.7; approved temporary illustration substitution; full lightbox |
| Decorative lower garden edge | Closing illustration and footer | 6.8; same SVG heads, names, details, three lanterns |
| Gold ornament | Dotted S-curve and translucent plane | 6.9; hero edge kept clear, LUT and clipping |
| Pink blooms, quiet gilded pattern | Rose petals, four-point glitter, candle canvas | 6.10–6.12; no pointer capture |
| Static reference has no recorded motion | Soft staggered entrances | 6.13–6.14; IntersectionObserver and full reduced-motion support |

## Deliberate interpretations

The researched reference is one printed invitation, not a full website or video. Extra required sections inherit its paper, arch, burgundy, botanical and gold vocabulary. The opening timing and scroll transitions are original, not measured from a video. All art is hand-authored SVG and never traces or embeds reference art. Portrait likeness and photographic crop tests are deferred until the user supplies real photos. Delivery stays local in public/, per the project workflow; no remote or hosting registration.
