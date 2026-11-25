# -*- coding: utf-8 -*-
"""Smoke test: abre index.html e o bundle no Edge headless, coleta erros e tira screenshots."""
import pathlib, sys
from playwright.sync_api import sync_playwright

root = pathlib.Path(__file__).parent.resolve()
targets = {
    "index": (root / "index.html").as_uri(),
    "bundle": (root / "apartamento-3d-compartilhavel.html").as_uri(),
}
failed = False
with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True, args=["--use-gl=swiftshader", "--enable-webgl", "--ignore-gpu-blocklist"])
    for name, url in targets.items():
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        errors = []
        page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
        page.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)
        page.goto(url)
        page.wait_for_timeout(4000)
        info = page.evaluate("""() => ({
            hasData: typeof APARTMENT_DATA !== 'undefined',
            walls: (typeof APARTMENT_DATA !== 'undefined' && APARTMENT_DATA.walls) ? APARTMENT_DATA.walls.length : -1,
            meshes: (typeof scene !== 'undefined' && scene) ? (()=>{let n=0; scene.traverse(o=>{if(o.isMesh)n++}); return n;})() : -1,
            doors: (typeof interactiveDoors !== 'undefined') ? interactiveDoors.length : -1
        })""")
        page.screenshot(path=str(root / f"smoke_{name}.png"))
        print(f"[{name}] {info}")
        for e in errors:
            print(f"   {e}")
        if errors or info["meshes"] <= 0:
            failed = True
        page.close()
    browser.close()
sys.exit(1 if failed else 0)
