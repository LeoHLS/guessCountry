import os
import functions
from unidecode import unidecode

while True:
    pais = functions.getCountry().upper()
    letras_acertadas = ''
    cont_letra = 0
    num_tent = 0
    coveredCountry = ''
    print(pais)
    for i in unidecode(pais):
        if i != ' ':
            coveredCountry += '*'
        else:
            coveredCountry += ' '

    print('País a ser descoberto: ', coveredCountry)

    while True:
        num_tent += 1
        while True:
            tentativa = input('Escreva uma letra: ').upper()
            if tentativa.isalpha() and len(tentativa) == 1:
                if tentativa in unidecode(pais):
                    letras_acertadas += tentativa
                palavra_formada = ''
                for i in unidecode(pais):
                    if i in letras_acertadas:
                        palavra_formada += i
                    elif i == ' ':
                        palavra_formada += ' '
                    else:
                        palavra_formada += '*'
                print(palavra_formada)

                break
            print('Por favor, escreve apenas UMA LETRA.')
        
        if palavra_formada == pais:
            os.system('cls')
            print(f'PARABÉNS, VOCÊ ACERTOU! Foram {num_tent} tentativas no total.')
            break
        print("Número de tentativas: ", num_tent)

    while True:
        novamente = input('Deseja jogar novamente? [S] ou [N]: ').upper()
        if novamente not in 'SN':
           print('Digite apenas S ou N!')
           continue         
        else:
            break
    if novamente == 'N':
        break