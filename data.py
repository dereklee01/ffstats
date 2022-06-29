# importing libraries
from turtle import xcor
from bs4 import BeautifulSoup
import requests
import pandas as pd

def collectData(configList, urlList, ptsList, playerNameList):

    """Creates beautifulsoup objects from constructed URLs 
    and obtains necessary data.

    For each position needed for the fantasy team, the necessary
    number of players for the respective year, season, and league
    scoring type are obtained. Player names are appended to the 
    'playerNameList'. Each player's name, team, and number of points
    scored are printed to the console. The total of points is also
    calculated from the points from each player stored in 'ptsList'
    and printed to the console.

    Args:
        configList: Python list that contains the year, week, scoring type, and position slots for the fantasy team.
        urlList: Python list that contains the URLs specific to each position.
        ptsList: Python list that contains the total points scored by the fantasy team's positions.
        playerNameList: Empty Python list that is initialized for use in collectData().

    Returns:
        None.
        Results from web scraping and data obtained are printed to the console.
    """

    for url in urlList:
        # ask hosting server to fetch the url
        pages = requests.get(url)
        # pages.text

        # parser-lxml = Change html to Python friendly format
        soup = BeautifulSoup(pages.text, "lxml")
        # soup

        # Obtain information from the table
        table1 = soup.find("table")
        # table1

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
            # limit is used to decrease processing time and find only the necessary number of players
            for j in table1.find_all("tr", limit=int(configList[2])+1)[1:]:
                row_data = j.find_all("td")
                row = [i.text for i in row_data]
                length = len(df)
                df.loc[length] = row

            # append each player's points scored to the respective total points variable
            for x in range(int(float(configList[2]))):
                ptsList[0] += float(df.iloc[x,len(df.loc[0])-1])
            
                # grabbing and printing the highest point output
                print("QB" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")
                
                # adding player name to the list
                playerNameList.append(df.iloc[x,1])

        elif "rb" in url:
            # limit is used to decrease processing time and find only the necessary number of players
            for j in table1.find_all("tr", limit=int(configList[3])+1)[1:]:
                row_data = j.find_all("td")
                row = [i.text for i in row_data]
                length = len(df)
                df.loc[length] = row
            
            # append each player's points scored to the respective total points variable
            for x in range(int(float(configList[3]))):
                ptsList[1] += float(df.iloc[x,len(df.loc[0])-1])
            
                # grabbing and printing the highest point output
                print("RB" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")
                
                # adding player name to the list
                playerNameList.append(df.iloc[x,1])

        elif "wr" in url:
            # limit is used to decrease processing time and find only the necessary number of players
            for j in table1.find_all("tr", limit=int(configList[4])+1)[1:]:
                row_data = j.find_all("td")
                row = [i.text for i in row_data]
                length = len(df)
                df.loc[length] = row
            
            # append each player's points scored to the respective total points variable
            for x in range(int(float(configList[4]))):
                ptsList[2] += float(df.iloc[x,len(df.loc[0])-1])
            
                # grabbing and printing the highest point output
                print("WR" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")

                # adding player name to the list
                playerNameList.append(df.iloc[x,1])

        elif "te" in url:
            # limit is used to decrease processing time and find only the necessary number of players
            for j in table1.find_all("tr", limit=int(configList[5])+1)[1:]:
                row_data = j.find_all("td")
                row = [i.text for i in row_data]
                length = len(df)
                df.loc[length] = row
            
            # append each player's points scored to the respective total points variable
            for x in range(int(float(configList[5]))):
                ptsList[3] += float(df.iloc[x,len(df.loc[0])-1])
            
                # grabbing and printing the highest point output
                print("TE" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")

                # adding player name to the list
                playerNameList.append(df.iloc[x,1])

        elif "flex" in url:
            # no limit used since there will be repeating WR/RB/TE in this list
            for j in table1.find_all("tr")[1:]:
                row_data = j.find_all("td")
                row = [i.text for i in row_data]
                length = len(df)
                df.loc[length] = row

            # initializing the position of the first flex player in the table to be identified for the results
            flexPos = 0

            # configList[6] determines the number of flex players being found in the for loop
            for y in range(int(float(configList[6]))):
                for x in range(len(df)):
                    playerName = df.iloc[x,1]
                    # if this player has not already been named a top WR/RB/TE, then he is a flex!
                    if playerName not in playerNameList:
                        flexPos = x
                        break

                # append each player's points scored to the respective total points variable
                ptsList[4] += float(df.iloc[flexPos,len(df.loc[0])-1])
                
                # grabbing and printing the highest point output
                print("FLEX" + str(y+1) + ": " + df.iloc[flexPos,1] + " " + df.iloc[flexPos,len(df.loc[0])-1] + " points")

                # adding player name to the list
                playerNameList.append(df.iloc[flexPos,1])

        elif "pk" in url:
            # limit is used to decrease processing time and find only the necessary number of players
            for j in table1.find_all("tr", limit=int(configList[7])+1)[1:]:
                row_data = j.find_all("td")
                row = [i.text for i in row_data]
                length = len(df)
                df.loc[length] = row

            # append each player's points scored to the respective total points variable
            for x in range(int(float(configList[7]))):
                ptsList[5] += float(df.iloc[x,len(df.loc[0])-1])
            
                # grabbing and printing the highest point output
                print("K" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")

                # adding player name to the list
                playerNameList.append(df.iloc[x,1])
        
        else:
            # limit is used to decrease processing time and find only the necessary number of players
            for j in table1.find_all("tr", limit=int(configList[8])+1)[1:]:
                row_data = j.find_all("td")
                row = [i.text for i in row_data]
                length = len(df)
                df.loc[length] = row

            # append each player's points scored to the respective total points variable
            for x in range(int(float(configList[8]))):
                ptsList[6] += float(df.iloc[x,len(df.loc[0])-1])
            
                # grabbing and printing the highest point output
                print("DEF" + str(x+1) + ": " + df.iloc[x,1] + " " + df.iloc[x,len(df.loc[0])-1] + " points")
                
                # adding player name to the list
                playerNameList.append(df.iloc[x,1])

    # initialize total number of points as zero
    total = 0
    # for loop through 'ptsList' and sum up the total points 
    for pts in ptsList:
        total += pts

    # print out results to the console
    print("\n")
    print("Max total points for the " + configList[0] + " season, Week " + configList[1] + ": " + str(total) + " " + configList[9].lower() + " points!")
    print("\n")