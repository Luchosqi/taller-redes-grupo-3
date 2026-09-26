# Línea base inicial del VPS

Consulta real por SSH a `200.13.5.39`, 26-09-2026 entre 06:06 y 06:09 CEST. Se ejecutaron consultas de solo lectura antes de modificar servicios. Este extracto textual complementa la bitácora; no contiene credenciales.

```text
$ hostname
localhost.localdomain

$ id
uid=1000(tredes3) gid=1000(tredes3) groups=1000(tredes3),10(wheel)

$ cat /etc/os-release
NAME="AlmaLinux"
VERSION="9.8 (Olive Jaguar)"
ID="almalinux"
VERSION_ID="9.8"
PRETTY_NAME="AlmaLinux 9.8 (Olive Jaguar)"

$ getenforce
Enforcing

$ systemctl --failed --no-pager
0 loaded units listed.

$ ss -tulpn (resumen)
udp  127.0.0.1:323
udp  [::1]:323
tcp  0.0.0.0:22
tcp  [::]:22
tcp  *:80

$ firewall-cmd --state
running

$ firewall-cmd --list-all (resumen)
public (active)
interfaces: ens18
services: cockpit dhcpv6-client http ssh
ports: 80/tcp

$ rpm -q mariadb-server bind pdns-server postfix dovecot vsftpd php
package mariadb-server is not installed
package bind is not installed
package pdns-server is not installed
package postfix is not installed
package dovecot is not installed
package vsftpd is not installed
package php is not installed
```

Interpretación: SSH y HTTP estaban escuchando; SELinux estaba activo en modo obligatorio. Apache ya se encontraba activo. El resto de los paquetes consultados aún no estaba instalado. La captura `pagina-prueba-almalinux.png` muestra el cuerpo de la página de bienvenida; el código HTTP fue 403 porque `welcome.conf` sirve `/.noindex.html` como página de error cuando no hay un índice en la raíz.
