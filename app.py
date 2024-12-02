# PP.3.3. Demonstre a técnica de agrupamento hierárquico de documentos similares utilizando
# alguns dados de reviews de produtos. Ilustre e explique o dendrograma em especial no que se
# refere aos pontos de corte para as distâncias. Faça uso de dados de reviews de produtos e não
# se esqueça de normalizar os dados antes de efetuar a montagem dos vetores de características.

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

# Baixar stop words do nltk
nltk.download('stopwords')
stop_words_pt = stopwords.words('portuguese')

# Exemplo de dados de reviews
reviews = [
    "O produto é excelente, gostei muito!",
    "Chegou no prazo e a qualidade é otima.",
    "Nao gostei do material, parece fragil.",
    "Produto razoavel, mas poderia ser melhor.",
    "Maravilhoso! Atendeu todas as minhas expectativas.",
    "A entrega foi rapida, mas o produto veio com defeito.",
    "Produto excelente, recomendo para todos.",
    "Nao vale o preço, qualidade abaixo do esperado."
]

# Etapa 1: Vetorização TF-IDF
vectorizer = TfidfVectorizer(stop_words=stop_words_pt)
tfidf_matrix = vectorizer.fit_transform(reviews)

# Normalização dos vetores
normalized_data = normalize(tfidf_matrix)

# Etapa 2: Agrupamento hierárquico
linkage_matrix = linkage(normalized_data.toarray(), method='ward')

# Etapa 3: Exibição do dendrograma
plt.figure(figsize=(10, 6))
dendrogram(
    linkage_matrix,
    labels=[f"Review {i+1}" for i in range(len(reviews))],
    leaf_rotation=90,
    leaf_font_size=10,
    color_threshold=1.5  # Distância de corte ilustrativa
)
plt.title("Dendrograma de Reviews")
plt.xlabel("Reviews")
plt.ylabel("Distância Euclidiana")
plt.axhline(y=1.5, color='r', linestyle='--', label="Corte")
plt.legend()
plt.show()

# Etapa 4: Obter os clusters
num_clusters = 3  # Pode variar conforme análise visual
clusters = fcluster(linkage_matrix, t=num_clusters, criterion='maxclust')

# Resultados
df = pd.DataFrame({'Review': reviews, 'Cluster': clusters})
print(df.sort_values('Cluster'))


