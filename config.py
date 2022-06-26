# importing libraries
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd


def config():

    """Retrieves input information from the user and constructs URLs.

    Football season year and week are obtained from the user. 
    Team position numbers are also obtained, then constructed
    into URLs. Lists of position slot numbers, URLs, and total 
    points per position are organized into Python lists and passed
    into the collectData function.

    Args:
        None

    Returns:
        configList: Python list that contains the year, week, and position slots for the fantasy team.
        urlList: Python list that contains the URLs specific to each position.
        ptsList: Python list that contains the total points scored by the fantasy team's positions.
        playerNameList: Empty Python list that is initialized for use in collectData().
    
    """

    # grabbing user input for year, week, scoring preference, and team positions
    year = input("Please input the year you are looking for.\n")
    week = input("Please input the week you are looking for.\n")
    # scoring = input("Standard or PPR scoring?")
    qb = input("How many quarterback slots?\n")
    rb = input("How many runningback slots?\n")
    wr = input("How many wide receiver slots?\n")
    te = input("How many tight end slots?\n")
    flex = input("How many flex (WR/RB/TE) slots?\n")
    k = input("How many kicker slots?\n")
    defense = input("How many team defense slots?\n")

    # concatenating and grabbing url string
    url = 'https://www.footballguys.com/playerhistoricalstats?pos=qb&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
    rburl = 'https://www.footballguys.com/playerhistoricalstats?pos=rb&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
    wrurl = 'https://www.footballguys.com/playerhistoricalstats?pos=wr&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
    teurl = 'https://www.footballguys.com/playerhistoricalstats?pos=te&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
    flexurl = 'https://www.footballguys.com/playerhistoricalstats?pos=flex&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
    kurl = 'https://www.footballguys.com/playerhistoricalstats?pos=pk&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'
    defurl = 'https://www.footballguys.com/playerhistoricalstats?pos=td&yr=' + year + '&startwk=' + week + '&stopwk=' + week + '&profile=p'

    qbPts, rbPts, wrPts, tePts, flexPts, kPts, defPts = 0, 0, 0, 0, 0, 0, 0

    configList, urlList, ptsList = [year, week, qb, rb, wr, te, flex, k, defense], [url, rburl, wrurl, teurl, flexurl, kurl, defurl], [qbPts, rbPts, wrPts, tePts, flexPts, kPts, defPts]
    playerNameList = []

    return configList, urlList, ptsList, playerNameList