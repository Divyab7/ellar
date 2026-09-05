# Thailand Family Trip itinerary

Customer-facing itinerary experience for Lurws Group, ref LG/TH/0926/01.

- 12 adults, ex Bangalore, 15–19 September 2026, Bangkok and Pattaya (04N/05D) with an optional 05N/06D extension
- Prepared by B Prudhivi Raj, Travel Operations
- Source: `Lurws_Quotation_Thailand.pdf` (the quotation this page expands on)

`index.html` is a single self-contained, mobile-first page:

- Hero with dates, group size, "from" price and two actions
- Postcards gallery (photo slots, see below)
- Five collapsible day cards with timed plans, meals, rain plans and "taken care of" notes
- Hotel category switch (3 / 4 / 5 star, 4 recommended) wired to the price panel
- Four add-on checkboxes with per-person and family totals
- Included / not included, six "good to know" items, three booking steps, cancellation and the 6-day option
- "Send your choice" form that stores the family's pick in the artifact database on claude.ai, with a clipboard fallback elsewhere
- Motion limited to feedback: accordions, checkboxes, the category switch and a mobile confirm bar

Prices are indicative ranges and must be reconfirmed with the airline group desk and hotels before booking.

## Adding photos

Web image hosts are not reachable from the build environment, so photos are embedded from local files:

1. Put JPG or PNG files in `photos/`, named by slot: `hero`, `day1` … `day5` (day banners), `sanctuary`, `korlarn`, `traimit`, `watpho`, `safari`, `pattaya`, `watarun` (postcards).
2. Optionally add `photos/credits.txt`, one credit line per photo.
3. Run `python3 embed_photos.py`. Photos are resized, compressed and embedded into `index.html` as data URIs; placeholders disappear automatically.

Use photos you have the right to publish: your own, the hotels' and attractions' press kits, or openly licensed ones (Wikimedia Commons, Unsplash, Pexels) with credit where the licence asks for it.
