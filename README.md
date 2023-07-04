# Yandex-GPT

YandexGPT will briefly retell the article

# Installation steps:
1. Clone or download repo
2. Download libraries `pip install -r requirements.txt`
```sh
git clone https://github.com/itzlayz/yandex-gpt
cd yandex-gpt
pip install -r requirements.txt
```
3. Make main file in your folder and import sync/async api ([Example](yandex-gpt/README.md#Example:))

# Example:
```python
from async_api import parap
from async_api import parse_text

import asyncio

token = 'YOUR_TOKEN'

async def main():
    article_url = "https://habr.com/ru/articles/731802/r"

    paraphrase_result = await parap(token=token, article_url=article_url)
    text_result = await parse_text(url=paraphrase_result.get('sharing_url'))

    print(text_result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
