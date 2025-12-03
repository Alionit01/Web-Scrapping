import requests
from bs4 import BeautifulSoup

html = requests.get("https://books.toscrape.com/catalogue/category/books_1/index.html").text
soup = BeautifulSoup(html,"lxml")

books = soup.find_all("article", class_="product_pod")
prices = soup.find_all("p", class_="price_color")

for book, price in zip(books, prices):
    print("Name:",book.h3.text)
    print("Price:",price.text)
    print("------------------")






# html = requests.get("https://quotes.toscrape.com").text
# soup = BeautifulSoup(html, "lxml")
#
# quotes = soup.find_all("span", class_="text")
# authors = soup.find_all("small", class_="author")
#
# for quote, author in zip(quotes, authors):
#     print(quote.text)
#     print(author.text)
#     print("------------------")
