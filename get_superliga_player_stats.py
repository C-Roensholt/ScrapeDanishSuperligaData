#%%
import pickle
import time
import pandas as pd
from selenium import webdriver
from functools import reduce

import scrapers.scrape_player_stats as scraper

url = 'https://superliga.dk/stats/stats-21-22/'
option = webdriver.ChromeOptions()
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', options=option)

player_stats = scraper.get_all_player_stats(driver, url)

gameweek = input('Enter gameweek: ')
player_stats['gameweek'] = gameweek
player_stats.to_csv(f'data/player_stats.csv', mode='a', header=False)


exit()
#%%
# ------- Secure/stupid way to get all player stats ---------- #
url = 'https://superliga.dk/stats/stats-21-22/'
option = webdriver.ChromeOptions()
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', options=option)
player_overall_stats = scraper.get_player_overall_stats(driver, url)

option = webdriver.ChromeOptions()
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', options=option)
player_offensive_stats = scraper.get_player_offensive_stats(driver, url)

option = webdriver.ChromeOptions()
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', options=option)
player_goals_stats = scraper.get_player_goals_stats(driver, url)

option = webdriver.ChromeOptions()
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', options=option)
player_pass_stats = scraper.get_player_pass_stats(driver, url)

option = webdriver.ChromeOptions()
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', options=option)
player_defensive_stats = scraper.get_player_defensive_stats(driver, url)

option = webdriver.ChromeOptions()
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', options=option)

player_fitness_stats = scraper.get_player_fitness_stats(driver, url)
option = webdriver.ChromeOptions()
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', options=option)
player_goalkeeper_stats = scraper.get_player_goalkeeping_stats(driver, url)

#%%
# Data is splitted into outfield players and goalkeepers, as goalkeepers have different stats
dfs_goalkeeper = [player_overall_stats, player_offensive_stats, player_defensive_stats, player_fitness_stats,
                    player_goals_stats, player_goalkeeper_stats, player_pass_stats]

dfs_players = [player_overall_stats, player_offensive_stats, player_defensive_stats, player_fitness_stats,
                    player_goals_stats, player_pass_stats]

# Merge outfield and goalkeeper dataframes
df_goalkeeper_final = reduce(lambda left, right: pd.merge(left, right,
                                                            on=['player', 'club', 'matches'],
                                                            suffixes=['', '_y']), dfs_goalkeeper)
df_player_final = reduce(lambda left, right: pd.merge(left, right,
                                                        on=['player', 'club', 'matches'],
                                                        suffixes=['', '_y']), dfs_players)

# Remove duplicate columns
df_goalkeeper_final.drop(df_goalkeeper_final.filter(regex='_y$').columns.tolist(), axis=1, inplace=True)
df_player_final.drop(df_player_final.filter(regex='_y$').columns.tolist(), axis=1, inplace=True)

# Remove goalkeepers from player dataframe
df_player_final = df_player_final[~df_player_final['player'].isin(df_goalkeeper_final['player'])]

# add playing round and write to csv
gameweek = input('Enter gameweek: ')
df_player_final['gameweek'] = gameweek
df_player_final.to_csv(f'data/player_stats.csv', mode='a', header=False)