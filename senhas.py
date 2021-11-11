from math import comb
import string
import time
from itertools import combinations_with_replacement
import random
from random import sample
import time
from tqdm import tqdm


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

print('_=_'*10)
print(f'{bcolors.OK}PROGRAMA:GERADOR DE SENHAS {bcolors.RESET}')
print('_=_'*10)
quantos_digitos =int(input('QUANTOS DIGITOS TEM A SENHA '))
se=str(input('DIGITE A SENHA '))
se=se.split(',')


print('PROCESSANDO..')
for i in tqdm(range(quantos_digitos)):
	time.sleep(0.9)


tipo= string.ascii_lowercase + string.digits
def gerar_senhas(tipo,quantos_digitos):
    comb = combinations_with_replacement(tipo,quantos_digitos)
    print('\nNumero de combinaçoes '+ str(len(list(comb))))
            
init_t = time.time()
gerar_senhas(tipo,quantos_digitos)
fin_t = time.time()
print('tempo '+str(fin_t-init_t)+'s')

d=input(f'{bcolors.WARNING}DESEJA REALIZAR VARREDURA..??(OBS: ACIMA DE 5 DIGITOS NAO RECOMENDADO) DIGITE SIM OU NAO  {bcolors.RESET}')
comb = combinations_with_replacement(tipo,quantos_digitos)
repete=(len(list(comb)))
if d =='sim':
    for x in range(repete):
        senha=''.join(random.choice(string.ascii_lowercase + string.digits) for _ in sample(range(quantos_digitos),quantos_digitos))
        x+=1
    
        if senha in se:
            print(senha)
            print(f'{bcolors.OK}\n_._SENHA QUEBRADA!!_.{bcolors.RESET}')
            print('Combinaçao: ','¨',x,'¨')
            break
        elif senha!=se:
            print(senha)
    if senha not in se:
         print(f'\n{bcolors.FAIL}NAO FOI POSSIVEL QUEBRAR A SENHA ...\nTENTE NOVAMENTE{bcolors.RESET} ...==>Combinaçao: ','¨',x,'¨')        

print(f'\n{bcolors.WARNING}PROGRAMA FINALIZADO!!{bcolors.RESET}')