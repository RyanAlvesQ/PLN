# Desenvolva um programa em Python que lê um arquivo de entrada, em
# formato txt, quebra o texto em palavras e contabiliza quantas vezes a palavra ocorre
# no texto. Como saída o programa gera um gráfico que ilustra o número de vezes que
# cada palavra ocorreu. 

# Em processamento de linguagem natural, como são
# chamadas as palavras que ocorrem com muita frequência e que podem não
# agregar muito significado? Para o texto que você analisou (que deve conter no
# mínimo 2000 palavras) quais seriam essas palavras? Quais as classes dessas
# palavras?

# Em Processamento de Linguagem Natural (PLN), as palavras que ocorrem com muita frequência e
# podem não agregar muito significado são chamadas de stopwords. Exemplos de stopwords em
# português incluem "e", "a", "o", "de", "que", "em", entre outras. Essas palavras geralmente pertencem
# a classes gramaticais como preposições, conjunções, artigos e pronomes.

#pip install matplotlib

import matplotlib.pyplot as plt
from collections import Counter
import string

# Função para limpar o texto
def clean_text(text):
    # Converte para minúsculas
    text = text.lower()
    # Remove pontuação
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Função para contar palavras
def count_words(text):
    words = text.split()
    word_count = Counter(words)
    return word_count

# Função para plotar o gráfico
def plot_word_frequency(word_count):
    # Ordena as palavras por frequência
    common_words = word_count.most_common()
    words = [word for word, count in common_words]
    counts = [count for word, count in common_words]

    plt.figure(figsize=(10, 8))
    plt.barh(words, counts)
    plt.xlabel('Frequência')
    plt.ylabel('Palavras')
    plt.title('Frequência das Palavras no Texto')
    plt.show()

# Caminho para o arquivo de texto
file_path = 'seu_arquivo.txt'

# Lê o arquivo de texto
with open(file_path, 'r') as file:
    text = file.read()

# Limpa o texto e conta as palavras
cleaned_text = clean_text(text)
word_count = count_words(cleaned_text)

# Plota o gráfico de frequência das palavras
plot_word_frequency(word_count)
