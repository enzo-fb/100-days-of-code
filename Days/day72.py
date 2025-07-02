"""Modelo de aprendizado de máquina"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Gerar dados sintéticos
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 pontos entre 0 e 10
y = 2.5 * X.flatten() + 1.5 + np.random.randn(100) * 2  # y = 2.5x + 1.5 + ruído

# Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Criar e treinar o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Coeficiente: {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")
print(f"Erro Quadrático Médio: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Visualizar resultados
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color="blue", label="Dados reais")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Predição")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Regressão Linear")
plt.legend()
plt.show()
