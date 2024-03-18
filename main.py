import os
import argparse
from art import tprint

"""
if __name__ == '__main__':
    os.system('uvicorn app:app --reload')
"""

def main(args):
    tprint('Oficina - Data Mining - Deploy')

    # Diretório onde main.py está localizado
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Diretório da subpasta que contém app.py
    app_directory = os.path.join(current_directory, "Aula_Deploy", "Git-API-13032024")

    # Comando para iniciar o Uvicorn com o módulo app
    os.system(f'uvicorn app:app --reload --app-dir "{app_directory}"' )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='API Oficina')
    parser.add_argument('--port', type=str, dest='port', help='Port ', default='5000')
    main(parser.parse_args())

