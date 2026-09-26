# Estado de avance — Grupo 3

Actualizado: 2026-09-26. Este documento permite que otro integrante o agente retome el trabajo sin repetir la inspección ni confundir el estado inicial con servicios implementados.

## Estado actual

- Repositorio: `git@github.com:Luchosqi/taller-redes-grupo-3.git`, rama `main`.
- Último avance previamente publicado: `cc1e294` (`docs: registrar línea base real del VPS`). Este archivo está pendiente de commit y publicación.
- Integrantes: Luis Jaramillo, Giovanny Toledo y Maximiliano Rivas.
- VPS: `tredes3@200.13.5.39`; dominio asignado `zorro-darwin.lazos.cl`.
- SSH funciona con la llave local `~/Descargas/tredes3.key`, actualmente con permisos `600`. La llave y el archivo de credenciales están fuera del repositorio y no deben copiarse a GitHub.
- La contraseña del archivo de acceso fue aceptada por sudo. No registrar ni pegar su valor.
- Se hicieron consultas de solo lectura. No se cambió configuración ni se instaló servicio alguno en el VPS.

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
- `REVISION_PAUTA_CAMPUS.md`: checklist heredado de otro grupo, aún debe cotejarse con la pauta oficial.
- `docs/bitacora-vps.md`: acceso y línea base.
- `informe/latex/informe-tecnico.tex`: ya describe la línea base e incluye la figura de la página de prueba.
- `informe/latex/informe-ejecutivo.tex`: plantilla vacía para completar al final.
- `evidencias/01-preparacion-vps/linea-base-inicial.md`: resumen de comandos y resultados.
- `evidencias/01-preparacion-vps/apache-linea-base.txt` y `http-respuestas-comparadas.txt`: transcripciones de consultas reales.
- `evidencias/01-preparacion-vps/pagina-prueba-almalinux.png`: captura visual del servidor web antes de configurar los sitios.

## Pendientes antes de modificar servicios

1. Cotejar la lista heredada con la actividad y pauta vigentes del Campus Virtual.
2. Definir los tres CMS y las cuentas/nombres de usuario para usuarios locales, FTP y correo.
3. Inspeccionar el cliente de sockets ya desarrollado por el grupo en la ubicación local informada: `/home/luchosqi/Documentos/Universidad/semestres/Semestre 6/Taller De Redes/5%infrome1/chat-texto`. Aún no se ha inspeccionado, copiado ni ejecutado. Al llegar a esa actividad, identificar lenguaje, protocolo, puerto, dependencias y uso; integrar solo lo necesario y documentar cómo se ejecuta.
4. Crear un respaldo local fuera del repositorio antes de modificar cada archivo de configuración del VPS.
5. Instalar y compilar con LaTeX cuando haya un motor disponible. En este entorno no se encontró `pdflatex`, `latexmk`, `tectonic`, `xelatex` ni `lualatex`; el intento local de instalar TeX fue interrumpido. No había proceso `apt-get`/`dpkg` activo al retomar. No se afectó el VPS.

## Seguridad y continuidad

- No reiniciar, apagar ni ejecutar `reboot`, `poweroff` o `shutdown` para salir de la VPS. Las conexiones SSH usadas hasta ahora fueron comandos no interactivos y ya terminaron. Si se abre una sesión interactiva, desconectarse escribiendo únicamente `exit`.
- Mantener SSH en el puerto 22, no modificar `sshd_config` ni la contraseña principal sin autorización expresa, y mantener SELinux en `Enforcing`.
- No copiar la llave, contraseña, certificados ni respaldos con secretos al repositorio, al informe o a capturas.
- No marcar actividades como cumplidas sin configuración aplicada, prueba observable y evidencia propia del Grupo 3.
