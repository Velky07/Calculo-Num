import math

def f(x):
	return math.exp(x) - (4 * math.pow(x, 2))

a= 4
b= 4.5

M_pond= (a+b)/2

k= 0

erro= 0.0001
print("A interação inicial é:", M_pond,"\n")

while abs (f(M_pond))>erro:
	M_pond = (a* f(b)- b*f(a))/ (f(b) - f(a))
	if f(a)*f(M_pond)<0:
		b= M_pond
	else:
		a= M_pond
	k=k+1
	print("A solução atual é:\n",a,"________",b, "\n\nA interação atual é:", k,"\n")

print("A solução final é:",M_pond,"\nTotal de interações foi:", k)