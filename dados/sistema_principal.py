from funcoes import *
from listas import * 
from time import sleep
from tqdm import tqdm

import random


# Criar uma mensagem de boas vindas
print()
cabecalho('''Bem vindo ao Gerador de dados!! - Para finalizar o programa digite [6]''')

while True:
    cabecalho('MENU PRINCIPAL')
    menu = input(
'''Digite sua(s) escolha(s) separadas por vírgula 

[1] - Nome
[2] - E-mail
[3] - Telefone
[4] - Cidade
[5] - Estado 
[6] - parar

Sua opção: ''')
    
    if menu <= '5':
        print()
        load_animation()
        for c in tqdm(range(2)):
            print(f'{c}', end='', flush=True)
            sleep(0.5)
        print()
    
        cabecalho('DADOS GERADOS')
        (opcao_usuario(menu))
    else:
        linha()
        palavra = 'Finalizando progra...'
        for letra in palavra:
            print(f'{letra}', end='', flush=True)
            sleep(0.1)
        print()
        linha()
        sleep(1)
        break

    # Fazer a função de salvar os dados em um arquivo.txt
    salvar_arquivo = str(input('Deseja salvar os dados [S/N]: ')).strip().upper()

    if salvar_arquivo == 'S':
        


