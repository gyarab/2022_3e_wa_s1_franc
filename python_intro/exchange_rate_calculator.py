from bs4 import BeautifulSoup
import httpx

url = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"
res = httpx.request("GET", url)

# Zpracování dat z tabulky
soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find("table", attrs={"class": "forextable"})
tableData = table.tbody.find_all("tr")
name = []
short = []
price = []

print("\u0332".join("Code")+"    "+"\u0332".join("Value [EUR]")+"     "+"\u0332".join("Currency"))
for tr in tableData:
    shor = ""
    val = 0
    nam = ""
    m = 0
    for td in tr.find_all("td"):
        if m==0:
            short.append(td.text.replace('\n', ' ').strip())
            shor = td.text.replace('\n', ' ').strip()
        if m==1:
            name.append(td.text.replace('\n', ' ').strip())
            nam = td.text.replace('\n', ' ').strip()
        if m==2:
            prePrice = td.text.replace('\n', ' ').strip()
            preprice = prePrice.replace(",", ".")
            preprice = float(prePrice)
            price.append(prePrice)
            val = prePrice
        m = m+1
    print(shor+"\t"+'{0: >#010.4f}'. format(float(val))+"\t"+nam)

# -------------     User inputs
zMena = ""
h = 0
while h==0:
    zMena = input("Enter code of the currency you want to exchange: ")
    for m in short:
        if m == zMena.upper():
            h = 1
            break
    if h == 0:
        print("The entered currency is not in the list. Please try it again.")
    
mnozstvi = 0
h = 0
while h==0:
    mnozstvi = input("Enter amount of money you want to exchange: ")
    try:
        mnozstvi = float(mnozstvi.replace(",", "."))
        break
    except ValueError:
        print("Only numbers are allowed.")
dMena = ""
while h == 0:
    dMena = input("Enter code of the currency you want to exchange to: ")
    for m in short:
        if m == dMena.upper():
            h = 1
            break
    if h == 0:
        print("The entered currency is not in the list. Please try it again.")
            
# -------------     Výpočet
eurVal = 0
for x in range(len(name)):
    if short[x] == zMena.upper():
        eurVal = mnozstvi/float(price[x])
        break
vysledek = 0
for x in range(len(name)):
    if short[x] == dMena.upper():
        vysledek = eurVal*float(price[x])
        break
res = "{0} {1}   →   {2} EUR   →   {3} {4}"
print(res.format(mnozstvi, zMena.upper(), eurVal, vysledek, dMena.upper()))
