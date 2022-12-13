#Método do Ponto Fixo
import math
def f(x):
	return math.exp(x) - (4 * math.pow(x, 2))
	
def phi(x):
	return math.exp(x)/(4 * math.sqrt(math.exp(x)))

#Intervalo Inicial
x= 4.4

#Contagem de Iterações
k= 0

#Precisão
erro= 0.0001

print("A solução inicial é:", x,"\n")
while abs (f(x))>erro:
	k=k+1
	x= phi(x)
	x_raiz=x
	print("A solução atual é",x_raiz, "\nA interação atual é:", k,"\n")
	if k>=30:
		break

print("A solução final é:",x_raiz,"\nTotal de interações foi:", k)