import pandas
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib import parse
import pandas as pd

# url = "https://www.capterra.com/360-degree-feedback-software/"
# header = {
#   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#   'Accept-Encoding': 'none',
#   'Accept-Language': 'en-US,en;q=0.8',
#   'Connection': 'keep-alive',
#   'refere': 'https://example.com',
#   'cookie': """your cookie value ( you can get that from your web page) """
# }
#
#
# req = Request(url, headers=header)
# webpage = urlopen(req).read()

final_data = {
    "Product": [],
    "Link": [],
    "Description": [],
    "Rating": [],
    "By": [],
    "Category": []
}

with open("webpages/Best Advertising Agency Software.html") as file:
    webpage = file.read()

soup = BeautifulSoup(webpage, "html.parser")

products = soup.findAll("h2", attrs= {"data-testid": "product-name"})
for product in products:
    if product.text is None:
        final_data["Product"].append("NIL")
    else:
        final_data["Product"].append(product.text)



links = soup.find_all(name="a", attrs= {"data-testid": "product-header-link"})
for link in links:
    if link.get("href") is None:
        final_data["Link"].append("NIL")
    else:
        final_data["Link"].append(f"www.capterra.com{link.get('href')}")



ratings = soup.find_all(name="div", attrs= {"data-test-id": "start-rating-count"})
for rating in ratings:
    if rating.text is None:
        final_data["Rating"].append("NIL")
    else:
        final_data["Rating"].append(rating.text)
        # print(link.get('href'))


descriptions = soup.find_all(name="div", attrs= {"data-test-id": "product-description-container"})
for description in descriptions:
    if description.div.text is None:
        final_data["Description"].append("NIL")
    else:
        final_data["Description"].append(description.div.text)
        # print(f"{description.div.text}\n<br>\n")


# test = []
# img_links = soup.find_all(name="a", class_= "nb-thumbnail nb-relative nb-thumbnail-medium nb-thumbnail-interactive")
# for img_link in img_links:
#     if img_link.get('href') is True :
#         final_data["Product Page Link"].append(img_link.get('href'))
#     else:
#         final_data["Product Page Link"].append("NIL")
#     # test.append(img_link.get('href'))

# print(len(test))
author_companies = soup.find_all(name="h3")
for author_company in author_companies:
    if author_company.span is not None:
        final_data["By"].append(author_company.span.text)
        final_data["Category"].append("Advertising Agency Softwares")
        # print(author_company.span.text)

print(final_data)

df = pd.DataFrame(final_data)
df.to_csv("Advertising Agency Softwares.csv")


