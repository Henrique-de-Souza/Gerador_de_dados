from listas import *
from time import sleep
import random


# estilização de linhas
def linha():
    print('-' * 50)

def cabecalho(mensagem):
    print('-' * 90)
    print()
    print(mensagem.center(90))
    print()
    print('-' * 90)


# Sorteando os valores de cada lista 
def sorteio_nome():
    nome_sorteado  = random.choice(nomes)
    return (nome_sorteado)


def sorteio_email():
    email_sorteado = random.choice(emails)
    return email_sorteado


def sorteio_telefone():
    telefone_sorteado = random.choice(telefones)
    return telefone_sorteado


def sorteio_cidade():
    cidade_sorteada = random.choice(cidades)
    return cidade_sorteada


def sorteio_estado():
    estado_sorteado = random.choice(estados)
    return estado_sorteado


# funcao para a logica do menu  ------------------------------------------------------------
def opcao_usuario(menu):

    opcoes = menu.split(',')

    for opcao in opcoes:
        opcao = opcao.strip()

        if opcao == '1':
            print(f'- O nome gerado foi: {sorteio_nome()}')
            

        elif opcao == '2':
            print(f'- O email gerado foi: {sorteio_email()}')
            
        elif opcao == '3':
            print(f'- O telefone gerado foi: {sorteio_telefone()}')
            

        elif opcao == '4':
            print(f'- A cidade gerada foi: {sorteio_cidade()}')
            

        elif opcao == '5':
            print(f'-O estado gerado foi: {sorteio_estado()}')

        else:
            print()
            print(f'Opção inválida: {opcao}. Por favor, escolha uma opção válida.')


def load_animation():
    frames = ["/", "-", "\\", "|", "/", "-", "\\", "|"]

    for _ in range(3):
        for frame in frames:
            print(f'\rGerando dados{frame}', end="", flush=True)
            sleep(0.1)
    print()
