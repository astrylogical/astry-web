"""Check the built landing-page artwork and its delivery policy."""
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'app/dist'


class Artwork(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.icons = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'img':
            self.images.append(attrs.get('src', ''))
        if tag == 'link' and 'icon' in attrs.get('rel', '').split():
            self.icons.append(attrs.get('href', ''))


artwork = Artwork()
artwork.feed((DIST / 'index.html').read_text())
if len(artwork.images) < 4 or len(artwork.icons) < 2:
    raise ValueError('Landing-page images or favicon fallbacks are missing')
for source in sorted(set(artwork.images + artwork.icons)):
    url = urlsplit(source)
    if url.scheme or url.netloc or not url.path.startswith('/'):
        raise ValueError('Artwork must use same-origin files: ' + source)
    path = (DIST / unquote(url.path).lstrip('/')).resolve()
    if not path.is_relative_to(DIST.resolve()) or not path.is_file():
        raise ValueError('Missing or invalid artwork: ' + source)
    if path.suffix == '.svg':
        if ET.fromstring(path.read_bytes()).tag != '{http://www.w3.org/2000/svg}svg':
            raise ValueError('Invalid SVG: ' + source)
    elif path.suffix == '.png':
        if not path.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'):
            raise ValueError('Invalid PNG: ' + source)
    else:
        raise ValueError('Unexpected artwork type: ' + source)
config = json.loads((ROOT / 'vercel.json').read_text())
headers = {row['key']: row['value'] for row in config['headers'][0]['headers']}
directives = {words[0]: words[1:] for part in headers['Content-Security-Policy'].split(';')
              if (words := part.split())}
if directives.get('img-src') != ["'self'"]:
    raise ValueError('Landing-page artwork requires a self-only image policy')
print(f'Artwork passed: {len(artwork.images)} images, {len(artwork.icons)} favicons.')
