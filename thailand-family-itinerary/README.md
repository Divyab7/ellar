# Thailand Family Trip itinerary

Customer-facing itinerary experience for Lurws Group, ref LG/TH/0926/01.

- 12 adults, ex Bangalore, 15–19 September 2026, Bangkok and Pattaya (04N/05D) with an optional 05N/06D extension
- Prepared by B Prudhivi Raj, Travel Operations
- Source: `Lurws_Quotation_Thailand.pdf` (the quotation this page expands on)

`index.html` is a single self-contained, mobile-first page in a plain white-and-blue brochure style:

- Cover photo slot, title, dates, "from" price and one button
- Five days as short plain-language blocks with one rain note
- Postcards grid (photo slots); tapping a picture shows a one-line fun fact
- One control: 3 / 4 / 5 star hotel level, which updates the hotel names and price
- Add-ons as a plain price list, included / not included lists, five "good to know" lines with the live time in Thailand
- Three booking steps with cancellation, the 6-day option and price notes behind "+" links
- "Send us your choice" form that stores the pick in the artifact database on claude.ai, with a clipboard fallback elsewhere

Prices are indicative ranges and must be reconfirmed with the airline group desk and hotels before booking.

## Adding photos

Web image hosts are not reachable from the build environment, so photos are embedded from local files:

1. Put JPG or PNG files in `photos/`, named by slot: `hero`, `sanctuary`, `korlarn`, `traimit`, `watpho`, `safari`, `pattaya`, `watarun` (postcards).
2. Optionally add `photos/credits.txt`, one credit line per photo.
3. Run `python3 embed_photos.py`. Photos are resized, compressed and embedded into `index.html` as data URIs; placeholders disappear automatically.

Use photos you have the right to publish: your own, the hotels' and attractions' press kits, or openly licensed ones (Wikimedia Commons, Unsplash, Pexels) with credit where the licence asks for it.
