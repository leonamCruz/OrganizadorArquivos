import os
import shutil


def moverArquivos(diretorio_origem, diretorio_destino):
    criaPastaSeNaoExiste(diretorio_destino)
    print('Acessando pasta.')
    print('Contando arquivos')
    contagemDeArquivos(diretorio_origem)

    for nome_do_arquivo in os.listdir(diretorio_origem):
        origem = os.path.join(diretorio_origem, nome_do_arquivo)

        if os.path.isfile(origem):
            extensao = os.path.splitext(nome_do_arquivo)[1].lower()
            destino = os.path.join(diretorio_destino, extensao[1:])
            print('Vai para a pasta: ' + destino)
            criaPastaSeNaoExiste(destino)
            shutil.move(origem, destino)
        elif os.path.isdir(origem) and not pastaTemMesmoNome(origem, diretorio_destino):
            destino = os.path.join(diretorio_destino, 'Pastas')
            print('Vai para a pasta: ' + destino)
            shutil.move(origem, destino)


def criaPastaSeNaoExiste(diretorio):
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)


def pastaTemMesmoNome(origem, destino):
    nome_pasta_origem = os.path.basename(origem)
    nome_pasta_destino = os.path.basename(destino)
    return nome_pasta_origem == nome_pasta_destino


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


if __name__ == '__main__':
    pastaOrigem = '/home/leonam/Downloads'
    pastaDestino = '/home/leonam/Downloads/Organizados'

    moverArquivos(pastaOrigem, pastaDestino)
