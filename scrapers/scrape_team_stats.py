#%%
import pickle
import time
import pandas as pd

from selenium import webdriver
from functools import reduce


def get_team_overall_stats(driver, url, get_all=False):
    
    driver.get(url)
    time.sleep(3)

    team_overall_stats = pd.DataFrame(columns=[
                'club', 'goals', 'goals_against', 'ball_possession', 'shots_incl_blocked', 'successfull_pass_percentage',
                'chances_created', 'open_chances', 'meters_run', 'red', 'yellow'
                ])
    
    team_names = []
    team_stats = []

    # Get team names
    team_table = driver.find_element_by_class_name('players')
    rows = team_table.find_elements_by_class_name('name') # get all of the rows in the table

    for row in rows:
        team_names.append(row.text)
        
    # Get team stats
    stats_table = driver.find_element_by_class_name('stats-table')
    team_table = stats_table.find_elements_by_css_selector('tr')
    
    for team in team_table[1:]:
        team_stats.append(team.text.split(' '))

    team_overall_stats['club'] = team_names
    team_overall_stats[team_overall_stats.columns[1:]] = team_stats

    if get_all == False:
        driver.close()
    
    return team_overall_stats

def get_team_offensive_stats(driver, url, get_all=False):
    
    if get_all == False:
        driver.get(url)
    time.sleep(3)

    # Click button to offensive stats page
    button = driver.find_element_by_xpath(f"//button[text()='offensiv']")
    button.click()
    time.sleep(3)

    team_offensive_stats = pd.DataFrame(columns=[
        'club', 'goals', 'goals_percentage', 'xG', 'shots', 'shot_on_goal', 'shots_headers', 
        'shots_blocked', 'shots_on_post', 'shots_in_box', 'shots_outside_box'
    ])

    team_names = []
    team_stats = []

    # Get team names
    team_table = driver.find_element_by_class_name('players')
    rows = team_table.find_elements_by_class_name('name') # get all of the rows in the table

    for row in rows:
        team_names.append(row.text)

    # Get team stats
    stats_table = driver.find_element_by_class_name('stats-table')
    team_table = stats_table.find_elements_by_css_selector('tr')
    for team in team_table[1:]:
        team_stats.append(team.text.split(' '))

    team_offensive_stats['club'] = team_names
    team_offensive_stats[team_offensive_stats.columns[1:]] = team_stats
    
    if get_all == False:
        driver.close()

    return team_offensive_stats

def get_team_goals_stats(driver, url, get_all=False):

    if get_all == False:
        driver.get(url)
    time.sleep(3)

    # Click button to offensive stats page
    button = driver.find_element_by_xpath(f"//button[text()='Mål']")
    button.click()

    team_goals_stats = pd.DataFrame(columns=[
        'club', 'goals', 'goals_in_box', 'goals_outside_box', 'goals_freekick', 'goals_headers', 'goals_penalties', 
        'goals_fastbreak', 'goals_left_foot', 'goals_right_foot'
    ])

    time.sleep(3)

    team_names = []
    team_stats = []

    # Get team names
    team_table = driver.find_element_by_class_name('players')
    rows = team_table.find_elements_by_class_name('name') # get all of the rows in the table

    for row in rows:
        team_names.append(row.text)

    # Get team stats
    stats_table = driver.find_element_by_class_name('stats-table')
    team_table = stats_table.find_elements_by_css_selector('tr')
    for team in team_table[1:]:
        team_stats.append(team.text.split(' '))

    team_goals_stats['club'] = team_names
    team_goals_stats[team_goals_stats.columns[1:]] = team_stats
    
    if get_all == False:
        driver.close()
    
    return team_goals_stats

def get_team_pass_stats(driver, url, get_all=False):

    if get_all == False:
        driver.get(url)
    time.sleep(3)

    # Click button to offensive stats page
    button = driver.find_element_by_xpath(f"//button[text()='afleveringer']")
    button.click()
    time.sleep(3)
    
    team_pass_stats = pd.DataFrame(columns=[
        'club', 'passes', 'successfull_pass_percentage', 'long_passes', 'successfull_long_pass', 'successfull_pass_own_half_percentage',
        'successfull_pass_opp_half_percentage', 'forward_pass_percentage', 'backwards_pass_percentage', 'sideway_pass_percentage'
    ])

    team_names = []
    team_stats = []

    # Get team names
    team_table = driver.find_element_by_class_name('players')
    rows = team_table.find_elements_by_class_name('name') # get all of the rows in the table

    for row in rows:
        team_names.append(row.text)

    # Get team stats
    stats_table = driver.find_element_by_class_name('stats-table')
    team_table = stats_table.find_elements_by_css_selector('tr')
    for team in team_table[1:]:
        team_stats.append(team.text.split(' '))

    team_pass_stats['club'] = team_names
    team_pass_stats[team_pass_stats.columns[1:]] = team_stats

    if get_all == False:
        driver.close()

    return team_pass_stats

def get_team_defensive_stats(driver, url, get_all=False):

    if get_all == False:
        driver.get(url)
    time.sleep(3)

    # Click button to offensive stats page
    button = driver.find_element_by_xpath(f"//button[text()='defensiv']")
    button.click()
    time.sleep(3)

    team_defensiv_stats = pd.DataFrame(columns=[
        'club', 'interceptions', 'tackles', 'blocks', 'clearances', 'freekicks', 'ground_duels_won', 'aerial_duels_won'
    ])

    team_names = []
    team_stats = []

    # Get team names
    team_table = driver.find_element_by_class_name('players')
    rows = team_table.find_elements_by_class_name('name') # get all of the rows in the table

    for row in rows:
        team_names.append(row.text)

    # Get team stats
    stats_table = driver.find_element_by_class_name('stats-table')
    team_table = stats_table.find_elements_by_css_selector('tr')
    for team in team_table[1:]:
        team_stats.append(team.text.split(' '))

    team_defensiv_stats['club'] = team_names
    team_defensiv_stats[team_defensiv_stats.columns[1:]] = team_stats

    if get_all == False:
        driver.close()
    
    return team_defensiv_stats

def get_team_var_stats(driver, url, get_all=False):
    
    if get_all == False:
        driver.get(url)
    time.sleep(3)

    # Click button to offensive stats page
    button = driver.find_element_by_xpath(f"//button[text()='var']")
    button.click()
    time.sleep(3)

    team_var_stats = pd.DataFrame(columns=[
        'club', 'var_decisions', 'changed_goal', 'changed_no_goal', 'changed_penalty', 'changed_no_penalty',
        'red_card_awarded', 'red_card_changed', 'yellow_to_red', 'var_others'
    ])

    team_names = []
    team_stats = []

    # Get team names
    team_table = driver.find_element_by_class_name('players')
    rows = team_table.find_elements_by_class_name('name') # get all of the rows in the table

    for row in rows:
        team_names.append(row.text)

    # Get team stats
    stats_table = driver.find_element_by_class_name('stats-table')
    team_table = stats_table.find_elements_by_css_selector('tr')
    for team in team_table[1:]:
        team_stats.append(team.text.split(' '))

    team_var_stats['club'] = team_names
    team_var_stats[team_var_stats.columns[1:]] = team_stats

    if get_all == False:
        driver.close()
    
    return team_var_stats

def get_all_team_stats(driver, url):
    team_overall_stats = get_team_overall_stats(driver, url, get_all=True)
    time.sleep(5)
    team_offensive_stats = get_team_offensive_stats(driver, url, get_all=True)
    time.sleep(5)
    team_goals_stats = get_team_goals_stats(driver, url, get_all=True)
    time.sleep(5)
    team_pass_stats = get_team_pass_stats(driver, url, get_all=True)
    time.sleep(5)
    team_defensive_stats = get_team_defensive_stats(driver, url, get_all=True)
    time.sleep(5)
    team_var_stats = get_team_var_stats(driver, url, get_all=True)
    time.sleep(5)
    
    driver.close()
    
    # Create list of all dataframes
    df_all = [team_overall_stats, team_defensive_stats, team_goals_stats, team_offensive_stats, 
              team_var_stats, team_pass_stats]

    # Join all dataframes
    df_team_final = reduce(lambda left, right: pd.merge(left, right, on=['club'], suffixes=['', '_y']), df_all)
    df_team_final.drop(df_team_final.filter(regex='_y$').columns.tolist(),axis=1, inplace=True)
    
    return df_team_final