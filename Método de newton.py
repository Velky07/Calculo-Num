#Método de Newton
import math
def f(x):
	return math.exp(x) - (4 * math.pow(x, 2))
	
def phi(x):
	return ((-4*x**2)+(math.exp(x)*x)-math.exp(x))/((math.exp(x))-8*x)

#Ponto inicial
x= 4

#Conatgem de Iterações
k= 0

#Precisão
erro= 0.0001

print("A solução inicial é:", x,"\n")
while abs (f(x))>erro:
	x= phi(x)	
	k=k+1
	print("A solução atual é",x, "\nA interação atual é:", k,"\n")

print("A solução final é:",x,"\nTotal de interações foi:", k)