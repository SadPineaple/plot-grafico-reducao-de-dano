import matplotlib.pyplot as plt
import numpy as np

def reducao_dano(resistencia):
    return resistencia / (100 + resistencia) * 100

resistencia = np.linspace(0, 2000, 100)

reducao = reducao_dano(resistencia)

plt.plot(resistencia, reducao)
plt.xlabel('Resistência')
plt.ylabel('Redução de Dano %')
plt.title('Gráfico da Fórmula de Redução de Dano')
plt.grid(True)
plt.show()