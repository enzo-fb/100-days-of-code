"""Sistema de Recomendação"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recomendar_produtos(produto, descricao_produtos):
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(descricao_produtos)

    similaridade = cosine_similarity(tfidf.transform([produto]), tfidf_matrix)

    indices = similaridade.argsort()[0][-3:][::-1]

    return [descricao_produtos[i] for i in indices]


descricao_produtos = [
    "Camiseta de algodão, confortável e leve.",
    "Calça jeans, estilo casual e durável.",
    "Tênis esportivo, ideal para corrida e academia.",
    "Jaqueta de couro, elegante e resistente.",
    "Camisa social, perfeita para ocasiões formais.",
    "Tênis casual, confortável para o dia a dia.",
]

produto = "Camiseta de algodão, confortável e leve."
produtos_recomendados = recomendar_produtos(produto, descricao_produtos)

print("Produtos recomendados para você:")
for p in produtos_recomendados:
    print(f"- {p}")
