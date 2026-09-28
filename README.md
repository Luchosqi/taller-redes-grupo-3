# Taller de Redes — Grupo 3

Entrega del Grupo 3 del Taller de Redes. Integrantes: Luis Jaramillo, Giovanny Toledo y Maximiliano Rivas.

## Entregables del 28-09-2026

- [Informe técnico final, PDF](informe/latex/informe-tecnico.pdf) y [fuente LaTeX](informe/latex/informe-tecnico.tex).
- [Informe ejecutivo final, PDF](informe/latex/informe-ejecutivo.pdf) y [fuente LaTeX](informe/latex/informe-ejecutivo.tex).
- [Video demostrativo MP4 sin voz](entrega/video/video-demostrativo-sin-voz.mp4), [guion y storyboard](entrega/video/guion-y-storyboard.md) y [proyecto de edición](entrega/video/crear_video.py).
- [Código e instrucciones del chat TCP](entrega/chat-texto/) y [evidencias originales](evidencias/).

El video dura 3:20 y está preparado para añadir la narración del equipo. El técnico distingue las pruebas funcionales del 26–27 de septiembre del lote DNS/PowerAdmin repetido el 28. Para el estado y los límites, ver [PROGRESO.md](PROGRESO.md).

Para retomar el trabajo, empezar por [PROGRESO.md](PROGRESO.md), luego leer [AGENT.md](AGENT.md) y [REVISION_PAUTA_CAMPUS.md](REVISION_PAUTA_CAMPUS.md).

## Antes de configurar el VPS

1. Leer [AGENT.md](AGENT.md) y [REVISION_PAUTA_CAMPUS.md](REVISION_PAUTA_CAMPUS.md).
2. Confirmar en Campus Virtual la pauta vigente y ajustar la lista heredada antes de tratarla como requisito.
3. Preparar el acceso SSH en el equipo local. La llave privada y cualquier frase de paso deben permanecer fuera de este repositorio.
4. Registrar la línea base y cada cambio en `docs/bitacora-vps.md`, sin copiar secretos.

## Organización

- `AGENT.md`: reglas de trabajo para el grupo.
- `REVISION_PAUTA_CAMPUS.md`: checklist provisional y criterios del informe.
- `docs/bitacora-vps.md`: registro de cambios, respaldos y pruebas en el VPS.
- `informe/latex/`: fuentes LaTeX del informe técnico y ejecutivo.
- `evidencias/`: capturas originales agrupadas por tema; ver sus instrucciones antes de añadir archivos.

Los nombres de las carpetas de evidencias son una organización inicial basada en la lista de otro grupo. Ajustarlos si la pauta vigente usa otra estructura. El repositorio no debe contener llaves, contraseñas, tokens ni respaldos con datos sensibles.

## Compilar los informes

Desde `informe/latex/`, compilar cada documento dos veces y revisar visualmente las páginas afectadas. Con una instalación completa de TeX Live:

```sh
pdflatex informe-tecnico.tex
pdflatex informe-tecnico.tex
pdflatex informe-ejecutivo.tex
pdflatex informe-ejecutivo.tex
```

No redactar resultados como cumplidos hasta disponer de pruebas propias del Grupo 3.

Los PDF de esta entrega se compilaron con Tectonic 0.17.0 (dos pasadas por fuente, desde `informe/latex/`). Ejemplo: `tectonic -X compile informe-tecnico.tex --outdir .`. Tectonic descarga el paquete de formatos y fuentes en su primera ejecución. Se comprobaron enlaces, páginas y legibilidad después de compilar.
