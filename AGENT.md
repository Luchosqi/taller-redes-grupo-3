# Guía de trabajo del Grupo 3 — informe del taller de redes

Integrantes: Luis Jaramillo, Giovanny Toledo y Maximiliano Rivas.

Esta guía prepara el trabajo del Grupo 3; no acredita que una tarea se haya ejecutado. Antes de configurar servicios o redactar resultados, contrastar la actividad y la pauta vigentes en el Campus Virtual. Ningún servicio se considera instalado ni probado por aparecer aquí.

## Regla crítica de operación: PROHIBICIÓN DE REINICIAR O APAGAR EL VPS

> [!CAUTION]
> **APAGAR O REINICIAR LA VPS ESTÁ ESTRICTAMENTE PROHIBIDO BAJO CUALQUIER CONDICIÓN.**
> - Jamás ejecutar comandos de reinicio o apagado: `reboot`, `shutdown`, `poweroff`, `init 0`, `init 6`, `systemctl reboot`, `systemctl poweroff`.
> - Cualquier recarga de configuración o reactivación de servicios debe realizarse exclusivamente a nivel de servicio mediante `systemctl restart <servicio>` o `systemctl reload <servicio>`.
> - Para finalizar sesiones interactivas SSH, desconectarse siempre y únicamente con el comando `exit`.

## Parámetros y definiciones técnicas del Grupo 3

1. **Acceso al VPS y credenciales base:**
   - Grupo: 3.
   - Dominio asignado: `zorro-darwin.lazos.cl`.
   - Dirección IP: `200.13.5.39`.
   - Usuario de acceso inicial: `tredes3`.
   - Llave privada SSH: `~/Descargas/tredes3.key` (tipo Ed25519, permisos `600`, fuera del repositorio).
   - Administración: La contraseña del archivo de acceso permite `sudo`. Mantener contraseñas y llaves estrictamente fuera de git, informe y capturas.

2. **Nomenclatura obligatoria (según pauta oficial):**
   - **Usuarios locales (para los sitios):** `tredes3-cms1`, `tredes3-cms2`, `tredes3-cms3`.
   - **Estructura de contraseña de usuarios:** `CmsX_tRedeSN_WXYZ` (ejemplo para CMS 1: `Cms1_tRedeS3_A7K2`). Guardar valores reales en el archivo local de credenciales fuera del repositorio.
   - **Base de datos PowerDNS:** Nombre de base de datos `pdns_redes3`, usuario `dominio_pdns`, contraseña con formato `PdnsX_RedeSN_WXYZ` (ejemplo: `Pdns1_RedeS3_K9P2`). MariaDB debe mantenerse solo en localhost (`127.0.0.1`), prohibido exponerla a Internet.

3. **Subdominios y registros DNS mínimos:**
   - `web1.zorro-darwin.lazos.cl` (A -> `200.13.5.39`) -> CMS 1 (`tredes3-cms1`)
   - `web2.zorro-darwin.lazos.cl` (A -> `200.13.5.39`) -> CMS 2 (`tredes3-cms2`)
   - `web3.zorro-darwin.lazos.cl` (A -> `200.13.5.39`) -> CMS 3 (`tredes3-cms3`)
   - `mail.zorro-darwin.lazos.cl` (A -> `200.13.5.39`) y registro `MX` para `zorro-darwin.lazos.cl` apuntando a `mail.zorro-darwin.lazos.cl`
   - `webmail.zorro-darwin.lazos.cl` (A -> `200.13.5.39`) -> RoundCube
   - `dnsadmin.zorro-darwin.lazos.cl` (A -> `200.13.5.39`) -> PowerAdmin

4. **Definición de los tres CMS (diferenciables e independientes):**
   - **CMS 1 (`web1` / `tredes3-cms1`): WordPress.** Plataforma relacional en PHP sobre MariaDB. Implementación verificada: base `web1_db`, usuario `web1_user`, tablas `wp3_`. Los nombres `cms1_wp/cms1_user` pertenecían a la planificación inicial y no describen el VPS.
   - **CMS 2 (`web2` / `tredes3-cms2`): Joomla.** CMS relacional MVC en PHP sobre MariaDB. Implementación verificada: base `web2_db`, usuario `web2_user`, tablas `g3j_`. Los nombres `cms2_joomla/cms2_user` pertenecían a la planificación inicial.
   - **CMS 3 (`web3` / `tredes3-cms3`): Grav.** CMS moderno Flat-File en PHP que no requiere base de datos relacional (almacenamiento en archivos Markdown). Permite cumplir la condición de tres arquitecturas y CMS totalmente diferentes sin recargar MariaDB.

5. **Parámetros del servicio FTP (vsftpd):**
   - Paquete: `vsftpd`.
   - **Puerto de escucha de control:** **`2121/tcp`** (alternativo, obligatorio debido al bloqueo institucional del puerto 21 en la red UFRO).
   - **Rango de puertos pasivos:** **`30000-30100/tcp`** (`pasv_min_port=30000`, `pasv_max_port=30100`, `pasv_address=200.13.5.39`).
   - **Aislamiento implementado:** `chroot_local_user=YES`, `allow_writeable_chroot=NO`, `local_root=/home/$USER`; HOME `root:root 755` no escribible y `public_html` de cada CMS escribible por su propietario. La pauta exige jaula y escritura controlada, no el valor YES en esta opción.
   - **Acceso anónimo:** Deshabilitado estrictamente (`anonymous_enable=NO`).
   - Usuarios autorizados: `tredes3-cms1`, `tredes3-cms2`, `tredes3-cms3`, cada uno restringido a su HOME, con `public_html` como directorio web. CMS1 y CMS2 también pueden ver su propio Maildir dentro del HOME; no pueden acceder al sistema ni a otros sitios.
   - Cortafuegos: Abrir `2121/tcp` y `30000-30100/tcp` en `firewalld`.

6. **Servicio de correo electrónico y cuentas de prueba:**
   - MTA: Postfix + Acceso IMAP: Dovecot + Webmail: RoundCube.
   - Cuentas de prueba para validar el flujo completo (remitente -> destinatario -> envío -> recepción):
     - **Remitente:** `tredes3-cms1@zorro-darwin.lazos.cl`
     - **Destinatario:** `tredes3-cms2@zorro-darwin.lazos.cl`
     - (Buzón administrativo adicional `admin@zorro-darwin.lazos.cl`: previsto en el plan, no demostrado ni declarado como implementado en el informe).

7. **Aplicación cliente-servidor mediante sockets:**
   - **Ubicación local confirmada:** `/home/gtoledo/programacion/laboratorios/taller-redes/chat-texto`.
   - **Archivos:** `servidor.py`, `cliente.py`, `README.md`.
   - **Lenguaje y dependencias:** Python 3 (biblioteca estándar: `socket`, `threading`; no requiere librerías externas ni entornos virtuales).
   - **Protocolo:** TCP.
   - **Puerto:** **`9000/tcp`** (parámetro `PUERTO = 9000` en ambos scripts; requiere apertura en `firewalld` en el VPS).
   - **Despliegue:** El archivo `servidor.py` se transfiere al VPS y se deja en ejecución en background; el cliente `cliente.py` se ejecuta desde la máquina del alumno apuntando a `zorro-darwin.lazos.cl` (o `200.13.5.39`).

## Antes de trabajar en el VPS

1. Leer `REVISION_PAUTA_CAMPUS.md`, la pauta oficial (`/home/gtoledo/programacion/laboratorios/taller-redes/gio.txt`) y el estado actual del informe.
2. Confirmar por SSH el estado real del VPS sin ejecutar comandos destructivos ni de reinicio.
3. Respaldar cada archivo de configuración antes de modificarlo y descargar una copia local. Para bases de datos, guardar un volcado (`mysqldump`) previo.
4. Verificar que SSH siga disponible antes y después de cambios en el cortafuegos. No cerrar el puerto 22 ni detener `sshd`.
5. Mantener SELinux estrictamente en modo `Enforcing`. Prohibido deshabilitar o desinstalar SELinux. Resolver denegaciones con contextos (`semanage fcontext`, `restorecon`), booleanos (`setsebool -P`) o etiquetas de puerto (`semanage port`).
6. No cambiar la contraseña de la cuenta principal entregada para el VPS ni modificar `sshd_config`. MariaDB no debe quedar expuesta a Internet. Evitar permisos `777`, FTP anónimo y cualquier ajuste que rompa el aislamiento de los sitios.

## Informe y evidencias

El informe es el medio principal para evaluar el trabajo: debe poder entenderse sin una explicación oral posterior. Para cada actividad, explicar qué se hizo, cómo se implementó, qué decisiones técnicas se tomaron y por qué, qué evidencia permite comprobarlo y cuál fue el resultado de las pruebas. Cerrar con el estado real: cumplido, parcial o pendiente, indicando qué falta. Si algo solo está planificado, escribirlo como plan.

Usar salidas obtenidas por el Grupo 3 en su VPS. Cada figura debe tener una breve explicación en el texto o pie que indique qué acción o configuración se observa, qué objetivo cumple y qué resultado o requisito respalda. Una captura aislada no sustituye esa explicación. Agrupar comandos o procedimientos relacionados y escoger capturas representativas; no hace falta una imagen por comando ni existe una cantidad mínima. Evitar capturas repetidas o que no aporten evidencia nueva.

En LaTeX, citar figuras mediante `Figura~\ref{fig:...}` para que la numeración se actualice sola. Después de editar secciones o imágenes, compilar dos veces el documento maestro y revisar visualmente las páginas afectadas. Antes de entregar, quitar instrucciones internas, marcadores de plantilla y figuras de reserva.

Redactar en español claro, con frases directas y sin afirmaciones que no estén respaldadas por una prueba. Mantener nombres de variables, funciones, clases y comentarios de código en inglés si el proyecto incluye software.

## Credenciales y repositorio

No subir llaves privadas, contraseñas del VPS o sudo, tokens ni respaldos con secretos. El archivo de acceso existente contiene datos sensibles: antes de crear o publicar un repositorio, excluirlo del control de versiones y revisar también el historial. No copiar secretos al informe ni a las capturas. Las capturas deben ocultar contraseñas, claves, tokens y datos de autenticación.

Trabajar con Gitflow (`main`/`master`, `develop`, `feature/*`, `release/*`, `hotfix/*`). Hacer commits atómicos, con mensaje en español del tipo `tipo: descripción breve`. No añadir coautorías automáticas ni identificadores de sesión a los commits. Antes de publicar, revisar el diff, las rutas añadidas y que no haya secretos fuera de las excepciones aprobadas.

## Orden de trabajo sugerido

1. Preparar el VPS y documentar la línea base.
2. Crear usuarios y directorios de los sitios.
3. Configurar MariaDB, PowerDNS, la zona y PowerAdmin; probar DNS desde el VPS y otro equipo.
4. Publicar el servidor web y tres CMS distintos, cada uno con su cuenta y base de datos.
5. Revisar propietarios, permisos y SELinux antes de habilitar FTP.
6. Configurar correo, cortafuegos y aplicación de sockets; ejecutar pruebas individuales e integradas.
7. Terminar informe ejecutivo, informe técnico y video con el estado realmente alcanzado.

El orden se ajusta a la pauta del curso y a las dependencias del equipo. Nunca marcar una actividad como terminada solo porque sus comandos se ejecutaron: hacen falta configuración, prueba y evidencia.
