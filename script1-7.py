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
def plot_word_frequency(word_count, num_words=20):
    # Ordena as palavras por frequência e seleciona as mais comuns
    common_words = word_count.most_common(num_words)
    words = [word for word, count in common_words]
    counts = [count for word, count in common_words]

    plt.figure(figsize=(12, 8))
    plt.barh(words, counts, color='red')
    plt.xlabel('Frequência')
    plt.ylabel('Palavras')
    plt.title('Frequência das Palavras no Texto')
    plt.gca().invert_yaxis()  # Inverte o eixo y para exibir as palavras mais frequentes no topo
    plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição
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
plot_word_frequency(word_count, num_words=20)
