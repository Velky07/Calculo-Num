def p(x, a):
  r = 0
  n = len(a)
  for i in range(0, n):
    r += a[i] * (x**i)
    return r

def elimGauss(A, b): 
    n = len(b)
    for k in range(0, n-1):
        for L in range(k+1, n):
          m = A[L][k]/A[k][k]
          for C in range(k, n):
            A[L][C] = A[L][C]-m*A[k][C]
          b[L] = b[L]-m*b[k]
        return A, b

def solucao(A, b):
   n = len(b)
   x = n*[0]
   x[n-1] = b[n-1]/A[n-1][n-1]
   for k in range(n-2, -1, -1):
     s = 0
     for j in range(k+1, n):
       s = s + A[k][j]*x[j]
     x[k] = (b[k]-s)/A[k][k]
   return x


def MatrizVandermonde(x):
    n = len(x)
    V = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(x[i]**j)
        V.append(row)
    return V

def interpolaçãoLin(d, x):
    saida = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))
    return saida
  

x = [30, 35]  #graus da tabela, onde 32,5° se encontra
fx = [0.99826, 0.99818] #valores dos respectivos calor específicos

w = [20, 25, 30, 35, 40, 45, 50] #Todos os graus da tabela
z = [0.99907, 0.99852, 0.99826, 0.99818, 0.99828, 0.99849, 0.99878] #e seus respectivos calor específicos 

M1 = MatrizVandermonde(x)
M2 = MatrizVandermonde(w)
#A matriz de Vandermonde associada aos vetores x e w.  

M1_vt, x_t = elimGauss(M1, fx)
S1 = solucao(M1_vt, x_t)
#Obtenha os coeficientes polinomiais que se ajustam à curva do problema usando a função gaussiana e a solução.
M2_t, y_t = elimGauss(M2, z)
S2 = solucao(M2_t, y_t)

print("com um polinômio de grau 2 temos:", p(32.5, S1)) 
print("com um polinômio de grau 6 temos:", p(32.5, S2))

x_2=[[0.99828, 40], [0.99849, 45]]

print("com um interpolação linear temos que a temperatura, em graus ceulsius, da água é de:",round(interpolaçãoLin(x_2, 0.99837),2),"°")#interpolação Linear
