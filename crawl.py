import json
import sys
from bs4 import BeautifulSoup
import requests
from serpapi.google_search import GoogleSearch

#search_input = 'Samsung zflip'
search_input = sys.argv[1]
search_query = search_input.replace(" ", '+')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# =========== GOOGLE SHOPPING =========== using SERPAPI
params = {
    "api_key": "db3de68874af1fa63f59ef58ef4443c64494af93f00a59302cbd5a11dcfe292a",
    "engine": "google",
    "q": search_input,
    "location_requested": "Seoul, Seoul, South Korea",
    "location_used": "Seoul,Seoul,South Korea",
    "tbm": "shop"
}

search = GoogleSearch(params)
results = search.get_dict()

item = results['shopping_results'][0]

try:
    title_google = item["title"]
except:
    title_google = "N/A"

try:
    picture_google = item["thumbnail"]
except:
    picture_google = "N/A"

try:
    a_google = item["product_link"]
except:
    a_google = "N/A"

try:
    price_google = item["extracted_price"]
except:
    price_google = "N/A"

try:
    rating_google = item["rating"]
except:
    rating_google = "N/A"

try:
    reviews_google = item["reviews"]
except:
    reviews_google = "N/A"


# =========== COUPANG ===========
link_coupang = 'https://www.coupang.com/np/search?component=&q=' + \
    search_query + '&channel=user'
source_coupang = requests.get(link_coupang, headers=headers)
source_coupang.raise_for_status()
soup_coupang = BeautifulSoup(source_coupang.text, 'lxml')

# gets the second item from the product list because the first one is always an ad and may not be the product searched
item_coupang = soup_coupang.find('ul', {"id": "productList"}).find_all('li')[1]
title_coupang = item_coupang.find('div', class_='name').text
picture_coupang = item_coupang.img['src']
a_coupang = 'http://coupang.com' + \
    item_coupang.find('a', class_='search-product-link')['href']
price_coupang = item_coupang.find('strong', class_='price-value').text

try:
    reviews_coupang = item_coupang.find(
        'span', class_='rating-total-count').text[1:-1]  # returns with
except:
    reviews_coupang = "N/A"

try:
    rating_coupang = item_coupang.find('em', class_='rating').text
except:
    rating_coupang = "N/A"
# =========== SSG ===========
search_query_ssg = search_input.replace(" ", '%20')
link_ssg = 'http://www.ssg.com/search.ssg?target=all&query=' + \
    search_query_ssg

source_ssg = requests.get(link_ssg, headers=headers).text
soup_ssg = BeautifulSoup(source_ssg, 'lxml')

item_ssg = soup_ssg.find('ul', {"id": "idProductImg"}).find('li')
title_ssg = item_ssg.find('em', class_='tx_en').text
picture_ssg = item_ssg.img['src']
a_ssg = 'http://www.ssg.com/' + \
    item_ssg.find('div', class_='cunit_info').find('a')['href']
price_ssg = item_ssg.find('div', class_='cunit_price notranslate').find(
    'em', class_='ssg_price').text

try:
    reviews_ssg = item_ssg.find('span', class_='rate_tx').find('em').text
except:
    reviews_ssg = "N/A"

try:
    rating_ssg = item_ssg.find('div', class_='rating').find(
        'span', class_="blind").text[3:-1]
except:
    rating_ssg = "N/A"
# # =========== Setting up JSON file ===========

# add review, star, brannd

data = [{
    "title": title_google,
    "picture": picture_google,
    "link": a_google,
    "price": price_google,
    "rating": rating_google,
        "reviews": reviews_google
        },
        {
    "title": title_coupang,
        "picture": picture_coupang,
        "link": a_coupang,
        "price": price_coupang,
        "rating": rating_coupang,
        "reviews": reviews_coupang
        },
        {
        "title": title_ssg,
        "picture": picture_ssg,
        "link": a_ssg,
        "price": price_ssg,
        "rating": rating_ssg,
        "reviews": reviews_ssg
        }
        ]

print(json.dumps(data, indent=2))
