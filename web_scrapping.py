from bs4 import BeautifulSoup
import requests
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

url = 'https://data.humdata.org/dataset/reliefweb-crisis-figures'

source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

# csv_file = open('epl_stats_2.csv', 'w')

# csv_writer = csv.writer(csv_file)