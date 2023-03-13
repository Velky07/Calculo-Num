from matplotlib import pyplot as plt
import numpy as np


def mmq(g1, g2, x, y):
    
    # g1 e g2 serão as funções as quais queremos fazer o ajuste para o conjunto de dados x e y
    
    a_1 = 0
    a_2 = 0
    
    # Esta função deve retornar os coeficientes a_1 e a_2 das funções g_1 e g_2, respectivamente
    
    # '''
    # Passo 1:
    # Monte a matriz dos coeficientes do sistema linear:
    
    # G = [[G_11, G_12] 
    #      [G_21, G_22]
         
    
         
    # Cada G_ij é obitido pelo produto interno <g_i(x), g_j(x)> em que g_i(x) = [g_i(x_1), g_i(x_2), ..., g_i(x_n)]
    
    # Para calcular os produtos internos você pode usar a biblioteca numpy, por exemplo:
    # G_11 = np.dot(g_1(x), g_1(x))
    # '''
    
    # #
    
    # '''
    # Passo 2:
    # Monte o vetor de termos independentes do sistema linear:
    
    # b = [b_1, b_2, ..., b_n]
    
    # em que cada b_i é obtido pelo produto interno b_i = <y, g_i(x)> e novamente
    # g_i(x) = [g_i(x_1), g_i(x_2), ..., g_i(x_n)]
    # '''
    
    #
    
    # '''
    # Passo 3:
    # Revolva o sistema linear G * a = b
    
    # Dica:
    # Você pode usar a biblioteca numpy da forma
    # a = np.linalg.solve(G, b)
    # Observação: deve-se importar a biblioteca numpy as np
    # '''

    a_1 = a[0]
    a_2 = a[1]

        
    return a_1, a_2

    # Defina as função à serem ajustadas:

def g_1(r):
    # Faça retornar a primeira função desejada
    
def g_2(r):
    # Faça retornar a segunda função desejada



# Considere o conjunto de dados:
x = np.array([1, 1.5, 2, 2.5, 3])
y = np.array([1.6, 5.6, 6, 7.1, 7])

# Os coeficientes do ajuste são obtidos através do comando:
a_1, a_2 = mmq(g_1, g_2, x, y)

# Defina a função de ajuste:
def phi(z):
    return a_1*g_1(z) + g_2(z)


# O conjunto de dados a seguir servirá para a plotagem da curva de ajuste
# Observação: deve-se importar a biblioteca numpy as np
x_r = np.linspace(1, 3, 100)
y_r = phi(x_r)
plt.plot(x, y, 'o')
plt.plot(x_r, y_r)
# Observação: deve-se importar a biblioteca matplotlib.pyplot as plt

# Cálculo do erro quadrático geral

# Calcule o erro quadrático geral da seguinte maneira:

#Inicialize a variável erro =0 
#faça um loop do tipo for de i = 0 até n (não incluindo n)
#em que n é o tamanho do vetor x (ou y, eles devem ter o mesmo tamanho)
#dentro do loop acumule o erro quadrático fazendo erro+= (y[i] - phi(x[i]))**2
#imprima o erro obtido após o loop
