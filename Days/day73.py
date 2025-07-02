"""Rede Neural"""

import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Gerar dados sintéticos
X, y = make_moons(n_samples=1000, noise=0.1, random_state=42)

# Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Criar e treinar o modelo
modelo = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)

# Fazer previsões
y_pred = modelo.predict(X_test)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2f}")
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))
print("Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred))

# Testar com novos dados
print("\n--- TESTANDO COM DADOS NOVOS ---")
novos_dados = np.array([[0.5, 0.5], [-0.5, -0.5], [1.5, 0.0], [0.0, 1.0], [2.0, -0.5]])

predicoes_novas = modelo.predict(novos_dados)
probabilidades = modelo.predict_proba(novos_dados)

print("Predições para novos dados:")
for i, (ponto, pred, prob) in enumerate(
    zip(novos_dados, predicoes_novas, probabilidades)
):
    print(f"Ponto {ponto}: Classe {pred} (Probabilidade: {prob[pred]:.2f})")

# Visualizar resultados
plt.figure(figsize=(12, 6))

# Dados de teste
plt.subplot(1, 2, 1)
plt.scatter(
    X_test[y_test == 0][:, 0],
    X_test[y_test == 0][:, 1],
    color="blue",
    label="Classe 0",
    alpha=0.5,
)
plt.scatter(
    X_test[y_test == 1][:, 0],
    X_test[y_test == 1][:, 1],
    color="red",
    label="Classe 1",
    alpha=0.5,
)
plt.scatter(
    X_test[y_pred == 0][:, 0],
    X_test[y_pred == 0][:, 1],
    color="cyan",
    marker="x",
    label="Predição Classe 0",
    alpha=0.5,
)
plt.scatter(
    X_test[y_pred == 1][:, 0],
    X_test[y_pred == 1][:, 1],
    color="magenta",
    marker="x",
    label="Predição Classe 1",
    alpha=0.5,
)
plt.title("Dados de Teste Original")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()

# Novos dados
plt.subplot(1, 2, 2)
plt.scatter(
    X_train[y_train == 0][:, 0],
    X_train[y_train == 0][:, 1],
    color="lightblue",
    alpha=0.3,
    label="Treino Classe 0",
)
plt.scatter(
    X_train[y_train == 1][:, 0],
    X_train[y_train == 1][:, 1],
    color="lightcoral",
    alpha=0.3,
    label="Treino Classe 1",
)

cores_pred = ["blue" if pred == 0 else "red" for pred in predicoes_novas]
plt.scatter(
    novos_dados[:, 0],
    novos_dados[:, 1],
    c=cores_pred,
    marker="*",
    s=200,
    edgecolors="black",
    linewidth=2,
    label="Novos Dados",
)

for i, (x, y) in enumerate(novos_dados):
    plt.annotate(f"{i+1}", (x, y), xytext=(5, 5), textcoords="offset points")

plt.title("Predições em Novos Dados")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()

plt.tight_layout()
plt.show()
