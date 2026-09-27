import socket
import threading

SERVIDOR = "127.0.0.1"
PUERTO = 9000
LONGITUD_MAXIMA = 1000


def recibir_mensajes(conexion: socket.socket, nombre: str) -> None:
    while True:
        try:
            datos = conexion.recv(1024)
            if not datos:
                print("\nLa conexión fue cerrada por el otro extremo.")
                break
            try:
                mensaje = datos.decode("utf-8")
                print(f"{nombre}: {mensaje}")
            except UnicodeDecodeError:
                print("Mensaje recibido descartado: codificación UTF-8 no válida.")
        except OSError:
            break


def enviar_mensajes(conexion: socket.socket) -> None:
    while True:
        try:
            mensaje = input().strip()
            if not mensaje:
                continue
            if len(mensaje) > LONGITUD_MAXIMA:
                print(f"Error: el mensaje supera el límite de {LONGITUD_MAXIMA} caracteres.")
                continue
            conexion.sendall(mensaje.encode("utf-8"))
        except (OSError, EOFError):
            break


def main() -> None:
    conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        conexion.connect((SERVIDOR, PUERTO))
        print(f"Conectado al servidor {SERVIDOR}:{PUERTO}")

        hilo_recepcion = threading.Thread(
            target=recibir_mensajes,
            args=(conexion, "Servidor"),
            daemon=True,
        )
        hilo_recepcion.start()

        enviar_mensajes(conexion)

    except ConnectionRefusedError:
        print(f"No se pudo conectar al servidor {SERVIDOR}:{PUERTO}. Conexión rechazada.")
    except OSError as error:
        print(f"Error al conectar con el servidor: {error}")
    except KeyboardInterrupt:
        print("\nCliente finalizado por el usuario.")
    finally:
        conexion.close()


if __name__ == "__main__":
    main()
