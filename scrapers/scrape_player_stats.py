#%%
import pickle
import time
import pandas as pd

from selenium import webdriver
from functools import reduce

def get_player_overall_stats(driver, url, get_all=False):
    
    driver.get(url)
    time.sleep(3)
    
    # change to player stats
    player_button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/article/div[2]/div/div/section[1]/div/div[1]/div/div/a[2]').click()
    time.sleep(3)
    
    # get number of player pages
    pages = driver.find_element_by_class_name('pagination').text
    max_page = pages.split('.')[-1]
    
    # get player stats
    player_overall_stats = pd.DataFrame(columns=[
            'player', 'club', 'matches', 'minutes', 'goals', 'assist', 'started', 'substituted', 
            'meters_run', 'red', 'yellow'
        ])

    player_names = []
    player_stats = []
    for i in range(1, int(max_page)+1):
        if i != 1:
            # Click to next page
            button = driver.find_element_by_xpath(f"//button[text()={str(i)}]")
            button.click()
            time.sleep(5)

        # Get player names
        players_table = driver.find_element_by_class_name('players')
        rows = players_table.find_elements_by_class_name('name') # get all of the rows in the table

        for row in rows:
            player_names.append(row.text)

        # Get player stats
        stats_table = driver.find_element_by_class_name('stats-table')
        player_table = stats_table.find_elements_by_css_selector('tr')
        for player in player_table[1:]:
            player_stats.append(player.text.split(' '))

    player_overall_stats['player'] = player_names
    player_overall_stats[player_overall_stats.columns[1:]] = player_stats
    
    if get_all == False:
        driver.close()
    
    return player_overall_stats

def get_player_offensive_stats(driver, url, get_all=False):
    
    if get_all == False:
        driver.get(url)
    time.sleep(3)
    
    # change to player stats
    if get_all == False:
        player_button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/article/div[2]/div/div/section[1]/div/div[1]/div/div/a[2]').click()
        time.sleep(3)
    
    # Click button to offensive stats page
    button = driver.find_element_by_xpath(f"//button[text()='offensiv']")
    button.click()
    
    # get number of player pages
    pages = driver.find_element_by_class_name('pagination').text
    max_page = pages.split('.')[-1]

    player_offensive_stats = pd.DataFrame(columns=[
        'player', 'club', 'matches', 'shots', 'goals', 'goals_percentage', 'xG', 'chances_created', 'open_chances', 
        'assist', 'succesfull_pass_percentage'
    ])

    time.sleep(3)

    player_names = []
    player_stats = []
    for i in range(1, int(max_page)+1):
        if i != 1:
            # Click to next page
            button = driver.find_element_by_xpath(f"//button[text()={str(i)}]")
            button.click()

            time.sleep(5)

        # Get player names
        players_table = driver.find_element_by_class_name('players')
        rows = players_table.find_elements_by_class_name('name') # get all of the rows in the table

        for row in rows:
            player_names.append(row.text)
        #player_overall_stats['player'] = player_names

        # Get player stats
        stats_table = driver.find_element_by_class_name('stats-table')
        player_table = stats_table.find_elements_by_css_selector('tr')
        for player in player_table[1:]:
            player_stats.append(player.text.split(' '))

    player_offensive_stats['player'] = player_names
    player_offensive_stats[player_offensive_stats.columns[1:]] = player_stats
    
    if get_all == False:
        driver.close()
    
    return player_offensive_stats

def get_player_goals_stats(driver, url, get_all=False):
    
    if get_all == False:
        driver.get(url)
    time.sleep(3)
    
    # change to player stats
    if get_all == False:
        player_button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/article/div[2]/div/div/section[1]/div/div[1]/div/div/a[2]').click()
        time.sleep(3)
    
    # Click button to goals stats page
    button = driver.find_element_by_xpath(f"//button[text()='Mål']")
    button.click()

    # get number of player pages
    pages = driver.find_element_by_class_name('pagination').text
    max_page = pages.split('.')[-1]

    player_goals_stats = pd.DataFrame(columns=[
                'player', 'club', 'matches', 'goals', 'goals_in_box', 'goals_outside_box', 'goals_freekick', 
                'goals_headers', 'goals_pen', 'goals_left_foot', 'goals_right_foot',
            ])

    time.sleep(3)

    player_names = []
    player_stats = []
    
    for i in range(1, int(max_page)+1):
        if i != 1:
            # Click to next page
            button = driver.find_element_by_xpath(f"//button[text()={str(i)}]")
            button.click()

            time.sleep(5)

        # Get player names
        players_table = driver.find_element_by_class_name('players')
        rows = players_table.find_elements_by_class_name('name') # get all of the rows in the table

        for row in rows:
            player_names.append(row.text)

        # Get player stats
        stats_table = driver.find_element_by_class_name('stats-table')
        player_table = stats_table.find_elements_by_css_selector('tr')
        for player in player_table[1:]:
            player_stats.append(player.text.split(' '))

    player_goals_stats['player'] = player_names
    player_goals_stats[player_goals_stats.columns[1:]] = player_stats
    
    if get_all == False:
        driver.close()
    
    return player_goals_stats
    
def get_player_pass_stats(driver, url, get_all=False):
    
    if get_all == False:
        driver.get(url)
    time.sleep(3)
    
    # change to player stats
    if get_all == False:
        player_button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/article/div[2]/div/div/section[1]/div/div[1]/div/div/a[2]').click()
        time.sleep(3)
    
    # Click button to passing stats page
    button = driver.find_element_by_xpath(f"//button[text()='Afleveringer']")
    button.click()

    # get number of player pages
    pages = driver.find_element_by_class_name('pagination').text
    max_page = pages.split('.')[-1]

    player_pass_stats = pd.DataFrame(columns=[
                'player', 'club', 'matches', 'passes', 'completed_pass_percentage', 'long_passes', 'long_passes_percentage', 
                'succesfull_pass_own_half_percentage', 'succesfull_pass_opp_half_percentage', 
                'forward_pass_percentage', 'backwards_pass_percentage', 'sideway_passes_percentage'
            ])

    time.sleep(3)

    player_names = []
    player_stats = []
    for i in range(1, int(max_page)+1):
        if i != 1:
            # Click to next page
            button = driver.find_element_by_xpath(f"//button[text()={str(i)}]")
            button.click()

            time.sleep(5)

        # Get player names
        players_table = driver.find_element_by_class_name('players')
        rows = players_table.find_elements_by_class_name('name') # get all of the rows in the table

        for row in rows:
            player_names.append(row.text)
        #player_overall_stats['player'] = player_names

        # Get player stats
        stats_table = driver.find_element_by_class_name('stats-table')
        player_table = stats_table.find_elements_by_css_selector('tr')
        for player in player_table[1:]:
            player_stats.append(player.text.split(' '))

    player_pass_stats['player'] = player_names
    player_pass_stats[player_pass_stats.columns[1:]] = player_stats
    
    if get_all == False:
        driver.close()
        
    return player_pass_stats
    
    
def get_player_defensive_stats(driver, url, get_all=False):
    
    if get_all == False:
        driver.get(url)
    time.sleep(3)
    
    # change to player stats
    if get_all == False:
        player_button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/article/div[2]/div/div/section[1]/div/div[1]/div/div/a[2]').click()
        time.sleep(3)
    
    # Click button to defensive stats page
    button = driver.find_element_by_xpath(f"//button[text()='defensiv']")
    button.click()

    # get number of player pages
    pages = driver.find_element_by_class_name('pagination').text
    max_page = pages.split('.')[-1]

    player_defensive_stats = pd.DataFrame(columns=[
                'player', 'club', 'matches', 'clearances', 'blocks', 'interceptions', 'tackles', 
                'ground_duels_won', 'aerial_duels_won', 
            ])

    time.sleep(3)

    player_names = []
    player_stats = []
    for i in range(1, int(max_page)+1):
        if i != 1:
            # Click to next page
            button = driver.find_element_by_xpath(f"//button[text()={str(i)}]")
            button.click()

            time.sleep(5)

        # Get player names
        players_table = driver.find_element_by_class_name('players')
        rows = players_table.find_elements_by_class_name('name') # get all of the rows in the table

        for row in rows:
            player_names.append(row.text)

        # Get player stats
        stats_table = driver.find_element_by_class_name('stats-table')
        player_table = stats_table.find_elements_by_css_selector('tr')
        for player in player_table[1:]:
            player_stats.append(player.text.split(' '))

    player_defensive_stats['player'] = player_names
    player_defensive_stats[player_defensive_stats.columns[1:]] = player_stats
    
    if get_all == False:
        driver.close()
    
    return player_defensive_stats
    
    
def get_player_fitness_stats(driver, url, get_all=False):
    
    if get_all == False:
        driver.get(url)
    time.sleep(3)
    
    # change to player stats
    if get_all == False:
        player_button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/article/div[2]/div/div/section[1]/div/div[1]/div/div/a[2]').click()
        time.sleep(3)
    
    # Click button to offensive stats page
    button = driver.find_element_by_xpath(f"//button[text()='fitness']")
    button.click()

    # get number of player pages
    pages = driver.find_element_by_class_name('pagination').text
    max_page = pages.split('.')[-1]

    player_fitness_stats = pd.DataFrame(columns=[
                'player', 'club', 'matches', 'minutes', 'meters_run', 'sprints', 'top_speed', 'average_speed', 'run_high_speed'
            ])

    time.sleep(3)

    player_names = []
    player_stats = []
    for i in range(1, int(max_page)+1):
        if i != 1:
            # Click to next page
            button = driver.find_element_by_xpath(f"//button[text()={str(i)}]")
            button.click()

            time.sleep(5)

        # Get player names
        players_table = driver.find_element_by_class_name('players')
        rows = players_table.find_elements_by_class_name('name') # get all of the rows in the table

        for row in rows:
            player_names.append(row.text)

        # Get player stats
        stats_table = driver.find_element_by_class_name('stats-table')
        player_table = stats_table.find_elements_by_css_selector('tr')
        for player in player_table[1:]:
            player_stats.append(player.text.split(' '))

    player_fitness_stats['player'] = player_names
    player_fitness_stats[player_fitness_stats.columns[1:]] = player_stats
    
    if get_all == False:
        driver.close()
    
    return player_fitness_stats
    
def get_player_goalkeeping_stats(driver, url, get_all=False):
    
    if get_all == False:
        driver.get(url)
    time.sleep(3)
    
    # change to player stats
    if get_all == False:
        player_button = driver.find_element_by_xpath('//*[@id="__layout"]/div/div/article/div[2]/div/div/section[1]/div/div[1]/div/div/a[2]').click()
        time.sleep(3)
    
    # Click button to offensive stats page
    button = driver.find_element_by_xpath(f"//button[text()='målmand']")
    button.click()

    # get number of player pages
    pages = driver.find_element_by_class_name('pagination').text
    max_page = pages[-1]
    
    player_goalkeeper_stats = pd.DataFrame(columns=[
            'player', 'club', 'matches', 'goals_against', 'shot_against', 'saves', 'save_percentage', 'clean_sheets',
            'saves_from_shots_in_box', 'saves_from_outside_box', 'balls_catched', 'balls_punched',
        ])

    time.sleep(3)

    player_names = []
    player_stats = []
    for i in range(1, int(max_page)+1):
        if i != 1:
            # Click to next page
            button = driver.find_element_by_xpath(f"//button[text()={str(i)}]")
            button.click()

            time.sleep(5)

        # Get player names
        players_table = driver.find_element_by_class_name('players')
        rows = players_table.find_elements_by_class_name('name') # get all of the rows in the table

        for row in rows:
            player_names.append(row.text)

        # Get player stats
        stats_table = driver.find_element_by_class_name('stats-table')
        player_table = stats_table.find_elements_by_css_selector('tr')
        for player in player_table[1:]:
            player_stats.append(player.text.split(' '))

    player_goalkeeper_stats['player'] = player_names
    player_goalkeeper_stats[player_goalkeeper_stats.columns[1:]] = player_stats
    
    if get_all == False:
        driver.close()

    return player_goalkeeper_stats

def get_all_player_stats(driver, url):
    player_overall_stats = get_player_overall_stats(driver, url, get_all=True)
    time.sleep(5)
    player_offensive_stats = get_player_offensive_stats(driver, url, get_all=True)
    time.sleep(5)
    player_goals_stats = get_player_goals_stats(driver, url, get_all=True)
    time.sleep(5)
    player_pass_stats = get_player_pass_stats(driver, url, get_all=True)
    time.sleep(5)
    player_defensive_stats = get_player_defensive_stats(driver, url, get_all=True)
    time.sleep(5)
    player_fitness_stats = get_player_fitness_stats(driver, url, get_all=True)
    time.sleep(5)
    player_goalkeeper_stats = get_player_goalkeeping_stats(driver, url, get_all=True)
    time.sleep(5)
    
    driver.close()
    
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

    return df_player_final, df_goalkeeper_final