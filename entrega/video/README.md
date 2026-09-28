# Video demostrativo

- `video-demostrativo-sin-voz.mp4`: 3:20, H.264, 1920 × 1080, 25 fps, sin pista de audio. Está listo para incorporar las tres voces siguiendo el [guion](guion-y-storyboard.md).
- `guion-y-storyboard.md`: escenas, tiempos, texto y cambios de narrador.
- `crear_video.py`: proyecto reproducible. Usa capturas originales de `evidencias/`, Pillow y FFmpeg; ejecutarlo desde cualquier directorio con `python3 entrega/video/crear_video.py`.

El MP4 presenta capturas de pruebas ya realizadas, no una sesión en vivo. Las imágenes originales se conservan sin modificación en `evidencias/`. El script genera placas de presentación y un esquema explicativo, que aparecen diferenciados de las capturas. Para cambiar la duración de una escena, modificar su primer número en `SCENES` y volver a ejecutar el script. La salida no incluye audio para que el equipo grabe y sincronice sus voces.
