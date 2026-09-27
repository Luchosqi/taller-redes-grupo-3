# Estado de avance — Grupo 3

Actualizado: 2026-09-27 CEST. El detalle histórico de implementación siguiente conserva el orden de intervención; el dictamen vigente está arriba. Este documento permite que otro integrante o agente retome el trabajo sin repetir la inspección ni confundir el estado inicial con servicios implementados.

## Estado verificado tras correcciones — 27-09-2026 CEST

**Las pruebas integradas de los servicios solicitados se completaron.** FTP permite subir y modificar archivos de los tres usuarios dentro de sus jaulas; RoundCube entregó un mensaje de CMS1 a CMS2 y la respuesta de CMS2 a CMS1, ambos abiertos en navegador. WordPress, Joomla y Grav publican contenido distinto. DNS tiene A raíz y subdominios, MX y zona válida de 11 registros. El chat aceptó dos sesiones consecutivas. SELinux continúa Enforcing y no se reinició ni apagó el VPS.

- Informe técnico: `informe/latex/informe-tecnico.pdf` (14 páginas, portada UFRO y figuras explicadas).
- Informe ejecutivo: `informe/latex/informe-ejecutivo.pdf` (2 páginas, portada UFRO).
- Validación final y capturas: [resumen](evidencias/11-validacion-final/resumen.md), con transcripciones y capturas originales en `evidencias/10-revision/`.
- Instrucciones directas: [guía de pruebas](docs/guia-pruebas-manuales.md).
- Historial de fallas detectadas antes de estas correcciones: [auditoría](docs/auditoria-pendientes-2026-09-26.md).
- Pendiente fuera de la validación técnica: video resumen exigido por la pauta. La cuenta adicional `admin@` del plan inicial no fue demostrada. HTTP/FTP públicos y certificado de correo autofirmado son límites documentados.

## Estado actual

- Repositorio: `git@github.com:Luchosqi/taller-redes-grupo-3.git`, rama `main`.
- Último avance previamente publicado: `cc1e294` (`docs: registrar línea base real del VPS`). Este archivo está pendiente de commit y publicación.
- Integrantes: Luis Jaramillo, Giovanny Toledo y Maximiliano Rivas.
- VPS: `tredes3@200.13.5.39`; dominio asignado `zorro-darwin.lazos.cl`.
- SSH funciona con la llave local `~/Descargas/tredes3.key`, actualmente con permisos `600`. La llave y el archivo de credenciales están fuera del repositorio y no deben copiarse a GitHub.
- La contraseña de acceso se aceptó por sudo. No registrar ni pegar su valor.
- La línea base inicial se obtuvo con consultas de solo lectura, antes de los cambios registrados abajo.

## Implementación en curso

- Actividad 2 completada el 2026-09-26: existen `tredes3-cms1..3`, UID 1001–1003, contraseñas establecidas y `/home/tredes3-cmsX/public_html` modo `755` propiedad del usuario correspondiente. En Fase 4, cada HOME se cambió a `root:root 755` para cumplir chroot no escribible; detalle en `evidencias/05-ftp/validacion-vsftpd.txt`.
- Las credenciales de CMS, PowerDNS y correo se guardaron fuera del repositorio en `/home/gtoledo/Descargas/credenciales-taller-redes-grupo-3.txt`, modo `600`. No incorporarlas a capturas ni documentos.
- Fase 2 (Actividades 3 y 4) completada el 2026-09-26: MariaDB 10.11 solo en loopback, PowerDNS Authoritative 5.1.4 con backend MySQL, zona `zorro-darwin.lazos.cl` con diez registros y Poweradmin 4.3.5 en `dnsadmin`. Ver `evidencias/03-dns/validacion-dns-poweradmin.txt`. En Fase 6, las consultas autoritativas se validaron desde fuera por UDP y TCP; la zona resuelve también mediante el resolvedor público.
- Fase 3 (Actividades 5 y 6) completada el 2026-09-26: Apache sirve WordPress 7.1.2 (`web1`), Joomla 6.1.3 (`web2`) y Grav 2.2.1 (`web3`) mediante VirtualHosts; los tres sitios y sus rutas de administración respondieron. Ver `evidencias/04-web-y-cms/validacion-vhosts-cms.txt`.
- Fase 4 (Actividad 7) completada el 2026-09-26: vsftpd 3.0.5 en 2121/tcp con pasivo 30000–30100, anónimo bloqueado, chroot estricto para los tres CMS. Subida FTP a web1 visible por HTTP. Ver `evidencias/05-ftp/validacion-vsftpd.txt`.
- Fase 5 (Actividad 8) completada el 2026-09-26: Postfix/Dovecot reciben y entregan mensajes entre CMS1 y CMS2; RoundCube 1.7.4 en `webmail` autenticó por IMAP TLS y mostró la lista de correo. Ver `evidencias/06-correo/validacion-postfix-dovecot-roundcube.txt`. SMTP/25 e IMAPS/993 abiertos y probados desde fuera en Fase 6.
- Fase 6 (Actividades 9 y 10) completada el 2026-09-26: firewall limitado a servicios requeridos y puertos de DNS, SMTP, IMAPS y FTP; DNS verificado desde fuera por TCP/UDP. SELinux continúa Enforcing y las etiquetas persistentes se conciliaron con los archivos reales. Ver `evidencias/07-firewall-selinux/validacion-firewall-selinux.txt`.
- Fase 7 (Actividad 11) completada el 2026-09-26: servidor transferido y corriendo como unidad systemd `chat-texto`, puerto 9000/TCP abierto; conversación bidireccional probada desde el cliente local. Ver `evidencias/08-sockets/validacion-chat-tcp.txt`.
- Fase 8 (Actividad 12) completada el 2026-09-26: validación cruzada de todos los servicios, firewall, buzones, jaulas y sitios; resultados resumidos en `evidencias/09-pruebas-integradas/resumen-servicios.txt` y en la tabla del informe técnico.
- El informe técnico y el ejecutivo se actualizaron y compilaron a PDF en `informe/latex/`.

## Línea base comprobada

- AlmaLinux 9.8; nombre de host reportado: `localhost.localdomain`.
- SELinux está en `Enforcing`.
- `firewalld` está activo en la zona `public`, interfaz `ens18`. Permite `cockpit`, `dhcpv6-client`, `http` y `ssh`, más `80/tcp` explícito.
- Sockets observados: SSH `22/tcp`, HTTP `80/tcp` y Chrony `323/udp` limitado a loopback. No había unidades systemd fallidas.
- Apache `2.4.62-13.el9_8.6` está activo. No hay VirtualHosts nombrados y el directorio `/var/www/html` estaba vacío, propiedad `root:root`.
- Una petición HTTP a la raíz devolvió estado 403. La configuración de `welcome.conf` sirve `/.noindex.html` como página de error; la captura pública muestra la página de prueba de AlmaLinux. Esto prueba que Apache responde, pero no que exista un sitio del taller.
- Desde el VPS, `getent ahostsv4 zorro-darwin.lazos.cl` no devolvió direcciones.
- No están instalados `mariadb-server`, `bind`, `pdns-server`, `postfix`, `dovecot`, `vsftpd` ni `php`.
- Recursos observados: 3.6 GiB RAM, 3.2 GiB swap y raíz de 28 GiB, con 2.3 GiB usados. Zona horaria del VPS: `Europe/Madrid`, NTP activo.

## Archivos y evidencias

- `AGENT.md`: reglas de trabajo y resguardo; incluye cuándo inspeccionar e integrar el cliente de sockets.
- `REVISION_PAUTA_CAMPUS.md`: checklist cotejado con la pauta oficial `gio.txt`.
- `docs/bitacora-vps.md`: acceso y línea base.
- `informe/latex/informe-tecnico.tex` y `informe/latex/informe-ejecutivo.tex`: resumen de implementación y verificación final; PDFs generados localmente.
- `evidencias/01-preparacion-vps/linea-base-inicial.md`: resumen de comandos y resultados.
- `evidencias/01-preparacion-vps/apache-linea-base.txt` y `http-respuestas-comparadas.txt`: transcripciones de consultas reales.
- `evidencias/01-preparacion-vps/pagina-prueba-almalinux.png`: captura visual del servidor web antes de configurar los sitios.

## Checklist de cierre

1. [COMPLETADO] Pauta oficial cotejada y confirmada con `gio.txt`.
2. [COMPLETADO] Definidos los tres CMS (WordPress, Joomla, Grav), usuarios locales (`tredes3-cms1..3`), contraseñas con fórmula `CmsX_tRedeSN_WXYZ`, puertos FTP (2121 y rango 30000-30100) y cuentas de correo de prueba en `AGENT.md`.
3. [COMPLETADO] Programa de sockets localizado e inspeccionado en `/home/gtoledo/programacion/laboratorios/taller-redes/chat-texto` (Python 3, TCP 9000).
4. [COMPLETADO] MariaDB, PowerDNS, zona autoritativa y Poweradmin instalados y validados; evidencia en `evidencias/03-dns/validacion-dns-poweradmin.txt`.
5. [COMPLETADO] Apache y los tres CMS desplegados y comprobados; evidencia en `evidencias/04-web-y-cms/validacion-vhosts-cms.txt`.
6. [COMPLETADO] vsftpd configurado y comprobado; evidencia en `evidencias/05-ftp/validacion-vsftpd.txt`.
7. [COMPLETADO] Postfix/Dovecot/RoundCube desplegados y correo bidireccional comprobado; evidencia en `evidencias/06-correo/validacion-postfix-dovecot-roundcube.txt`.
8. [COMPLETADO] Firewall revisado y SELinux validado en Enforcing; evidencia en `evidencias/07-firewall-selinux/validacion-firewall-selinux.txt`.
9. [COMPLETADO] Chat TCP activo como servicio y conversación bidireccional probada; evidencia en `evidencias/08-sockets/validacion-chat-tcp.txt`.
10. [COMPLETADO] Pruebas integradas ejecutadas e informe técnico y ejecutivo compilados en PDF.

## Seguridad y continuidad

- No reiniciar, apagar ni ejecutar `reboot`, `poweroff` o `shutdown` para salir de la VPS. Las conexiones SSH usadas hasta ahora fueron comandos no interactivos y ya terminaron. Si se abre una sesión interactiva, desconectarse escribiendo únicamente `exit`.
- Mantener SSH en el puerto 22, no modificar `sshd_config` ni la contraseña principal sin autorización expresa, y mantener SELinux en `Enforcing`. Las sesiones SSH interactivas usadas se cerraron con `exit`.
- No copiar la llave, contraseña, certificados ni respaldos con secretos al repositorio, al informe o a capturas.
- No marcar actividades como cumplidas sin configuración aplicada, prueba observable y evidencia propia del Grupo 3.
