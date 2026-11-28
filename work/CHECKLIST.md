# Data checklist

Source: DETAILS.md, supplied screenshot and user replies on 28 November 2026. Unconfirmed demo details were removed with approval.

| Item | As typed in DETAILS.md | As used in index.html | Match | Flag |
|---|---|---|---|---|
| Bride | Sneha | Sneha | YES | Copied exactly from screenshot or confirmed user reply. |
| Groom | Sanghpal | Sanghpal | YES | Copied exactly from screenshot or confirmed user reply. |
| Name order | Bride & Groom | Bride & Groom | YES |  |
| Initials | s&s | s&s | YES | Retained existing derived initials; not supplied in screenshot. |
| Blessing | EMPTY | — omitted — | YES |  |
| Hero subtitle | Wedding Invitation | Wedding Invitation | YES |  |
| Hero introduction | EMPTY | — omitted — | YES |  |
| Main date | 1 January 2027 | 1 January 2027 | YES | Copied exactly from screenshot or confirmed user reply. |
| Main day | Friday | Friday | YES |  |
| Main time | 1:35 pm | 1:35 pm | YES | Copied exactly from screenshot or confirmed user reply. |
| Time zone offset | +05:30 | +05:30 | YES |  |
| Venue | Tirupati mangal karyalay | Tirupati mangal karyalay | YES | Copied exactly from screenshot or confirmed user reply. |
| Address | Tirupati mangal karyalay, itke corner,Tharmal rode , Parli vaijnath,Beed 431515 | Tirupati mangal karyalay, itke corner,Tharmal rode , Parli vaijnath,Beed 431515 | YES | Copied exactly from screenshot or confirmed user reply. |
| City | EMPTY | — omitted — | YES |  |
| Maps link | https://www.google.com/maps/search/?api=1&query=Tirupati%20mangal%20karyalay%2C%20itke%20corner%2CTharmal%20rode%20%2C%20Parli%20vaijnath%2CBeed%20431515 | https://www.google.com/maps/search/?api=1&query=Tirupati%20mangal%20karyalay%2C%20itke%20corner%2CTharmal%20rode%20%2C%20Parli%20vaijnath%2CBeed%20431515 | YES | Derived exact-address search URL; verify selected place. |
| Dress code | EMPTY | — omitted — | YES |  |
| Bride bio | EMPTY | — omitted — | YES |  |
| Groom bio | EMPTY | — omitted — | YES |  |
| Couple heading | The couple | The couple | YES |  |
| Footer message | EMPTY | — omitted — | YES |  |
| Families line | EMPTY | — omitted — | YES |  |
| RSVP number | EMPTY | — omitted — | YES | Optional, blank: no WhatsApp button or invented contact. |
| Site URL | EMPTY | — omitted — | YES | Unknown: og:url and og:image omitted. |
| Bride outfit | EMPTY | — omitted — | YES | Fictional SVG portrait; real likeness awaits supplied photos. |
| Groom outfit | EMPTY | — omitted — | YES | Fictional SVG portrait; real likeness awaits supplied photos. |
| Demo label | Invitation preview | Invitation preview | YES |  |
| Demo notice | Illustrations shown in place of photos. | Illustrations shown in place of photos. | YES |  |
| Countdown timestamp | 1 January 2027; 1:35 pm; +05:30 | 2027-01-01T13:35:00+05:30 | YES | Technical value only; display remains exact. |
| RSVP wa.me href | EMPTY | — omitted — | YES | No personal telephone number fabricated. |
| Main computed weekday | Friday | Friday | YES | Computed with Python; never rewritten. |
| Function 1 Name | Haldi | Haldi | YES |  |
| Function 1 Date | 31st Dec | 31st Dec | YES |  |
| Function 1 Day | EMPTY | — omitted — | YES |  |
| Function 1 Time | 8.00pm. | 8.00pm. | YES |  |
| Function 1 Venue | near om caching classes, new shivaji nagar, parli vaijnath,Beed 431515 | near om caching classes, new shivaji nagar, parli vaijnath,Beed 431515 | YES |  |
| Function 1 Dress code | EMPTY | — omitted — | YES |  |
| Function 1 Maps link | https://www.google.com/maps/search/?api=1&query=near%20om%20caching%20classes%2C%20new%20shivaji%20nagar%2C%20parli%20vaijnath%2CBeed%20431515 | https://www.google.com/maps/search/?api=1&query=near%20om%20caching%20classes%2C%20new%20shivaji%20nagar%2C%20parli%20vaijnath%2CBeed%20431515 | YES |  |
| Function 1 computed weekday | Not supplied | Thursday | COMPUTED | Unprovided weekdays are not added to the page. |
| Function 2 Name | Sangeet | Sangeet | YES |  |
| Function 2 Date | 31 December 2026 | 31 December 2026 | YES |  |
| Function 2 Day | EMPTY | — omitted — | YES |  |
| Function 2 Time | 6.00 pm | 6.00 pm | YES |  |
| Function 2 Venue | near om caching classes, new shivaji nagar, parli vaijnath,Beed 431515 | near om caching classes, new shivaji nagar, parli vaijnath,Beed 431515 | YES |  |
| Function 2 Dress code | EMPTY | — omitted — | YES |  |
| Function 2 Maps link | https://www.google.com/maps/search/?api=1&query=near%20om%20caching%20classes%2C%20new%20shivaji%20nagar%2C%20parli%20vaijnath%2CBeed%20431515 | https://www.google.com/maps/search/?api=1&query=near%20om%20caching%20classes%2C%20new%20shivaji%20nagar%2C%20parli%20vaijnath%2CBeed%20431515 | YES |  |
| Function 2 computed weekday | Not supplied | Thursday | COMPUTED | Unprovided weekdays are not added to the page. |
| Function 3 Name | Wedding | Wedding | YES |  |
| Function 3 Date | 1 January 2027 | 1 January 2027 | YES |  |
| Function 3 Day | Friday | Friday | YES |  |
| Function 3 Time | 1:35 pm | 1:35 pm | YES |  |
| Function 3 Venue | EMPTY | Tirupati mangal karyalay | YES | Inherited main value. |
| Function 3 Dress code | EMPTY | — omitted — | YES |  |
| Function 3 Maps link | EMPTY | https://www.google.com/maps/search/?api=1&query=Tirupati%20mangal%20karyalay%2C%20itke%20corner%2CTharmal%20rode%20%2C%20Parli%20vaijnath%2CBeed%20431515 | YES | Inherited main value. |
| Function 3 computed weekday | Friday | Friday | COMPUTED | Unprovided weekdays are not added to the page. |
| Calendar end-time rule | Start only supplied | Start + 3 hours | DERIVED | Hidden constant CONFIG.calendarDurationHours = 3; end times never displayed. |
| Event order | Haldi; Sangeet; Wedding | Haldi; Sangeet; Wedding | YES | Source order retained although Sangeet starts earlier than Haldi. |
| Haldi year | 31st Dec | 2026 internally; display unchanged | DERIVED | Year derived from the confirmed wedding and Sangeet dates. |
| Maps URLs | Supplied addresses | Address-search links | DERIVED | Not supplied place-pin links; verify the selected places. |
| Real photos | None supplied | Three original inline SVG scenes | APPROVED | Temporary illustrations previously approved. Photo EXIF, likeness and crop checks are deferred. |
| OG photograph | None supplied | Omitted | APPROVED | No real photo or published URL yet. |
