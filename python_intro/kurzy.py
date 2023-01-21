from bs4 import BeautifulSoup
import httpx

url = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"
res = httpx.request("GET", url)

# Zpracování dat z tabulky
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find("table", attrs={"class": "forextable"})
tableData = table.tbody.find_all("tr")
for tr in tableData:
    zprava = ""
    m = True
    for td in tr.find_all("td"):
        m = not m
        if m == True:
            continue
        zprava = zprava+(td.text.replace('\n', ' ').strip())+"\t"   
    print(zprava)



