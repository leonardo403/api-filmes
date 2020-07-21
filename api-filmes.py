import requests
import json


def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=d17ba54b&s='+titulo+'&type=movie')
        dicionario = json.loads(req.text)
        return dicionario
    except SystemError:
        print("Erro:")
        return None

def imprimir_filme(filme):
    print('Titulo: ', filme['Title'])
    print('Atores: ', filme['Actors'])
    print('Diretor:', filme['Director'])
    print('Ano:', filme['Year'])
    print('Nota:', filme['imdbRating'])
    print('Premios: ',filme['Awards'])
    print('Poster: ',filme['Poster'])
    print('\n')

sair = False
while not sair:
    op = input("Digitar nome do filme ou SAIR para fechar: ")

    if op == 'SAIR':
        sair = True
        print("Saindo.....")
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print("Filme nao encontrado.")
        else:
            imprimir_filme(filme)