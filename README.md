# Taller de Redes — Grupo 3

Repositorio de trabajo para preparar, documentar y evidenciar las actividades del taller. Integrantes: Luis Jaramillo, Giovanny Toledo y Maximiliano Rivas.

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

Desde `informe/latex/`, compilar cada documento dos veces con `pdflatex` y revisar visualmente las páginas afectadas:

```sh
pdflatex informe-tecnico.tex
pdflatex informe-tecnico.tex
pdflatex informe-ejecutivo.tex
pdflatex informe-ejecutivo.tex
```

No redactar resultados como cumplidos hasta disponer de pruebas propias del Grupo 3.
