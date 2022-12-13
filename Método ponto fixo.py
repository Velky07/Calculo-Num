import math

def f(x):
	return math.exp(x) - (4 * math.pow(x, 2))
	
def phi(x):
	return math.exp(x)/(4 * math.sqrt(math.exp(x)))

x=-0.4
k= 0

erro= 0.0001
print("A solução inicial é:", x,"\n")
while abs (f(x))>erro:
	x= phi(x)	
	k=k+1
	print("A solução atual é",x, "\nA interação atual é:", k,"\n")
	if k>=19:
		break

print("A solução final é:",x,"\nTotal de interações foi:", k)