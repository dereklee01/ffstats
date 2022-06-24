# importing libraries
from turtle import xcor
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import config

configList, urlList, ptsList = config.config()
playerNameList = []

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

        for x in range(int(float(configList[2]))):
            ptsList[0] += float(df.iloc[x,len(df.loc[0])-1])
           
            # grabbing the highest point output
            print("QB" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")

            playerNameList.append(df.iloc[x,1])

    elif "rb" in url:
        # Create a for loop to fill mydata
        # all rows are located under the <tr> tags
        # all row items are located under the <td> tags
        for j in table1.find_all("tr", limit=int(configList[3])+1)[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            length = len(df)
            df.loc[length] = row

        for x in range(int(float(configList[3]))):
            ptsList[1] += float(df.iloc[x,len(df.loc[0])-1])
           
            # grabbing the highest point output
            print("RB" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")

            playerNameList.append(df.iloc[x,1])

    elif "wr" in url:
        # Create a for loop to fill mydata
        # all rows are located under the <tr> tags
        # all row items are located under the <td> tags
        for j in table1.find_all("tr", limit=int(configList[4])+1)[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            length = len(df)
            df.loc[length] = row

        for x in range(int(float(configList[4]))):
            ptsList[2] += float(df.iloc[x,len(df.loc[0])-1])
           
            # grabbing the highest point output
            print("WR" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")

            playerNameList.append(df.iloc[x,1])

    elif "te" in url:
        # Create a for loop to fill mydata
        # all rows are located under the <tr> tags
        # all row items are located under the <td> tags
        for j in table1.find_all("tr", limit=int(configList[5])+1)[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            length = len(df)
            df.loc[length] = row

        for x in range(int(float(configList[5]))):
            ptsList[3] += float(df.iloc[x,len(df.loc[0])-1])
           
            # grabbing the highest point output
            print("TE" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")

            playerNameList.append(df.iloc[x,1])

    elif "flex" in url:
        # Create a for loop to fill mydata
        # all rows are located under the <tr> tags
        # all row items are located under the <td> tags

        for j in table1.find_all("tr")[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            length = len(df)
            df.loc[length] = row

        flexPos = 0

        for y in range(int(float(configList[6]))):
            for x in range(len(df)):
                playerName = df.iloc[x,1]
                if playerName not in playerNameList:
                    flexPos = x
                    break

            ptsList[4] += float(df.iloc[flexPos,len(df.loc[0])-1])
            
            # grabbing the highest point output
            print("FLEX" + str(y+1) + ": " + df.iloc[flexPos,1] + " " + df.iloc[flexPos,len(df.loc[0])-1] + " points")

            playerNameList.append(df.iloc[flexPos,1])

    elif "pk" in url:
        # Create a for loop to fill mydata
        # all rows are located under the <tr> tags
        # all row items are located under the <td> tags
        for j in table1.find_all("tr", limit=int(configList[7])+1)[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            length = len(df)
            df.loc[length] = row

        for x in range(int(float(configList[7]))):
            ptsList[5] += float(df.iloc[x,len(df.loc[0])-1])
           
            # grabbing the highest point output
            print("K" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")

            playerNameList.append(df.iloc[x,1])
    
    else:
        # Create a for loop to fill mydata
        # all rows are located under the <tr> tags
        # all row items are located under the <td> tags
        for j in table1.find_all("tr", limit=int(configList[8])+1)[1:]:
            row_data = j.find_all("td")
            row = [i.text for i in row_data]
            length = len(df)
            df.loc[length] = row

        for x in range(int(float(configList[8]))):
            ptsList[6] += float(df.iloc[x,len(df.loc[0])-1])
           
            # grabbing the highest point output
            print("DEF" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")

            playerNameList.append(df.iloc[x,1])

total = 0
for pts in ptsList:
    total += pts

print("\n")
print("Max total points for the " + configList[0] + " season, Week " + configList[1] + ": " + str(total) + " points!")

# to-do: create new file for finding the correct players for each week; basically better file organization