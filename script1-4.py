# Exemplifique a stemização e a lematização de um texto, em língua
# inglesa. Ilustre um caso onde textos diferentes conduzem a uma mesma saída
# através do stemming ou lemmatization. Considere como saída um vetor ordenado
# contendo lemas e stems.

# pip install nltk spacy
# py -m spacy download en_core_web_sm

import nltk
from nltk.stem import PorterStemmer
import spacy

# Inicializando stemmer e lematizador
stemmer = PorterStemmer()
nlp = spacy.load("en_core_web_sm")

# Exemplo de textos
text1 = "running"
text2 = "runs"
text3 = "ran"

# Stemming - O stemmer reduz as palavras às suas raízes
stems = [stemmer.stem(word) for word in [text1, text2, text3]]

# Lemmatization - O lematizador transforma as palavras em suas formas básicas, considerando o contexto
lemmas = [nlp(word)[0].lemma_ for word in [text1, text2, text3]]

# Resultados
print("Stems:", stems)
print("Lemmas:", lemmas)

