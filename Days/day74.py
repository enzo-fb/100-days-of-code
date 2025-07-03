"""Análise de Sentimentos com PLN"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Exemplos de frases e seus sentimentos (1 = positivo, 0 = negativo)
frases = [
    "Eu adorei esse filme!",
    "O produto é excelente.",
    "Que experiência horrível.",
    "Não gostei do atendimento.",
    "Muito bom, recomendo.",
    "Péssimo, nunca mais volto.",
]
sentimentos = [1, 1, 0, 0, 1, 0]

# Vetorização (transforma texto em números)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases)

# Treinamento do modelo
modelo = MultinomialNB()
modelo.fit(X, sentimentos)

# Testando com novas frases
novas_frases = [
    "O filme foi ótimo!",
    "O serviço é ruim.",
    "Gostei muito do produto.",
    "Não recomendo para ninguém.",
]
X_novas = vectorizer.transform(novas_frases)
predicoes = modelo.predict(X_novas)

for frase, sentimento in zip(novas_frases, predicoes):
    print(f'"{frase}" → {"Positivo" if sentimento == 1 else "Negativo"}')
