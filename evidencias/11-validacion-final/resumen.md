# Validación integrada final — 26/09/2026 CLT, 27/09/2026 CEST

Pruebas efectuadas después de corregir las fallas de la auditoría. Los comandos, salidas y capturas originales están en `../10-revision/`. Se utilizó conexión SSH no interactiva y túnel SOCKS para credenciales web; SELinux permaneció Enforcing. No hubo reinicio ni apagado del VPS.

| Actividad | Resultado observado | Evidencia final |
|---|---|---|
| Entorno | AlmaLinux 9.8, ens18 200.13.5.39/26, Enforcing y salida HTTP/2 200 posterior al despliegue. | `../10-revision/solucion-entorno.png` |
| Usuarios | Tres cuentas CMS; tres public_html de propietario individual y modo 755; HOME root:root para chroot. | `../02-usuarios/usuarios-directorios.txt`; `../10-revision/solucion-web.png` |
| MariaDB/PowerDNS | MariaDB solo 127.0.0.1; zona con 11 registros y 0 errores; A raíz/subdominios y MX confirmados desde cliente. | `../10-revision/solucion-dns.png`, `solucion-web.png`, `solucion-seguridad.png` |
| PowerAdmin | Login autenticado, zona visible, prueba temporal TXT servida por DNS; TXT retirado. | `../10-revision/poweradmin-zona.png`, `poweradmin-cambio-dns.txt`; DNS final en `solucion-dns.png` |
| Apache y 3 CMS | Web1/2/3 HTTP200; WordPress, Joomla y Grav con contenido público distinto. Joomla: artículo publicado; Grav: Markdown propio. | `../10-revision/web1-final.png`, `joomla-contenido-publico.png`, `web3-final.png`, `solucion-web.png` |
| FTP | Tres logins; cada usuario hizo subida y reemplazo con `226`, contenido nuevo visto HTTP200; salida de jaula 550; anónimo 530. | `../10-revision/solucion-ftp.png` y `.txt` |
| Correo | CMS1→CMS2 leído, CMS2→CMS1 respondido y leído en RoundCube. | `../10-revision/correo-02-recibido.png`, `correo-04-respuesta-recibida.png` |
| Firewall/SELinux | Nueve unidades activas; Enforcing; módulos locales presentes; MariaDB loopback. | `../10-revision/solucion-seguridad.png` y `.txt` |
| Chat | Dos sesiones consecutivas desde cliente local con envío y respuesta. | `../10-revision/solucion-chat.png` y `.txt` |

Límites declarados: HTTP y FTP públicos sin cifrado; certificado de correo autofirmado; cuenta adicional admin no demostrada; video solicitado por la pauta pendiente. Los PDF de `informe/latex/` contienen la explicación y la tabla integrada.
