# Guía de trabajo del Grupo 3 — informe del taller de redes

Integrantes: Luis Jaramillo, Giovanny Toledo y Maximiliano Rivas.

Esta guía prepara el trabajo del Grupo 3; no acredita que una tarea se haya ejecutado. Antes de configurar servicios o redactar resultados, contrastar la actividad y la pauta vigentes en el Campus Virtual. Ningún servicio se considera instalado ni probado por aparecer aquí.

## Datos que debe definir el equipo

Datos confirmados en `CredencialesdeACCESOVPSGRUPO3.md`: Grupo 3, dominio `zorro-darwin.lazos.cl`, IP `200.13.5.39` y usuario `tredes3`. El archivo de acceso indica autenticación con certificado; el usuario informa que recibió por correo un archivo `tredes3.key`, que probablemente sea la llave privada SSH del grupo. Confirmar con el docente o probar el método indicado antes de usarla. No copiar ni publicar la llave, su frase de paso o la contraseña.

Completar cuando el equipo lo confirme: fecha de entrega, tres CMS y versiones, cuentas de correo de prueba, programa de sockets, protocolo y puerto. No copiar valores de otro grupo.

Guardar la llave SSH y las credenciales del VPS fuera del repositorio. Anotar dónde están los respaldos, quién puede acceder a ellos y cómo se recuperan. No pegar contraseñas en este archivo.

## Antes de trabajar en el VPS

1. Leer `REVISION_PAUTA_CAMPUS.md`, la pauta original y el estado actual del informe. Si ya existe un repositorio, comprobar `git status` y la rama activa. Si aún no existe, excluir primero el archivo de acceso y crear el repositorio sin secretos.
2. Confirmar por SSH el estado real del VPS. No reutilizar capturas, versiones, direcciones ni salidas de consola de otro equipo.
3. Respaldar cada archivo de configuración antes de modificarlo y descargar una copia. Para bases de datos, guardar un volcado previo cuando el cambio pueda afectar sus datos.
4. Verificar que SSH siga disponible antes y después de cambios en el cortafuegos. No cerrar el puerto 22 ni detener `sshd`.
5. Mantener SELinux en modo `Enforcing`. Resolver denegaciones con contextos, booleanos o etiquetas de puerto, dejando constancia de lo aplicado.

No cambiar la contraseña de la cuenta principal entregada para el VPS ni modificar `sshd_config` sin una instrucción expresa del responsable del equipo. MariaDB no debe quedar expuesta a Internet. Evitar permisos `777`, FTP anónimo y cualquier ajuste que rompa el aislamiento de los sitios.

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
