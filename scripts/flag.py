"""Escribe assets/flag.svg (bandera de Brasil simplificada) y assets/favicon.svg."""

from pathlib import Path

GREEN = "#009B3A"
YELLOW = "#FFDF00"
BLUE = "#002776"

flag = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 20">'
    f'<rect width="30" height="20" fill="{GREEN}"/>'
    f'<polygon points="15,1.8 27.6,10 15,18.2 2.4,10" fill="{YELLOW}"/>'
    f'<circle cx="15" cy="10" r="4.6" fill="{BLUE}"/>'
    '<path d="M10.5 9.2 Q15 7.6 19.5 10.8" stroke="#FFFFFF" stroke-width="0.7" fill="none"/>'
    "</svg>"
)

favicon = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    f'<rect width="64" height="64" rx="14" fill="{GREEN}"/>'
    f'<polygon points="32,10 56,32 32,54 8,32" fill="{YELLOW}"/>'
    f'<circle cx="32" cy="32" r="12" fill="{BLUE}"/>'
    '<path d="M21 29.5 Q32 25.5 43 33" stroke="#FFFFFF" stroke-width="1.8" fill="none"/>'
    "</svg>"
)

assets = Path(__file__).resolve().parents[1] / "assets"
assets.joinpath("flag.svg").write_text(flag, encoding="utf-8")
assets.joinpath("favicon.svg").write_text(favicon, encoding="utf-8")
