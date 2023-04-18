import os
import shutil


def criar_diretorio(caminho):
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        print(f"Diretório '{caminho}' criado com sucesso!")
    else:
        print(f"Diretório '{caminho}' já existe.")


def criar_arquivo(caminho, conteudo):
    with open(caminho, 'w') as arquivo:
        arquivo.write(conteudo)
    print(f"Arquivo '{caminho}' criado com sucesso!")


def ler_arquivo(caminho):
    with open(caminho, 'r') as arquivo:
        conteudo = arquivo.read()
    print(f"Conteúdo do arquivo '{caminho}':\n{conteudo}")


def escrever_arquivo(caminho, conteudo):
    with open(caminho, 'a') as arquivo:
        arquivo.write(conteudo)
    print(f"Conteúdo adicionado ao arquivo '{caminho}'!")


def copiar_arquivo(origem, destino):
    shutil.copy2(origem, destino)
    print(f"Arquivo '{origem}' copiado para '{destino}'.")


def mover_arquivo(origem, destino):
    shutil.move(origem, destino)
    print(f"Arquivo '{origem}' movido para '{destino}'.")


def apagar_arquivo(caminho):
    os.remove(caminho)
    print(f"Arquivo '{caminho}' apagado.")


def apagar_diretorio(caminho):
    shutil.rmtree(caminho)
    print(f"Diretório '{caminho}' e seu conteúdo apagados.")


# Exemplo de uso
diretorio = 'meu_diretorio'
arquivo_origem = 'arquivo_origem.txt'
arquivo_destino = 'arquivo_destino.txt'

criar_diretorio(diretorio)
criar_arquivo(f'{diretorio}/{arquivo_origem}',
              'Conteúdo do arquivo de origem.')
ler_arquivo(f'{diretorio}/{arquivo_origem}')
escrever_arquivo(f'{diretorio}/{arquivo_origem}', '\nNova linha adicionada.')
ler_arquivo(f'{diretorio}/{arquivo_origem}')
copiar_arquivo(f'{diretorio}/{arquivo_origem}',
               f'{diretorio}/{arquivo_destino}')
apagar_arquivo(f'{diretorio}/{arquivo_origem}')
mover_arquivo(f'{diretorio}/{arquivo_destino}',
              f'{diretorio}/{arquivo_origem}')
apagar_diretorio(diretorio)
