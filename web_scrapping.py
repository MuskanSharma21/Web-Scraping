from bs4 import BeautifulSoup
import requests
url = "https://www.amazon.in/s?k=mi+phone&sprefix=mi+pho%2Caps%2C298&ref=nb_sb_ss_ts-doa-p_2_6"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
product_containers = soup.find_all("div", class_="sg-col-inner")

for container in product_containers:
    
    title_element = container.find("span", class_="a-size-medium")
    if title_element:
        title = title_element.text.strip()
    else:
        continue

    
    price_element = container.find("span", class_="a-price-whole")
    if price_element:
        price = price_element.text.strip()
    else:
        continue

    
    rating_element = container.find("span", class_="a-icon-alt")
    if rating_element:
        rating = rating_element.text.strip()
    else:
        rating = "N/A"

    
    print("Title:", title)
    print("Price:", price)
    print("Rating:", rating)
    print("--------------------")
