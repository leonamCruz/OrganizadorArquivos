import os
import shutil


def verificaSeNaoHaNadaNaPasta(diretorio):
    if len(os.listdir(diretorio)) == 0:
        print('Não há nada da pasta.')
        exit()


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

    return arquivos + pastas


def criaPastaSeNaoExiste(diretorio):
    if not os.path.exists(diretorio):
        print('Criando diretório')
        os.mkdir(diretorio)

def moverArquivos(diretorio_origem, diretorio_destino, qntdArquivos):
    lidos = 0
    listaArquivos = os.listdir(diretorio_origem)
    for nome_do_arquivo in listaArquivos:
        if len(listaArquivos) == 1 and nome_do_arquivo == os.path.basename(diretorio_destino):
            print('Só há a pasta de organizados.')
            exit()

        calculaPorcentagem(qntdArquivos, lidos)

        origem = os.path.join(diretorio_origem, nome_do_arquivo)

        if os.path.isfile(origem):
            extensao = os.path.splitext(nome_do_arquivo)[1].lower()
            destino = os.path.join(diretorio_destino, extensao[1:])
            print('Vai para a pasta: ' + destino)
            criaPastaSeNaoExiste(destino)
            shutil.move(origem, destino)
            lidos = lidos + 1

        elif os.path.isdir(origem) and not pastaTemMesmoNome(origem, diretorio_destino):
            destino = os.path.join(diretorio_destino, 'Pastas')
            print('Vai para a pasta: ' + destino)
            shutil.move(origem, destino)
            lidos = lidos + 1

    print('Concluído.')

def calculaPorcentagem(qntdArquivos, lidos):
    conta = (lidos / qntdArquivos) * 10000
    print(str(conta.__round__() / 100) + '%')

def pastaTemMesmoNome(origem, destino):
    nome_pasta_origem = os.path.basename(origem)
    nome_pasta_destino = os.path.basename(destino)
    return nome_pasta_origem == nome_pasta_destino


if __name__ == '__main__':
    diretorio_origem = '/home/leonam/Downloads'
    diretorio_destino = '/home/leonam/Downloads/Organizados'

    print('Acessando pasta.')
    print('Contando arquivos')
    verificaSeNaoHaNadaNaPasta(diretorio_origem)
    qntdArquivos = contagemDeArquivos(diretorio_origem)
    criaPastaSeNaoExiste(diretorio_destino)

    moverArquivos(diretorio_origem, diretorio_destino, qntdArquivos)
