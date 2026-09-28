#!/usr/bin/env python3
"""Monta el video mudo con capturas originales y placas de contexto.

Uso: python3 entrega/video/crear_video.py [--preview]
Requiere Pillow y ffmpeg. --preview crea una versión corta para revisar montaje.
"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
E = ROOT / "evidencias"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SIZE = (1920, 1080)

# Segundos y evidencia original. None significa placa explicativa.
SCENES = [
    (12, "Taller de Redes · Grupo 3", "zorro-darwin.lazos.cl  |  VPS 200.13.5.39", None),
    (15, "Arquitectura del sistema", "Un VPS, servicios separados por nombre, cuenta y puerto", None),
    (17, "DNS autoritativo", "A y MX comprobados desde el cliente; UDP y TCP 53", "12-auditoria-lote1-dns-poweradmin/terminal-cliente-resumen.png"),
    (8, "PowerAdmin · edición", "TXT de prueba creado y consultado por DNS", "12-auditoria-lote1-dns-poweradmin/poweradmin-txt-creado.png"),
    (8, "PowerAdmin · cierre", "TXT retirado; la zona final conserva once registros", "12-auditoria-lote1-dns-poweradmin/poweradmin-zona-final-completa.png"),
    (13, "WordPress · web1", "Artículo público sobre el zorro de Darwin", "10-revision/web1-final.png"),
    (13, "Joomla · web2", "Artículo publicado desde el administrador", "10-revision/joomla-contenido-publico.png"),
    (13, "Grav · web3", "Página propia guardada en Markdown", "10-revision/web3-final.png"),
    (17, "FTP enjaulado · TCP 2121", "Tres usuarios: subida, reemplazo y lectura HTTP; anónimo rechazado", "10-revision/solucion-ftp.png"),
    (17, "Correo · CMS1 a CMS2", "Mensaje enviado por RoundCube y abierto por el destinatario", "10-revision/correo-02-recibido.png"),
    (16, "Correo · respuesta a CMS1", "Respuesta abierta en el buzón original", "10-revision/correo-04-respuesta-recibida.png"),
    (16, "Firewall y SELinux", "Puertos comprobados; MariaDB local; Enforcing activo", "10-revision/solucion-seguridad.png"),
    (16, "Chat TCP · puerto 9000", "Dos sesiones consecutivas desde el cliente externo", "10-revision/solucion-chat.png"),
    (19, "Resultados y correcciones", "DNS, 3 CMS, FTP, correo y chat comprobados  |  Informes en informe/latex", None),
]


def fit_text(draw: ImageDraw.ImageDraw, text: str, max_width: int, size: int, bold=False):
    path = BOLD if bold else FONT
    while size > 22:
        font = ImageFont.truetype(path, size)
        if draw.textbbox((0, 0), text, font=font)[2] <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(path, size)


def architecture(draw: ImageDraw.ImageDraw):
    boxes = [
        ("Cliente externo", (660, 235, 1260, 325), "#29465f"),
        ("PowerDNS + PowerAdmin", (140, 480, 690, 615), "#234b68"),
        ("Apache: web1, web2, web3", (705, 480, 1270, 615), "#24566a"),
        ("Correo, FTP y chat TCP", (1285, 480, 1780, 615), "#265c6b"),
        ("MariaDB local · SELinux · firewalld", (470, 775, 1450, 870), "#38465a"),
    ]
    line = (113, 182, 197)
    for start, end in [((960, 325), (410, 480)), ((960, 325), (985, 480)), ((960, 325), (1530, 480)), ((410, 615), (750, 775)), ((985, 615), (985, 775)), ((1530, 615), (1240, 775))]:
        draw.line((start, end), fill=line, width=5)
    for text, box, color in boxes:
        draw.rounded_rectangle(box, radius=22, fill=color, outline="#6db6c5", width=3)
        f = fit_text(draw, text, box[2] - box[0] - 30, 35, True)
        bb = draw.textbbox((0, 0), text, font=f)
        draw.text(((box[0] + box[2] - (bb[2] - bb[0])) / 2, (box[1] + box[3] - (bb[3] - bb[1])) / 2 - 4), text, fill="white", font=f)


def slide(index: int, total: int, title: str, subtitle: str, source: str | None):
    image = Image.new("RGB", SIZE, "#101b2b")
    d = ImageDraw.Draw(image)
    d.rectangle((0, 0, 1920, 146), fill="#173247")
    d.rectangle((0, 1040, 1920, 1080), fill="#173247")
    d.text((68, 35), title, font=fit_text(d, title, 1775, 58, True), fill="#ffffff")
    d.text((69, 1010), subtitle, font=fit_text(d, subtitle, 1780, 28), fill="#d6e8ef")
    d.text((1820, 1047), f"{index + 1:02d}/{total:02d}", font=ImageFont.truetype(FONT, 20), fill="#e6f0f3")
    if source:
        src = Image.open(E / source).convert("RGB")
        factor = min(1770 / src.width, 820 / src.height)
        src = src.resize((round(src.width * factor), round(src.height * factor)), Image.Resampling.LANCZOS)
        x = (1920 - src.width) // 2
        y = 160 + (820 - src.height) // 2
        image.paste(src, (x, y))
        d.rectangle((x - 2, y - 2, x + src.width + 2, y + src.height + 2), outline="#8bc7d4", width=3)
        d.text((70, 965), f"Captura original: evidencias/{source}", font=ImageFont.truetype(FONT, 20), fill="#a8c2cf")
    elif index == 1:
        architecture(d)
        d.text((68, 965), "Diagrama explicativo · no representa una captura de funcionamiento", font=ImageFont.truetype(FONT, 20), fill="#a8c2cf")
    else:
        summary = "Grupo 3  |  Luis Jaramillo · Giovanny Toledo · Maximiliano Rivas" if index == 0 else "Pruebas y transcripciones: evidencias/  |  Informes: informe/latex/"
        d.text((130, 500), summary, font=fit_text(d, summary, 1660, 42, True), fill="#d9eaf0")
    return image


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", action="store_true")
    args = ap.parse_args()
    frames = OUT / "fotogramas"
    frames.mkdir(exist_ok=True)
    scenes = SCENES[:4] if args.preview else SCENES
    manifest = OUT / "fotogramas.txt"
    lines = []
    for i, (seconds, title, subtitle, source) in enumerate(scenes):
        path = frames / f"escena-{i + 1:02d}.png"
        slide(i, len(scenes), title, subtitle, source).save(path, optimize=True)
        lines += [f"file '{path}'", f"duration {seconds}"]
    lines += [f"file '{path}'", "duration 0.04"]
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    target = OUT / ("video-preliminar.mp4" if args.preview else "video-demostrativo-sin-voz.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(manifest), "-vf", "fps=25,format=yuv420p", "-t", str(sum(s[0] for s in scenes)), "-c:v", "libx264", "-preset", "veryfast", "-crf", "24", "-an", "-movflags", "+faststart", str(target)], check=True)
    print(target)


if __name__ == "__main__":
    main()
