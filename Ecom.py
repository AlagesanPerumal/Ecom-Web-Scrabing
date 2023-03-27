import requests, openpyxl
from bs4 import BeautifulSoup
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Tablets"
sheet.append(["Item No","Item Name","Price","Description","Reviews"])
try:
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")
    boxes = soup.find("div",class_="col-md-9").find_all("div",class_="col-sm-4 col-lg-4 col-md-4")
    row = 1
    for box in boxes:
        name = box.find("a", class_="title").text
        price = box.find("h4", class_="pull-right price").text
        des = box.find("p",class_="description").text
        rating = box.find("div",class_="ratings").find("p",class_="pull-right").text
        sheet.append([row,name, price, des,rating])
        row += 1

except Exception as e:
    print(e)

excel.save("Ecommerce.xlsx")
