import os
import shutil


def contagemDeArquivos(diretorio_origem):
    lista = os.listdir(diretorio_origem)
    arquivos = 0
    pastas = 0
    for daVez in lista:
        if os.path.isfile(os.path.join(diretorio_origem, daVez)):
            arquivos = arquivos + 1
        else:
            pastas = pastas + 1

    print('São ' + str(arquivos) + ' arquivos.')
    print('São ' + str(pastas) + ' pastas.')

def moverArquivos(diretorio_origem, diretorio_destino):
    criaPastaSeNaoExiste(diretorio_destino)
    print('Acessando pasta.')
    print('Contando arquivos')
    contagemDeArquivos(diretorio_origem)

    for nome_do_arquivo in os.listdir(diretorio_origem):
        origem = os.path.join(diretorio_origem, nome_do_arquivo)
        print(origem)
        if os.path.isfile(origem):
            extensao = os.path.splitext(nome_do_arquivo)[1].lower()
            destino = os.path.join(diretorio_destino, extensao[1:])
            print('Vai para a pasta: ' + destino)
            criaPastaSeNaoExiste(destino)
            shutil.move(origem, destino)
        else:
            destino = os.path.join(diretorio_destino, 'Pastas')
            criaPastaSeNaoExiste(destino)
            shutil.move(origem, destino)


def criaPastaSeNaoExiste(diretorio_destino):
    if not os.path.exists(diretorio_destino):
        os.mkdir(diretorio_destino)


if __name__ == '__main__':
    pastaOrigem = '/home/leonam/Downloads'
    pastaDestino = '/home/leonam/Downloads/Organizados'

    moverArquivos(pastaOrigem, pastaDestino)
