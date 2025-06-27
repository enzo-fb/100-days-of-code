"""Matplotlib"""

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y)

# Add titles and labels
plt.title("Gráfico de Linha Simples (tempo vs velocidade)")
plt.xlabel("Eixo do Tempo")
plt.ylabel("Eixo da Velocidade")

# Show the plot
plt.show()

a = [1, 2, 3, 4, 5]
b = [2, 3, 5, 7, 11]
plt.title("Gráfico de Pizza")
plt.pie(a, labels=b, autopct="%1.1f%%")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
