# importing libraries
from turtle import xcor
from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import config
import data

configList, urlList, ptsList, playerNameList = config.config()

data.collectData(configList, urlList, ptsList, playerNameList)