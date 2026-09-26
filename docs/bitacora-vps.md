# Bitácora del VPS — Grupo 3

Registrar aquí las intervenciones reales. No incluir contraseñas, frases de paso, llaves, tokens ni contenido de archivos secretos. Guardar respaldos fuera del repositorio.

## Línea base

- Fecha/hora del VPS: 2026-09-26 06:09 CEST; zona `Europe/Madrid` (UTC+02:00), NTP activo.
- Sistema operativo: AlmaLinux 9.8; kernel y recursos detallados pueden registrarse antes de cambios.
- Host/IP asignados: `zorro-darwin.lazos.cl` / `200.13.5.39`; el nombre reportado por el sistema es `localhost.localdomain`.
- Acceso SSH verificado con `tredes3@200.13.5.39` y la llave local `~/Descargas/tredes3.key` (permisos `600`). El archivo permanece fuera del repositorio. Sudo acepta la contraseña del archivo de acceso; no registrar su valor.
- Usuario: `tredes3`, UID/GID 1000, miembro de `wheel`.
- SELinux: `Enforcing`.
- Firewall: `firewalld` activo; zona `public`, interfaz `ens18`, servicios permitidos `cockpit`, `dhcpv6-client`, `http` y `ssh`, además de `80/tcp` explícito.
- Puertos escuchando al momento de la consulta: TCP `22` y `80`; UDP `323` solo en loopback IPv4/IPv6.
- Servicios activos relevantes: `sshd`, `httpd` y `firewalld`; no había unidades fallidas.
- Paquetes consultados: Apache `2.4.62-13.el9_8.6` presente; `mariadb-server`, `bind`, `pdns-server`, `postfix`, `dovecot`, `vsftpd` y `php` no instalados.
- Recursos observados: 3.6 GiB RAM, 3.2 GiB swap, raíz de 28 GiB con 2.3 GiB usados.
- Estado de cambios: solo consultas de lectura; aún no se modificó la configuración del VPS.
- Respaldo inicial externo: pendiente antes de cualquier cambio.

## Registro de intervenciones

| Fecha y hora | Actividad | Cambio realizado | Respaldo | Prueba y resultado | Evidencia |
|---|---|---|---|---|---|
| 2026-09-26 06:06–06:18 CEST | Preparación / línea base | Ninguno; consultas de solo lectura por SSH | No aplica todavía | Login SSH y sudo confirmados; AlmaLinux 9.8, SELinux `Enforcing`; Apache responde con la página de bienvenida, no hay VirtualHosts nombrados y el dominio no resuelve desde el VPS | `evidencias/01-preparacion-vps/linea-base-inicial.md`, `apache-linea-base.txt`, `http-respuestas-comparadas.txt` y `pagina-prueba-almalinux.png` |

## Problemas y soluciones

| Síntoma | Causa comprobada | Solución aplicada | Verificación posterior |
|---|---|---|---|
| SSH ignoraba la llave con permisos `664` | OpenSSH exige que la llave privada no sea accesible por otros usuarios | Se cambiaron sus permisos locales a `600`, sin moverla | La conexión SSH funcionó con verificación estricta de host |
