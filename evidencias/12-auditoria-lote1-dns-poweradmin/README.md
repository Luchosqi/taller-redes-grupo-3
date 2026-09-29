# Lote 1: PowerDNS, base de datos y PowerAdmin

Pruebas realizadas el 28-09-2026 desde el cliente `home` (Chile, UTC-03) y por SSH en el VPS `200.13.5.39` (Europe/Madrid, UTC+02). Los archivos `terminal-*.txt` son **salidas de comandos ejecutados**, con fecha, origen, comando y código de salida. `terminal-cliente-resumen.png` y `terminal-vps-resumen.png` son capturas de una terminal Xterm mientras ejecutaba consultas nuevas; el texto completo está en las transcripciones. Las imágenes `poweradmin-*.png` son capturas de una ventana real de Chrome con la URL visible, conectada a PowerAdmin mediante un túnel SOCKS5 por SSH. Ninguna imagen contiene contraseñas.

## Resultado breve

| Prueba | Esperado | Obtenido | Conclusión |
|---|---|---|---|
| Delegación padre y zona hija | Ambos caminos llegan al VPS y la zona hija publica NS/SOA | Padre: `zorro-darwin-ns.lazos.cl` con A `200.13.5.39`; hija: `ns1.zorro-darwin.lazos.cl` con A `200.13.5.39`; SOA servido con autoridad | Los nombres NS difieren, pero ambos apuntan al mismo servidor. La resolución funciona; no se alteró la delegación. |
| A raíz y nombres publicados | `200.13.5.39` desde PowerDNS y un recursor | Raíz, `ns1`, `web1` a `web3`, `mail`, `webmail` y `dnsadmin` responden con esa IP; 1.1.1.1 coincide | Zona accesible por nombres operativos. |
| MX y destino | MX 10 a `mail`, cuyo A existe | MX `10 mail.zorro-darwin.lazos.cl`; A de `mail` a `200.13.5.39` | Destino DNS del correo resuelve. |
| UDP/TCP 53 y firewall | Respuesta autoritativa por ambos transportes; reglas permanentes | `dig` UDP/TCP con respuesta y bandera `aa`; `pdns` activo en `0.0.0.0:53`; 53/TCP y 53/UDP en reglas runtime y permanentes | Servicio publicado y reglas concordantes. |
| Zona, backend y base | Zona válida; `pdns_redes3` en MariaDB local; usuario acotado | 11 registros, 0 errores/avisos; `launch=gmysql`, base `pdns_redes3`, cuenta `dominio_pdns@127.0.0.1` con privilegios sobre esa base y `USAGE` global; MariaDB en `127.0.0.1:3306` | Configuración y datos coinciden. La contraseña aparece únicamente como `[OCULTA]` en la transcripción. |
| PowerAdmin crea TXT | Alta visible en la interfaz y en DNS autoritativo | Formulario y tabla con URL capturados; `dig` devolvió el TXT creado | La edición web llegó a la base y al DNS después de purgar la respuesta negativa en caché. |
| PowerAdmin elimina TXT | La zona vuelve a 11 registros y el TXT deja de responder | Borrado desde la interfaz; tabla final con 11 filas capturada; `dig` devolvió `NXDOMAIN` tras purga; cuenta temporal retirada | La zona quedó sin artefactos temporales de esta prueba. |

El nombre de la delegación publicada por el padre y el NS declarado por la zona hija no son iguales. La respuesta del padre incluye una dirección para su NS y el A de `ns1` existe dentro de la zona hija; ambos llevan a `200.13.5.39`. Esto no demuestra una falla de resolución. Conviene conservar la explicación en el informe antes de usar una captura como prueba final.

## Secuencia de PowerAdmin y caché

Antes de editar se creó un volcado de `pdns_redes3` en `/home/tredes3/vps-backups/auditoria-lote1-20260928-172254/` y una copia privada en `~/Descargas/respaldos-vps/auditoria-lote1-20260928-172254/`. Ambos archivos están fuera de Git, modo `600`, con SHA-256 idéntico. No se modificó ningún archivo de configuración.

Para acceder a la interfaz se creó una cuenta administradora temporal en la base después del respaldo. La contraseña temporal se mantuvo fuera del repositorio. Desde PowerAdmin se añadió `_auditoria-g3-20260928.zorro-darwin.lazos.cl` como TXT con TTL 300, se comprobó por `dig`, se eliminó desde la misma interfaz y se comprobó su ausencia. La cuenta temporal se borró después: una fila eliminada, cero remanentes.

El TXT aparecía en PowerAdmin y en MariaDB, pero una consulta anterior al alta había dejado una respuesta `NXDOMAIN` en la caché de PowerDNS. `pdns_control purge _auditoria-g3-20260928.zorro-darwin.lazos.cl` retiró esa entrada y el TXT respondió. Tras borrarlo, una respuesta positiva siguió sirviéndose hasta repetir la purga del mismo nombre. Esta fue una acción sobre caché, sin reinicio del VPS ni cambio de configuración. El SOA pasó de serial `2026092602` a `2026092801` por las ediciones realizadas en PowerAdmin; los demás registros operativos conservaron sus nombres y destinos.

La primera captura de la tabla final se descartó porque el navegador aún mostraba un fotograma anterior. `poweradmin-zona-final-completa.png` se obtuvo después de abrir de nuevo la zona: se comprobaron 11 filas y ningún TXT temporal. La captura de la confirmación de borrado también se descartó por ese retraso visual; la selección del único registro temporal se verificó antes de confirmar, y el borrado quedó corroborado por la tabla final, MariaDB y `dig`.

La captura inicial de la tabla era idéntica a la final a nivel de píxeles: muestra los mismos 11 registros y la parte visible del SOA no incluye el serial que cambió. Se descartó la copia redundante. La tabla final no prueba por sí sola el momento del borrado; para ese cambio se usan la captura intermedia de 12 registros, las consultas y el conteo SQL.

## Archivos

- `terminal-cliente-dns.txt`: delegación de ambos servidores padre, NS/SOA, A, MX, recursor, UDP y TCP.
- `terminal-cierre-externo.txt`: repetición de 25 consultas desde el cliente después de retirar el TXT y purgar la caché.
- `terminal-vps-dns-base.txt`: `pdns`, escucha, firewall, zona, MariaDB, registros, backend y permisos sin contraseña.
- `terminal-poweradmin-txt.txt`: TXT visible, borrado, respuestas de `dig` y purgas de caché.
- `terminal-cierre.txt`: zona y registros finales, cuenta temporal ausente y servicio activo.
- `terminal-cliente-resumen.png`, `terminal-vps-resumen.png`: capturas completas de terminal durante consultas nuevas.
- `terminal-cliente-resumen-recorte.png`, `terminal-vps-resumen-recorte.png`: recortes usados en el informe y el video. El recorte del VPS omite la invocación local y conserva la salida remota; los originales se mantienen intactos.
- `poweradmin-txt-formulario.png`, `poweradmin-txt-creado.png`, `poweradmin-zona-final-completa.png`: interfaz real con URL visible y 12 y 11 registros en las etapas verificables.

El informe técnico y el video usan los recortes indicados; las capturas completas y transcripciones originales permanecen disponibles para auditoría. No comprobamos la contraseña de la cuenta `admin` preexistente; la operación de PowerAdmin se ensayó con la cuenta temporal descrita arriba. La captura del clic de confirmación del borrado se descartó por mostrar un fotograma anterior; el borrado está documentado por la tabla final, MariaDB y `dig`.
