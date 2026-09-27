"""Adaptación del servidor del equipo: una conexión a la vez, con reconexión.

La entrada estándar conserva el chat manual; systemd la conecta a un FIFO.
El hilo receptor avisa del cierre para liberar la sesión y aceptar otra.
"""
import select
import socket
import sys
import threading

HOST = '0.0.0.0'
PORT = 9000
MAX_LENGTH = 1000

def receive_messages(connection, finished):
    try:
        while not finished.is_set():
            data = connection.recv(1024)
            if not data:
                print('Cliente desconectado; sesión liberada.', flush=True)
                break
            try:
                print('Cliente: ' + data.decode('utf-8'), flush=True)
            except UnicodeDecodeError:
                print('Mensaje descartado: UTF-8 inválido.', flush=True)
    except OSError as error:
        print('Conexión terminada: ' + str(error), flush=True)
    finally:
        finished.set()

def handle_client(connection):
    finished = threading.Event()
    receiver = threading.Thread(target=receive_messages, args=(connection, finished), daemon=True)
    receiver.start()
    try:
        while not finished.is_set():
            ready, _, _ = select.select([sys.stdin], [], [], 0.25)
            if not ready:
                continue
            line = sys.stdin.readline()
            if not line:
                finished.wait(0.25)
                continue
            message = line.strip()
            if not message:
                continue
            if len(message) > MAX_LENGTH:
                print('Mensaje descartado: máximo 1000 caracteres.', flush=True)
                continue
            connection.sendall(message.encode('utf-8'))
            print('Servidor: ' + message, flush=True)
    except OSError as error:
        print('Error de envío: ' + str(error), flush=True)
    finally:
        finished.set()
        try:
            connection.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        connection.close()
        receiver.join(timeout=1)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((HOST, PORT))
        listener.listen(1)
        print(f'Esperando conexiones en {HOST}:{PORT}', flush=True)
        try:
            while True:
                connection, address = listener.accept()
                print(f'Cliente conectado desde {address[0]}:{address[1]}', flush=True)
                handle_client(connection)
        except KeyboardInterrupt:
            print('Servidor finalizado por el operador.', flush=True)

if __name__ == '__main__':
    main()
