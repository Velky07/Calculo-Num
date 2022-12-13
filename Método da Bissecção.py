#Método da Bissecção
import math
def f(x):
    return math.exp(x) - 4*math.pow(x,2)

#Intervalo Inicial
a= 4
b= 4.5

#Contagem de iterações
i= 0

#Precisão
erro_max = 0.0001

while b-a> erro_max:
    print("A solução atual é:\n",a,"________",b, "\n\nA interação atual é:", i,"\n")
    M= (a+b)/2
    if f(a) * f(M)<0:
        b= M
    else:
        a= M
    i= i+1
    


print("A solução é:", M, "\nO Número de Iterações foi:", i)

