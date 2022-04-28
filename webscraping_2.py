from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import requests
import re


url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"

result = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
doc = BeautifulSoup(result.text, "html.parser")

Presearch = doc.find(["fin-streamer"], class_="C($primaryColor) Fz(24px) Fw(b)")
Presearch = ("The Pre-Market Price is: " + str(Presearch))
Opensearch = doc.find(["fin-streamer"], class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")

print(Presearch)
print("The Market Price is: ",Opensearch['value'])

print("__________________________________________________________________________________________")
url2 = "https://finance.yahoo.com/quote/FB?p=FB&ncid=yahooproperties_peoplealso_km0o32z3jzm"

result2 = requests.get(url2, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
doc2 = BeautifulSoup(result2.text, "html.parser")

Presearch2 = doc2.find(["fin-streamer"], class_="C($primaryColor) Fz(24px) Fw(b)")
Presearch2 = ("The Pre-Market Price is: " + str(Presearch2))
Opensearch2 = doc2.find(["fin-streamer"], class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")

print(Presearch2)
print("The Market Price is: ",Opensearch2['value'])

