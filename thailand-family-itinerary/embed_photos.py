#!/usr/bin/env python3
"""Embed photos into index.html.

Drop JPG/PNG files into ./photos named by slot, then run:  python3 embed_photos.py
Slots: hero, day1..day5, sanctuary, korlarn, traimit, watpho, safari, pattaya, watarun
Optional ./photos/credits.txt (one line per photo, e.g. "Wat Arun: Photo by X, CC BY-SA 4.0, Wikimedia Commons")
Images are resized to 1600px wide and embedded as JPEG data URIs. Re-running replaces earlier embeds.
"""
import base64, io, os, re, sys
from PIL import Image, ImageOps

here = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(here, 'index.html')
photos = os.path.join(here, 'photos')
s = open(html_path, encoding='utf-8').read()
WIDTH = {'hero': 1920, 'day1': 1600, 'day2': 1600, 'day3': 1600, 'day4': 1600, 'day5': 1600}

def data_uri(path, key):
    im = ImageOps.exif_transpose(Image.open(path)).convert('RGB')
    w = WIDTH.get(key, 1400)
    if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=78, optimize=True, progressive=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()

done = []
for f in sorted(os.listdir(photos)):
    key, ext = os.path.splitext(f)
    if ext.lower() not in ('.jpg', '.jpeg', '.png', '.webp'): continue
    uri = data_uri(os.path.join(photos, f), key)
    m = re.search(r'<[a-z]+ class="([^"]*)" data-photo="%s" data-mode="(\w+)"' % key, s) or re.search(r'<span data-photo="%s" data-mode="(hero)" hidden>' % key, s)
    if not m: print('no slot for', key); continue
    mode = m.group(m.lastindex)
    if mode == 'shot':
        s = re.sub(r'(<figure class="shot)( ph)?([^>]*data-photo="%s"[^>]*>)<span class="badge">Photo slot</span>(<img )(?:src="[^"]*" )?(alt="[^"]*")(?: hidden)?>' % key,
                   lambda mm: f'{mm.group(1)}{mm.group(3)}{mm.group(4)}src="{uri}" {mm.group(5)}>', s, count=1)
        s = s.replace(f'<figure class="shot ph', '<figure class="shot ph') # no-op
    elif mode == 'banner':
        s = re.sub(r'(<div class="banner [^"]*?)( has-photo)?(" data-photo="%s" data-mode="banner">)(?:<img class="bg" src="[^"]*" alt="">)?' % key,
                   lambda mm: f'{mm.group(1)} has-photo{mm.group(3)}<img class="bg" src="{uri}" alt="">', s, count=1)
    elif mode == 'hero':
        s = re.sub(r'<span data-photo="hero" data-mode="hero" hidden></span>(?:<img class="hero-photo" src="[^"]*" alt="">)?',
                   lambda mm: f'<span data-photo="hero" data-mode="hero" hidden></span><img class="hero-photo" src="{uri}" alt="">', s, count=1)
        s = s.replace('<header class="hero" id="top">', '<header class="hero has-photo" id="top">')
    done.append(key)

# gallery placeholders: drop ph class + badge where a photo was embedded
s = re.sub(r'<figure class="shot ph((?: wide)?)"([^>]*)><span class="badge">Photo slot</span>(<img src=)', r'<figure class="shot\1"\2>\3', s)
s = re.sub(r'<figure class="shot ph((?: wide)?)"([^>]*)>(<img src=)', r'<figure class="shot\1"\2>\3', s)

cred = os.path.join(photos, 'credits.txt')
if os.path.exists(cred):
    lines = [l.strip() for l in open(cred, encoding='utf-8') if l.strip()]
    s = re.sub(r'<p class="credits" id="credits"( hidden)?>.*?</p>', '<p class="credits" id="credits">Photos: ' + ' · '.join(lines).replace('<','&lt;') + '</p>', s, count=1, flags=re.S)

open(html_path, 'w', encoding='utf-8').write(s)
print('embedded:', ', '.join(done) or 'nothing', '| file size', round(len(s.encode())/1024), 'KB')
