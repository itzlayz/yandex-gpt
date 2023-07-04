import aiohttp
import asyncio
from bs4 import BeautifulSoup

URL = "https://300.ya.ru/api/sharing-url"


async def parap(*, token: str, article_url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        headers = {
            'Authorization': f'OAuth {token}'
        }
        async with session.post(URL, json={'article_url': article_url}, headers=headers) as response:
            return await response.json()


async def parse_text(*, url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            quotes = soup.find_all('li', class_='svelte-h3ittf')
            text = ""
            for quote in quotes:
                text += (quote.text + '\n')
                
            return text