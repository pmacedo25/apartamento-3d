import os
import urllib.request

os.makedirs(r'c:\Users\sport\Documents\apartamento\lib', exist_ok=True)

files = [
    ('https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js', r'c:\Users\sport\Documents\apartamento\lib\three.min.js'),
    ('https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js', r'c:\Users\sport\Documents\apartamento\lib\OrbitControls.js')
]

for url, path in files:
    if not os.path.exists(path):
        print(f"Downloading {url}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp, open(path, 'wb') as f:
                f.write(resp.read())
            print(f"Saved {path}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")
    else:
        print(f"Already exists: {path}")
