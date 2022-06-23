# importing libraries
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import config

configList, urlList, ptsList = config.config()

for url in urlList:
    # ask hosting server to fetch the url
    pages = requests.get(url)
    pages.text

    # parser-lxml = Change html to Python friendly format
    soup = BeautifulSoup(pages.text, "lxml")
    soup

    # Obtain information from the table
    table1 = soup.find("table")
    table1

    # Obtain every title of columns with tag <th>
    # start with an empty list
    headers = []
    # for loop to iterate through all <th> tags
    for i in table1.find_all("th"):
        title = i.text
        headers.append(title)

    # Create a pandas dataframe
    df = pd.DataFrame(columns = headers)

    # Create a for loop to fill mydata
    # all rows are located under the <tr> tags
    # all row items are located under the <td> tags

    if "qb" in url:
        # limit is used to decrease processing time and find only the necessary number of qb
        for j in table1.find_all("tr", limit=int(configList[2])+1)[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            length = len(df)
            df.loc[length] = row

        ptsList[0] = float(df.iloc[0,len(df.loc[0])-1])

        # grabbing the highest point output
        print("QB: " + df.iloc[0,1] + " " + df.iloc[0,len(df.loc[0])-1] + " points")
    else:
        # Create a for loop to fill mydata
        # all rows are located under the <tr> tags
        # all row items are located under the <td> tags
        for j in table1.find_all("tr", limit=int(configList[3])+1)[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            length = len(df)
            df.loc[length] = row

        ptsList[1] = float(df.iloc[0,len(df.loc[0])-1]) + float(df.iloc[1,len(df.loc[0])-1])

        # grabbing the highest point output
        print("WR1: " + df.iloc[0,1] + " " + df.iloc[0,len(df.loc[0])-1] + " points")
        print("WR2: " + df.iloc[1,1] + " " + df.iloc[1,len(df.loc[0])-1] + " points")

print(ptsList)
total = 0
for pts in ptsList:
    total += pts

print("\n")
print("Total points for the " + configList[0] + " season, Week " + configList[1] + ": " + str(total) + " points!")
