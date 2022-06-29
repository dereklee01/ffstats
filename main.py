# importing
import config
import data

# Obtaining the lists necessary to web scrape data
configList, urlList, ptsList, playerNameList = config.config()
# Collecting all results and then printing them back to the console
data.collectData(configList, urlList, ptsList, playerNameList)

# TODO: find Python function that checks strings regardless of upper/lowercase for ppr/standard inputs by user
# TODO: check out possible 0.5 PPR scoring for players
# TODO: look into creating a GUI(?) and making an actual popup appear for the app 
# TODO: once a week's highest scoring player names are obtained, try to also get their pictures to pop up with points next to them