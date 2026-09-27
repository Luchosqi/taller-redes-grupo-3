# Auditoría de resultados y pendientes — Grupo 3

> **Documento histórico.** Registra el estado previo a las correcciones del 27-09-2026 CEST. A01 (FTP), A02/A03 (SMTP), A04 (Joomla/Grav), A05 (informes), A06 (A raíz), A09 (documentación del chat) y A11 (artefactos temporales) fueron atendidos. Las nuevas pruebas y límites actuales constan en `evidencias/11-validacion-final/resumen.md` y los PDF actualizados. A07/A08 se explican como diferencias de diseño; A10 conserva AVC históricos; el buzón adicional A12 no se demostró. El video de la pauta continúa pendiente. No usar el dictamen de esta fecha como estado final actual.

Fecha: 26 de septiembre de 2026, hora de Chile (UTC−03). El VPS usa Europe/Madrid: algunos registros muestran 27 de septiembre. No se cambió su reloj.

## Alcance y conclusión

Por instrucción del usuario, la etapa final se limita a inspección y documentación: **no se aplicaron nuevas correcciones después de esa instrucción**. Se revisaron la pauta, los informes, las evidencias anteriores, interfaces web y resultados reales. Se conservaron los PDF y sus fuentes sin reformularlos durante esta etapa.

**El taller no puede considerarse íntegramente validado:** FTP falla al subir archivos con las tres cuentas y RoundCube falla al enviar. Joomla y Grav no demuestran todavía el contenido diferenciado requerido. La declaración previa de actividades completadas queda sustituida por este dictamen. Un servicio activo o una respuesta HTTP 200 no acredita por sí solo el flujo funcional.

Las seis capturas `auditoria-*.png` de `evidencias/10-revision/` son fotografías reales de una ventana de terminal mediante captura de pantalla, con consultas de lectura ejecutadas por SSH. Sus archivos `.txt` contienen los comandos y salidas correspondientes. No son imágenes generadas ni reconstrucciones de resultados. Las imágenes de navegador se obtuvieron de páginas reales. Las consultas no apagaron ni reiniciaron el VPS; SELinux sigue Enforcing.

## Hallazgos priorizados

| ID | Prioridad / estado | Observación comprobada | Impacto y pendiente |
|---|---|---|---|
| A01 | Alta — falla abierta | En pruebas anteriores a la orden de detener reparaciones, los tres usuarios autenticaron por FTP, pero STOR devolvió `553 Could not create file`. Los logs conservan `FAIL UPLOAD` para CMS1, CMS2 y CMS3. | Actividad 7 incompleta: falta subir y modificar con cada cuenta y comprobar contenido por HTTP. Causa no establecida; no atribuirla a SELinux sin evidencia específica. |
| A02 | Alta — falla abierta | RoundCube autenticó y permitió redactar, pero al enviar mostró `Error SMTP (): Ha fallado la conexión al servidor`. El log registra `Connection refused` y `SMTP Error: Connection failed`. | Actividad 8 incompleta: falta envío, recepción y apertura efectiva mediante RoundCube en ambos sentidos. La entrega previa por comandos no sustituye esta prueba. |
| A03 | Alta — inconsistencia SMTP | Configuración local: `smtp_server=127.0.0.1`, `smtp_port=25`; archivo de valores predeterminados: `smtp_host=localhost:587`. Se observan listeners 25/143/993. | Hipótesis principal: opciones antiguas y destino efectivo incorrecto. Falta confirmar el valor consumido durante ejecución; no se editó la configuración. Véase `auditoria-correo`. |
| A04 | Alta — contenido incompleto | Joomla tiene cero filas en `web2_db.g3j_content`; su página pública carece de contenido de demostración. Grav conserva la página de bienvenida. | Actividad 6 necesita contenido diferenciable, evidencia pública y de administración/publicación. HTTP 200 solo confirma respuesta. |
| A05 | Alta — informes sobrestiman cierre | Ambos informes concluyen que la infraestructura quedó completada; la tabla integrada anterior no detectó las fallas A01/A02. | Los PDF actuales son borradores pendientes de revisión, no prueba de cumplimiento completo. No se corrigieron ni recompilaron en esta etapa. |
| A06 | Media — DNS/documentación | Consultas A al nombre raíz devuelven NOERROR sin respuesta A. Los subdominios sí tienen A. El técnico afirma que el A del dominio apunta a la IP. | Corregir posteriormente la discrepancia entre diseño, DNS e informe. No usar el nombre raíz como destino del cliente de chat mientras no resuelva A; usar la IP. |
| A07 | Media — trazabilidad | AGENT prevé `cms1_wp/cms1_user` y `cms2_joomla/cms2_user`; implementación usa `web1_db/web1_user` y `web2_db/web2_user`. Hay BD/usuario web3 aunque Grav es flat-file. | Documentar decisiones y recursos innecesarios; no borrar bases durante esta auditoría. |
| A08 | Media — FTP/diseño | Implementación: HOME root:root 755, `allow_writeable_chroot=NO`, raíz `/home/$USER`; AGENT contempla otra opción. CMS1/CMS2 ven también su propio Maildir. | Describir alcance real de la jaula y justificar decisión. No confundir confinamiento a HOME con confinamiento exclusivo a public_html. |
| A09 | Media — sockets/documentación | El informe dice que corre el servidor original. Antes de detener reparaciones se adaptó para liberar la sesión y aceptar reconexiones. Logs muestran dos sesiones consecutivas. | Documentar versión desplegada y diferencias con el original. Falta captura del cliente mostrando la respuesta y explicación del FIFO. |
| A10 | Media — seguridad/evidencia | SELinux Enforcing confirmado, pero existen AVC de httpd/php-fpm y otros procesos en el historial. | No afirmar “sin denegaciones” globalmente. Correlacionar por hora, acción y proceso. Esos eventos no prueban por sí solos la causa de FTP o SMTP. |
| A11 | Media — artefactos de prueba | Permanece TXT `_revision.zorro-darwin.lazos.cl` con valor `verificacion-grupo3`, creado desde PowerAdmin; existe `audit-upload-check.php` en web1 (restringido a loopback). | Limpieza pendiente expresamente registrada. No eliminados tras la orden de auditar solamente. La zona tiene un registro temporal adicional respecto de los diez originales. |
| A12 | Baja — alcance pendiente | No se demostró la cuenta adicional admin mencionada en AGENT. Delegación padre y NS del hijo usan nombres distintos; ambos apuntan al VPS según revisión previa. | Cotejar obligación real de admin con pauta y documentar la delegación. No declarar falla DNS solo por diferencia de nombres. |

## Cobertura por actividad y capturas necesarias

No se exige una cantidad fija de imágenes. Cada figura debe acreditar un resultado concreto, con explicación de acción, configuración, objetivo y resultado. Un fallo debe conservarse como fallo.

| Actividad | Estado que puede sostenerse | Evidencia disponible | Captura o comprobación aún necesaria |
|---|---|---|---|
| 1 Preparación | Línea base documentada | `01-preparacion-vps/`; bienvenida AlmaLinux | Explicar que la captura es anterior al despliegue y no representa el servicio final. |
| 2 Usuarios | Cuentas y directorios comprobados | `02-usuarios/`; `auditoria-servicios` | Agrupar identidad, HOME, propietarios y permisos. La nueva captura cubre public_html, no reemplaza toda la evidencia de cuentas. |
| 3 MariaDB y DNS | Backend y subdominios operativos; raíz sin A | `03-dns/`; `auditoria-dns`, `auditoria-servicios` | Tabla exacta SOA/NS/A/MX; escucha local BD; consulta externa UDP/TCP y aclaración del A raíz ausente. |
| 4 PowerAdmin | Acceso autenticado y creación TXT comprobados | `poweradmin-autenticado.png`, `poweradmin-zona.png`, `poweradmin-txt-prueba.png`, `poweradmin-cambio-dns.txt` | Incorporar al informe con explicación y dejar registrada limpieza pendiente del TXT. Login HTTP 200 anterior era insuficiente. |
| 5 Apache | VirtualHosts responden | `04-web-y-cms/`; capturas públicas web1..3 | Captura agrupada `httpd -S` + respuestas Host y explicación de DocumentRoot. |
| 6 CMS | Instalados; contenido aún incompleto | `web1-navegador.png`, `web2-navegador.png`, `web3-navegador.png`; `auditoria-ftp-cms` | WordPress necesita captura posterior al cambio de contenido; Joomla/Grav necesitan demostrar contenido propio y edición/publicación cuando se autorice resolver. |
| 7 FTP | Login/jaula observados; escritura falla | `05-ftp/` histórico; `auditoria-ftp-cms` actual | Por cada usuario: subida, modificación, lectura HTTP e intento de salir de jaula. No presentar la subida histórica de CMS1 como éxito actual de los tres. |
| 8 Correo | Backend con entrega histórica; login web; envío web falla | `06-correo/`; `correo-01-redaccion.png`, `correo-navegador.txt`, `auditoria-correo` | Error visual del envío; posteriormente mensaje abierto en CMS2 y respuesta abierta en CMS1, con asunto/fecha coincidentes. Redacción no acredita envío. |
| 9 Firewall | Reglas actuales visibles | `07-firewall-selinux/`; `auditoria-firewall` | Comparar runtime/permanente y justificar cada puerto y dhcpv6-client. Prueba externa de puertos requeridos y de exclusión de BD. |
| 10 SELinux | Enforcing y booleanos comprobados | `auditoria-firewall`; historial de contextos | Captura de contextos persistentes/efectivos y módulo local; correlación AVC con pruebas funcionales. No basta getenforce. |
| 11 Sockets | Dos sesiones registradas tras adaptación | `auditoria-chat`; `entrega/chat-texto/` | Cliente y servidor mostrando intercambio coincidente, instrucciones de FIFO y diferencias respecto del original. |
| 12 Integración | No aprobada integralmente | Evidencia histórica `09-pruebas-integradas/`, contradicha por hallazgos actuales | Repetir matriz después de futuras correcciones; incluir fecha, origen, esperado, obtenido y referencia. Hoy FTP y RoundCube deben figurar fallidos. |

## Revisión específica de los informes

### Técnico: `informe/latex/informe-tecnico.tex` y PDF

- Solo contiene una inclusión de imagen: bienvenida inicial de AlmaLinux (línea 54 de la fuente revisada). No muestra visualmente los resultados finales de todas las actividades.
- La sección Implementación y pruebas conserva texto de instrucción editorial (“En cada subsección explicar…”), línea 60.
- Arquitectura, línea 41: afirma un A raíz inexistente. Falta diagrama de arquitectura solicitado y plan de nombres con tipos/valores reales.
- Administración DNS, líneas 71–72: acredita HTTP 200, aunque inicialmente existía el bloqueo por instalador. Las capturas nuevas sí muestran administración autenticada; aún no están incorporadas.
- CMS, líneas 74–75: versiones/HTTP no acreditan publicación diferenciada ni todos los permisos de operación.
- FTP, líneas 77–78: éxito histórico de una cuenta; falta tres usuarios y el fallo actual contradice un cierre general.
- Correo, líneas 80–81: distingue entrega de backend y listado, pero no demuestra envío web completo. Debe registrar el error actual.
- Sockets, líneas 86–87: descripción de original sin modificar quedó desactualizada tras la adaptación previa a la orden de detener correcciones.
- Tabla integrada y conclusión, líneas 89–121: necesitan estados parciales/fallidos y trazabilidad por prueba.
- Faltan extractos de configuración sin secretos, comandos principales agrupados, decisiones técnicas suficientemente explicadas, análisis de resultados y referencias técnicas verificables. Enlaces a carpetas del repositorio no sustituyen contenido autosuficiente en el PDF.

### Ejecutivo: `informe/latex/informe-ejecutivo.tex` y PDF

- El resumen presenta tres CMS “diferenciados” sin demostrar contenido propio de Joomla/Grav.
- “Las actividades de infraestructura quedaron completadas”, línea 31, no representa los resultados actuales.
- Debe comunicar necesidades atendidas, solución, resultados confirmados, fallas abiertas y alcance pendiente, en lenguaje breve. No requiere replicar todas las capturas técnicas.

### Portada y entrega

El ejemplo UFRO indicado por el usuario fue localizado en Descargas. Se extrajo previamente el recurso `informe/latex/recursos/ufro.png`; **no se aplicó aún la portada a los PDF**. Queda pendiente cuando se autorice actualizar los informes. Revisar nombres, asignatura, docente y fecha real; no adoptar automáticamente los datos del ejemplo. También queda pendiente comprobar el video exigido por la pauta; no se produjo en esta revisión.

## Cambios realizados antes de la instrucción de solo auditar

Se registran para no confundir auditoría con ausencia total de intervenciones durante la conversación:

1. Retiro del directorio de instalación de PowerAdmin al respaldo; acceso autenticado comprobado.
2. ACL para Apache y contexto persistente de escritura en uploads de WordPress; prueba PHP local de crear/eliminar archivo exitosa. Cambio de título y artículo de WordPress.
3. Eliminación de cuentas anónimas MariaDB y base predeterminada test, con respaldo previo.
4. Adaptación del servidor de chat para reconectar; reinicio exclusivamente de `chat-texto`, dos conversaciones consecutivas comprobadas. Cliente original y adaptador local conservados en `entrega/chat-texto/`.
5. Diagnóstico temporal con dontaudit desactivado, luego restaurado. SELinux permaneció Enforcing; no se instaló una solución FTP.
6. Registro TXT y endpoint PHP temporales mencionados en A11.

Respaldos previos en VPS: `/home/tredes3/vps-backups/revision-20260926/`; copias externas locales: `/home/gtoledo/Descargas/respaldos-vps/revision-20260926/`. Contienen configuración/BD sensible y no deben incorporarse al repositorio. Documentos anteriores a esta anotación preservados temporalmente fuera del repositorio.

## Criterio de cierre futuro

Resolver A01/A02, completar contenido CMS y repetir los flujos completos antes de declarar cierre; conciliar documentación con configuración real; retirar artefactos de prueba cuando se autorice; incorporar figuras explicadas; actualizar ambos informes y revisar sus PDF. **Esta lista es trabajo pendiente, no una autorización ni una ejecución de soluciones.** Guía de comprobaciones: `docs/guia-pruebas-manuales.md`.
