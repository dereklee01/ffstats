# importing libraries
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

# grabbing user input for year, week, scoring preference, and team positions
year = input("Please input the year you are looking for.\n")
week = input("Please input the week you are looking for.\n")
# scoring = input("Standard or PPR scoring?")
qb = input("How many quarterback slots?\n")
rb = input("How many runningback slots?\n")
# wr = input("How many wide receiver slots?\n")
# flex = input("How many flex (WR/RB/TE) slots?\n")
# k = input("How many kicker slots?")
# defense = input("How many team defense slots?")

# concatenating and grabbing url string
url = 'https://www.footballguys.com/playerhistoricalstats?pos=qb&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
wrurl = 'https://www.footballguys.com/playerhistoricalstats?pos=wr&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'

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
for j in table1.find_all("tr")[1:]:
    row_data = j.find_all("td")
    row = [i.text for i in row_data]
    length = len(df)
    df.loc[length] = row

# grabbing the highest point output
print("QB: " + df.iloc[0,len(df.loc[0])-1])

# ask hosting server to fetch the url
pages = requests.get(wrurl)
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
for j in table1.find_all("tr")[1:]:
    row_data = j.find_all("td")
    row = [i.text for i in row_data]
    length = len(df)
    df.loc[length] = row

# grabbing the highest point output
print("WR1: " + df.iloc[0,len(df.loc[0])-1])
print("WR2: " + df.iloc[1,len(df.loc[0])-1])