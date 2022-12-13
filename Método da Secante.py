import math

def f(x):
	return math.exp(x) - (4 * math.pow(x, 2))

x_0= 4
x_1= 4.5

x_2= (x_0+x_1)/2

k= 0

erro= 0.0001
print("Solução inicial é:", x_2,"\n")

while abs (f(x_2))>erro:
	x_2 = (x_0* f(x_1)- x_1*f(x_0))/ (f(x_1) - f(x_0))
	x_0=x_1
	x_1=x_2
	k=k+1
	print("A solução atual é",x_2, "\nA interação atual é:", k,"\n")

print("A solução final é:",x_2,"\nTotal de interações foi:", k)