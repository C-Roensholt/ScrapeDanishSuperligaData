#%%
import pickle
import time
import pandas as pd
from selenium import webdriver
from functools import reduce

import scrapers.scrape_team_stats as scraper


url = 'https://superliga.dk/stats/stats-21-22/'
option = webdriver.ChromeOptions()
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', options=option)

team_stats = scraper.get_all_team_stats(driver, url)

# add playing round
gameweek = input('Enter gameweek: ')
team_stats['gameweek'] = gameweek
team_stats.to_csv(f'data/team_stats.csv', mode='a', header=False)