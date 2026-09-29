# Taller de Redes — Grupo 3

Implementación y documentación de una infraestructura de servicios para Fauna Araucanía en un VPS con AlmaLinux 9.8.

Repositorio: <https://github.com/Luchosqi/taller-redes-grupo-3>

## Entrega

- [Informe técnico (PDF)](informe/latex/informe-tecnico.pdf) y [fuente LaTeX](informe/latex/informe-tecnico.tex).
- [Informe ejecutivo (PDF)](informe/latex/informe-ejecutivo.pdf) y [fuente LaTeX](informe/latex/informe-ejecutivo.tex).
- [Video demostrativo sin voz](entrega/video/video-demostrativo-sin-voz.mp4), [guion y storyboard](entrega/video/guion-y-storyboard.md) y [código de edición](entrega/video/crear_video.py).
- [Aplicación de chat TCP](entrega/chat-texto/) y [evidencias de configuración y pruebas](evidencias/).
- [Política local de SELinux para FTP y contenido web](configuraciones/selinux/ftpd_httpd_content.te).

## Estructura

- `informe/latex/`: informes y sus fuentes.
- `evidencias/`: capturas y transcripciones organizadas por servicio.
- `entrega/`: video, guion y código del chat.
- `configuraciones/`: política de SELinux usada en el despliegue.
- `docs/`: bitácora del VPS y guía de pruebas manuales.

## Compilar los informes

Desde `informe/latex/`, con Tectonic instalado:

```sh
tectonic -X compile informe-tecnico.tex --outdir .
tectonic -X compile informe-ejecutivo.tex --outdir .
```

Tectonic ejecuta las pasadas necesarias para actualizar referencias. En una primera compilación puede descargar paquetes y fuentes de LaTeX.

El repositorio no debe contener llaves privadas, contraseñas, tokens ni respaldos con información sensible.
