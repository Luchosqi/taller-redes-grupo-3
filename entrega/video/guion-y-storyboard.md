# Guion y storyboard del video demostrativo — Grupo 3

Duración: **5 min 56 s**. Formato: MP4, 1920 × 1080, 25 fps, sin pista de audio. El video conserva una sección principal narrable y cierra con un anexo visual de capturas originales de consola. Las escenas muestran pruebas registradas entre el 26 y el 29 de septiembre de 2026; no representan una sesión en vivo. El guion amplía qué se hizo, cómo se comprobó y qué límites quedan.

## Guion por escena

| Tiempo | Imagen / acción en pantalla | Narración sugerida |
|---|---|---|
| 00:00–00:12 | Portada: dominio, IP y Grupo 3. | **Luis:** «Somos el Grupo 3 del Taller de Redes. En este proyecto reunimos en un VPS los servicios para el dominio zorro-darwin.lazos.cl. El servidor usa la dirección 200.13.5.39. En los siguientes minutos mostramos el diseño y las pruebas funcionales que dejamos registradas.» |
| 00:12–00:32 | Diagrama generado de arquitectura. | **Luis:** «Todos los servicios principales se ejecutan en el mismo VPS. PowerDNS responde por la zona; Apache publica tres sitios; Postfix y Dovecot entregan y exponen los buzones; vsftpd permite transferir archivos; y un programa Python ofrece el chat TCP. MariaDB escucha solo en la interfaz local. El firewall y SELinux controlan el acceso desde dos capas distintas.» |
| 00:32–00:56 | Captura de terminal externa con consultas DNS. | **Luis:** «Primero comprobamos los nombres desde un equipo externo. Consultamos el servidor autoritativo por UDP y TCP, y comparamos la respuesta de la raíz con un resolvedor público. Revisamos SOA, NS, direcciones A y el MX que dirige el correo a mail. La delegación del padre y el NS de la zona tienen nombres distintos, pero ambos resuelven hacia la IP del VPS.» |
| 00:56–01:14 | PowerAdmin con TXT temporal creado. | **Luis:** «También verificamos que PowerAdmin pudiera modificar datos que PowerDNS realmente sirve. Creamos un TXT temporal, consultamos su respuesta con dig y encontramos una respuesta negativa antigua en caché. Purgamos solo ese nombre de prueba y repetimos la consulta. Así enlazamos la edición web con la respuesta DNS.» |
| 01:14–01:24 | Vista final de la zona en PowerAdmin. | **Luis:** «Después borramos el registro temporal y comprobamos que dejara de responder. La zona final conserva once registros. La cuenta temporal usada para la edición se retiró al terminar.» |
| 01:24–01:42 | Portada WordPress web1. | **Giovanny:** «Apache comparte la IP entre los tres sitios y elige cada uno según el nombre solicitado. Web1 ejecuta WordPress. Publicamos un artículo sobre el zorro de Darwin y comprobamos que la página pública muestra ese contenido. WordPress usa su propia base de datos y limita la escritura de Apache a la carpeta necesaria para subir archivos.» |
| 01:42–02:00 | Joomla web2 y artículo público. | **Giovanny:** «Web2 ejecuta Joomla y usa una base separada de WordPress. Publicamos un artículo sobre el bosque nativo desde la administración del CMS. Una primera edición mostró etiquetas HTML como texto; corregimos el artículo y comprobamos la versión pública final. La captura muestra el contenido después de esa corrección.» |
| 02:00–02:18 | Grav web3 y contenido propio. | **Giovanny:** «Web3 ejecuta Grav. A diferencia de WordPress y Joomla, este CMS guarda sus páginas como archivos Markdown y no necesita una base relacional. Publicamos una guía de hábitats y verificamos que apareciera bajo su propio nombre. Los tres sitios comparten VPS, pero mantienen contenido y persistencia distintos.» |
| 02:18–02:40 | Captura de cliente FTP con transferencias. | **Giovanny:** «Para transferir archivos configuramos vsftpd en el puerto 2121 y un rango pasivo del 30000 al 30100. Cada cuenta quedó dentro de su HOME, que no puede modificar; sí puede escribir en su propio public_html. Con un cliente automatizado, las tres cuentas subieron y reemplazaron archivos. Después comparamos el contenido publicado por HTTP. El acceso anónimo fue rechazado.» |
| 02:40–03:02 | RoundCube, mensaje de CMS1 en buzón CMS2. | **Maximiliano:** «El flujo de correo conecta RoundCube con Postfix para enviar, Maildir para guardar y Dovecot para consultar. CMS1 envió un mensaje a CMS2. Automatizamos un navegador real mediante un túnel SSH y abrimos el mensaje en el buzón de destino. La captura muestra el remitente, el asunto y el contenido recibido.» |
| 03:02–03:22 | Respuesta CMS2 a CMS1. | **Maximiliano:** «Luego CMS2 respondió y CMS1 abrió la respuesta en su buzón. Esta ida y vuelta dejó evidencia de entrega y lectura para las dos cuentas. La interfaz se manejó con automatización; no presentamos la prueba como una acción manual. El servicio de correo usa TLS con un certificado autofirmado. La webmail, en este despliegue, quedó publicada por HTTP.» |
| 03:22–03:44 | Captura de firewall, servicios y SELinux. | **Maximiliano:** «Revisamos las reglas de firewalld para DNS, web, correo, FTP y chat. MariaDB permanece en 127.0.0.1 y no está publicada. Mantuvimos SELinux en Enforcing y activamos políticas específicas para los flujos necesarios. La evidencia guardada muestra los puertos autorizados y los módulos locales. No contamos con un escaneo externo posterior a la configuración.» |
| 03:44–04:06 | Chat: dos conversaciones consecutivas. | **Maximiliano:** «El último servicio funcional es el chat en TCP 9000. El servidor corre como unidad systemd y recibe su entrada mediante un FIFO privado. El cliente se conectó, envió texto y recibió la respuesta del servidor. Cerramos esa sesión y abrimos una segunda sin reiniciar la unidad. La captura permite asociar cada respuesta a su conexión.» |
| 04:06–04:26 | Placa de cierre con síntesis y rutas de entrega. | **Luis:** «En conjunto, comprobamos DNS, tres CMS, transferencia FTP, correo en ambos sentidos, controles de acceso y dos sesiones de chat. Los informes explican las decisiones, las fallas y sus correcciones. Quedan identificados los datos documentales que no pudimos respaldar, como algunos extractos de configuración y una cabecera completa Received. A continuación dejamos recortes de las capturas de consola; los archivos originales completos se conservan junto a sus transcripciones.» |

## Anexo visual al final: capturas de consola

Estas seis escenas se colocan **después del cierre narrado**, al final del MP4. Presentan recortes de capturas de consola existentes: retiramos las líneas auxiliares del capturador y las rutas temporales que no aportaban evidencia. En la captura SSH del VPS también omitimos la invocación local para no divulgar la ruta de la llave. Conservamos los archivos fuente completos e intactos en `evidencias/`; no recreamos ninguna salida. El anexo queda sin narración para que las imágenes puedan consultarse con pausa.

| Tiempo | Captura y rótulo | Qué permite revisar |
|---|---|---|
| 04:26–04:34 | Placa «Anexo · capturas de consola». | Separa el cierre narrado de las capturas originales. |
| 04:34–04:46 | `12-auditoria-lote1-dns-poweradmin/terminal-vps-resumen-recorte.png`. | Salida remota de PowerDNS, MariaDB, puerto DNS, SOA y MX; captura SSH del 28-09-2026. |
| 04:46–04:58 | `12-auditoria-lote1-dns-poweradmin/terminal-cliente-resumen-recorte.png`. | Consultas DNS desde el equipo cliente del 28-09-2026. |
| 04:58–05:10 | `10-revision/solucion-web-permisos-recorte.png`. | Propietarios y modos de los tres `public_html`; 27-09-2026. |
| 05:10–05:22 | `10-revision/solucion-ftp-recorte.png`. | Transferencias automatizadas y comparación HTTP; 27-09-2026. |
| 05:22–05:34 | `10-revision/solucion-seguridad-recorte.png`. | Servicios y puertos permitidos por firewalld; 27-09-2026. |
| 05:34–05:46 | `10-revision/solucion-chat-recorte.png`. | Dos intercambios consecutivos con el servidor TCP; 27-09-2026. |
| 05:46–05:56 | Placa final con entregables del grupo. | Informe técnico, informe ejecutivo y video. |

## Montaje y reproducción

El montaje usa capturas existentes y sus recortes seguros; cada imagen se presenta dentro de una placa con título, contexto y ruta de origen. Los archivos completos permanecen intactos en `evidencias/`. La arquitectura es un diagrama explicativo generado para el informe, no evidencia de una ejecución. El anexo final deja a la vista las capturas útiles para contrastar los resultados.

Para regenerar el archivo, instalar Pillow y FFmpeg y ejecutar desde cualquier directorio:

```sh
python3 entrega/video/crear_video.py
```

La salida se guarda en `entrega/video/video-demostrativo-sin-voz.mp4`. El archivo no incluye pista de audio; las narraciones sugeridas se pueden grabar y sincronizar siguiendo los tiempos de la tabla. El montaje no contiene credenciales ni presenta una medición histórica como si fuera una sesión en vivo.
