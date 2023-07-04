import requests
from bs4 import BeautifulSoup

URL = "https://300.ya.ru/api/sharing-url"

def parap(*, token: str, article_url: str) -> dict:
    response = requests.post(
        URL,
        json={
            'article_url': article_url
        },
        headers={
            'Authorization': f'OAuth {token}'
        }
    )

    return response.json()

def parse_text(*, url: str) -> str:
    text = ""

    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('li', class_='svelte-h3ittf')

    for quote in quotes:
        text += (quote.text + '\n')

    return text