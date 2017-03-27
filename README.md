# Web scraper to access market prices from Yahoo finance

Data source: Yahoo Finance Goal: Run fundamental analysis on public stock data to understand potential investments

Necessary Modules:
- Utilizing built in urllib
- BeautifulSoup4

The goal of this is to create a process to scrape data from Yahoo Finance for stock prices but later expand to gathering fundamental data (Ex: P/B Ratios, P/E, Book Values, Market Cap, etc.). This is done through BeautifulSoup4, so even though it's probably a terrible way to gather market prices, the ability to scrape pages for material is wonderful.

Improvements: Possibly could utilize Yahoo Finance API to make things easier. The script executes extremely slow, so speed would be an issue especially if we were scanning 20+ tickers. 
