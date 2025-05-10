import os
import json
from bs4 import BeautifulSoup
import requests
import re
import dotenv
from .utils import exponential_retry, multi_threading
dotenv.load_dotenv()

SERPER_API_KEY = os.environ["SERPER_API_KEY"]
URL = "https://google.serper.dev/news"


def search_news(q, gl="us", hl="en", num=10, tbs="qdr:d"):
    payload = json.dumps({
        "q": q,
        "gl": gl,
        "hl": hl,
        "num": num,
        "tbs": tbs
    })
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.post(URL, headers=headers, data=payload)
    search_result = response.json()
    news_results = search_result['news']

    return news_results


@exponential_retry(retries=3, return_value_if_fail="")
def scrape_url(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    page = requests.get(  # Await the get request
        url,
        timeout=15,
        headers=headers
    )

    # page.encoding = page.apparent_encoding
    parsed = BeautifulSoup(page.text, "html.parser")

    text = parsed.get_text(" ")
    text = re.sub('[ \t]+', ' ', text)
    text = re.sub('\\s+\n\\s+', '\n', text)
    return text


def search_and_scrape_url(query):
    search_results = search_news(q=query)
    urls = [res["link"] for res in search_results]
    contents = multi_threading(scrape_url, urls, max_workers=5)
    for content, res in zip(contents, search_results):
        res['content'] = content
    return search_results


if __name__ == "__main__":
    # search_result = search_news("Apple Stock News", num=3)
    # print(search_result)
    search_and_scrape_result = search_and_scrape_url("Apple Stock News")
    print(search_and_scrape_result)

    # python -m src.utils_news
