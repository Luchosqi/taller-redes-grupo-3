# Video demostrativo

- `video-demostrativo-sin-voz.mp4`: 5:56, H.264, 1920 × 1080, 25 fps, sin pista de audio. La narración sugerida ocupa la sección principal; las capturas originales de consola quedan reunidas en el anexo visual final. El [guion](guion-y-storyboard.md) incluye texto ampliado, narradores, tiempos y fuentes de imagen.
- `guion-y-storyboard.md`: escenas, tiempos, texto y cambios de narrador.
- `crear_video.py`: proyecto reproducible. Usa capturas originales de `evidencias/`, el diagrama de `informe/latex/recursos/`, Pillow y FFmpeg; ejecutarlo desde cualquier directorio con `python3 entrega/video/crear_video.py`.

El MP4 presenta capturas de pruebas ya realizadas, no una sesión en vivo. Al final se presentan seis recortes de consola. Eliminan líneas auxiliares del capturador y rutas temporales; el recorte de la sesión SSH del VPS también omite la invocación local que mostraba la ubicación de la llave. Los originales completos permanecen intactos en `evidencias/`. El diagrama de arquitectura es una ilustración explicativa, no evidencia de una ejecución. Para cambiar la duración de una escena, modificar su primer número en `SCENES` y volver a ejecutar el script. La salida no incluye audio para que el equipo grabe y sincronice sus voces con el guion.
