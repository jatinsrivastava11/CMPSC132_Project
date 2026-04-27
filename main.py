import requests
from bs4 import BeautifulSoup

def fetch():
    base = "https://xoticpc.com/collections/custom-gaming-laptops-notebooks"

    response = requests.get(
            base,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
            },
        )

    soup = BeautifulSoup(response.text, "html.parser")

    cards = soup.find_all("li", class_="column")
    for card in cards:
        title = card.find("a", class_="product-card-title")
        price = card.find("span", class_="amount")
        rating = card.find_all("span", class_="jdgm--on")

        if title:
            title = title.text.strip()
        if price:
            price = price.text.strip()
        rating = len(rating)

        yield (title, price, rating)

def main():
    for laptop in fetch():
        print("Name: ", laptop[0])
        print("Price: ", laptop[1])
        print("Rating: ", laptop[2])

def search(query):
    for laptop in fetch():
        if query.lower() in laptop[0].lower():
            print("Name: ", laptop[0])
            print("Price: ", laptop[1])
            print("Rating: ", laptop[2])

def filter_rating(query):
    for laptop in fetch():
        if float(query) <= laptop[2]:
            print("Name: ", laptop[0])
            print("Price: ", laptop[1])
            print("Rating: ", laptop[2])

def filter_price(query):
    for laptop in fetch():
        if laptop[1] and float(query) >= float(''.join(laptop[1][1:].split(","))):
            print("Name: ", laptop[0])
            print("Price: ", laptop[1])
            print("Rating: ", laptop[2])

main()

k = 0
while k == 0:
    print("filter by price [P] ; filter by rating [R] ; search [S] ; end [E]")
    ask = input("choose one: ").upper()
    if ask == "P":
        query = input("enter highest price: ")
        filter_price(query)
    elif ask == "R":
        query = input("enter lowest rating: ")
        filter_rating(query)
    elif ask == "S":
        query = input("enter brand name: ")
        search(query)
    elif ask == "E":
        k = 1
    else:
        print("wrong input")