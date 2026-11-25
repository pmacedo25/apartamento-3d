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
    # Substitui o bloco inteiro (scripts externos + fallbacks de CDN) de uma vez,
    # sem filtrar linha a linha (isso mutilava os <script> de fallback e deixava '}' solto).
    import re
    block = re.compile(r'[ \t]*<script src="lib/three\.min\.js"></script>.*?<script src="app\.js"></script>', re.S)
    if not block.search(html):
        raise SystemExit("ERRO: bloco de scripts nao encontrado em index.html")
    single_html = block.sub(lambda m: script_replacement, html, count=1)

out_path = os.path.join(base_dir, 'apartamento-3d-compartilhavel.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(single_html)

size_kb = os.path.getsize(out_path) / 1024
print(f"Created single-file standalone bundle: {out_path} ({size_kb:.1f} KB)")
