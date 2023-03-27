import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

try:
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
    r = requests.get(url)
    tablets = {"Item_No":[],"Item_Name":[],"Price":[],"Description":[],"Review":[]};

    soup = BeautifulSoup(r.text, "html.parser")
    boxes = soup.find("div",class_="col-md-9").find_all("div",class_="col-sm-4 col-lg-4 col-md-4")
    row = 1
    for box in boxes:
        name = box.find("a", class_="title").text
        price = box.find("h4", class_="pull-right price").text
        des = box.find("p",class_="description").text
        rating = box.find("div",class_="ratings").find("p",class_="pull-right").text
        tablets["Item_No"].append(row)
        tablets["Item_Name"].append(name)
        tablets["Price"].append(price)
        tablets["Description"].append(des)
        tablets["Review"].append(rating)

        row += 1

except Exception as e:
    print(e)

df = pd.DataFrame(data=tablets)
#print(df.head())

connection = sqlite3.connect("test1.db")
cursor = connection.cursor()
qry = "CREATE TABLE IF NOT EXISTS tablets(Item_No, Item_Name, Price, Description, Review)"
cursor.execute(qry)

for i in range(len(df)):
    cursor.execute("insert into tablets values (?,?,?,?,?)",df.iloc[i])

connection.commit()
connection.close()
