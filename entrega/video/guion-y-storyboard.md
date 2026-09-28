# Video demostrativo, Grupo 3

Duración objetivo: 3 min 20 s. Formato: MP4, 1920 × 1080, 25 fps, sin voz. Las placas mantienen cada prueba visible para que el grupo grabe e incorpore una narración después. La pauta disponible confirma que el video es obligatorio, pero no fija aquí una duración máxima. Las capturas son auténticas y están en `evidencias/`; el guion no supone una demostración en vivo.

| Tiempo | Imagen y acción en pantalla | Narración sugerida |
|---|---|---|
| 00:00–00:12 | Portada con dominio e IP del proyecto. | **Luis:** «Somos el Grupo 3. En el VPS 200.13.5.39 integramos los servicios del dominio zorro-darwin.lazos.cl.» |
| 00:12–00:27 | Esquema de arquitectura del informe; DNS, Apache, MariaDB y servicios. | «El mismo servidor publica tres sitios, correo, FTP, un chat TCP y la administración de DNS. Cada servicio tiene una comprobación propia.» |
| 00:27–00:44 | Terminal DNS del lote 1: NS/SOA, A y MX, UDP/TCP. | «Desde un equipo externo consultamos PowerDNS por UDP y TCP. La zona devolvió los registros A y MX; la raíz y los servicios apuntan a la IP del VPS.» |
| 00:44–01:00 | PowerAdmin: TXT creado y vista final sin el TXT. | «Probamos la edición en PowerAdmin con un TXT temporal, consultamos su respuesta en DNS y lo eliminamos. La zona final quedó con once registros.» |
| 01:00–01:13 | WordPress, web1. | **Giovanny:** «Apache separa los sitios por nombre. Web1 ejecuta WordPress y muestra un artículo propio sobre el zorro de Darwin.» |
| 01:13–01:26 | Joomla, web2. | «Web2 usa Joomla. Publicamos un artículo desde su administración y comprobamos que aparece en la página pública.» |
| 01:26–01:39 | Grav, web3. | «Web3 usa Grav y conserva sus páginas en Markdown. Los tres sitios responden con contenido distinto.» |
| 01:39–01:56 | Terminal FTP, tres cuentas y HTTP. | «En el puerto 2121, cada cuenta subió y reemplazó archivos dentro de su jaula. La versión actualizada apareció por HTTP; el acceso anónimo fue rechazado.» |
| 01:56–02:13 | Correo CMS1 a CMS2 abierto en RoundCube. | **Maximiliano:** «Desde RoundCube enviamos un mensaje de CMS1 a CMS2 y lo abrimos en el buzón de destino.» |
| 02:13–02:29 | Respuesta CMS2 a CMS1 abierta. | «CMS2 respondió y CMS1 recibió la respuesta. Esta ida y vuelta comprueba Postfix, Dovecot y el acceso web al correo.» |
| 02:29–02:45 | Firewall y SELinux Enforcing. | «Verificamos los puertos autorizados, MariaDB solo en 127.0.0.1 y SELinux en modo Enforcing.» |
| 02:45–03:01 | Chat: dos sesiones consecutivas. | «El cliente externo conversó dos veces con el servidor Python en TCP 9000, sin reiniciar el servicio.» |
| 03:01–03:20 | Cierre con tabla resumida y dificultades. | «Corregimos escritura FTP, el destino SMTP de RoundCube y el contenido de los CMS. Los informes contienen el procedimiento y las evidencias completas.» |

## Storyboard y montaje

Una placa por fila, con rótulo breve y captura original a tamaño suficiente para leer el resultado. Para DNS y PowerAdmin usar las capturas del lote `12-auditoria-lote1-dns-poweradmin`; para el resto usar las imágenes finales de `10-revision`. El esquema inicial es una figura explicativa, no una captura de prueba. Se conservarán transiciones discretas y silencio de audio para añadir tres voces según los cambios de narrador marcados arriba. El proyecto de edición es `crear_video.py`; los tiempos se ajustan allí si las grabaciones definitivas duran más.

El video muestra evidencia registrada el 26–28 de septiembre de 2026. No incluye credenciales ni recrea una terminal o interfaz como si fuera una medición real.
