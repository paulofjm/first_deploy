import os

if __name__ == '__main__':
    # Obtém o diretório atual
    current_directory = os.getcwd()
    print("Diretório atual:", current_directory)

    # Lista os arquivos no diretório atual
    files_in_directory = os.listdir(current_directory)
    print("Arquivos no diretório atual:")
    for file in files_in_directory:
        print(file)