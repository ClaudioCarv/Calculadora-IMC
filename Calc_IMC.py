
import time
from colors import cores
from colors import tipos
import platform
import os

def limpar():
    if platform.system() == 'Windows':
        os.system('cls')


while True:
    limpar()
    print('{}{}Calcule seu IMC{}'.center(50).format(cores['ciano'], tipos['negrito'], cores['limpa']))

    alt = float(input('{}\nDigite aqui sua altura: {}'.format(cores['ciano'], cores['limpa'])))
    peso = float(input('{}Digite aqui seu peso: {}'.format(cores['ciano'], cores['limpa'])))

    print('{}Processando...\n{}'.format(cores['amarelo'], cores['limpa']))
    time.sleep(1)

    calc = (peso / alt)  
    imc = calc / alt

    if(imc <= 18.5):
        print('{}{:.2f} Abaixo do peso\n{}'.format(cores['ciano'], imc, cores['limpa']))
    elif(imc >= 18.5 and imc <= 25):
        print('{}{:.2f} Peso Ideal\n{}'.format(cores['verde'], imc, cores['limpa']))
    elif(imc >= 25 and imc <= 30):
        print('{}{:.2f} Sobrepeso\n{}'.format(cores['amarelo'],imc, cores['limpa']))
    elif(imc > 30 and imc <= 40):
        print('{}{:.2f} Obesidade\n{}'.format(cores['vermelho'], imc, cores['limpa']))
    elif(imc > 40):
        print('{}{}{:.2f} Obesidade Mórbida\n{}'.format(cores['vermelho'], tipos['negrito'], imc, cores['limpa']))
    
    esc = str(input('{}Deseja calcular novamente ? S/N: {}'.format(cores['ciano'], cores['limpa']))).lower()

    if(esc == 's'):
        print('{}Reiniciando...{}'.format(cores['amarelo'], cores['limpa']))
        time.sleep(1)
        limpar()
    elif(esc == 'n'):
        print('{}Encerrado{}'.format(cores['vermelho'], cores['limpa']))
        time.sleep(1)
        break