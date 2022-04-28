from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import requests

def tesla_tracker():
    url = "https://www.google.com/finance/quote/TSLA:NASDAQ"

    result = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    doc = BeautifulSoup(result.text, "html.parser")

    gsearch = doc.find(["div"], class_="YMlKec fxKbKc")
    cName = doc.find(["div"], class_="zzDege")

    return cName.string, gsearch.string
def meta_tracker():
    url2 = "https://www.google.com/finance/quote/FB:NASDAQ"

    result2 = requests.get(url2, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    doc2 = BeautifulSoup(result2.text, "html.parser")

    gsearch = doc2.find(["div"], class_="YMlKec fxKbKc")
    cName2 = doc2.find(["div"], class_="zzDege")

    return cName2.string, gsearch.string
def apple_tracker():
    url3 = "https://www.google.com/finance/quote/AAPL:NASDAQ"

    result3 = requests.get(url3, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    doc3 = BeautifulSoup(result3.text, "html.parser")

    gsearch = doc3.find(["div"], class_="YMlKec fxKbKc")
    cName3 = doc3.find(["div"], class_="zzDege")

    return cName3.string, gsearch.string

print(apple_tracker(), meta_tracker(), tesla_tracker())