# usuário informa o numero
# importar bibliotecas

import os
import time

contador = int(input('Informe um número inteiro: '))
os.system('cls')

# conta a partir do numero informado até zero

while contador >= 0:
    print(f'Contagem regressiva: {contador}...')
    time.sleep(1)
    os.system('cls')
    contador -= 1

print('BOOM!!!')
