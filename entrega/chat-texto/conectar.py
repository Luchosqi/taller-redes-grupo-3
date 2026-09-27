#!/usr/bin/env python3
"""Ejecuta el cliente original del taller contra el VPS, sin editar el origen."""
import argparse
import cliente
parser = argparse.ArgumentParser(description='Chat TCP del Grupo 3')
parser.add_argument('--host', default='200.13.5.39', help='IP o nombre DNS del servidor')
parser.add_argument('--port', type=int, default=9000)
args = parser.parse_args()
cliente.SERVIDOR, cliente.PUERTO = args.host, args.port
cliente.main()
