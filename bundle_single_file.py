import os

base_dir = r'c:\Users\sport\Documents\apartamento'

with open(os.path.join(base_dir, 'lib', 'three.min.js'), 'r', encoding='utf-8') as f:
    three_js = f.read()

with open(os.path.join(base_dir, 'lib', 'OrbitControls.js'), 'r', encoding='utf-8') as f:
    orbit_js = f.read()

with open(os.path.join(base_dir, 'plan_image_b64.js'), 'r', encoding='utf-8') as f:
    plan_b64 = f.read()

with open(os.path.join(base_dir, 'apartment_geometry.js'), 'r', encoding='utf-8') as f:
    geometry_js = f.read()

with open(os.path.join(base_dir, 'app.js'), 'r', encoding='utf-8') as f:
    app_js = f.read()

with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()

# Replace script tags with inline scripts
script_replacement = f"""
  <script>{three_js}</script>
  <script>{orbit_js}</script>
  <script>{plan_b64}</script>
  <script>{geometry_js}</script>
  <script>{app_js}</script>
"""

# Find where the script tags are in index.html
old_scripts = """  <!-- Local Libraries & Geometry Scripts -->
  <script src="lib/three.min.js"></script>
  <script src="lib/OrbitControls.js"></script>
  <script src="plan_image_b64.js"></script>
  <script src="apartment_geometry.js"></script>
  <script src="app.js"></script>"""

if old_scripts in html:
    single_html = html.replace(old_scripts, script_replacement)
else:
    # Fallback replace
    lines = html.split('\n')
    filtered = [l for l in lines if not any(s in l for s in ['lib/three', 'OrbitControls', 'plan_image_b64', 'apartment_geometry', 'app.js'])]
    body_idx = [i for i, l in enumerate(filtered) if '</body>' in l][0]
    filtered.insert(body_idx, script_replacement)
    single_html = '\n'.join(filtered)

out_path = os.path.join(base_dir, 'apartamento-3d-compartilhavel.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(single_html)

size_kb = os.path.getsize(out_path) / 1024
print(f"Created single-file standalone bundle: {out_path} ({size_kb:.1f} KB)")
