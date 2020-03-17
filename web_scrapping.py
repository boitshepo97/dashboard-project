# from BeautifulSoup import BeautifulSoup
# from selenium import webdriver
# import requests
# from requests import get
# import pandas as pd
# import itertools
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set()


# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# driver.get("<a class="heading" title="latest_figures.csv">
#     latest_figures.csv<span class="format-label" property="dc:format" data-format="csv">CSV</span></a>")

# content = driver.page_source
# soup = BeautifulSoup(content)

           
# from bs4 import BeautifulSoup
# import requests
# import csv

# url = 'https://data.humdata.org/dataset/reliefweb-crisis-figures'


# source = requests.get(url).text

# soup = BeautifulSoup(source, 'lxml')

# csv_file = open('Data_ ReliefWeb Crisis Figures Data - latest_figures.csv', 'w')

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['People in Need', 'Assistance Targeted' .])
# # stats_table = soup.find('tbody')
# # team,apps, wins,draws,losses,goals_for,goals_against, = [] ,[]
# for i in range(19):
#     for stats_table in soup.find_all('tbody'):
#         team = stats_table.select('tr')[i].select('td')[0].get_text(strip=True)
#         apps = stats_table.select('tr')[i].select('td')[1].get_text(strip=True)
           
import requests
from bs4 import BeautifulSoup

URL = 'https://data.humdata.org/dataset/reliefweb-crisis-figures'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('<a class="heading" title="latest_figures.csv">latest_figures.csv<span class="format-label" property="dc:format" data-format="csv">CSV</span></a>')