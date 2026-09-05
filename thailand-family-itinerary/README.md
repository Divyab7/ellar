# Thailand Family Trip itinerary

Customer-facing itinerary experience for Lurws Group, ref LG/TH/0926/01.

- 12 adults, ex Bangalore, 15–19 September 2026, Bangkok and Pattaya (04N/05D) with an optional 05N/06D extension
- Prepared by B Prudhivi Raj, Travel Operations
- Source: `Lurws_Quotation_Thailand.pdf` (the quotation this page expands on)

`index.html` is a single self-contained page:

- Generative sea hero with a live countdown to departure
- Sticky glass navigation with scroll progress and active section
- Animated route map, September weather and group facts
- Day-by-day program with timings, meals, rain plans and coordinator notes, revealed on scroll
- Hotel category cards linked to a live package builder with add-on switches and animated totals
- "Send this package" form that stores the family's choice in the artifact database when published on claude.ai, with a clipboard fallback elsewhere
- Pre-departure checklist with progress ring (saved per device), THB/INR converter, coordination timeline, terms

Prices are indicative ranges and must be reconfirmed with the airline group desk and hotels before booking.

## Adding photos

Web image hosts are not reachable from the build environment, so photos are embedded from local files:

1. Put JPG or PNG files in `photos/`, named by slot: `hero`, `day1` … `day5` (day banners), `sanctuary`, `korlarn`, `traimit`, `watpho`, `safari`, `pattaya`, `watarun` (postcards).
2. Optionally add `photos/credits.txt`, one credit line per photo.
3. Run `python3 embed_photos.py`. Photos are resized, compressed and embedded into `index.html` as data URIs; placeholders disappear automatically.

Use photos you have the right to publish: your own, the hotels' and attractions' press kits, or openly licensed ones (Wikimedia Commons, Unsplash, Pexels) with credit where the licence asks for it.
