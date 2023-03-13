from matplotlib import pyplot as plt
import numpy as np


def mmq(g1, g2, xA, yB):    
    G_11 = np.dot(g1(xA), g1(xA))
    G_12 = np.dot(g1(xA), g2(xA))
    G_21 = G_12
    G_22 = np.dot(g2(xA), g2(xA))

    G = np.array([[G_11, G_12], [G_21, G_22]])

    b_1 = np.dot(yB, g1(xA))
    b_2 = np.dot(yB, g2(xA))

    b = np.array([b_1, b_2])

    eg = np.linalg.solve(G, b)
    a1 = eg[0]
    a2 = eg[1]
    return a1, a2


def g_1(r):
    return np.ones(len(r))
    
def g_2(r):
    return np.sqrt(r)


x = np.array([1, 1.5, 2, 2.5, 3])
y = np.array([1.6, 5.6, 6, 7.1, 7])


a_1, a_2 = mmq(g_1, g_2, x, y)


def phi_1(z):
    fA = a_1 * g_1(z) + a_2 * g_2(z)
    return fA

def phi_2(z):
    fA = a_1 * g_1(z) + a_2 * np.log(z)
    return fA


x_r = np.linspace(1, 3, 100)
y_r = phi_1(x_r)

plt.plot(x, y, 'o')
plt.plot(x_r, y_r)
plt.show()

erro = ((y - phi_1(x)) ** 2).sum()
print("Erro quadrático geral para phi:", erro)

x_r = np.linspace(1, 3, 100)
y_r = phi_2(x_r)

plt.plot(x, y, 'o')
plt.plot(x_r, y_r)
plt.show()

erro = ((y - phi_2(x)) ** 2).sum()
print("Erro quadrático geral para phi:", erro)