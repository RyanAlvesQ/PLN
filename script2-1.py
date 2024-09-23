from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        reviews = scrape_reviews(url)
        return render_template('index.html', reviews=reviews)
    return render_template('index.html', reviews=[])

def scrape_reviews(url):
    # Faça a requisição para o site
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar os elementos que contêm as avaliações e as estrelas
    review_elements = soup.find_all('article', class_='ui-review-capability-comments__comment')  # Ajuste essa classe conforme o site
    reviews = []
    for review in review_elements:
        # Extraia a avaliação em estrelas
        star_element = review.find('div', class_='ui-review-capability-comments__comment__rating')  # Ajuste esta classe para a do seu site
        stars = star_element.get_text(strip=True) if star_element else 'Sem avaliação'  # Padrão se não encontrar estrelas
        
        # Extraia o texto da avaliação
        text = review.get_text(" ", strip=True)  # Adiciona espaço como separador para elementos internos
        formatted_text = ' '.join(text.split())  # Remove espaços extras e formata o texto
        
        reviews.append({'stars': stars, 'comment': formatted_text})
    
    return reviews

if __name__ == '__main__':
    app.run(debug=True)
