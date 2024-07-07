from bs4 import BeautifulSoup
import requests

response=requests.get("https://books.toscrape.com")
soup=BeautifulSoup(response.content,"html.parser")

books_element= soup.find_all('article', class_='product_pod')

books=[]
for book in books_element:
    titles = book.h3.a['title']
    price = book.find('p', class_='price_color').get_text().strip()
    rates  = book.p["class"][1]
    books.append({'title': titles, 'price': price , 'rate': rates})
if books:
    for book in books:
        print(f"Title: {book['title']}, Price: {book['price']} , Rate: {book['rate']}")
else:
    print("Failed to scrap the webpage.")