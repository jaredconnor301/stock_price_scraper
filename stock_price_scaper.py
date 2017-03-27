from bs4 import BeautifulSoup
import urllib

sp500short = ['a', 'aa', 'aapl', 'abbv', 'abc', 'abt', 'ace', 'aci', 'acn', 'act', 'adbe', 'adi', 'adm', 'adp']

for stock in sp500short:
    #Specify the url
    quotes_page = "https://finance.yahoo.com/quote/" + stock

    #Query the website and return the HTML to the variable 'page'
    page = urllib.urlopen(quotes_page)

    #Parse the query 'page' using BeautifulSoup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    #Take out the <span> to return price data inside of container
    price_box = soup.find('span', attrs={'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    name_box = soup.find('h1', attrs={'class': 'D(ib) Fz(18px)'})

    #Strip all remaining container to get the price data
    name = name_box.text.split('(')[1].strip(')')
    price = price_box.text.strip()

    print name
    print price
