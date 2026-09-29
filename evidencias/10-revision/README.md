# Evidencias originales: auditoría y correcciones

Esta carpeta conserva capturas del diagnóstico inicial, las correcciones y las pruebas posteriores. El estado final por actividad está resumido en `../11-validacion-final/resumen.md` y en la tabla integrada del informe técnico. Los PDF citan las figuras seleccionadas y explican qué acredita cada prueba. Las capturas de terminal tienen transcripciones `.txt` con comandos y resultados.

## Capturas finales incorporadas al informe

### Recortes seguros derivados para informe y video

Los archivos originales `solucion-web.png`, `solucion-ftp.png`, `solucion-seguridad.png` y `solucion-chat.png` permanecen intactos. Para evitar mostrar trazas del capturador o rutas temporales en las piezas finales, generamos recortes que conservan los resultados útiles:

- `solucion-web-permisos-recorte.png`: propietario y modo de los tres `public_html`.
- `solucion-ftp-recorte.png`: transferencias y comparación de contenido HTTP para las tres cuentas.
- `solucion-seguridad-recorte.png`: lista de servicios y puertos de firewalld.
- `solucion-chat-recorte.png`: resultado de las dos sesiones consecutivas.

| Archivo | Evidencia y alcance |
|---|---|
| `solucion-entorno.png` | Inspección final de AlmaLinux, interfaz/IP, Enforcing y salida HTTP/2 200 desde el VPS. Es posterior a la línea base inicial. |
| `solucion-dns.png` | Consultas desde el equipo local contra PowerDNS y 1.1.1.1: A raíz/subdominios y MX. |
| `poweradmin-zona.png` | Vista autenticada de la zona; imagen anterior al A raíz y limpieza del TXT, expresamente indicado en el informe. `poweradmin-cambio-dns.txt` registra una modificación de prueba previa. |
| `web1-final.png`, `joomla-contenido-publico.png`, `web3-final.png` | Portadas finales distintas de WordPress, Joomla y Grav; `cms-final.txt` confirma HTTP200 y texto esperado. |
| `solucion-web.png` | VirtualHosts, artículo Joomla en BD y propietarios de public_html. |
| `solucion-ftp.png` | Tres cuentas: login, doble escritura, comparación HTTP, jaula y rechazo anónimo. |
| `correo-02-recibido.png`, `correo-04-respuesta-recibida.png` | Mensaje abierto en CMS2 y respuesta abierta en CMS1, con asunto, remitente y cuerpo visibles; transcripciones `solucion-correo-*.txt`. |
| `solucion-seguridad.png` | Nueve servicios activos, firewall, MariaDB local, Enforcing y módulos SELinux. |
| `solucion-chat.png` | Dos conversaciones consecutivas desde cliente local y respuestas del servidor. |

## Historial no usado como estado final

`auditoria-*.png` muestra el diagnóstico anterior. `dnsadmin-antes-error.png`, `web1-navegador.png`, `web2-navegador.png`, `web3-navegador.png`, `correo-01-redaccion.png` y `correo-navegador.txt` son estados iniciales o fallidos; tienen valor para el análisis de dificultades, no para demostrar cierre. `wordpress-permisos-tras-ajuste.png/.txt` documenta el ajuste específico de uploads. `joomla-formulario-previo.png` y `joomla-articulo-publicado-admin.png` muestran el flujo editorial; la primera publicación contenía HTML literal y fue corregida antes de la captura final. Las capturas de composición no se presentan como prueba de entrega.

No se incluyeron contraseñas, llaves privadas ni tokens en estas imágenes o transcripciones. Las fechas difieren entre Chile (UTC−03) y el VPS (Europe/Madrid); el informe conserva esa distinción. Las imágenes finales de terminal fueron inspeccionadas visualmente tras la captura para confirmar que muestran la ventana de evidencia, no otra ventana del escritorio.

En el informe técnico, las seis figuras de terminal usan recorte de presentación en LaTeX para mostrar únicamente comandos y salidas. Los PNG originales se conservan intactos como respaldo; sus títulos, fechas, indicaciones de origen y cierre de captura quedan fuera del área visible del PDF. El contexto de cada prueba se explica en el cuerpo y el pie de figura del informe.
