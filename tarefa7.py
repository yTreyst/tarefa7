import numpy as np
#troquei o nome do professor pelo meu :D
# mas no final eu deixo a do professor xD
# caso o comando não der certo no seu pc prof, tem que abrir o prompt e digitar: pip install numpy
celso_matriz = np.array([[3,4,1], [3,1,2]])

soma_elementos = 0

for linha in celso_matriz:
    for elemento in linha:
        soma_elementos += elemento

print("A soma dos elementos da matriz é:", soma_elementos)

#import numpy as np

#dieimes_matriz = np.array([[3,4,1], [3,1,2]])

#soma_elementos = 0

#for linha in dieimes_matriz:
#    for elemento in linha:
#        soma_elementos += elemento
#
#print("A soma dos elementos da matriz é:", soma_elementos)