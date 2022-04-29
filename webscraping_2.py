from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import requests
from datetime import datetime

def time_sorter():
    now = datetime.now()
    ntime = now.strftime("%H:%M")
    preMTime = ntime.split(":")
    if(int(preMTime[0]) < 14) or (int(preMTime[0]) >= 21):
        if(int(preMTime[1]) < 30) or (int(preMTime[1]) > 0):
            preMarket = "Pre-market"
            return ntime, preMarket
    return ntime


def URL_getter():
    tracker = input("Enter a company tracker(E.G AAPL): ")
    url = "https://www.google.com/finance/quote/"+tracker.upper()+":NASDAQ"
    return url

print("Get price of company stock")
while(True):
    url = URL_getter()
    if(url == "quit"):
        False
    result = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    doc = BeautifulSoup(result.text, "html.parser")

    search = doc.find("div", class_="YMlKec fxKbKc")
    print(time_sorter(),":",search.string)