# Pruebas directas de la infraestructura — Grupo 3

Estado comprobado el 26/09/2026 por la noche en Chile (27/09 en el VPS, zona Europe/Madrid). Resumen con imágenes y resultados: `evidencias/11-validacion-final/resumen.md`. Usa las contraseñas del archivo local externo al repositorio; no las copies en terminales grabadas, capturas ni documentos. No apagar ni reiniciar el VPS. SELinux debe seguir `Enforcing`.

## 1. DNS desde tu computador

```bash
dig @200.13.5.39 zorro-darwin.lazos.cl A +short
dig @200.13.5.39 zorro-darwin.lazos.cl MX +short
for n in web1 web2 web3 mail webmail dnsadmin; do echo "$n: $(dig @200.13.5.39 "$n.zorro-darwin.lazos.cl" A +short)"; done
dig @1.1.1.1 zorro-darwin.lazos.cl A +short
```

Esperado: raíz y seis subdominios `200.13.5.39`; MX `10 mail.zorro-darwin.lazos.cl.`. Para verificar DNS por TCP añade `+tcp` al primer `dig`. Las respuestas directas deben tener autoridad de la zona. Evidencia: `evidencias/10-revision/solucion-dns.png`.

## 2. Tres sitios y PowerAdmin

Abrir en navegador:

- `http://web1.zorro-darwin.lazos.cl/`: WordPress, artículo «Zorro de Darwin: patrimonio del bosque templado».
- `http://web2.zorro-darwin.lazos.cl/`: Joomla, artículo «Conservación del bosque nativo en La Araucanía».
- `http://web3.zorro-darwin.lazos.cl/`: Grav, «Guía de hábitats de La Araucanía».
- `http://dnsadmin.zorro-darwin.lazos.cl/`: iniciar sesión, abrir la zona y comprobar A, NS y MX. No crear registros durante una revisión de lectura.

Para cotejar los VirtualHosts desde el VPS: `sudo httpd -S`; cada webN debe apuntar a su `public_html`. Las capturas finales están en `evidencias/10-revision/web1-final.png`, `joomla-contenido-publico.png`, `web3-final.png` y `poweradmin-zona.png` (esta última es anterior al A raíz; usa `dig` para el estado actualizado).

## 3. FTP con cada cuenta

En FileZilla: servidor `200.13.5.39`, puerto `2121`, modo pasivo, usuario `tredes3-cms1` y su contraseña externa. Repetir con cms2 y cms3.

1. Debe abrirse la raíz `/` de su jaula y existir `/public_html`.
2. Intentar entrar en `/etc` o en el HOME de otro CMS: debe responder 550.
3. Subir a `/public_html` un archivo de texto nuevo con un nombre único; abrir `http://webN.zorro-darwin.lazos.cl/<archivo>`.
4. Cambiar el texto, subir el mismo archivo y actualizar el navegador sin caché. Debe verse la nueva versión.
5. Intentar acceso `anonymous`: debe responder 530.

No sustituir archivos del CMS. La prueba automatizada ya hizo estos cinco pasos con los tres usuarios y obtuvo seis transferencias `226` y seis lecturas HTTP200 con contenido idéntico: `evidencias/10-revision/solucion-ftp.png`. Los archivos `prueba-grupo3-cmsN.txt` de versión 2 quedan como muestra pública verificable.

## 4. Correo por RoundCube

El sitio `http://webmail.zorro-darwin.lazos.cl/` aún usa HTTP. Para ingresar credenciales desde el equipo local mediante túnel cifrado, inicia en una consola:

```bash
ssh -i ~/Descargas/tredes3.key -N -D 127.0.0.1:1088 tredes3@200.13.5.39
```

Configura el navegador con proxy SOCKS5 `127.0.0.1:1088` y resolución DNS por SOCKS. Abre RoundCube y entra como `tredes3-cms1@zorro-darwin.lazos.cl` (contraseña de cms1). Envía un mensaje de asunto único a `tredes3-cms2@zorro-darwin.lazos.cl`; entra como CMS2, abre el mensaje, responde, vuelve a CMS1 y abre la respuesta. Confirmar remitente, asunto, fecha y cuerpo en las vistas de lectura. La prueba previa quedó capturada en `correo-02-recibido.png` y `correo-04-respuesta-recibida.png` de `evidencias/10-revision/`. La consola de túnel es solo reenvío SSH, no una sesión interactiva. Para revisión de estado en el VPS: `sudo systemctl is-active postfix dovecot` y `sudo ss -lnt | grep -E ':(25|993)[[:space:]]'`.

## 5. Servidor y seguridad

Accede por SSH, sin incluir contraseñas en comandos:

```bash
ssh -i ~/Descargas/tredes3.key tredes3@200.13.5.39
```

En el VPS:

```bash
date -Is
getenforce
systemctl is-active mariadb pdns httpd php-fpm vsftpd postfix dovecot firewalld chat-texto
sudo firewall-cmd --list-services
sudo firewall-cmd --list-ports
sudo ss -lnt | grep -E ':(3306|2121|9000)[[:space:]]'
sudo semodule -l | grep -E 'ftpd_httpd_content|roundcube_http_mail'
```

Esperado: Enforcing, nueve líneas `active`, SSH/HTTP/DNS/SMTP/IMAPS/FTP pasivo/chat habilitados, MariaDB solo en `127.0.0.1:3306`. El módulo FTP y el de correo deben figurar. Cierra la sesión interactiva solo con:

```bash
exit
```

## 6. Aplicación de sockets

Desde la raíz del repositorio local:

```bash
python3 entrega/chat-texto/conectar.py --host 200.13.5.39 --port 9000
```

Escribe `Prueba de chat Grupo 3`. Desde una sesión SSH autorizada, responde con `printf 'Respuesta desde VPS\n' > /run/chat-texto/chat.stdin`. El cliente debe mostrar la respuesta; cierra el cliente y repite para comprobar una segunda sesión sin reiniciar el servicio. Evidencia de dos sesiones anteriores: `evidencias/10-revision/solucion-chat.png`. Instrucciones de entrega en `entrega/chat-texto/README.md`.

## Registro de cada comprobación

Anota fecha y zona horaria, origen, acción, esperado, obtenido y evidencia. Las capturas prueban el resultado que muestran, con explicación en el informe técnico. El video resumen de la pauta sigue como entregable pendiente y se puede grabar siguiendo este orden.
