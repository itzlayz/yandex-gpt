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