# Cliente de chat TCP — Grupo 3

El servidor del taller funciona en el VPS `200.13.5.39`, puerto `9000/TCP`. Esta carpeta incluye el cliente original (`cliente.py`), un adaptador de conexión (`conectar.py`) y la versión del servidor desplegada (`servidor.py`). El original externo se conserva fuera del repositorio; el servidor desplegado fue adaptado para aceptar conexiones sucesivas.

Desde el equipo local, con Python 3 y sin dependencias adicionales:

```bash
python3 entrega/chat-texto/conectar.py --host 200.13.5.39 --port 9000
```

Escribir un mensaje y pulsar Enter. Para producir una respuesta desde el VPS, el integrante autorizado puede conectarse por SSH y escribir en el FIFO del servicio:

```bash
printf 'Respuesta desde el VPS\n' > /run/chat-texto/chat.stdin
```

El cliente mostrará `Servidor: Respuesta desde el VPS`. La prueba se puede repetir tras cerrar la primera conexión; la unidad `chat-texto` permanece activa. El servidor atiende una sesión a la vez. Terminar cualquier sesión SSH interactiva con `exit`. No apagar ni reiniciar el VPS.
