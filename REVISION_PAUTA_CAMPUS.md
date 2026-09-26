# Revisión de pauta y preparación del Grupo 3

Esta lista de trabajo fue preparada por integrantes de otro grupo y se adapta como borrador para el Grupo 3. No es la pauta oficial ni demuestra avances. Contrastar cada requisito, puntaje, formato y entregable con la actividad y la pauta vigentes en el Campus Virtual UFRO; esas fuentes son la referencia para la entrega. No dar por confirmado el número de actividades ni los detalles de la tabla hasta hacer ese contraste.

## Datos por completar

- Grupo e integrantes: Grupo 3 — Luis Jaramillo, Giovanny Toledo y Maximiliano Rivas.
- Dominio, IP y usuario indicados en el archivo de acceso del Grupo 3: `zorro-darwin.lazos.cl`, `200.13.5.39`, `tredes3`. La autenticación indicada es mediante certificado; no transcribir contraseñas ni llaves aquí.
- Tres CMS elegidos y versión de cada uno: pendiente.
- Cuentas de correo para las pruebas: pendiente.
- Cliente de sockets: el usuario indicó que el código del grupo está en `/home/luchosqi/Documentos/Universidad/semestres/Semestre 6/Taller De Redes/5%infrome1/chat-texto`, fuera del repositorio; pendiente de inspección cuando se aborde esa actividad. Protocolo y puerto: pendientes de confirmar con la pauta.
- Fecha de entrega y formatos exigidos: verificar en el campus.

## Criterio para redactar y evaluar el informe

El informe técnico debe permitir entender y evaluar el trabajo sin depender de una explicación posterior. En cada actividad, describir qué se realizó, cómo se configuró o implementó, las decisiones técnicas y sus motivos, la evidencia que lo respalda y el resultado de las pruebas. Indicar con claridad si el requisito quedó cumplido, parcial o pendiente.

Las capturas respaldan el relato, pero no lo reemplazan. Acompañar cada figura con una breve explicación de lo que muestra, la configuración o acción realizada, su objetivo y el resultado que permite comprobar. Se pueden agrupar comandos y procedimientos relacionados y usar capturas representativas. No se exige un mínimo de imágenes; evitar las repetitivas y asegurar que, en conjunto, cubran las actividades evaluadas. Usar solo evidencias propias del Grupo 3 y ocultar credenciales.

## Cómo registrar el avance

Cambiar cada apartado de «pendiente» a «en curso» o «terminado» solo después de ejecutar y comprobar la actividad. Anotar la sección del informe, la prueba realizada y la evidencia que la respalda. Separar el estado del servicio del estado de su documentación: pueden ser distintos. Si una captura no tiene contexto, resultado o relación clara con un requisito, completar el relato antes de considerarla evidencia suficiente.

## Lista de verificación de trabajo (30 apartados del borrador heredado)

Los nombres y alcances de estos apartados son una guía provisional, no una transcripción verificada de la pauta oficial. Ajustarlos o eliminarlos si difieren de las instrucciones vigentes del Campus.

| N.º | Apartado | Qué debe revisar o demostrar el equipo |
|---:|---|---|
| 1 | Descripción general | Presentar el VPS, el dominio asignado y el alcance del taller. Distinguir servicios previstos de servicios activos. |
| 2 | Objetivo general | Explicar la integración de DNS, web, correo, FTP y sockets en la infraestructura asignada. |
| 3 | Servicios requeridos | Inventariar los componentes y sus relaciones; no dar por implementado lo que solo aparece en un diagrama. |
| 4 | Regla de evidencia | Acompañar cada actividad con configuración, validación y resultado legibles. |
| 5 | Actividad 1: preparación inicial | Caracterizar el VPS, actualizarlo cuando corresponda e instalar herramientas de apoyo. Conservar la línea base anterior a los servicios. |
| 6 | Actividad 2: usuarios locales | Crear tres cuentas, sus HOME y `public_html`; comprobar UID, GID, propietarios y permisos. No cambiar la clave de la cuenta principal del VPS. |
| 7 | Actividad 3: DNS | Configurar PowerDNS, crear la zona y probar los registros A, NS, MX y los demás que exija el diseño, tanto local como externamente. Revisar la delegación pública. |
| 8 | Base de datos de PowerDNS | Crear la base y el usuario MariaDB con los nombres exigidos por la pauta. Comprobar el backend y limitar el acceso de la base. |
| 9 | Actividad 4: PowerAdmin | Instalar el panel, comprobar que puede ver y editar la zona, probar un cambio por DNS y documentar el resultado. Retirar registros temporales de prueba. |
| 10 | Actividad 5: servidor web | Instalar Apache y PHP, configurar los sitios y comprobar que cada nombre llega al VirtualHost correcto. Documentar PHP-FPM y HTTPS si se usan. |
| 11 | Actividad 6: tres CMS | Instalar tres CMS distintos. Para cada uno, registrar versión, usuario, ruta, base de datos, DNS, acceso al panel y contenido propio. |
| 12 | Actividad 7: FTP | Instalar `vsftpd`, asociar cada cuenta con su sitio y demostrar subida o modificación de archivos. |
| 13 | Configuración obligatoria de FTP | Deshabilitar el acceso anónimo, habilitar usuarios locales y escritura donde corresponda, configurar chroot, puerto alternativo y rango pasivo. Probar el aislamiento sin usar permisos `777`. |
| 14 | Actividad 8: correo | Configurar Postfix, Dovecot y RoundCube; comprobar DNS, autenticación, envío y recepción entre cuentas del dominio. |
| 15 | Actividad 9: firewall | Documentar los puertos realmente abiertos para SSH, DNS, web, correo, FTP y sockets. Probar conectividad y mantener MariaDB fuera del acceso público. |
| 16 | Actividad 10: SELinux | Mantener `Enforcing` y registrar contextos, booleanos o puertos ajustados. Si hay una denegación, explicar diagnóstico y corrección. |
| 17 | Actividad 11: sockets | Incorporar el programa cliente-servidor del equipo; indicar lenguaje, protocolo, puerto, forma de ejecución y prueba desde otro equipo. |
| 18 | Actividad 12: verificación integrada | Probar todos los servicios juntos, incluidos tres sitios, tres accesos FTP, correo, sockets, firewall y SELinux. |
| 19 | Problemas y soluciones | Registrar problemas reales con síntoma, causa, cambio aplicado y comprobación posterior. |
| 20 | Informe ejecutivo | Redactar al final un resumen comprensible del estado alcanzado, los resultados y las dificultades. |
| 21 | Informe técnico | Completar las secciones con datos del equipo, comandos relevantes, decisiones, pruebas y evidencias. Eliminar marcadores sin resolver. |
| 22 | Calidad de evidencias | Usar capturas legibles y pertinentes, con texto que explique qué se ve y qué requisito cumple. |
| 23 | Video resumen | Preparar el video cuando los servicios estén listos; mostrar las pruebas pedidas por la pauta y las dificultades principales. |
| 24 | Entregables | Comprobar informe ejecutivo, informe técnico, video, cliente de sockets con instrucciones y archivos adicionales que pida el docente. |
| 25 | Restricciones obligatorias | No desactivar SELinux, no permitir FTP anónimo, usar chroot, respetar nombres y evitar permisos inseguros. |
| 26 | Pauta de evaluación | Leer los puntajes vigentes y dedicar pruebas suficientes a los servicios de mayor peso. |
| 27 | Criterios generales de corrección | Revisar que configuración, prueba y evidencia coincidan con lo escrito en el informe. |
| 28 | Consideraciones sobre evidencias | No confundir una captura de un comando con una prueba de funcionamiento; mostrar el resultado observable. |
| 29 | Penalizaciones | Revisar CMS repetidos, FTP en el puerto equivocado, falta de chroot, permisos inseguros, SELinux deshabilitado y nombres inconsistentes. |
| 30 | Resultado esperado | Comparar la arquitectura prometida con los servicios activos y sus pruebas antes de entregar. |

## Inconsistencias y datos por confirmar

- El acceso SSH quedó verificado con la llave privada Ed25519 `~/Descargas/tredes3.key`, sin frase de paso y con permisos locales `600`. El campo `pass` del archivo de acceso fue aceptado por sudo para el usuario `tredes3`; corresponde a la contraseña de la cuenta para administración, no a la llave SSH. Mantener la llave y la contraseña fuera de Git, el informe y las capturas.
- Ese mismo archivo pide una contraseña de «16 dígitos» y luego especifica que sea alfanumérica y combine mayúsculas y minúsculas. Dígitos y caracteres alfanuméricos no significan lo mismo. Para crear usuarios nuevos, confirmar si la exigencia es de 16 caracteres alfanuméricos; no cambiar la clave de acceso entregada para el VPS.
- La lista de 30 apartados y varios detalles de configuración provienen del material de otro grupo. Verificar en Campus Virtual los nombres exactos, requisitos, restricciones, puntajes, formatos y entregables antes de tratarlos como obligatorios.
- Aún falta que el Grupo 3 defina y registre los tres CMS y las cuentas de correo para pruebas. El cliente de sockets ya existe fuera del repositorio, pero faltan inspeccionar su protocolo, puerto, dependencias y forma de ejecución, y contrastarlos con la pauta. No inventar datos ni presentar servicios como implementados.
- Los nombres del equipo y los datos de host consignados aquí provienen de la instrucción del usuario y del archivo `CredencialesdeACCESOVPSGRUPO3.md`, respectivamente. No se detectó en los otros Markdown un nombre de integrante o credencial contradictorios.

## Decisiones que no deben copiarse de otro equipo

La pauta puede fijar una plantilla para los nombres de la base, del usuario de PowerDNS y de las contraseñas. Aplicarla al dominio y al número de grupo propios; no trasladar valores ni iniciales ajenas. Elegir los tres CMS y registrar las cuentas de correo que se usarán en las pruebas. Para sockets, recuperar el programa desarrollado por el equipo antes de fijar puerto y protocolo en el informe.

El plan de firewall debe incluir SSH y solo los puertos que se ocupen. PowerAdmin y RoundCube usan el servidor web; MariaDB debe permanecer local. Antes de cambiar reglas, comprobar que el acceso SSH seguirá permitido.
