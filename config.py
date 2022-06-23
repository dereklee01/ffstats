# importing libraries
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

def config():
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

    return [year, week, qb, rb], [url, wrurl]