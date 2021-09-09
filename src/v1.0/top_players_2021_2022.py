# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#--------------------------------------------------------PLAYERS--------------------------------------------------------------


## Stage 1: REST API call 

import requests 
import pandas as pd
import csv
import os



############################################# 1. PREMIER LEAGUE ##############################################




####### ARSENAL ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"42","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
arsenal_players1 = pd.DataFrame()

arsenal_players1['name'] = df_p1['name']
arsenal_players1['first_name'] = df_p1['firstname']
arsenal_players1['last_name'] = df_p1['lastname']
arsenal_players1['id'] = df_p1['id']
arsenal_players1['team'] = player_team['name']
arsenal_players1['team_id'] = player_team['id']
arsenal_players1['league'] = player_league['name']
arsenal_players1['league_id'] = player_league['id']
arsenal_players1['age'] = df_p1['age']
arsenal_players1['birth'] = player_birth['date']
arsenal_players1['nationality'] = df_p1['nationality']
arsenal_players1['app'] = player_games['appearences']
arsenal_players1['mins'] = player_games['minutes']
arsenal_players1['goals'] = player_goals['total']
arsenal_players1['shots'] = player_shots['total']
arsenal_players1['shots_on_target'] = player_shots['on']
arsenal_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
arsenal_players1['assists'] = player_goals['assists']
arsenal_players1['passes'] = player_passes['total']
arsenal_players1['passes_completed'] = player_passes['accuracy']
# arsenal_players1['pass_accuracy_%'] = df_p1['name']
arsenal_players1['dribbles'] = player_dribbles['attempts']
arsenal_players1['dribbles_completed'] = player_dribbles['success']
arsenal_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
arsenal_players1['tackles'] = player_tackles['total']
arsenal_players1['blocks'] = player_tackles['blocks']
arsenal_players1['interceptions'] = player_tackles['interceptions']
arsenal_players1['fouls_drawn'] = player_fouls['drawn']
arsenal_players1['fouls_committed'] = player_fouls['committed']
arsenal_players1['yellow_cards'] = player_cards['yellow']
arsenal_players1['red_cards'] = player_cards['red']
arsenal_players1['yellow_to_red_cards'] = player_cards['yellowred']
arsenal_players1['sub_in'] = player_subs['in']
arsenal_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
arsenal_players1 = arsenal_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"42","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
arsenal_players2 = pd.DataFrame()

arsenal_players2['name'] = df_p1['name']
arsenal_players2['first_name'] = df_p1['firstname']
arsenal_players2['last_name'] = df_p1['lastname']
arsenal_players2['id'] = df_p1['id']
arsenal_players2['team'] = player_team['name']
arsenal_players2['team_id'] = player_team['id']
arsenal_players2['league'] = player_league['name']
arsenal_players2['league_id'] = player_league['id']
arsenal_players2['age'] = df_p1['age']
arsenal_players2['birth'] = player_birth['date']
arsenal_players2['nationality'] = df_p1['nationality']
arsenal_players2['app'] = player_games['appearences']
arsenal_players2['mins'] = player_games['minutes']
arsenal_players2['goals'] = player_goals['total']
arsenal_players2['shots'] = player_shots['total']
arsenal_players2['shots_on_target'] = player_shots['on']
arsenal_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
arsenal_players2['assists'] = player_goals['assists']
arsenal_players2['passes'] = player_passes['total']
arsenal_players2['passes_completed'] = player_passes['accuracy']
# arsenal_players2['pass_accuracy_%'] = df_p1['name']
arsenal_players2['dribbles'] = player_dribbles['attempts']
arsenal_players2['dribbles_completed'] = player_dribbles['success']
arsenal_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
arsenal_players2['tackles'] = player_tackles['total']
arsenal_players2['blocks'] = player_tackles['blocks']
arsenal_players2['interceptions'] = player_tackles['interceptions']
arsenal_players2['fouls_drawn'] = player_fouls['drawn']
arsenal_players2['fouls_committed'] = player_fouls['committed']
arsenal_players2['yellow_cards'] = player_cards['yellow']
arsenal_players2['red_cards'] = player_cards['red']
arsenal_players2['yellow_to_red_cards'] = player_cards['yellowred']
arsenal_players2['sub_in'] = player_subs['in']
arsenal_players2['sub_out'] = player_subs['out']

arsenal_players2 = arsenal_players2.fillna(0)



# Stage 3: Append More Player Data   


API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"42","season":"2021","page":"3"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)


# Create data frame for the first set of imported players 
arsenal_players3 = pd.DataFrame()

arsenal_players3['name'] = df_p1['name']
arsenal_players3['first_name'] = df_p1['firstname']
arsenal_players3['last_name'] = df_p1['lastname']
arsenal_players3['id'] = df_p1['id']
arsenal_players3['team'] = player_team['name']
arsenal_players3['team_id'] = player_team['id']
arsenal_players3['league'] = player_league['name']
arsenal_players3['league_id'] = player_league['id']
arsenal_players3['age'] = df_p1['age']
arsenal_players3['birth'] = player_birth['date']
arsenal_players3['nationality'] = df_p1['nationality']
arsenal_players3['app'] = player_games['appearences']
arsenal_players3['mins'] = player_games['minutes']
arsenal_players3['goals'] = player_goals['total']
arsenal_players3['shots'] = player_shots['total']
arsenal_players3['shots_on_target'] = player_shots['on']
arsenal_players3['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
arsenal_players3['assists'] = player_goals['assists']
arsenal_players3['passes'] = player_passes['total']
arsenal_players3['passes_completed'] = player_passes['accuracy']
# arsenal_players3['pass_accuracy_%'] = df_p1['name']
arsenal_players3['dribbles'] = player_dribbles['attempts']
arsenal_players3['dribbles_completed'] = player_dribbles['success']
arsenal_players3['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
arsenal_players3['tackles'] = player_tackles['total']
arsenal_players3['blocks'] = player_tackles['blocks']
arsenal_players3['interceptions'] = player_tackles['interceptions']
arsenal_players3['fouls_drawn'] = player_fouls['drawn']
arsenal_players3['fouls_committed'] = player_fouls['committed']
arsenal_players3['yellow_cards'] = player_cards['yellow']
arsenal_players3['red_cards'] = player_cards['red']
arsenal_players3['yellow_to_red_cards'] = player_cards['yellowred']
arsenal_players3['sub_in'] = player_subs['in']
arsenal_players3['sub_out'] = player_subs['out']

arsenal_players3 = arsenal_players3.fillna(0)


# Stage 4: Concatenate all data frames for the team's players
arsenal_players = pd.concat([arsenal_players1, arsenal_players2, arsenal_players3])
arsenal_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### ASTON VILLA ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"66","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
aston_villa_players1 = pd.DataFrame()

aston_villa_players1['name'] = df_p1['name']
aston_villa_players1['first_name'] = df_p1['firstname']
aston_villa_players1['last_name'] = df_p1['lastname']
aston_villa_players1['id'] = df_p1['id']
aston_villa_players1['team'] = player_team['name']
aston_villa_players1['team_id'] = player_team['id']
aston_villa_players1['league'] = player_league['name']
aston_villa_players1['league_id'] = player_league['id']
aston_villa_players1['age'] = df_p1['age']
aston_villa_players1['birth'] = player_birth['date']
aston_villa_players1['nationality'] = df_p1['nationality']
aston_villa_players1['app'] = player_games['appearences']
aston_villa_players1['mins'] = player_games['minutes']
aston_villa_players1['goals'] = player_goals['total']
aston_villa_players1['shots'] = player_shots['total']
aston_villa_players1['shots_on_target'] = player_shots['on']
aston_villa_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
aston_villa_players1['assists'] = player_goals['assists']
aston_villa_players1['passes'] = player_passes['total']
aston_villa_players1['passes_completed'] = player_passes['accuracy']
# aston_villa_players1['pass_accuracy_%'] = df_p1['name']
aston_villa_players1['dribbles'] = player_dribbles['attempts']
aston_villa_players1['dribbles_completed'] = player_dribbles['success']
aston_villa_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
aston_villa_players1['tackles'] = player_tackles['total']
aston_villa_players1['blocks'] = player_tackles['blocks']
aston_villa_players1['interceptions'] = player_tackles['interceptions']
aston_villa_players1['fouls_drawn'] = player_fouls['drawn']
aston_villa_players1['fouls_committed'] = player_fouls['committed']
aston_villa_players1['yellow_cards'] = player_cards['yellow']
aston_villa_players1['red_cards'] = player_cards['red']
aston_villa_players1['yellow_to_red_cards'] = player_cards['yellowred']
aston_villa_players1['sub_in'] = player_subs['in']
aston_villa_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
aston_villa_players1 = aston_villa_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"66","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
aston_villa_players2 = pd.DataFrame()

aston_villa_players2['name'] = df_p1['name']
aston_villa_players2['first_name'] = df_p1['firstname']
aston_villa_players2['last_name'] = df_p1['lastname']
aston_villa_players2['id'] = df_p1['id']
aston_villa_players2['team'] = player_team['name']
aston_villa_players2['team_id'] = player_team['id']
aston_villa_players2['league'] = player_league['name']
aston_villa_players2['league_id'] = player_league['id']
aston_villa_players2['age'] = df_p1['age']
aston_villa_players2['birth'] = player_birth['date']
aston_villa_players2['nationality'] = df_p1['nationality']
aston_villa_players2['app'] = player_games['appearences']
aston_villa_players2['mins'] = player_games['minutes']
aston_villa_players2['goals'] = player_goals['total']
aston_villa_players2['shots'] = player_shots['total']
aston_villa_players2['shots_on_target'] = player_shots['on']
aston_villa_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
aston_villa_players2['assists'] = player_goals['assists']
aston_villa_players2['passes'] = player_passes['total']
aston_villa_players2['passes_completed'] = player_passes['accuracy']
# aston_villa_players2['pass_accuracy_%'] = df_p1['name']
aston_villa_players2['dribbles'] = player_dribbles['attempts']
aston_villa_players2['dribbles_completed'] = player_dribbles['success']
aston_villa_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
aston_villa_players2['tackles'] = player_tackles['total']
aston_villa_players2['blocks'] = player_tackles['blocks']
aston_villa_players2['interceptions'] = player_tackles['interceptions']
aston_villa_players2['fouls_drawn'] = player_fouls['drawn']
aston_villa_players2['fouls_committed'] = player_fouls['committed']
aston_villa_players2['yellow_cards'] = player_cards['yellow']
aston_villa_players2['red_cards'] = player_cards['red']
aston_villa_players2['yellow_to_red_cards'] = player_cards['yellowred']
aston_villa_players2['sub_in'] = player_subs['in']
aston_villa_players2['sub_out'] = player_subs['out']

aston_villa_players2 = aston_villa_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
aston_villa_players = pd.concat([aston_villa_players1, aston_villa_players2])
aston_villa_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column









####### BRENTFORD ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"55","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
brentford_players1 = pd.DataFrame()

brentford_players1['name'] = df_p1['name']
brentford_players1['first_name'] = df_p1['firstname']
brentford_players1['last_name'] = df_p1['lastname']
brentford_players1['id'] = df_p1['id']
brentford_players1['team'] = player_team['name']
brentford_players1['team_id'] = player_team['id']
brentford_players1['league'] = player_league['name']
brentford_players1['league_id'] = player_league['id']
brentford_players1['age'] = df_p1['age']
brentford_players1['birth'] = player_birth['date']
brentford_players1['nationality'] = df_p1['nationality']
brentford_players1['app'] = player_games['appearences']
brentford_players1['mins'] = player_games['minutes']
brentford_players1['goals'] = player_goals['total']
brentford_players1['shots'] = player_shots['total']
brentford_players1['shots_on_target'] = player_shots['on']
brentford_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
brentford_players1['assists'] = player_goals['assists']
brentford_players1['passes'] = player_passes['total']
brentford_players1['passes_completed'] = player_passes['accuracy']
# brentford_players1['pass_accuracy_%'] = df_p1['name']
brentford_players1['dribbles'] = player_dribbles['attempts']
brentford_players1['dribbles_completed'] = player_dribbles['success']
brentford_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
brentford_players1['tackles'] = player_tackles['total']
brentford_players1['blocks'] = player_tackles['blocks']
brentford_players1['interceptions'] = player_tackles['interceptions']
brentford_players1['fouls_drawn'] = player_fouls['drawn']
brentford_players1['fouls_committed'] = player_fouls['committed']
brentford_players1['yellow_cards'] = player_cards['yellow']
brentford_players1['red_cards'] = player_cards['red']
brentford_players1['yellow_to_red_cards'] = player_cards['yellowred']
brentford_players1['sub_in'] = player_subs['in']
brentford_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
brentford_players1 = brentford_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"55","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
brentford_players2 = pd.DataFrame()

brentford_players2['name'] = df_p1['name']
brentford_players2['first_name'] = df_p1['firstname']
brentford_players2['last_name'] = df_p1['lastname']
brentford_players2['id'] = df_p1['id']
brentford_players2['team'] = player_team['name']
brentford_players2['team_id'] = player_team['id']
brentford_players2['league'] = player_league['name']
brentford_players2['league_id'] = player_league['id']
brentford_players2['age'] = df_p1['age']
brentford_players2['birth'] = player_birth['date']
brentford_players2['nationality'] = df_p1['nationality']
brentford_players2['app'] = player_games['appearences']
brentford_players2['mins'] = player_games['minutes']
brentford_players2['goals'] = player_goals['total']
brentford_players2['shots'] = player_shots['total']
brentford_players2['shots_on_target'] = player_shots['on']
brentford_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
brentford_players2['assists'] = player_goals['assists']
brentford_players2['passes'] = player_passes['total']
brentford_players2['passes_completed'] = player_passes['accuracy']
# brentford_players2['pass_accuracy_%'] = df_p1['name']
brentford_players2['dribbles'] = player_dribbles['attempts']
brentford_players2['dribbles_completed'] = player_dribbles['success']
brentford_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
brentford_players2['tackles'] = player_tackles['total']
brentford_players2['blocks'] = player_tackles['blocks']
brentford_players2['interceptions'] = player_tackles['interceptions']
brentford_players2['fouls_drawn'] = player_fouls['drawn']
brentford_players2['fouls_committed'] = player_fouls['committed']
brentford_players2['yellow_cards'] = player_cards['yellow']
brentford_players2['red_cards'] = player_cards['red']
brentford_players2['yellow_to_red_cards'] = player_cards['yellowred']
brentford_players2['sub_in'] = player_subs['in']
brentford_players2['sub_out'] = player_subs['out']

brentford_players2 = brentford_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
brentford_players = pd.concat([brentford_players1, brentford_players2])
brentford_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column







####### BRIGHTON ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"51","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
brighton_players1 = pd.DataFrame()

brighton_players1['name'] = df_p1['name']
brighton_players1['first_name'] = df_p1['firstname']
brighton_players1['last_name'] = df_p1['lastname']
brighton_players1['id'] = df_p1['id']
brighton_players1['team'] = player_team['name']
brighton_players1['team_id'] = player_team['id']
brighton_players1['league'] = player_league['name']
brighton_players1['league_id'] = player_league['id']
brighton_players1['age'] = df_p1['age']
brighton_players1['birth'] = player_birth['date']
brighton_players1['nationality'] = df_p1['nationality']
brighton_players1['app'] = player_games['appearences']
brighton_players1['mins'] = player_games['minutes']
brighton_players1['goals'] = player_goals['total']
brighton_players1['shots'] = player_shots['total']
brighton_players1['shots_on_target'] = player_shots['on']
brighton_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
brighton_players1['assists'] = player_goals['assists']
brighton_players1['passes'] = player_passes['total']
brighton_players1['passes_completed'] = player_passes['accuracy']
# brighton_players1['pass_accuracy_%'] = df_p1['name']
brighton_players1['dribbles'] = player_dribbles['attempts']
brighton_players1['dribbles_completed'] = player_dribbles['success']
brighton_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
brighton_players1['tackles'] = player_tackles['total']
brighton_players1['blocks'] = player_tackles['blocks']
brighton_players1['interceptions'] = player_tackles['interceptions']
brighton_players1['fouls_drawn'] = player_fouls['drawn']
brighton_players1['fouls_committed'] = player_fouls['committed']
brighton_players1['yellow_cards'] = player_cards['yellow']
brighton_players1['red_cards'] = player_cards['red']
brighton_players1['yellow_to_red_cards'] = player_cards['yellowred']
brighton_players1['sub_in'] = player_subs['in']
brighton_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
brighton_players1 = brighton_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"51","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
brighton_players2 = pd.DataFrame()

brighton_players2['name'] = df_p1['name']
brighton_players2['first_name'] = df_p1['firstname']
brighton_players2['last_name'] = df_p1['lastname']
brighton_players2['id'] = df_p1['id']
brighton_players2['team'] = player_team['name']
brighton_players2['team_id'] = player_team['id']
brighton_players2['league'] = player_league['name']
brighton_players2['league_id'] = player_league['id']
brighton_players2['age'] = df_p1['age']
brighton_players2['birth'] = player_birth['date']
brighton_players2['nationality'] = df_p1['nationality']
brighton_players2['app'] = player_games['appearences']
brighton_players2['mins'] = player_games['minutes']
brighton_players2['goals'] = player_goals['total']
brighton_players2['shots'] = player_shots['total']
brighton_players2['shots_on_target'] = player_shots['on']
brighton_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
brighton_players2['assists'] = player_goals['assists']
brighton_players2['passes'] = player_passes['total']
brighton_players2['passes_completed'] = player_passes['accuracy']
# brighton_players2['pass_accuracy_%'] = df_p1['name']
brighton_players2['dribbles'] = player_dribbles['attempts']
brighton_players2['dribbles_completed'] = player_dribbles['success']
brighton_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
brighton_players2['tackles'] = player_tackles['total']
brighton_players2['blocks'] = player_tackles['blocks']
brighton_players2['interceptions'] = player_tackles['interceptions']
brighton_players2['fouls_drawn'] = player_fouls['drawn']
brighton_players2['fouls_committed'] = player_fouls['committed']
brighton_players2['yellow_cards'] = player_cards['yellow']
brighton_players2['red_cards'] = player_cards['red']
brighton_players2['yellow_to_red_cards'] = player_cards['yellowred']
brighton_players2['sub_in'] = player_subs['in']
brighton_players2['sub_out'] = player_subs['out']

brighton_players2 = brighton_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
brighton_players = pd.concat([brighton_players1, brighton_players2])
brighton_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### BURNLEY ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"44","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
burnley_players1 = pd.DataFrame()

burnley_players1['name'] = df_p1['name']
burnley_players1['first_name'] = df_p1['firstname']
burnley_players1['last_name'] = df_p1['lastname']
burnley_players1['id'] = df_p1['id']
burnley_players1['team'] = player_team['name']
burnley_players1['team_id'] = player_team['id']
burnley_players1['league'] = player_league['name']
burnley_players1['league_id'] = player_league['id']
burnley_players1['age'] = df_p1['age']
burnley_players1['birth'] = player_birth['date']
burnley_players1['nationality'] = df_p1['nationality']
burnley_players1['app'] = player_games['appearences']
burnley_players1['mins'] = player_games['minutes']
burnley_players1['goals'] = player_goals['total']
burnley_players1['shots'] = player_shots['total']
burnley_players1['shots_on_target'] = player_shots['on']
burnley_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
burnley_players1['assists'] = player_goals['assists']
burnley_players1['passes'] = player_passes['total']
burnley_players1['passes_completed'] = player_passes['accuracy']
# burnley_players1['pass_accuracy_%'] = df_p1['name']
burnley_players1['dribbles'] = player_dribbles['attempts']
burnley_players1['dribbles_completed'] = player_dribbles['success']
burnley_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
burnley_players1['tackles'] = player_tackles['total']
burnley_players1['blocks'] = player_tackles['blocks']
burnley_players1['interceptions'] = player_tackles['interceptions']
burnley_players1['fouls_drawn'] = player_fouls['drawn']
burnley_players1['fouls_committed'] = player_fouls['committed']
burnley_players1['yellow_cards'] = player_cards['yellow']
burnley_players1['red_cards'] = player_cards['red']
burnley_players1['yellow_to_red_cards'] = player_cards['yellowred']
burnley_players1['sub_in'] = player_subs['in']
burnley_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
burnley_players1 = burnley_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"44","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
burnley_players2 = pd.DataFrame()

burnley_players2['name'] = df_p1['name']
burnley_players2['first_name'] = df_p1['firstname']
burnley_players2['last_name'] = df_p1['lastname']
burnley_players2['id'] = df_p1['id']
burnley_players2['team'] = player_team['name']
burnley_players2['team_id'] = player_team['id']
burnley_players2['league'] = player_league['name']
burnley_players2['league_id'] = player_league['id']
burnley_players2['age'] = df_p1['age']
burnley_players2['birth'] = player_birth['date']
burnley_players2['nationality'] = df_p1['nationality']
burnley_players2['app'] = player_games['appearences']
burnley_players2['mins'] = player_games['minutes']
burnley_players2['goals'] = player_goals['total']
burnley_players2['shots'] = player_shots['total']
burnley_players2['shots_on_target'] = player_shots['on']
burnley_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
burnley_players2['assists'] = player_goals['assists']
burnley_players2['passes'] = player_passes['total']
burnley_players2['passes_completed'] = player_passes['accuracy']
# burnley_players2['pass_accuracy_%'] = df_p1['name']
burnley_players2['dribbles'] = player_dribbles['attempts']
burnley_players2['dribbles_completed'] = player_dribbles['success']
burnley_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
burnley_players2['tackles'] = player_tackles['total']
burnley_players2['blocks'] = player_tackles['blocks']
burnley_players2['interceptions'] = player_tackles['interceptions']
burnley_players2['fouls_drawn'] = player_fouls['drawn']
burnley_players2['fouls_committed'] = player_fouls['committed']
burnley_players2['yellow_cards'] = player_cards['yellow']
burnley_players2['red_cards'] = player_cards['red']
burnley_players2['yellow_to_red_cards'] = player_cards['yellowred']
burnley_players2['sub_in'] = player_subs['in']
burnley_players2['sub_out'] = player_subs['out']

burnley_players2 = burnley_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
burnley_players = pd.concat([burnley_players1, burnley_players2])
burnley_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### CHELSEA  ######




# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"49","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
chelsea_players1 = pd.DataFrame()

chelsea_players1['name'] = df_p1['name']
chelsea_players1['first_name'] = df_p1['firstname']
chelsea_players1['last_name'] = df_p1['lastname']
chelsea_players1['id'] = df_p1['id']
chelsea_players1['team'] = player_team['name']
chelsea_players1['team_id'] = player_team['id']
chelsea_players1['league'] = player_league['name']
chelsea_players1['league_id'] = player_league['id']
chelsea_players1['age'] = df_p1['age']
chelsea_players1['birth'] = player_birth['date']
chelsea_players1['nationality'] = df_p1['nationality']
chelsea_players1['app'] = player_games['appearences']
chelsea_players1['mins'] = player_games['minutes']
chelsea_players1['goals'] = player_goals['total']
chelsea_players1['shots'] = player_shots['total']
chelsea_players1['shots_on_target'] = player_shots['on']
chelsea_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
chelsea_players1['assists'] = player_goals['assists']
chelsea_players1['passes'] = player_passes['total']
chelsea_players1['passes_completed'] = player_passes['accuracy']
# chelsea_players1['pass_accuracy_%'] = df_p1['name']
chelsea_players1['dribbles'] = player_dribbles['attempts']
chelsea_players1['dribbles_completed'] = player_dribbles['success']
chelsea_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
chelsea_players1['tackles'] = player_tackles['total']
chelsea_players1['blocks'] = player_tackles['blocks']
chelsea_players1['interceptions'] = player_tackles['interceptions']
chelsea_players1['fouls_drawn'] = player_fouls['drawn']
chelsea_players1['fouls_committed'] = player_fouls['committed']
chelsea_players1['yellow_cards'] = player_cards['yellow']
chelsea_players1['red_cards'] = player_cards['red']
chelsea_players1['yellow_to_red_cards'] = player_cards['yellowred']
chelsea_players1['sub_in'] = player_subs['in']
chelsea_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
chelsea_players1 = chelsea_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"49","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
chelsea_players2 = pd.DataFrame()

chelsea_players2['name'] = df_p1['name']
chelsea_players2['first_name'] = df_p1['firstname']
chelsea_players2['last_name'] = df_p1['lastname']
chelsea_players2['id'] = df_p1['id']
chelsea_players2['team'] = player_team['name']
chelsea_players2['team_id'] = player_team['id']
chelsea_players2['league'] = player_league['name']
chelsea_players2['league_id'] = player_league['id']
chelsea_players2['age'] = df_p1['age']
chelsea_players2['birth'] = player_birth['date']
chelsea_players2['nationality'] = df_p1['nationality']
chelsea_players2['app'] = player_games['appearences']
chelsea_players2['mins'] = player_games['minutes']
chelsea_players2['goals'] = player_goals['total']
chelsea_players2['shots'] = player_shots['total']
chelsea_players2['shots_on_target'] = player_shots['on']
chelsea_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
chelsea_players2['assists'] = player_goals['assists']
chelsea_players2['passes'] = player_passes['total']
chelsea_players2['passes_completed'] = player_passes['accuracy']
# chelsea_players2['pass_accuracy_%'] = df_p1['name']
chelsea_players2['dribbles'] = player_dribbles['attempts']
chelsea_players2['dribbles_completed'] = player_dribbles['success']
chelsea_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
chelsea_players2['tackles'] = player_tackles['total']
chelsea_players2['blocks'] = player_tackles['blocks']
chelsea_players2['interceptions'] = player_tackles['interceptions']
chelsea_players2['fouls_drawn'] = player_fouls['drawn']
chelsea_players2['fouls_committed'] = player_fouls['committed']
chelsea_players2['yellow_cards'] = player_cards['yellow']
chelsea_players2['red_cards'] = player_cards['red']
chelsea_players2['yellow_to_red_cards'] = player_cards['yellowred']
chelsea_players2['sub_in'] = player_subs['in']
chelsea_players2['sub_out'] = player_subs['out']

chelsea_players2 = chelsea_players2.fillna(0)



# Stage 3: Append More Player Data   


API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"49","season":"2021","page":"3"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)


# Create data frame for the first set of imported players 
chelsea_players3 = pd.DataFrame()

chelsea_players3['name'] = df_p1['name']
chelsea_players3['first_name'] = df_p1['firstname']
chelsea_players3['last_name'] = df_p1['lastname']
chelsea_players3['id'] = df_p1['id']
chelsea_players3['team'] = player_team['name']
chelsea_players3['team_id'] = player_team['id']
chelsea_players3['league'] = player_league['name']
chelsea_players3['league_id'] = player_league['id']
chelsea_players3['age'] = df_p1['age']
chelsea_players3['birth'] = player_birth['date']
chelsea_players3['nationality'] = df_p1['nationality']
chelsea_players3['app'] = player_games['appearences']
chelsea_players3['mins'] = player_games['minutes']
chelsea_players3['goals'] = player_goals['total']
chelsea_players3['shots'] = player_shots['total']
chelsea_players3['shots_on_target'] = player_shots['on']
chelsea_players3['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
chelsea_players3['assists'] = player_goals['assists']
chelsea_players3['passes'] = player_passes['total']
chelsea_players3['passes_completed'] = player_passes['accuracy']
# chelsea_players3['pass_accuracy_%'] = df_p1['name']
chelsea_players3['dribbles'] = player_dribbles['attempts']
chelsea_players3['dribbles_completed'] = player_dribbles['success']
chelsea_players3['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
chelsea_players3['tackles'] = player_tackles['total']
chelsea_players3['blocks'] = player_tackles['blocks']
chelsea_players3['interceptions'] = player_tackles['interceptions']
chelsea_players3['fouls_drawn'] = player_fouls['drawn']
chelsea_players3['fouls_committed'] = player_fouls['committed']
chelsea_players3['yellow_cards'] = player_cards['yellow']
chelsea_players3['red_cards'] = player_cards['red']
chelsea_players3['yellow_to_red_cards'] = player_cards['yellowred']
chelsea_players3['sub_in'] = player_subs['in']
chelsea_players3['sub_out'] = player_subs['out']

chelsea_players3 = chelsea_players3.fillna(0)


# Stage 4: Concatenate all data frames for the team's players
chelsea_players = pd.concat([chelsea_players1, chelsea_players2, chelsea_players3])
chelsea_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### CRYSTAL PALACE ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"52","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
crystal_palace_players1 = pd.DataFrame()

crystal_palace_players1['name'] = df_p1['name']
crystal_palace_players1['first_name'] = df_p1['firstname']
crystal_palace_players1['last_name'] = df_p1['lastname']
crystal_palace_players1['id'] = df_p1['id']
crystal_palace_players1['team'] = player_team['name']
crystal_palace_players1['team_id'] = player_team['id']
crystal_palace_players1['league'] = player_league['name']
crystal_palace_players1['league_id'] = player_league['id']
crystal_palace_players1['age'] = df_p1['age']
crystal_palace_players1['birth'] = player_birth['date']
crystal_palace_players1['nationality'] = df_p1['nationality']
crystal_palace_players1['app'] = player_games['appearences']
crystal_palace_players1['mins'] = player_games['minutes']
crystal_palace_players1['goals'] = player_goals['total']
crystal_palace_players1['shots'] = player_shots['total']
crystal_palace_players1['shots_on_target'] = player_shots['on']
crystal_palace_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
crystal_palace_players1['assists'] = player_goals['assists']
crystal_palace_players1['passes'] = player_passes['total']
crystal_palace_players1['passes_completed'] = player_passes['accuracy']
# crystal_palace_players1['pass_accuracy_%'] = df_p1['name']
crystal_palace_players1['dribbles'] = player_dribbles['attempts']
crystal_palace_players1['dribbles_completed'] = player_dribbles['success']
crystal_palace_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
crystal_palace_players1['tackles'] = player_tackles['total']
crystal_palace_players1['blocks'] = player_tackles['blocks']
crystal_palace_players1['interceptions'] = player_tackles['interceptions']
crystal_palace_players1['fouls_drawn'] = player_fouls['drawn']
crystal_palace_players1['fouls_committed'] = player_fouls['committed']
crystal_palace_players1['yellow_cards'] = player_cards['yellow']
crystal_palace_players1['red_cards'] = player_cards['red']
crystal_palace_players1['yellow_to_red_cards'] = player_cards['yellowred']
crystal_palace_players1['sub_in'] = player_subs['in']
crystal_palace_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
crystal_palace_players1 = crystal_palace_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"52","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
crystal_palace_players2 = pd.DataFrame()

crystal_palace_players2['name'] = df_p1['name']
crystal_palace_players2['first_name'] = df_p1['firstname']
crystal_palace_players2['last_name'] = df_p1['lastname']
crystal_palace_players2['id'] = df_p1['id']
crystal_palace_players2['team'] = player_team['name']
crystal_palace_players2['team_id'] = player_team['id']
crystal_palace_players2['league'] = player_league['name']
crystal_palace_players2['league_id'] = player_league['id']
crystal_palace_players2['age'] = df_p1['age']
crystal_palace_players2['birth'] = player_birth['date']
crystal_palace_players2['nationality'] = df_p1['nationality']
crystal_palace_players2['app'] = player_games['appearences']
crystal_palace_players2['mins'] = player_games['minutes']
crystal_palace_players2['goals'] = player_goals['total']
crystal_palace_players2['shots'] = player_shots['total']
crystal_palace_players2['shots_on_target'] = player_shots['on']
crystal_palace_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
crystal_palace_players2['assists'] = player_goals['assists']
crystal_palace_players2['passes'] = player_passes['total']
crystal_palace_players2['passes_completed'] = player_passes['accuracy']
# crystal_palace_players2['pass_accuracy_%'] = df_p1['name']
crystal_palace_players2['dribbles'] = player_dribbles['attempts']
crystal_palace_players2['dribbles_completed'] = player_dribbles['success']
crystal_palace_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
crystal_palace_players2['tackles'] = player_tackles['total']
crystal_palace_players2['blocks'] = player_tackles['blocks']
crystal_palace_players2['interceptions'] = player_tackles['interceptions']
crystal_palace_players2['fouls_drawn'] = player_fouls['drawn']
crystal_palace_players2['fouls_committed'] = player_fouls['committed']
crystal_palace_players2['yellow_cards'] = player_cards['yellow']
crystal_palace_players2['red_cards'] = player_cards['red']
crystal_palace_players2['yellow_to_red_cards'] = player_cards['yellowred']
crystal_palace_players2['sub_in'] = player_subs['in']
crystal_palace_players2['sub_out'] = player_subs['out']

crystal_palace_players2 = crystal_palace_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
crystal_palace_players = pd.concat([crystal_palace_players1, crystal_palace_players2])
crystal_palace_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### EVERTON ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"45","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
everton_players1 = pd.DataFrame()

everton_players1['name'] = df_p1['name']
everton_players1['first_name'] = df_p1['firstname']
everton_players1['last_name'] = df_p1['lastname']
everton_players1['id'] = df_p1['id']
everton_players1['team'] = player_team['name']
everton_players1['team_id'] = player_team['id']
everton_players1['league'] = player_league['name']
everton_players1['league_id'] = player_league['id']
everton_players1['age'] = df_p1['age']
everton_players1['birth'] = player_birth['date']
everton_players1['nationality'] = df_p1['nationality']
everton_players1['app'] = player_games['appearences']
everton_players1['mins'] = player_games['minutes']
everton_players1['goals'] = player_goals['total']
everton_players1['shots'] = player_shots['total']
everton_players1['shots_on_target'] = player_shots['on']
everton_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
everton_players1['assists'] = player_goals['assists']
everton_players1['passes'] = player_passes['total']
everton_players1['passes_completed'] = player_passes['accuracy']
# everton_players1['pass_accuracy_%'] = df_p1['name']
everton_players1['dribbles'] = player_dribbles['attempts']
everton_players1['dribbles_completed'] = player_dribbles['success']
everton_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
everton_players1['tackles'] = player_tackles['total']
everton_players1['blocks'] = player_tackles['blocks']
everton_players1['interceptions'] = player_tackles['interceptions']
everton_players1['fouls_drawn'] = player_fouls['drawn']
everton_players1['fouls_committed'] = player_fouls['committed']
everton_players1['yellow_cards'] = player_cards['yellow']
everton_players1['red_cards'] = player_cards['red']
everton_players1['yellow_to_red_cards'] = player_cards['yellowred']
everton_players1['sub_in'] = player_subs['in']
everton_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
everton_players1 = everton_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"45","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
everton_players2 = pd.DataFrame()

everton_players2['name'] = df_p1['name']
everton_players2['first_name'] = df_p1['firstname']
everton_players2['last_name'] = df_p1['lastname']
everton_players2['id'] = df_p1['id']
everton_players2['team'] = player_team['name']
everton_players2['team_id'] = player_team['id']
everton_players2['league'] = player_league['name']
everton_players2['league_id'] = player_league['id']
everton_players2['age'] = df_p1['age']
everton_players2['birth'] = player_birth['date']
everton_players2['nationality'] = df_p1['nationality']
everton_players2['app'] = player_games['appearences']
everton_players2['mins'] = player_games['minutes']
everton_players2['goals'] = player_goals['total']
everton_players2['shots'] = player_shots['total']
everton_players2['shots_on_target'] = player_shots['on']
everton_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
everton_players2['assists'] = player_goals['assists']
everton_players2['passes'] = player_passes['total']
everton_players2['passes_completed'] = player_passes['accuracy']
# everton_players2['pass_accuracy_%'] = df_p1['name']
everton_players2['dribbles'] = player_dribbles['attempts']
everton_players2['dribbles_completed'] = player_dribbles['success']
everton_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
everton_players2['tackles'] = player_tackles['total']
everton_players2['blocks'] = player_tackles['blocks']
everton_players2['interceptions'] = player_tackles['interceptions']
everton_players2['fouls_drawn'] = player_fouls['drawn']
everton_players2['fouls_committed'] = player_fouls['committed']
everton_players2['yellow_cards'] = player_cards['yellow']
everton_players2['red_cards'] = player_cards['red']
everton_players2['yellow_to_red_cards'] = player_cards['yellowred']
everton_players2['sub_in'] = player_subs['in']
everton_players2['sub_out'] = player_subs['out']

everton_players2 = everton_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
everton_players = pd.concat([everton_players1, everton_players2])
everton_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### LEEDS ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"63","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
leeds_players1 = pd.DataFrame()

leeds_players1['name'] = df_p1['name']
leeds_players1['first_name'] = df_p1['firstname']
leeds_players1['last_name'] = df_p1['lastname']
leeds_players1['id'] = df_p1['id']
leeds_players1['team'] = player_team['name']
leeds_players1['team_id'] = player_team['id']
leeds_players1['league'] = player_league['name']
leeds_players1['league_id'] = player_league['id']
leeds_players1['age'] = df_p1['age']
leeds_players1['birth'] = player_birth['date']
leeds_players1['nationality'] = df_p1['nationality']
leeds_players1['app'] = player_games['appearences']
leeds_players1['mins'] = player_games['minutes']
leeds_players1['goals'] = player_goals['total']
leeds_players1['shots'] = player_shots['total']
leeds_players1['shots_on_target'] = player_shots['on']
leeds_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
leeds_players1['assists'] = player_goals['assists']
leeds_players1['passes'] = player_passes['total']
leeds_players1['passes_completed'] = player_passes['accuracy']
# leeds_players1['pass_accuracy_%'] = df_p1['name']
leeds_players1['dribbles'] = player_dribbles['attempts']
leeds_players1['dribbles_completed'] = player_dribbles['success']
leeds_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
leeds_players1['tackles'] = player_tackles['total']
leeds_players1['blocks'] = player_tackles['blocks']
leeds_players1['interceptions'] = player_tackles['interceptions']
leeds_players1['fouls_drawn'] = player_fouls['drawn']
leeds_players1['fouls_committed'] = player_fouls['committed']
leeds_players1['yellow_cards'] = player_cards['yellow']
leeds_players1['red_cards'] = player_cards['red']
leeds_players1['yellow_to_red_cards'] = player_cards['yellowred']
leeds_players1['sub_in'] = player_subs['in']
leeds_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
leeds_players1 = leeds_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"63","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
leeds_players2 = pd.DataFrame()

leeds_players2['name'] = df_p1['name']
leeds_players2['first_name'] = df_p1['firstname']
leeds_players2['last_name'] = df_p1['lastname']
leeds_players2['id'] = df_p1['id']
leeds_players2['team'] = player_team['name']
leeds_players2['team_id'] = player_team['id']
leeds_players2['league'] = player_league['name']
leeds_players2['league_id'] = player_league['id']
leeds_players2['age'] = df_p1['age']
leeds_players2['birth'] = player_birth['date']
leeds_players2['nationality'] = df_p1['nationality']
leeds_players2['app'] = player_games['appearences']
leeds_players2['mins'] = player_games['minutes']
leeds_players2['goals'] = player_goals['total']
leeds_players2['shots'] = player_shots['total']
leeds_players2['shots_on_target'] = player_shots['on']
leeds_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
leeds_players2['assists'] = player_goals['assists']
leeds_players2['passes'] = player_passes['total']
leeds_players2['passes_completed'] = player_passes['accuracy']
# leeds_players2['pass_accuracy_%'] = df_p1['name']
leeds_players2['dribbles'] = player_dribbles['attempts']
leeds_players2['dribbles_completed'] = player_dribbles['success']
leeds_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
leeds_players2['tackles'] = player_tackles['total']
leeds_players2['blocks'] = player_tackles['blocks']
leeds_players2['interceptions'] = player_tackles['interceptions']
leeds_players2['fouls_drawn'] = player_fouls['drawn']
leeds_players2['fouls_committed'] = player_fouls['committed']
leeds_players2['yellow_cards'] = player_cards['yellow']
leeds_players2['red_cards'] = player_cards['red']
leeds_players2['yellow_to_red_cards'] = player_cards['yellowred']
leeds_players2['sub_in'] = player_subs['in']
leeds_players2['sub_out'] = player_subs['out']

leeds_players2 = leeds_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
leeds_players = pd.concat([leeds_players1, leeds_players2])
leeds_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column



####### LEICESTER ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"46","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
leicester_players1 = pd.DataFrame()

leicester_players1['name'] = df_p1['name']
leicester_players1['first_name'] = df_p1['firstname']
leicester_players1['last_name'] = df_p1['lastname']
leicester_players1['id'] = df_p1['id']
leicester_players1['team'] = player_team['name']
leicester_players1['team_id'] = player_team['id']
leicester_players1['league'] = player_league['name']
leicester_players1['league_id'] = player_league['id']
leicester_players1['age'] = df_p1['age']
leicester_players1['birth'] = player_birth['date']
leicester_players1['nationality'] = df_p1['nationality']
leicester_players1['app'] = player_games['appearences']
leicester_players1['mins'] = player_games['minutes']
leicester_players1['goals'] = player_goals['total']
leicester_players1['shots'] = player_shots['total']
leicester_players1['shots_on_target'] = player_shots['on']
leicester_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
leicester_players1['assists'] = player_goals['assists']
leicester_players1['passes'] = player_passes['total']
leicester_players1['passes_completed'] = player_passes['accuracy']
# leicester_players1['pass_accuracy_%'] = df_p1['name']
leicester_players1['dribbles'] = player_dribbles['attempts']
leicester_players1['dribbles_completed'] = player_dribbles['success']
leicester_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
leicester_players1['tackles'] = player_tackles['total']
leicester_players1['blocks'] = player_tackles['blocks']
leicester_players1['interceptions'] = player_tackles['interceptions']
leicester_players1['fouls_drawn'] = player_fouls['drawn']
leicester_players1['fouls_committed'] = player_fouls['committed']
leicester_players1['yellow_cards'] = player_cards['yellow']
leicester_players1['red_cards'] = player_cards['red']
leicester_players1['yellow_to_red_cards'] = player_cards['yellowred']
leicester_players1['sub_in'] = player_subs['in']
leicester_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
leicester_players1 = leicester_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"46","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
leicester_players2 = pd.DataFrame()

leicester_players2['name'] = df_p1['name']
leicester_players2['first_name'] = df_p1['firstname']
leicester_players2['last_name'] = df_p1['lastname']
leicester_players2['id'] = df_p1['id']
leicester_players2['team'] = player_team['name']
leicester_players2['team_id'] = player_team['id']
leicester_players2['league'] = player_league['name']
leicester_players2['league_id'] = player_league['id']
leicester_players2['age'] = df_p1['age']
leicester_players2['birth'] = player_birth['date']
leicester_players2['nationality'] = df_p1['nationality']
leicester_players2['app'] = player_games['appearences']
leicester_players2['mins'] = player_games['minutes']
leicester_players2['goals'] = player_goals['total']
leicester_players2['shots'] = player_shots['total']
leicester_players2['shots_on_target'] = player_shots['on']
leicester_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
leicester_players2['assists'] = player_goals['assists']
leicester_players2['passes'] = player_passes['total']
leicester_players2['passes_completed'] = player_passes['accuracy']
# leicester_players2['pass_accuracy_%'] = df_p1['name']
leicester_players2['dribbles'] = player_dribbles['attempts']
leicester_players2['dribbles_completed'] = player_dribbles['success']
leicester_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
leicester_players2['tackles'] = player_tackles['total']
leicester_players2['blocks'] = player_tackles['blocks']
leicester_players2['interceptions'] = player_tackles['interceptions']
leicester_players2['fouls_drawn'] = player_fouls['drawn']
leicester_players2['fouls_committed'] = player_fouls['committed']
leicester_players2['yellow_cards'] = player_cards['yellow']
leicester_players2['red_cards'] = player_cards['red']
leicester_players2['yellow_to_red_cards'] = player_cards['yellowred']
leicester_players2['sub_in'] = player_subs['in']
leicester_players2['sub_out'] = player_subs['out']

leicester_players2 = leicester_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
leicester_players = pd.concat([leicester_players1, leicester_players2])
leicester_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### LIVERPOOL ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"40","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
liverpool_players1 = pd.DataFrame()

liverpool_players1['name'] = df_p1['name']
liverpool_players1['first_name'] = df_p1['firstname']
liverpool_players1['last_name'] = df_p1['lastname']
liverpool_players1['id'] = df_p1['id']
liverpool_players1['team'] = player_team['name']
liverpool_players1['team_id'] = player_team['id']
liverpool_players1['league'] = player_league['name']
liverpool_players1['league_id'] = player_league['id']
liverpool_players1['age'] = df_p1['age']
liverpool_players1['birth'] = player_birth['date']
liverpool_players1['nationality'] = df_p1['nationality']
liverpool_players1['app'] = player_games['appearences']
liverpool_players1['mins'] = player_games['minutes']
liverpool_players1['goals'] = player_goals['total']
liverpool_players1['shots'] = player_shots['total']
liverpool_players1['shots_on_target'] = player_shots['on']
liverpool_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
liverpool_players1['assists'] = player_goals['assists']
liverpool_players1['passes'] = player_passes['total']
liverpool_players1['passes_completed'] = player_passes['accuracy']
# liverpool_players1['pass_accuracy_%'] = df_p1['name']
liverpool_players1['dribbles'] = player_dribbles['attempts']
liverpool_players1['dribbles_completed'] = player_dribbles['success']
liverpool_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
liverpool_players1['tackles'] = player_tackles['total']
liverpool_players1['blocks'] = player_tackles['blocks']
liverpool_players1['interceptions'] = player_tackles['interceptions']
liverpool_players1['fouls_drawn'] = player_fouls['drawn']
liverpool_players1['fouls_committed'] = player_fouls['committed']
liverpool_players1['yellow_cards'] = player_cards['yellow']
liverpool_players1['red_cards'] = player_cards['red']
liverpool_players1['yellow_to_red_cards'] = player_cards['yellowred']
liverpool_players1['sub_in'] = player_subs['in']
liverpool_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
liverpool_players1 = liverpool_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"40","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
liverpool_players2 = pd.DataFrame()

liverpool_players2['name'] = df_p1['name']
liverpool_players2['first_name'] = df_p1['firstname']
liverpool_players2['last_name'] = df_p1['lastname']
liverpool_players2['id'] = df_p1['id']
liverpool_players2['team'] = player_team['name']
liverpool_players2['team_id'] = player_team['id']
liverpool_players2['league'] = player_league['name']
liverpool_players2['league_id'] = player_league['id']
liverpool_players2['age'] = df_p1['age']
liverpool_players2['birth'] = player_birth['date']
liverpool_players2['nationality'] = df_p1['nationality']
liverpool_players2['app'] = player_games['appearences']
liverpool_players2['mins'] = player_games['minutes']
liverpool_players2['goals'] = player_goals['total']
liverpool_players2['shots'] = player_shots['total']
liverpool_players2['shots_on_target'] = player_shots['on']
liverpool_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
liverpool_players2['assists'] = player_goals['assists']
liverpool_players2['passes'] = player_passes['total']
liverpool_players2['passes_completed'] = player_passes['accuracy']
# liverpool_players2['pass_accuracy_%'] = df_p1['name']
liverpool_players2['dribbles'] = player_dribbles['attempts']
liverpool_players2['dribbles_completed'] = player_dribbles['success']
liverpool_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
liverpool_players2['tackles'] = player_tackles['total']
liverpool_players2['blocks'] = player_tackles['blocks']
liverpool_players2['interceptions'] = player_tackles['interceptions']
liverpool_players2['fouls_drawn'] = player_fouls['drawn']
liverpool_players2['fouls_committed'] = player_fouls['committed']
liverpool_players2['yellow_cards'] = player_cards['yellow']
liverpool_players2['red_cards'] = player_cards['red']
liverpool_players2['yellow_to_red_cards'] = player_cards['yellowred']
liverpool_players2['sub_in'] = player_subs['in']
liverpool_players2['sub_out'] = player_subs['out']

liverpool_players2 = liverpool_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
liverpool_players = pd.concat([liverpool_players1, liverpool_players2])
liverpool_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### MAN CITY ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"50","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
man_city_players1 = pd.DataFrame()

man_city_players1['name'] = df_p1['name']
man_city_players1['first_name'] = df_p1['firstname']
man_city_players1['last_name'] = df_p1['lastname']
man_city_players1['id'] = df_p1['id']
man_city_players1['team'] = player_team['name']
man_city_players1['team_id'] = player_team['id']
man_city_players1['league'] = player_league['name']
man_city_players1['league_id'] = player_league['id']
man_city_players1['age'] = df_p1['age']
man_city_players1['birth'] = player_birth['date']
man_city_players1['nationality'] = df_p1['nationality']
man_city_players1['app'] = player_games['appearences']
man_city_players1['mins'] = player_games['minutes']
man_city_players1['goals'] = player_goals['total']
man_city_players1['shots'] = player_shots['total']
man_city_players1['shots_on_target'] = player_shots['on']
man_city_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
man_city_players1['assists'] = player_goals['assists']
man_city_players1['passes'] = player_passes['total']
man_city_players1['passes_completed'] = player_passes['accuracy']
# man_city_players1['pass_accuracy_%'] = df_p1['name']
man_city_players1['dribbles'] = player_dribbles['attempts']
man_city_players1['dribbles_completed'] = player_dribbles['success']
man_city_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
man_city_players1['tackles'] = player_tackles['total']
man_city_players1['blocks'] = player_tackles['blocks']
man_city_players1['interceptions'] = player_tackles['interceptions']
man_city_players1['fouls_drawn'] = player_fouls['drawn']
man_city_players1['fouls_committed'] = player_fouls['committed']
man_city_players1['yellow_cards'] = player_cards['yellow']
man_city_players1['red_cards'] = player_cards['red']
man_city_players1['yellow_to_red_cards'] = player_cards['yellowred']
man_city_players1['sub_in'] = player_subs['in']
man_city_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
man_city_players1 = man_city_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"50","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
man_city_players2 = pd.DataFrame()

man_city_players2['name'] = df_p1['name']
man_city_players2['first_name'] = df_p1['firstname']
man_city_players2['last_name'] = df_p1['lastname']
man_city_players2['id'] = df_p1['id']
man_city_players2['team'] = player_team['name']
man_city_players2['team_id'] = player_team['id']
man_city_players2['league'] = player_league['name']
man_city_players2['league_id'] = player_league['id']
man_city_players2['age'] = df_p1['age']
man_city_players2['birth'] = player_birth['date']
man_city_players2['nationality'] = df_p1['nationality']
man_city_players2['app'] = player_games['appearences']
man_city_players2['mins'] = player_games['minutes']
man_city_players2['goals'] = player_goals['total']
man_city_players2['shots'] = player_shots['total']
man_city_players2['shots_on_target'] = player_shots['on']
man_city_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
man_city_players2['assists'] = player_goals['assists']
man_city_players2['passes'] = player_passes['total']
man_city_players2['passes_completed'] = player_passes['accuracy']
# man_city_players2['pass_accuracy_%'] = df_p1['name']
man_city_players2['dribbles'] = player_dribbles['attempts']
man_city_players2['dribbles_completed'] = player_dribbles['success']
man_city_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
man_city_players2['tackles'] = player_tackles['total']
man_city_players2['blocks'] = player_tackles['blocks']
man_city_players2['interceptions'] = player_tackles['interceptions']
man_city_players2['fouls_drawn'] = player_fouls['drawn']
man_city_players2['fouls_committed'] = player_fouls['committed']
man_city_players2['yellow_cards'] = player_cards['yellow']
man_city_players2['red_cards'] = player_cards['red']
man_city_players2['yellow_to_red_cards'] = player_cards['yellowred']
man_city_players2['sub_in'] = player_subs['in']
man_city_players2['sub_out'] = player_subs['out']

man_city_players2 = man_city_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
man_city_players = pd.concat([man_city_players1, man_city_players2])
man_city_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column









####### MANCHESTER UNITED ######




# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"33","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
man_utd_players1 = pd.DataFrame()

man_utd_players1['name'] = df_p1['name']
man_utd_players1['first_name'] = df_p1['firstname']
man_utd_players1['last_name'] = df_p1['lastname']
man_utd_players1['id'] = df_p1['id']
man_utd_players1['team'] = player_team['name']
man_utd_players1['team_id'] = player_team['id']
man_utd_players1['league'] = player_league['name']
man_utd_players1['league_id'] = player_league['id']
man_utd_players1['age'] = df_p1['age']
man_utd_players1['birth'] = player_birth['date']
man_utd_players1['nationality'] = df_p1['nationality']
man_utd_players1['app'] = player_games['appearences']
man_utd_players1['mins'] = player_games['minutes']
man_utd_players1['goals'] = player_goals['total']
man_utd_players1['shots'] = player_shots['total']
man_utd_players1['shots_on_target'] = player_shots['on']
man_utd_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
man_utd_players1['assists'] = player_goals['assists']
man_utd_players1['passes'] = player_passes['total']
man_utd_players1['passes_completed'] = player_passes['accuracy']
# man_utd_players1['pass_accuracy_%'] = df_p1['name']
man_utd_players1['dribbles'] = player_dribbles['attempts']
man_utd_players1['dribbles_completed'] = player_dribbles['success']
man_utd_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
man_utd_players1['tackles'] = player_tackles['total']
man_utd_players1['blocks'] = player_tackles['blocks']
man_utd_players1['interceptions'] = player_tackles['interceptions']
man_utd_players1['fouls_drawn'] = player_fouls['drawn']
man_utd_players1['fouls_committed'] = player_fouls['committed']
man_utd_players1['yellow_cards'] = player_cards['yellow']
man_utd_players1['red_cards'] = player_cards['red']
man_utd_players1['yellow_to_red_cards'] = player_cards['yellowred']
man_utd_players1['sub_in'] = player_subs['in']
man_utd_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
man_utd_players1 = man_utd_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"33","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
man_utd_players2 = pd.DataFrame()

man_utd_players2['name'] = df_p1['name']
man_utd_players2['first_name'] = df_p1['firstname']
man_utd_players2['last_name'] = df_p1['lastname']
man_utd_players2['id'] = df_p1['id']
man_utd_players2['team'] = player_team['name']
man_utd_players2['team_id'] = player_team['id']
man_utd_players2['league'] = player_league['name']
man_utd_players2['league_id'] = player_league['id']
man_utd_players2['age'] = df_p1['age']
man_utd_players2['birth'] = player_birth['date']
man_utd_players2['nationality'] = df_p1['nationality']
man_utd_players2['app'] = player_games['appearences']
man_utd_players2['mins'] = player_games['minutes']
man_utd_players2['goals'] = player_goals['total']
man_utd_players2['shots'] = player_shots['total']
man_utd_players2['shots_on_target'] = player_shots['on']
man_utd_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
man_utd_players2['assists'] = player_goals['assists']
man_utd_players2['passes'] = player_passes['total']
man_utd_players2['passes_completed'] = player_passes['accuracy']
# man_utd_players2['pass_accuracy_%'] = df_p1['name']
man_utd_players2['dribbles'] = player_dribbles['attempts']
man_utd_players2['dribbles_completed'] = player_dribbles['success']
man_utd_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
man_utd_players2['tackles'] = player_tackles['total']
man_utd_players2['blocks'] = player_tackles['blocks']
man_utd_players2['interceptions'] = player_tackles['interceptions']
man_utd_players2['fouls_drawn'] = player_fouls['drawn']
man_utd_players2['fouls_committed'] = player_fouls['committed']
man_utd_players2['yellow_cards'] = player_cards['yellow']
man_utd_players2['red_cards'] = player_cards['red']
man_utd_players2['yellow_to_red_cards'] = player_cards['yellowred']
man_utd_players2['sub_in'] = player_subs['in']
man_utd_players2['sub_out'] = player_subs['out']

man_utd_players2 = man_utd_players2.fillna(0)



# Stage 3: Append More Player Data   


API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"33","season":"2021","page":"3"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)


# Create data frame for the first set of imported players 
man_utd_players3 = pd.DataFrame()

man_utd_players3['name'] = df_p1['name']
man_utd_players3['first_name'] = df_p1['firstname']
man_utd_players3['last_name'] = df_p1['lastname']
man_utd_players3['id'] = df_p1['id']
man_utd_players3['team'] = player_team['name']
man_utd_players3['team_id'] = player_team['id']
man_utd_players3['league'] = player_league['name']
man_utd_players3['league_id'] = player_league['id']
man_utd_players3['age'] = df_p1['age']
man_utd_players3['birth'] = player_birth['date']
man_utd_players3['nationality'] = df_p1['nationality']
man_utd_players3['app'] = player_games['appearences']
man_utd_players3['mins'] = player_games['minutes']
man_utd_players3['goals'] = player_goals['total']
man_utd_players3['shots'] = player_shots['total']
man_utd_players3['shots_on_target'] = player_shots['on']
man_utd_players3['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
man_utd_players3['assists'] = player_goals['assists']
man_utd_players3['passes'] = player_passes['total']
man_utd_players3['passes_completed'] = player_passes['accuracy']
# man_utd_players3['pass_accuracy_%'] = df_p1['name']
man_utd_players3['dribbles'] = player_dribbles['attempts']
man_utd_players3['dribbles_completed'] = player_dribbles['success']
man_utd_players3['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
man_utd_players3['tackles'] = player_tackles['total']
man_utd_players3['blocks'] = player_tackles['blocks']
man_utd_players3['interceptions'] = player_tackles['interceptions']
man_utd_players3['fouls_drawn'] = player_fouls['drawn']
man_utd_players3['fouls_committed'] = player_fouls['committed']
man_utd_players3['yellow_cards'] = player_cards['yellow']
man_utd_players3['red_cards'] = player_cards['red']
man_utd_players3['yellow_to_red_cards'] = player_cards['yellowred']
man_utd_players3['sub_in'] = player_subs['in']
man_utd_players3['sub_out'] = player_subs['out']

man_utd_players3 = man_utd_players3.fillna(0)


# Stage 4: Concatenate all data frames for the team's players
man_utd_players = pd.concat([man_utd_players1, man_utd_players2, man_utd_players3])
man_utd_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### NEWCASTLE ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"34","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
newcastle_players1 = pd.DataFrame()

newcastle_players1['name'] = df_p1['name']
newcastle_players1['first_name'] = df_p1['firstname']
newcastle_players1['last_name'] = df_p1['lastname']
newcastle_players1['id'] = df_p1['id']
newcastle_players1['team'] = player_team['name']
newcastle_players1['team_id'] = player_team['id']
newcastle_players1['league'] = player_league['name']
newcastle_players1['league_id'] = player_league['id']
newcastle_players1['age'] = df_p1['age']
newcastle_players1['birth'] = player_birth['date']
newcastle_players1['nationality'] = df_p1['nationality']
newcastle_players1['app'] = player_games['appearences']
newcastle_players1['mins'] = player_games['minutes']
newcastle_players1['goals'] = player_goals['total']
newcastle_players1['shots'] = player_shots['total']
newcastle_players1['shots_on_target'] = player_shots['on']
newcastle_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
newcastle_players1['assists'] = player_goals['assists']
newcastle_players1['passes'] = player_passes['total']
newcastle_players1['passes_completed'] = player_passes['accuracy']
# newcastle_players1['pass_accuracy_%'] = df_p1['name']
newcastle_players1['dribbles'] = player_dribbles['attempts']
newcastle_players1['dribbles_completed'] = player_dribbles['success']
newcastle_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
newcastle_players1['tackles'] = player_tackles['total']
newcastle_players1['blocks'] = player_tackles['blocks']
newcastle_players1['interceptions'] = player_tackles['interceptions']
newcastle_players1['fouls_drawn'] = player_fouls['drawn']
newcastle_players1['fouls_committed'] = player_fouls['committed']
newcastle_players1['yellow_cards'] = player_cards['yellow']
newcastle_players1['red_cards'] = player_cards['red']
newcastle_players1['yellow_to_red_cards'] = player_cards['yellowred']
newcastle_players1['sub_in'] = player_subs['in']
newcastle_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
newcastle_players1 = newcastle_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"34","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
newcastle_players2 = pd.DataFrame()

newcastle_players2['name'] = df_p1['name']
newcastle_players2['first_name'] = df_p1['firstname']
newcastle_players2['last_name'] = df_p1['lastname']
newcastle_players2['id'] = df_p1['id']
newcastle_players2['team'] = player_team['name']
newcastle_players2['team_id'] = player_team['id']
newcastle_players2['league'] = player_league['name']
newcastle_players2['league_id'] = player_league['id']
newcastle_players2['age'] = df_p1['age']
newcastle_players2['birth'] = player_birth['date']
newcastle_players2['nationality'] = df_p1['nationality']
newcastle_players2['app'] = player_games['appearences']
newcastle_players2['mins'] = player_games['minutes']
newcastle_players2['goals'] = player_goals['total']
newcastle_players2['shots'] = player_shots['total']
newcastle_players2['shots_on_target'] = player_shots['on']
newcastle_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
newcastle_players2['assists'] = player_goals['assists']
newcastle_players2['passes'] = player_passes['total']
newcastle_players2['passes_completed'] = player_passes['accuracy']
# newcastle_players2['pass_accuracy_%'] = df_p1['name']
newcastle_players2['dribbles'] = player_dribbles['attempts']
newcastle_players2['dribbles_completed'] = player_dribbles['success']
newcastle_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
newcastle_players2['tackles'] = player_tackles['total']
newcastle_players2['blocks'] = player_tackles['blocks']
newcastle_players2['interceptions'] = player_tackles['interceptions']
newcastle_players2['fouls_drawn'] = player_fouls['drawn']
newcastle_players2['fouls_committed'] = player_fouls['committed']
newcastle_players2['yellow_cards'] = player_cards['yellow']
newcastle_players2['red_cards'] = player_cards['red']
newcastle_players2['yellow_to_red_cards'] = player_cards['yellowred']
newcastle_players2['sub_in'] = player_subs['in']
newcastle_players2['sub_out'] = player_subs['out']

newcastle_players2 = newcastle_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
newcastle_players = pd.concat([newcastle_players1, newcastle_players2])
newcastle_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### NORWICH ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"71","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
norwich_players1 = pd.DataFrame()

norwich_players1['name'] = df_p1['name']
norwich_players1['first_name'] = df_p1['firstname']
norwich_players1['last_name'] = df_p1['lastname']
norwich_players1['id'] = df_p1['id']
norwich_players1['team'] = player_team['name']
norwich_players1['team_id'] = player_team['id']
norwich_players1['league'] = player_league['name']
norwich_players1['league_id'] = player_league['id']
norwich_players1['age'] = df_p1['age']
norwich_players1['birth'] = player_birth['date']
norwich_players1['nationality'] = df_p1['nationality']
norwich_players1['app'] = player_games['appearences']
norwich_players1['mins'] = player_games['minutes']
norwich_players1['goals'] = player_goals['total']
norwich_players1['shots'] = player_shots['total']
norwich_players1['shots_on_target'] = player_shots['on']
norwich_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
norwich_players1['assists'] = player_goals['assists']
norwich_players1['passes'] = player_passes['total']
norwich_players1['passes_completed'] = player_passes['accuracy']
# norwich_players1['pass_accuracy_%'] = df_p1['name']
norwich_players1['dribbles'] = player_dribbles['attempts']
norwich_players1['dribbles_completed'] = player_dribbles['success']
norwich_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
norwich_players1['tackles'] = player_tackles['total']
norwich_players1['blocks'] = player_tackles['blocks']
norwich_players1['interceptions'] = player_tackles['interceptions']
norwich_players1['fouls_drawn'] = player_fouls['drawn']
norwich_players1['fouls_committed'] = player_fouls['committed']
norwich_players1['yellow_cards'] = player_cards['yellow']
norwich_players1['red_cards'] = player_cards['red']
norwich_players1['yellow_to_red_cards'] = player_cards['yellowred']
norwich_players1['sub_in'] = player_subs['in']
norwich_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
norwich_players1 = norwich_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"71","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
norwich_players2 = pd.DataFrame()

norwich_players2['name'] = df_p1['name']
norwich_players2['first_name'] = df_p1['firstname']
norwich_players2['last_name'] = df_p1['lastname']
norwich_players2['id'] = df_p1['id']
norwich_players2['team'] = player_team['name']
norwich_players2['team_id'] = player_team['id']
norwich_players2['league'] = player_league['name']
norwich_players2['league_id'] = player_league['id']
norwich_players2['age'] = df_p1['age']
norwich_players2['birth'] = player_birth['date']
norwich_players2['nationality'] = df_p1['nationality']
norwich_players2['app'] = player_games['appearences']
norwich_players2['mins'] = player_games['minutes']
norwich_players2['goals'] = player_goals['total']
norwich_players2['shots'] = player_shots['total']
norwich_players2['shots_on_target'] = player_shots['on']
norwich_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
norwich_players2['assists'] = player_goals['assists']
norwich_players2['passes'] = player_passes['total']
norwich_players2['passes_completed'] = player_passes['accuracy']
# norwich_players2['pass_accuracy_%'] = df_p1['name']
norwich_players2['dribbles'] = player_dribbles['attempts']
norwich_players2['dribbles_completed'] = player_dribbles['success']
norwich_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
norwich_players2['tackles'] = player_tackles['total']
norwich_players2['blocks'] = player_tackles['blocks']
norwich_players2['interceptions'] = player_tackles['interceptions']
norwich_players2['fouls_drawn'] = player_fouls['drawn']
norwich_players2['fouls_committed'] = player_fouls['committed']
norwich_players2['yellow_cards'] = player_cards['yellow']
norwich_players2['red_cards'] = player_cards['red']
norwich_players2['yellow_to_red_cards'] = player_cards['yellowred']
norwich_players2['sub_in'] = player_subs['in']
norwich_players2['sub_out'] = player_subs['out']

norwich_players2 = norwich_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
norwich_players = pd.concat([norwich_players1, norwich_players2])
norwich_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### SOUTHAMPTON ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"41","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
southampton_players1 = pd.DataFrame()

southampton_players1['name'] = df_p1['name']
southampton_players1['first_name'] = df_p1['firstname']
southampton_players1['last_name'] = df_p1['lastname']
southampton_players1['id'] = df_p1['id']
southampton_players1['team'] = player_team['name']
southampton_players1['team_id'] = player_team['id']
southampton_players1['league'] = player_league['name']
southampton_players1['league_id'] = player_league['id']
southampton_players1['age'] = df_p1['age']
southampton_players1['birth'] = player_birth['date']
southampton_players1['nationality'] = df_p1['nationality']
southampton_players1['app'] = player_games['appearences']
southampton_players1['mins'] = player_games['minutes']
southampton_players1['goals'] = player_goals['total']
southampton_players1['shots'] = player_shots['total']
southampton_players1['shots_on_target'] = player_shots['on']
southampton_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
southampton_players1['assists'] = player_goals['assists']
southampton_players1['passes'] = player_passes['total']
southampton_players1['passes_completed'] = player_passes['accuracy']
# southampton_players1['pass_accuracy_%'] = df_p1['name']
southampton_players1['dribbles'] = player_dribbles['attempts']
southampton_players1['dribbles_completed'] = player_dribbles['success']
southampton_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
southampton_players1['tackles'] = player_tackles['total']
southampton_players1['blocks'] = player_tackles['blocks']
southampton_players1['interceptions'] = player_tackles['interceptions']
southampton_players1['fouls_drawn'] = player_fouls['drawn']
southampton_players1['fouls_committed'] = player_fouls['committed']
southampton_players1['yellow_cards'] = player_cards['yellow']
southampton_players1['red_cards'] = player_cards['red']
southampton_players1['yellow_to_red_cards'] = player_cards['yellowred']
southampton_players1['sub_in'] = player_subs['in']
southampton_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
southampton_players1 = southampton_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"41","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
southampton_players2 = pd.DataFrame()

southampton_players2['name'] = df_p1['name']
southampton_players2['first_name'] = df_p1['firstname']
southampton_players2['last_name'] = df_p1['lastname']
southampton_players2['id'] = df_p1['id']
southampton_players2['team'] = player_team['name']
southampton_players2['team_id'] = player_team['id']
southampton_players2['league'] = player_league['name']
southampton_players2['league_id'] = player_league['id']
southampton_players2['age'] = df_p1['age']
southampton_players2['birth'] = player_birth['date']
southampton_players2['nationality'] = df_p1['nationality']
southampton_players2['app'] = player_games['appearences']
southampton_players2['mins'] = player_games['minutes']
southampton_players2['goals'] = player_goals['total']
southampton_players2['shots'] = player_shots['total']
southampton_players2['shots_on_target'] = player_shots['on']
southampton_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
southampton_players2['assists'] = player_goals['assists']
southampton_players2['passes'] = player_passes['total']
southampton_players2['passes_completed'] = player_passes['accuracy']
# southampton_players2['pass_accuracy_%'] = df_p1['name']
southampton_players2['dribbles'] = player_dribbles['attempts']
southampton_players2['dribbles_completed'] = player_dribbles['success']
southampton_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
southampton_players2['tackles'] = player_tackles['total']
southampton_players2['blocks'] = player_tackles['blocks']
southampton_players2['interceptions'] = player_tackles['interceptions']
southampton_players2['fouls_drawn'] = player_fouls['drawn']
southampton_players2['fouls_committed'] = player_fouls['committed']
southampton_players2['yellow_cards'] = player_cards['yellow']
southampton_players2['red_cards'] = player_cards['red']
southampton_players2['yellow_to_red_cards'] = player_cards['yellowred']
southampton_players2['sub_in'] = player_subs['in']
southampton_players2['sub_out'] = player_subs['out']

southampton_players2 = southampton_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
southampton_players = pd.concat([southampton_players1, southampton_players2])
southampton_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column



####### SPURS ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"47","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
spurs_players1 = pd.DataFrame()

spurs_players1['name'] = df_p1['name']
spurs_players1['first_name'] = df_p1['firstname']
spurs_players1['last_name'] = df_p1['lastname']
spurs_players1['id'] = df_p1['id']
spurs_players1['team'] = player_team['name']
spurs_players1['team_id'] = player_team['id']
spurs_players1['league'] = player_league['name']
spurs_players1['league_id'] = player_league['id']
spurs_players1['age'] = df_p1['age']
spurs_players1['birth'] = player_birth['date']
spurs_players1['nationality'] = df_p1['nationality']
spurs_players1['app'] = player_games['appearences']
spurs_players1['mins'] = player_games['minutes']
spurs_players1['goals'] = player_goals['total']
spurs_players1['shots'] = player_shots['total']
spurs_players1['shots_on_target'] = player_shots['on']
spurs_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
spurs_players1['assists'] = player_goals['assists']
spurs_players1['passes'] = player_passes['total']
spurs_players1['passes_completed'] = player_passes['accuracy']
# spurs_players1['pass_accuracy_%'] = df_p1['name']
spurs_players1['dribbles'] = player_dribbles['attempts']
spurs_players1['dribbles_completed'] = player_dribbles['success']
spurs_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
spurs_players1['tackles'] = player_tackles['total']
spurs_players1['blocks'] = player_tackles['blocks']
spurs_players1['interceptions'] = player_tackles['interceptions']
spurs_players1['fouls_drawn'] = player_fouls['drawn']
spurs_players1['fouls_committed'] = player_fouls['committed']
spurs_players1['yellow_cards'] = player_cards['yellow']
spurs_players1['red_cards'] = player_cards['red']
spurs_players1['yellow_to_red_cards'] = player_cards['yellowred']
spurs_players1['sub_in'] = player_subs['in']
spurs_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
spurs_players1 = spurs_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"47","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2','data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
spurs_players2 = pd.DataFrame()

spurs_players2['name'] = df_p1['name']
spurs_players2['first_name'] = df_p1['firstname']
spurs_players2['last_name'] = df_p1['lastname']
spurs_players2['id'] = df_p1['id']
spurs_players2['team'] = player_team['name']
spurs_players2['team_id'] = player_team['id']
spurs_players2['league'] = player_league['name']
spurs_players2['league_id'] = player_league['id']
spurs_players2['age'] = df_p1['age']
spurs_players2['birth'] = player_birth['date']
spurs_players2['nationality'] = df_p1['nationality']
spurs_players2['app'] = player_games['appearences']
spurs_players2['mins'] = player_games['minutes']
spurs_players2['goals'] = player_goals['total']
spurs_players2['shots'] = player_shots['total']
spurs_players2['shots_on_target'] = player_shots['on']
spurs_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
spurs_players2['assists'] = player_goals['assists']
spurs_players2['passes'] = player_passes['total']
spurs_players2['passes_completed'] = player_passes['accuracy']
# spurs_players2['pass_accuracy_%'] = df_p1['name']
spurs_players2['dribbles'] = player_dribbles['attempts']
spurs_players2['dribbles_completed'] = player_dribbles['success']
spurs_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
spurs_players2['tackles'] = player_tackles['total']
spurs_players2['blocks'] = player_tackles['blocks']
spurs_players2['interceptions'] = player_tackles['interceptions']
spurs_players2['fouls_drawn'] = player_fouls['drawn']
spurs_players2['fouls_committed'] = player_fouls['committed']
spurs_players2['yellow_cards'] = player_cards['yellow']
spurs_players2['red_cards'] = player_cards['red']
spurs_players2['yellow_to_red_cards'] = player_cards['yellowred']
spurs_players2['sub_in'] = player_subs['in']
spurs_players2['sub_out'] = player_subs['out']

spurs_players2 = spurs_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
spurs_players = pd.concat([spurs_players1, spurs_players2])
spurs_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### WATFORD ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"38","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
watford_players1 = pd.DataFrame()

watford_players1['name'] = df_p1['name']
watford_players1['first_name'] = df_p1['firstname']
watford_players1['last_name'] = df_p1['lastname']
watford_players1['id'] = df_p1['id']
watford_players1['team'] = player_team['name']
watford_players1['team_id'] = player_team['id']
watford_players1['league'] = player_league['name']
watford_players1['league_id'] = player_league['id']
watford_players1['age'] = df_p1['age']
watford_players1['birth'] = player_birth['date']
watford_players1['nationality'] = df_p1['nationality']
watford_players1['app'] = player_games['appearences']
watford_players1['mins'] = player_games['minutes']
watford_players1['goals'] = player_goals['total']
watford_players1['shots'] = player_shots['total']
watford_players1['shots_on_target'] = player_shots['on']
watford_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
watford_players1['assists'] = player_goals['assists']
watford_players1['passes'] = player_passes['total']
watford_players1['passes_completed'] = player_passes['accuracy']
# watford_players1['pass_accuracy_%'] = df_p1['name']
watford_players1['dribbles'] = player_dribbles['attempts']
watford_players1['dribbles_completed'] = player_dribbles['success']
watford_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
watford_players1['tackles'] = player_tackles['total']
watford_players1['blocks'] = player_tackles['blocks']
watford_players1['interceptions'] = player_tackles['interceptions']
watford_players1['fouls_drawn'] = player_fouls['drawn']
watford_players1['fouls_committed'] = player_fouls['committed']
watford_players1['yellow_cards'] = player_cards['yellow']
watford_players1['red_cards'] = player_cards['red']
watford_players1['yellow_to_red_cards'] = player_cards['yellowred']
watford_players1['sub_in'] = player_subs['in']
watford_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
watford_players1 = watford_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"38","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
watford_players2 = pd.DataFrame()

watford_players2['name'] = df_p1['name']
watford_players2['first_name'] = df_p1['firstname']
watford_players2['last_name'] = df_p1['lastname']
watford_players2['id'] = df_p1['id']
watford_players2['team'] = player_team['name']
watford_players2['team_id'] = player_team['id']
watford_players2['league'] = player_league['name']
watford_players2['league_id'] = player_league['id']
watford_players2['age'] = df_p1['age']
watford_players2['birth'] = player_birth['date']
watford_players2['nationality'] = df_p1['nationality']
watford_players2['app'] = player_games['appearences']
watford_players2['mins'] = player_games['minutes']
watford_players2['goals'] = player_goals['total']
watford_players2['shots'] = player_shots['total']
watford_players2['shots_on_target'] = player_shots['on']
watford_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
watford_players2['assists'] = player_goals['assists']
watford_players2['passes'] = player_passes['total']
watford_players2['passes_completed'] = player_passes['accuracy']
# watford_players2['pass_accuracy_%'] = df_p1['name']
watford_players2['dribbles'] = player_dribbles['attempts']
watford_players2['dribbles_completed'] = player_dribbles['success']
watford_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
watford_players2['tackles'] = player_tackles['total']
watford_players2['blocks'] = player_tackles['blocks']
watford_players2['interceptions'] = player_tackles['interceptions']
watford_players2['fouls_drawn'] = player_fouls['drawn']
watford_players2['fouls_committed'] = player_fouls['committed']
watford_players2['yellow_cards'] = player_cards['yellow']
watford_players2['red_cards'] = player_cards['red']
watford_players2['yellow_to_red_cards'] = player_cards['yellowred']
watford_players2['sub_in'] = player_subs['in']
watford_players2['sub_out'] = player_subs['out']

watford_players2 = watford_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
watford_players = pd.concat([watford_players1, watford_players2])
watford_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### WEST HAM ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"48","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
west_ham_players1 = pd.DataFrame()

west_ham_players1['name'] = df_p1['name']
west_ham_players1['first_name'] = df_p1['firstname']
west_ham_players1['last_name'] = df_p1['lastname']
west_ham_players1['id'] = df_p1['id']
west_ham_players1['team'] = player_team['name']
west_ham_players1['team_id'] = player_team['id']
west_ham_players1['league'] = player_league['name']
west_ham_players1['league_id'] = player_league['id']
west_ham_players1['age'] = df_p1['age']
west_ham_players1['birth'] = player_birth['date']
west_ham_players1['nationality'] = df_p1['nationality']
west_ham_players1['app'] = player_games['appearences']
west_ham_players1['mins'] = player_games['minutes']
west_ham_players1['goals'] = player_goals['total']
west_ham_players1['shots'] = player_shots['total']
west_ham_players1['shots_on_target'] = player_shots['on']
west_ham_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
west_ham_players1['assists'] = player_goals['assists']
west_ham_players1['passes'] = player_passes['total']
west_ham_players1['passes_completed'] = player_passes['accuracy']
# west_ham_players1['pass_accuracy_%'] = df_p1['name']
west_ham_players1['dribbles'] = player_dribbles['attempts']
west_ham_players1['dribbles_completed'] = player_dribbles['success']
west_ham_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
west_ham_players1['tackles'] = player_tackles['total']
west_ham_players1['blocks'] = player_tackles['blocks']
west_ham_players1['interceptions'] = player_tackles['interceptions']
west_ham_players1['fouls_drawn'] = player_fouls['drawn']
west_ham_players1['fouls_committed'] = player_fouls['committed']
west_ham_players1['yellow_cards'] = player_cards['yellow']
west_ham_players1['red_cards'] = player_cards['red']
west_ham_players1['yellow_to_red_cards'] = player_cards['yellowred']
west_ham_players1['sub_in'] = player_subs['in']
west_ham_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
west_ham_players1 = west_ham_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"48","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
west_ham_players2 = pd.DataFrame()

west_ham_players2['name'] = df_p1['name']
west_ham_players2['first_name'] = df_p1['firstname']
west_ham_players2['last_name'] = df_p1['lastname']
west_ham_players2['id'] = df_p1['id']
west_ham_players2['team'] = player_team['name']
west_ham_players2['team_id'] = player_team['id']
west_ham_players2['league'] = player_league['name']
west_ham_players2['league_id'] = player_league['id']
west_ham_players2['age'] = df_p1['age']
west_ham_players2['birth'] = player_birth['date']
west_ham_players2['nationality'] = df_p1['nationality']
west_ham_players2['app'] = player_games['appearences']
west_ham_players2['mins'] = player_games['minutes']
west_ham_players2['goals'] = player_goals['total']
west_ham_players2['shots'] = player_shots['total']
west_ham_players2['shots_on_target'] = player_shots['on']
west_ham_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
west_ham_players2['assists'] = player_goals['assists']
west_ham_players2['passes'] = player_passes['total']
west_ham_players2['passes_completed'] = player_passes['accuracy']
# west_ham_players2['pass_accuracy_%'] = df_p1['name']
west_ham_players2['dribbles'] = player_dribbles['attempts']
west_ham_players2['dribbles_completed'] = player_dribbles['success']
west_ham_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
west_ham_players2['tackles'] = player_tackles['total']
west_ham_players2['blocks'] = player_tackles['blocks']
west_ham_players2['interceptions'] = player_tackles['interceptions']
west_ham_players2['fouls_drawn'] = player_fouls['drawn']
west_ham_players2['fouls_committed'] = player_fouls['committed']
west_ham_players2['yellow_cards'] = player_cards['yellow']
west_ham_players2['red_cards'] = player_cards['red']
west_ham_players2['yellow_to_red_cards'] = player_cards['yellowred']
west_ham_players2['sub_in'] = player_subs['in']
west_ham_players2['sub_out'] = player_subs['out']

west_ham_players2 = west_ham_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
west_ham_players = pd.concat([west_ham_players1, west_ham_players2])
west_ham_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column



####### WOLVERHAMPTON ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"39","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
wolves_players1 = pd.DataFrame()

wolves_players1['name'] = df_p1['name']
wolves_players1['first_name'] = df_p1['firstname']
wolves_players1['last_name'] = df_p1['lastname']
wolves_players1['id'] = df_p1['id']
wolves_players1['team'] = player_team['name']
wolves_players1['team_id'] = player_team['id']
wolves_players1['league'] = player_league['name']
wolves_players1['league_id'] = player_league['id']
wolves_players1['age'] = df_p1['age']
wolves_players1['birth'] = player_birth['date']
wolves_players1['nationality'] = df_p1['nationality']
wolves_players1['app'] = player_games['appearences']
wolves_players1['mins'] = player_games['minutes']
wolves_players1['goals'] = player_goals['total']
wolves_players1['shots'] = player_shots['total']
wolves_players1['shots_on_target'] = player_shots['on']
wolves_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
wolves_players1['assists'] = player_goals['assists']
wolves_players1['passes'] = player_passes['total']
wolves_players1['passes_completed'] = player_passes['accuracy']
# wolves_players1['pass_accuracy_%'] = df_p1['name']
wolves_players1['dribbles'] = player_dribbles['attempts']
wolves_players1['dribbles_completed'] = player_dribbles['success']
wolves_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
wolves_players1['tackles'] = player_tackles['total']
wolves_players1['blocks'] = player_tackles['blocks']
wolves_players1['interceptions'] = player_tackles['interceptions']
wolves_players1['fouls_drawn'] = player_fouls['drawn']
wolves_players1['fouls_committed'] = player_fouls['committed']
wolves_players1['yellow_cards'] = player_cards['yellow']
wolves_players1['red_cards'] = player_cards['red']
wolves_players1['yellow_to_red_cards'] = player_cards['yellowred']
wolves_players1['sub_in'] = player_subs['in']
wolves_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
wolves_players1 = wolves_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"39","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
wolves_players2 = pd.DataFrame()

wolves_players2['name'] = df_p1['name']
wolves_players2['first_name'] = df_p1['firstname']
wolves_players2['last_name'] = df_p1['lastname']
wolves_players2['id'] = df_p1['id']
wolves_players2['team'] = player_team['name']
wolves_players2['team_id'] = player_team['id']
wolves_players2['league'] = player_league['name']
wolves_players2['league_id'] = player_league['id']
wolves_players2['age'] = df_p1['age']
wolves_players2['birth'] = player_birth['date']
wolves_players2['nationality'] = df_p1['nationality']
wolves_players2['app'] = player_games['appearences']
wolves_players2['mins'] = player_games['minutes']
wolves_players2['goals'] = player_goals['total']
wolves_players2['shots'] = player_shots['total']
wolves_players2['shots_on_target'] = player_shots['on']
wolves_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
wolves_players2['assists'] = player_goals['assists']
wolves_players2['passes'] = player_passes['total']
wolves_players2['passes_completed'] = player_passes['accuracy']
# wolves_players2['pass_accuracy_%'] = df_p1['name']
wolves_players2['dribbles'] = player_dribbles['attempts']
wolves_players2['dribbles_completed'] = player_dribbles['success']
wolves_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
wolves_players2['tackles'] = player_tackles['total']
wolves_players2['blocks'] = player_tackles['blocks']
wolves_players2['interceptions'] = player_tackles['interceptions']
wolves_players2['fouls_drawn'] = player_fouls['drawn']
wolves_players2['fouls_committed'] = player_fouls['committed']
wolves_players2['yellow_cards'] = player_cards['yellow']
wolves_players2['red_cards'] = player_cards['red']
wolves_players2['yellow_to_red_cards'] = player_cards['yellowred']
wolves_players2['sub_in'] = player_subs['in']
wolves_players2['sub_out'] = player_subs['out']

wolves_players2 = wolves_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
wolves_players = pd.concat([wolves_players1, wolves_players2])
wolves_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column


# Combine players from all teams in the league into a single data frame
prem_league_players = pd.concat([arsenal_players, 
                                 aston_villa_players, 
                                 brentford_players, 
                                 brighton_players, 
                                 burnley_players, 
                                 chelsea_players, 
                                 crystal_palace_players, 
                                 everton_players, 
                                 leeds_players, 
                                 leicester_players, 
                                 liverpool_players, 
                                 man_city_players, 
                                 man_utd_players, 
                                 newcastle_players, 
                                 norwich_players, 
                                 southampton_players, 
                                 spurs_players, 
                                 watford_players, 
                                 wolves_players], ignore_index=True)







####################################### 2. BUNDESLIGA ##############################################


####### 1899 HOFFENHEIM ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"167","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
hoffenheim_players1 = pd.DataFrame()

hoffenheim_players1['name'] = df_p1['name']
hoffenheim_players1['first_name'] = df_p1['firstname']
hoffenheim_players1['last_name'] = df_p1['lastname']
hoffenheim_players1['id'] = df_p1['id']
hoffenheim_players1['team'] = player_team['name']
hoffenheim_players1['team_id'] = player_team['id']
hoffenheim_players1['league'] = player_league['name']
hoffenheim_players1['league_id'] = player_league['id']
hoffenheim_players1['age'] = df_p1['age']
hoffenheim_players1['birth'] = player_birth['date']
hoffenheim_players1['nationality'] = df_p1['nationality']
hoffenheim_players1['app'] = player_games['appearences']
hoffenheim_players1['mins'] = player_games['minutes']
hoffenheim_players1['goals'] = player_goals['total']
hoffenheim_players1['shots'] = player_shots['total']
hoffenheim_players1['shots_on_target'] = player_shots['on']
hoffenheim_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
hoffenheim_players1['assists'] = player_goals['assists']
hoffenheim_players1['passes'] = player_passes['total']
hoffenheim_players1['passes_completed'] = player_passes['accuracy']
# hoffenheim_players1['pass_accuracy_%'] = df_p1['name']
hoffenheim_players1['dribbles'] = player_dribbles['attempts']
hoffenheim_players1['dribbles_completed'] = player_dribbles['success']
hoffenheim_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
hoffenheim_players1['tackles'] = player_tackles['total']
hoffenheim_players1['blocks'] = player_tackles['blocks']
hoffenheim_players1['interceptions'] = player_tackles['interceptions']
hoffenheim_players1['fouls_drawn'] = player_fouls['drawn']
hoffenheim_players1['fouls_committed'] = player_fouls['committed']
hoffenheim_players1['yellow_cards'] = player_cards['yellow']
hoffenheim_players1['red_cards'] = player_cards['red']
hoffenheim_players1['yellow_to_red_cards'] = player_cards['yellowred']
hoffenheim_players1['sub_in'] = player_subs['in']
hoffenheim_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
hoffenheim_players1 = hoffenheim_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"167","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
hoffenheim_players2 = pd.DataFrame()

hoffenheim_players2['name'] = df_p1['name']
hoffenheim_players2['first_name'] = df_p1['firstname']
hoffenheim_players2['last_name'] = df_p1['lastname']
hoffenheim_players2['id'] = df_p1['id']
hoffenheim_players2['team'] = player_team['name']
hoffenheim_players2['team_id'] = player_team['id']
hoffenheim_players2['league'] = player_league['name']
hoffenheim_players2['league_id'] = player_league['id']
hoffenheim_players2['age'] = df_p1['age']
hoffenheim_players2['birth'] = player_birth['date']
hoffenheim_players2['nationality'] = df_p1['nationality']
hoffenheim_players2['app'] = player_games['appearences']
hoffenheim_players2['mins'] = player_games['minutes']
hoffenheim_players2['goals'] = player_goals['total']
hoffenheim_players2['shots'] = player_shots['total']
hoffenheim_players2['shots_on_target'] = player_shots['on']
hoffenheim_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
hoffenheim_players2['assists'] = player_goals['assists']
hoffenheim_players2['passes'] = player_passes['total']
hoffenheim_players2['passes_completed'] = player_passes['accuracy']
# hoffenheim_players2['pass_accuracy_%'] = df_p1['name']
hoffenheim_players2['dribbles'] = player_dribbles['attempts']
hoffenheim_players2['dribbles_completed'] = player_dribbles['success']
hoffenheim_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
hoffenheim_players2['tackles'] = player_tackles['total']
hoffenheim_players2['blocks'] = player_tackles['blocks']
hoffenheim_players2['interceptions'] = player_tackles['interceptions']
hoffenheim_players2['fouls_drawn'] = player_fouls['drawn']
hoffenheim_players2['fouls_committed'] = player_fouls['committed']
hoffenheim_players2['yellow_cards'] = player_cards['yellow']
hoffenheim_players2['red_cards'] = player_cards['red']
hoffenheim_players2['yellow_to_red_cards'] = player_cards['yellowred']
hoffenheim_players2['sub_in'] = player_subs['in']
hoffenheim_players2['sub_out'] = player_subs['out']

hoffenheim_players2 = hoffenheim_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
hoffenheim_players = pd.concat([hoffenheim_players1, hoffenheim_players2])
hoffenheim_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### BIELEFELD ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"188","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
bielefeld_players1 = pd.DataFrame()

bielefeld_players1['name'] = df_p1['name']
bielefeld_players1['first_name'] = df_p1['firstname']
bielefeld_players1['last_name'] = df_p1['lastname']
bielefeld_players1['id'] = df_p1['id']
bielefeld_players1['team'] = player_team['name']
bielefeld_players1['team_id'] = player_team['id']
bielefeld_players1['league'] = player_league['name']
bielefeld_players1['league_id'] = player_league['id']
bielefeld_players1['age'] = df_p1['age']
bielefeld_players1['birth'] = player_birth['date']
bielefeld_players1['nationality'] = df_p1['nationality']
bielefeld_players1['app'] = player_games['appearences']
bielefeld_players1['mins'] = player_games['minutes']
bielefeld_players1['goals'] = player_goals['total']
bielefeld_players1['shots'] = player_shots['total']
bielefeld_players1['shots_on_target'] = player_shots['on']
bielefeld_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
bielefeld_players1['assists'] = player_goals['assists']
bielefeld_players1['passes'] = player_passes['total']
bielefeld_players1['passes_completed'] = player_passes['accuracy']
# bielefeld_players1['pass_accuracy_%'] = df_p1['name']
bielefeld_players1['dribbles'] = player_dribbles['attempts']
bielefeld_players1['dribbles_completed'] = player_dribbles['success']
bielefeld_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
bielefeld_players1['tackles'] = player_tackles['total']
bielefeld_players1['blocks'] = player_tackles['blocks']
bielefeld_players1['interceptions'] = player_tackles['interceptions']
bielefeld_players1['fouls_drawn'] = player_fouls['drawn']
bielefeld_players1['fouls_committed'] = player_fouls['committed']
bielefeld_players1['yellow_cards'] = player_cards['yellow']
bielefeld_players1['red_cards'] = player_cards['red']
bielefeld_players1['yellow_to_red_cards'] = player_cards['yellowred']
bielefeld_players1['sub_in'] = player_subs['in']
bielefeld_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
bielefeld_players1 = bielefeld_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"188","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
bielefeld_players2 = pd.DataFrame()

bielefeld_players2['name'] = df_p1['name']
bielefeld_players2['first_name'] = df_p1['firstname']
bielefeld_players2['last_name'] = df_p1['lastname']
bielefeld_players2['id'] = df_p1['id']
bielefeld_players2['team'] = player_team['name']
bielefeld_players2['team_id'] = player_team['id']
bielefeld_players2['league'] = player_league['name']
bielefeld_players2['league_id'] = player_league['id']
bielefeld_players2['age'] = df_p1['age']
bielefeld_players2['birth'] = player_birth['date']
bielefeld_players2['nationality'] = df_p1['nationality']
bielefeld_players2['app'] = player_games['appearences']
bielefeld_players2['mins'] = player_games['minutes']
bielefeld_players2['goals'] = player_goals['total']
bielefeld_players2['shots'] = player_shots['total']
bielefeld_players2['shots_on_target'] = player_shots['on']
bielefeld_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
bielefeld_players2['assists'] = player_goals['assists']
bielefeld_players2['passes'] = player_passes['total']
bielefeld_players2['passes_completed'] = player_passes['accuracy']
# bielefeld_players2['pass_accuracy_%'] = df_p1['name']
bielefeld_players2['dribbles'] = player_dribbles['attempts']
bielefeld_players2['dribbles_completed'] = player_dribbles['success']
bielefeld_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
bielefeld_players2['tackles'] = player_tackles['total']
bielefeld_players2['blocks'] = player_tackles['blocks']
bielefeld_players2['interceptions'] = player_tackles['interceptions']
bielefeld_players2['fouls_drawn'] = player_fouls['drawn']
bielefeld_players2['fouls_committed'] = player_fouls['committed']
bielefeld_players2['yellow_cards'] = player_cards['yellow']
bielefeld_players2['red_cards'] = player_cards['red']
bielefeld_players2['yellow_to_red_cards'] = player_cards['yellowred']
bielefeld_players2['sub_in'] = player_subs['in']
bielefeld_players2['sub_out'] = player_subs['out']

bielefeld_players2 = bielefeld_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
bielefeld_players = pd.concat([bielefeld_players1, bielefeld_players2])
bielefeld_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### BAYER LEVERKUSEN ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"168","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
leverkusen_players1 = pd.DataFrame()

leverkusen_players1['name'] = df_p1['name']
leverkusen_players1['first_name'] = df_p1['firstname']
leverkusen_players1['last_name'] = df_p1['lastname']
leverkusen_players1['id'] = df_p1['id']
leverkusen_players1['team'] = player_team['name']
leverkusen_players1['team_id'] = player_team['id']
leverkusen_players1['league'] = player_league['name']
leverkusen_players1['league_id'] = player_league['id']
leverkusen_players1['age'] = df_p1['age']
leverkusen_players1['birth'] = player_birth['date']
leverkusen_players1['nationality'] = df_p1['nationality']
leverkusen_players1['app'] = player_games['appearences']
leverkusen_players1['mins'] = player_games['minutes']
leverkusen_players1['goals'] = player_goals['total']
leverkusen_players1['shots'] = player_shots['total']
leverkusen_players1['shots_on_target'] = player_shots['on']
leverkusen_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
leverkusen_players1['assists'] = player_goals['assists']
leverkusen_players1['passes'] = player_passes['total']
leverkusen_players1['passes_completed'] = player_passes['accuracy']
# leverkusen_players1['pass_accuracy_%'] = df_p1['name']
leverkusen_players1['dribbles'] = player_dribbles['attempts']
leverkusen_players1['dribbles_completed'] = player_dribbles['success']
leverkusen_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
leverkusen_players1['tackles'] = player_tackles['total']
leverkusen_players1['blocks'] = player_tackles['blocks']
leverkusen_players1['interceptions'] = player_tackles['interceptions']
leverkusen_players1['fouls_drawn'] = player_fouls['drawn']
leverkusen_players1['fouls_committed'] = player_fouls['committed']
leverkusen_players1['yellow_cards'] = player_cards['yellow']
leverkusen_players1['red_cards'] = player_cards['red']
leverkusen_players1['yellow_to_red_cards'] = player_cards['yellowred']
leverkusen_players1['sub_in'] = player_subs['in']
leverkusen_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
leverkusen_players1 = leverkusen_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"168","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
leverkusen_players2 = pd.DataFrame()

leverkusen_players2['name'] = df_p1['name']
leverkusen_players2['first_name'] = df_p1['firstname']
leverkusen_players2['last_name'] = df_p1['lastname']
leverkusen_players2['id'] = df_p1['id']
leverkusen_players2['team'] = player_team['name']
leverkusen_players2['team_id'] = player_team['id']
leverkusen_players2['league'] = player_league['name']
leverkusen_players2['league_id'] = player_league['id']
leverkusen_players2['age'] = df_p1['age']
leverkusen_players2['birth'] = player_birth['date']
leverkusen_players2['nationality'] = df_p1['nationality']
leverkusen_players2['app'] = player_games['appearences']
leverkusen_players2['mins'] = player_games['minutes']
leverkusen_players2['goals'] = player_goals['total']
leverkusen_players2['shots'] = player_shots['total']
leverkusen_players2['shots_on_target'] = player_shots['on']
leverkusen_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
leverkusen_players2['assists'] = player_goals['assists']
leverkusen_players2['passes'] = player_passes['total']
leverkusen_players2['passes_completed'] = player_passes['accuracy']
# leverkusen_players2['pass_accuracy_%'] = df_p1['name']
leverkusen_players2['dribbles'] = player_dribbles['attempts']
leverkusen_players2['dribbles_completed'] = player_dribbles['success']
leverkusen_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
leverkusen_players2['tackles'] = player_tackles['total']
leverkusen_players2['blocks'] = player_tackles['blocks']
leverkusen_players2['interceptions'] = player_tackles['interceptions']
leverkusen_players2['fouls_drawn'] = player_fouls['drawn']
leverkusen_players2['fouls_committed'] = player_fouls['committed']
leverkusen_players2['yellow_cards'] = player_cards['yellow']
leverkusen_players2['red_cards'] = player_cards['red']
leverkusen_players2['yellow_to_red_cards'] = player_cards['yellowred']
leverkusen_players2['sub_in'] = player_subs['in']
leverkusen_players2['sub_out'] = player_subs['out']

leverkusen_players2 = leverkusen_players2.fillna(0)



# Stage 3: Concatenate all data frames for the team's players
leverkusen_players = pd.concat([leverkusen_players1, leverkusen_players2])
leverkusen_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### BAYERN MUNICH ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"157","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
bayern_munich_players1 = pd.DataFrame()

bayern_munich_players1['name'] = df_p1['name']
bayern_munich_players1['first_name'] = df_p1['firstname']
bayern_munich_players1['last_name'] = df_p1['lastname']
bayern_munich_players1['id'] = df_p1['id']
bayern_munich_players1['team'] = player_team['name']
bayern_munich_players1['team_id'] = player_team['id']
bayern_munich_players1['league'] = player_league['name']
bayern_munich_players1['league_id'] = player_league['id']
bayern_munich_players1['age'] = df_p1['age']
bayern_munich_players1['birth'] = player_birth['date']
bayern_munich_players1['nationality'] = df_p1['nationality']
bayern_munich_players1['app'] = player_games['appearences']
bayern_munich_players1['mins'] = player_games['minutes']
bayern_munich_players1['goals'] = player_goals['total']
bayern_munich_players1['shots'] = player_shots['total']
bayern_munich_players1['shots_on_target'] = player_shots['on']
bayern_munich_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
bayern_munich_players1['assists'] = player_goals['assists']
bayern_munich_players1['passes'] = player_passes['total']
bayern_munich_players1['passes_completed'] = player_passes['accuracy']
# bayern_munich_players1['pass_accuracy_%'] = df_p1['name']
bayern_munich_players1['dribbles'] = player_dribbles['attempts']
bayern_munich_players1['dribbles_completed'] = player_dribbles['success']
bayern_munich_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
bayern_munich_players1['tackles'] = player_tackles['total']
bayern_munich_players1['blocks'] = player_tackles['blocks']
bayern_munich_players1['interceptions'] = player_tackles['interceptions']
bayern_munich_players1['fouls_drawn'] = player_fouls['drawn']
bayern_munich_players1['fouls_committed'] = player_fouls['committed']
bayern_munich_players1['yellow_cards'] = player_cards['yellow']
bayern_munich_players1['red_cards'] = player_cards['red']
bayern_munich_players1['yellow_to_red_cards'] = player_cards['yellowred']
bayern_munich_players1['sub_in'] = player_subs['in']
bayern_munich_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
bayern_munich_players1 = bayern_munich_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"157","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
bayern_munich_players2 = pd.DataFrame()

bayern_munich_players2['name'] = df_p1['name']
bayern_munich_players2['first_name'] = df_p1['firstname']
bayern_munich_players2['last_name'] = df_p1['lastname']
bayern_munich_players2['id'] = df_p1['id']
bayern_munich_players2['team'] = player_team['name']
bayern_munich_players2['team_id'] = player_team['id']
bayern_munich_players2['league'] = player_league['name']
bayern_munich_players2['league_id'] = player_league['id']
bayern_munich_players2['age'] = df_p1['age']
bayern_munich_players2['birth'] = player_birth['date']
bayern_munich_players2['nationality'] = df_p1['nationality']
bayern_munich_players2['app'] = player_games['appearences']
bayern_munich_players2['mins'] = player_games['minutes']
bayern_munich_players2['goals'] = player_goals['total']
bayern_munich_players2['shots'] = player_shots['total']
bayern_munich_players2['shots_on_target'] = player_shots['on']
bayern_munich_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
bayern_munich_players2['assists'] = player_goals['assists']
bayern_munich_players2['passes'] = player_passes['total']
bayern_munich_players2['passes_completed'] = player_passes['accuracy']
# bayern_munich_players2['pass_accuracy_%'] = df_p1['name']
bayern_munich_players2['dribbles'] = player_dribbles['attempts']
bayern_munich_players2['dribbles_completed'] = player_dribbles['success']
bayern_munich_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
bayern_munich_players2['tackles'] = player_tackles['total']
bayern_munich_players2['blocks'] = player_tackles['blocks']
bayern_munich_players2['interceptions'] = player_tackles['interceptions']
bayern_munich_players2['fouls_drawn'] = player_fouls['drawn']
bayern_munich_players2['fouls_committed'] = player_fouls['committed']
bayern_munich_players2['yellow_cards'] = player_cards['yellow']
bayern_munich_players2['red_cards'] = player_cards['red']
bayern_munich_players2['yellow_to_red_cards'] = player_cards['yellowred']
bayern_munich_players2['sub_in'] = player_subs['in']
bayern_munich_players2['sub_out'] = player_subs['out']

bayern_munich_players2 = bayern_munich_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
bayern_munich_players = pd.concat([bayern_munich_players1, bayern_munich_players2])
bayern_munich_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### BORUSSIA DORTMUND ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"165","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
dortmund_players1 = pd.DataFrame()

dortmund_players1['name'] = df_p1['name']
dortmund_players1['first_name'] = df_p1['firstname']
dortmund_players1['last_name'] = df_p1['lastname']
dortmund_players1['id'] = df_p1['id']
dortmund_players1['team'] = player_team['name']
dortmund_players1['team_id'] = player_team['id']
dortmund_players1['league'] = player_league['name']
dortmund_players1['league_id'] = player_league['id']
dortmund_players1['age'] = df_p1['age']
dortmund_players1['birth'] = player_birth['date']
dortmund_players1['nationality'] = df_p1['nationality']
dortmund_players1['app'] = player_games['appearences']
dortmund_players1['mins'] = player_games['minutes']
dortmund_players1['goals'] = player_goals['total']
dortmund_players1['shots'] = player_shots['total']
dortmund_players1['shots_on_target'] = player_shots['on']
dortmund_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
dortmund_players1['assists'] = player_goals['assists']
dortmund_players1['passes'] = player_passes['total']
dortmund_players1['passes_completed'] = player_passes['accuracy']
# dortmund_players1['pass_accuracy_%'] = df_p1['name']
dortmund_players1['dribbles'] = player_dribbles['attempts']
dortmund_players1['dribbles_completed'] = player_dribbles['success']
dortmund_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
dortmund_players1['tackles'] = player_tackles['total']
dortmund_players1['blocks'] = player_tackles['blocks']
dortmund_players1['interceptions'] = player_tackles['interceptions']
dortmund_players1['fouls_drawn'] = player_fouls['drawn']
dortmund_players1['fouls_committed'] = player_fouls['committed']
dortmund_players1['yellow_cards'] = player_cards['yellow']
dortmund_players1['red_cards'] = player_cards['red']
dortmund_players1['yellow_to_red_cards'] = player_cards['yellowred']
dortmund_players1['sub_in'] = player_subs['in']
dortmund_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
dortmund_players1 = dortmund_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"165","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
dortmund_players2 = pd.DataFrame()

dortmund_players2['name'] = df_p1['name']
dortmund_players2['first_name'] = df_p1['firstname']
dortmund_players2['last_name'] = df_p1['lastname']
dortmund_players2['id'] = df_p1['id']
dortmund_players2['team'] = player_team['name']
dortmund_players2['team_id'] = player_team['id']
dortmund_players2['league'] = player_league['name']
dortmund_players2['league_id'] = player_league['id']
dortmund_players2['age'] = df_p1['age']
dortmund_players2['birth'] = player_birth['date']
dortmund_players2['nationality'] = df_p1['nationality']
dortmund_players2['app'] = player_games['appearences']
dortmund_players2['mins'] = player_games['minutes']
dortmund_players2['goals'] = player_goals['total']
dortmund_players2['shots'] = player_shots['total']
dortmund_players2['shots_on_target'] = player_shots['on']
dortmund_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
dortmund_players2['assists'] = player_goals['assists']
dortmund_players2['passes'] = player_passes['total']
dortmund_players2['passes_completed'] = player_passes['accuracy']
# dortmund_players2['pass_accuracy_%'] = df_p1['name']
dortmund_players2['dribbles'] = player_dribbles['attempts']
dortmund_players2['dribbles_completed'] = player_dribbles['success']
dortmund_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
dortmund_players2['tackles'] = player_tackles['total']
dortmund_players2['blocks'] = player_tackles['blocks']
dortmund_players2['interceptions'] = player_tackles['interceptions']
dortmund_players2['fouls_drawn'] = player_fouls['drawn']
dortmund_players2['fouls_committed'] = player_fouls['committed']
dortmund_players2['yellow_cards'] = player_cards['yellow']
dortmund_players2['red_cards'] = player_cards['red']
dortmund_players2['yellow_to_red_cards'] = player_cards['yellowred']
dortmund_players2['sub_in'] = player_subs['in']
dortmund_players2['sub_out'] = player_subs['out']

dortmund_players2 = dortmund_players2.fillna(0)


# Stage 3: Concatenate all data frames for the team's players
dortmund_players = pd.concat([dortmund_players1, dortmund_players2])
dortmund_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### BORUSSIA MONCHENGLADBACH ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"163","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
monchengladbach_players1 = pd.DataFrame()

monchengladbach_players1['name'] = df_p1['name']
monchengladbach_players1['first_name'] = df_p1['firstname']
monchengladbach_players1['last_name'] = df_p1['lastname']
monchengladbach_players1['id'] = df_p1['id']
monchengladbach_players1['team'] = player_team['name']
monchengladbach_players1['team_id'] = player_team['id']
monchengladbach_players1['league'] = player_league['name']
monchengladbach_players1['league_id'] = player_league['id']
monchengladbach_players1['age'] = df_p1['age']
monchengladbach_players1['birth'] = player_birth['date']
monchengladbach_players1['nationality'] = df_p1['nationality']
monchengladbach_players1['app'] = player_games['appearences']
monchengladbach_players1['mins'] = player_games['minutes']
monchengladbach_players1['goals'] = player_goals['total']
monchengladbach_players1['shots'] = player_shots['total']
monchengladbach_players1['shots_on_target'] = player_shots['on']
monchengladbach_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
monchengladbach_players1['assists'] = player_goals['assists']
monchengladbach_players1['passes'] = player_passes['total']
monchengladbach_players1['passes_completed'] = player_passes['accuracy']
# monchengladbach_players1['pass_accuracy_%'] = df_p1['name']
monchengladbach_players1['dribbles'] = player_dribbles['attempts']
monchengladbach_players1['dribbles_completed'] = player_dribbles['success']
monchengladbach_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
monchengladbach_players1['tackles'] = player_tackles['total']
monchengladbach_players1['blocks'] = player_tackles['blocks']
monchengladbach_players1['interceptions'] = player_tackles['interceptions']
monchengladbach_players1['fouls_drawn'] = player_fouls['drawn']
monchengladbach_players1['fouls_committed'] = player_fouls['committed']
monchengladbach_players1['yellow_cards'] = player_cards['yellow']
monchengladbach_players1['red_cards'] = player_cards['red']
monchengladbach_players1['yellow_to_red_cards'] = player_cards['yellowred']
monchengladbach_players1['sub_in'] = player_subs['in']
monchengladbach_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
monchengladbach_players1 = monchengladbach_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"163","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
monchengladbach_players2 = pd.DataFrame()

monchengladbach_players2['name'] = df_p1['name']
monchengladbach_players2['first_name'] = df_p1['firstname']
monchengladbach_players2['last_name'] = df_p1['lastname']
monchengladbach_players2['id'] = df_p1['id']
monchengladbach_players2['team'] = player_team['name']
monchengladbach_players2['team_id'] = player_team['id']
monchengladbach_players2['league'] = player_league['name']
monchengladbach_players2['league_id'] = player_league['id']
monchengladbach_players2['age'] = df_p1['age']
monchengladbach_players2['birth'] = player_birth['date']
monchengladbach_players2['nationality'] = df_p1['nationality']
monchengladbach_players2['app'] = player_games['appearences']
monchengladbach_players2['mins'] = player_games['minutes']
monchengladbach_players2['goals'] = player_goals['total']
monchengladbach_players2['shots'] = player_shots['total']
monchengladbach_players2['shots_on_target'] = player_shots['on']
monchengladbach_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
monchengladbach_players2['assists'] = player_goals['assists']
monchengladbach_players2['passes'] = player_passes['total']
monchengladbach_players2['passes_completed'] = player_passes['accuracy']
# monchengladbach_players2['pass_accuracy_%'] = df_p1['name']
monchengladbach_players2['dribbles'] = player_dribbles['attempts']
monchengladbach_players2['dribbles_completed'] = player_dribbles['success']
monchengladbach_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
monchengladbach_players2['tackles'] = player_tackles['total']
monchengladbach_players2['blocks'] = player_tackles['blocks']
monchengladbach_players2['interceptions'] = player_tackles['interceptions']
monchengladbach_players2['fouls_drawn'] = player_fouls['drawn']
monchengladbach_players2['fouls_committed'] = player_fouls['committed']
monchengladbach_players2['yellow_cards'] = player_cards['yellow']
monchengladbach_players2['red_cards'] = player_cards['red']
monchengladbach_players2['yellow_to_red_cards'] = player_cards['yellowred']
monchengladbach_players2['sub_in'] = player_subs['in']
monchengladbach_players2['sub_out'] = player_subs['out']

monchengladbach_players2 = monchengladbach_players2.fillna(0)


# Stage 3: Concatenate all data frames for the team's players
monchengladbach_players = pd.concat([monchengladbach_players1, monchengladbach_players2])
monchengladbach_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### FRANKFURT ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"169","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
frankfurt_players1 = pd.DataFrame()

frankfurt_players1['name'] = df_p1['name']
frankfurt_players1['first_name'] = df_p1['firstname']
frankfurt_players1['last_name'] = df_p1['lastname']
frankfurt_players1['id'] = df_p1['id']
frankfurt_players1['team'] = player_team['name']
frankfurt_players1['team_id'] = player_team['id']
frankfurt_players1['league'] = player_league['name']
frankfurt_players1['league_id'] = player_league['id']
frankfurt_players1['age'] = df_p1['age']
frankfurt_players1['birth'] = player_birth['date']
frankfurt_players1['nationality'] = df_p1['nationality']
frankfurt_players1['app'] = player_games['appearences']
frankfurt_players1['mins'] = player_games['minutes']
frankfurt_players1['goals'] = player_goals['total']
frankfurt_players1['shots'] = player_shots['total']
frankfurt_players1['shots_on_target'] = player_shots['on']
frankfurt_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
frankfurt_players1['assists'] = player_goals['assists']
frankfurt_players1['passes'] = player_passes['total']
frankfurt_players1['passes_completed'] = player_passes['accuracy']
# frankfurt_players1['pass_accuracy_%'] = df_p1['name']
frankfurt_players1['dribbles'] = player_dribbles['attempts']
frankfurt_players1['dribbles_completed'] = player_dribbles['success']
frankfurt_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
frankfurt_players1['tackles'] = player_tackles['total']
frankfurt_players1['blocks'] = player_tackles['blocks']
frankfurt_players1['interceptions'] = player_tackles['interceptions']
frankfurt_players1['fouls_drawn'] = player_fouls['drawn']
frankfurt_players1['fouls_committed'] = player_fouls['committed']
frankfurt_players1['yellow_cards'] = player_cards['yellow']
frankfurt_players1['red_cards'] = player_cards['red']
frankfurt_players1['yellow_to_red_cards'] = player_cards['yellowred']
frankfurt_players1['sub_in'] = player_subs['in']
frankfurt_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
frankfurt_players1 = frankfurt_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"169","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
frankfurt_players2 = pd.DataFrame()

frankfurt_players2['name'] = df_p1['name']
frankfurt_players2['first_name'] = df_p1['firstname']
frankfurt_players2['last_name'] = df_p1['lastname']
frankfurt_players2['id'] = df_p1['id']
frankfurt_players2['team'] = player_team['name']
frankfurt_players2['team_id'] = player_team['id']
frankfurt_players2['league'] = player_league['name']
frankfurt_players2['league_id'] = player_league['id']
frankfurt_players2['age'] = df_p1['age']
frankfurt_players2['birth'] = player_birth['date']
frankfurt_players2['nationality'] = df_p1['nationality']
frankfurt_players2['app'] = player_games['appearences']
frankfurt_players2['mins'] = player_games['minutes']
frankfurt_players2['goals'] = player_goals['total']
frankfurt_players2['shots'] = player_shots['total']
frankfurt_players2['shots_on_target'] = player_shots['on']
frankfurt_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
frankfurt_players2['assists'] = player_goals['assists']
frankfurt_players2['passes'] = player_passes['total']
frankfurt_players2['passes_completed'] = player_passes['accuracy']
# frankfurt_players2['pass_accuracy_%'] = df_p1['name']
frankfurt_players2['dribbles'] = player_dribbles['attempts']
frankfurt_players2['dribbles_completed'] = player_dribbles['success']
frankfurt_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
frankfurt_players2['tackles'] = player_tackles['total']
frankfurt_players2['blocks'] = player_tackles['blocks']
frankfurt_players2['interceptions'] = player_tackles['interceptions']
frankfurt_players2['fouls_drawn'] = player_fouls['drawn']
frankfurt_players2['fouls_committed'] = player_fouls['committed']
frankfurt_players2['yellow_cards'] = player_cards['yellow']
frankfurt_players2['red_cards'] = player_cards['red']
frankfurt_players2['yellow_to_red_cards'] = player_cards['yellowred']
frankfurt_players2['sub_in'] = player_subs['in']
frankfurt_players2['sub_out'] = player_subs['out']

frankfurt_players2 = frankfurt_players2.fillna(0)


# Stage 3: Concatenate all data frames for the team's players
frankfurt_players = pd.concat([frankfurt_players1, frankfurt_players2])
frankfurt_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### FRANKFURT ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"169","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
augsburg_players1 = pd.DataFrame()

augsburg_players1['name'] = df_p1['name']
augsburg_players1['first_name'] = df_p1['firstname']
augsburg_players1['last_name'] = df_p1['lastname']
augsburg_players1['id'] = df_p1['id']
augsburg_players1['team'] = player_team['name']
augsburg_players1['team_id'] = player_team['id']
augsburg_players1['league'] = player_league['name']
augsburg_players1['league_id'] = player_league['id']
augsburg_players1['age'] = df_p1['age']
augsburg_players1['birth'] = player_birth['date']
augsburg_players1['nationality'] = df_p1['nationality']
augsburg_players1['app'] = player_games['appearences']
augsburg_players1['mins'] = player_games['minutes']
augsburg_players1['goals'] = player_goals['total']
augsburg_players1['shots'] = player_shots['total']
augsburg_players1['shots_on_target'] = player_shots['on']
augsburg_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
augsburg_players1['assists'] = player_goals['assists']
augsburg_players1['passes'] = player_passes['total']
augsburg_players1['passes_completed'] = player_passes['accuracy']
# augsburg_players1['pass_accuracy_%'] = df_p1['name']
augsburg_players1['dribbles'] = player_dribbles['attempts']
augsburg_players1['dribbles_completed'] = player_dribbles['success']
augsburg_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
augsburg_players1['tackles'] = player_tackles['total']
augsburg_players1['blocks'] = player_tackles['blocks']
augsburg_players1['interceptions'] = player_tackles['interceptions']
augsburg_players1['fouls_drawn'] = player_fouls['drawn']
augsburg_players1['fouls_committed'] = player_fouls['committed']
augsburg_players1['yellow_cards'] = player_cards['yellow']
augsburg_players1['red_cards'] = player_cards['red']
augsburg_players1['yellow_to_red_cards'] = player_cards['yellowred']
augsburg_players1['sub_in'] = player_subs['in']
augsburg_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
augsburg_players1 = augsburg_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"169","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
augsburg_players2 = pd.DataFrame()

augsburg_players2['name'] = df_p1['name']
augsburg_players2['first_name'] = df_p1['firstname']
augsburg_players2['last_name'] = df_p1['lastname']
augsburg_players2['id'] = df_p1['id']
augsburg_players2['team'] = player_team['name']
augsburg_players2['team_id'] = player_team['id']
augsburg_players2['league'] = player_league['name']
augsburg_players2['league_id'] = player_league['id']
augsburg_players2['age'] = df_p1['age']
augsburg_players2['birth'] = player_birth['date']
augsburg_players2['nationality'] = df_p1['nationality']
augsburg_players2['app'] = player_games['appearences']
augsburg_players2['mins'] = player_games['minutes']
augsburg_players2['goals'] = player_goals['total']
augsburg_players2['shots'] = player_shots['total']
augsburg_players2['shots_on_target'] = player_shots['on']
augsburg_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
augsburg_players2['assists'] = player_goals['assists']
augsburg_players2['passes'] = player_passes['total']
augsburg_players2['passes_completed'] = player_passes['accuracy']
# augsburg_players2['pass_accuracy_%'] = df_p1['name']
augsburg_players2['dribbles'] = player_dribbles['attempts']
augsburg_players2['dribbles_completed'] = player_dribbles['success']
augsburg_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
augsburg_players2['tackles'] = player_tackles['total']
augsburg_players2['blocks'] = player_tackles['blocks']
augsburg_players2['interceptions'] = player_tackles['interceptions']
augsburg_players2['fouls_drawn'] = player_fouls['drawn']
augsburg_players2['fouls_committed'] = player_fouls['committed']
augsburg_players2['yellow_cards'] = player_cards['yellow']
augsburg_players2['red_cards'] = player_cards['red']
augsburg_players2['yellow_to_red_cards'] = player_cards['yellowred']
augsburg_players2['sub_in'] = player_subs['in']
augsburg_players2['sub_out'] = player_subs['out']

augsburg_players2 = augsburg_players2.fillna(0)


# Stage 3: Concatenate all data frames for the team's players
augsburg_players = pd.concat([augsburg_players1, augsburg_players2])
augsburg_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### FC KOLN ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"192","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
koln_players1 = pd.DataFrame()

koln_players1['name'] = df_p1['name']
koln_players1['first_name'] = df_p1['firstname']
koln_players1['last_name'] = df_p1['lastname']
koln_players1['id'] = df_p1['id']
koln_players1['team'] = player_team['name']
koln_players1['team_id'] = player_team['id']
koln_players1['league'] = player_league['name']
koln_players1['league_id'] = player_league['id']
koln_players1['age'] = df_p1['age']
koln_players1['birth'] = player_birth['date']
koln_players1['nationality'] = df_p1['nationality']
koln_players1['app'] = player_games['appearences']
koln_players1['mins'] = player_games['minutes']
koln_players1['goals'] = player_goals['total']
koln_players1['shots'] = player_shots['total']
koln_players1['shots_on_target'] = player_shots['on']
koln_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
koln_players1['assists'] = player_goals['assists']
koln_players1['passes'] = player_passes['total']
koln_players1['passes_completed'] = player_passes['accuracy']
# koln_players1['pass_accuracy_%'] = df_p1['name']
koln_players1['dribbles'] = player_dribbles['attempts']
koln_players1['dribbles_completed'] = player_dribbles['success']
koln_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
koln_players1['tackles'] = player_tackles['total']
koln_players1['blocks'] = player_tackles['blocks']
koln_players1['interceptions'] = player_tackles['interceptions']
koln_players1['fouls_drawn'] = player_fouls['drawn']
koln_players1['fouls_committed'] = player_fouls['committed']
koln_players1['yellow_cards'] = player_cards['yellow']
koln_players1['red_cards'] = player_cards['red']
koln_players1['yellow_to_red_cards'] = player_cards['yellowred']
koln_players1['sub_in'] = player_subs['in']
koln_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
koln_players1 = koln_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"192","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
koln_players2 = pd.DataFrame()

koln_players2['name'] = df_p1['name']
koln_players2['first_name'] = df_p1['firstname']
koln_players2['last_name'] = df_p1['lastname']
koln_players2['id'] = df_p1['id']
koln_players2['team'] = player_team['name']
koln_players2['team_id'] = player_team['id']
koln_players2['league'] = player_league['name']
koln_players2['league_id'] = player_league['id']
koln_players2['age'] = df_p1['age']
koln_players2['birth'] = player_birth['date']
koln_players2['nationality'] = df_p1['nationality']
koln_players2['app'] = player_games['appearences']
koln_players2['mins'] = player_games['minutes']
koln_players2['goals'] = player_goals['total']
koln_players2['shots'] = player_shots['total']
koln_players2['shots_on_target'] = player_shots['on']
koln_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
koln_players2['assists'] = player_goals['assists']
koln_players2['passes'] = player_passes['total']
koln_players2['passes_completed'] = player_passes['accuracy']
# koln_players2['pass_accuracy_%'] = df_p1['name']
koln_players2['dribbles'] = player_dribbles['attempts']
koln_players2['dribbles_completed'] = player_dribbles['success']
koln_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
koln_players2['tackles'] = player_tackles['total']
koln_players2['blocks'] = player_tackles['blocks']
koln_players2['interceptions'] = player_tackles['interceptions']
koln_players2['fouls_drawn'] = player_fouls['drawn']
koln_players2['fouls_committed'] = player_fouls['committed']
koln_players2['yellow_cards'] = player_cards['yellow']
koln_players2['red_cards'] = player_cards['red']
koln_players2['yellow_to_red_cards'] = player_cards['yellowred']
koln_players2['sub_in'] = player_subs['in']
koln_players2['sub_out'] = player_subs['out']

koln_players2 = koln_players2.fillna(0)


# Stage 3: Concatenate all data frames for the team's players
koln_players = pd.concat([koln_players1, koln_players2])
koln_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### FSV MAINZ ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"164","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
mainz_players1 = pd.DataFrame()

mainz_players1['name'] = df_p1['name']
mainz_players1['first_name'] = df_p1['firstname']
mainz_players1['last_name'] = df_p1['lastname']
mainz_players1['id'] = df_p1['id']
mainz_players1['team'] = player_team['name']
mainz_players1['team_id'] = player_team['id']
mainz_players1['league'] = player_league['name']
mainz_players1['league_id'] = player_league['id']
mainz_players1['age'] = df_p1['age']
mainz_players1['birth'] = player_birth['date']
mainz_players1['nationality'] = df_p1['nationality']
mainz_players1['app'] = player_games['appearences']
mainz_players1['mins'] = player_games['minutes']
mainz_players1['goals'] = player_goals['total']
mainz_players1['shots'] = player_shots['total']
mainz_players1['shots_on_target'] = player_shots['on']
mainz_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
mainz_players1['assists'] = player_goals['assists']
mainz_players1['passes'] = player_passes['total']
mainz_players1['passes_completed'] = player_passes['accuracy']
# mainz_players1['pass_accuracy_%'] = df_p1['name']
mainz_players1['dribbles'] = player_dribbles['attempts']
mainz_players1['dribbles_completed'] = player_dribbles['success']
mainz_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
mainz_players1['tackles'] = player_tackles['total']
mainz_players1['blocks'] = player_tackles['blocks']
mainz_players1['interceptions'] = player_tackles['interceptions']
mainz_players1['fouls_drawn'] = player_fouls['drawn']
mainz_players1['fouls_committed'] = player_fouls['committed']
mainz_players1['yellow_cards'] = player_cards['yellow']
mainz_players1['red_cards'] = player_cards['red']
mainz_players1['yellow_to_red_cards'] = player_cards['yellowred']
mainz_players1['sub_in'] = player_subs['in']
mainz_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
mainz_players1 = mainz_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"164","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
mainz_players2 = pd.DataFrame()

mainz_players2['name'] = df_p1['name']
mainz_players2['first_name'] = df_p1['firstname']
mainz_players2['last_name'] = df_p1['lastname']
mainz_players2['id'] = df_p1['id']
mainz_players2['team'] = player_team['name']
mainz_players2['team_id'] = player_team['id']
mainz_players2['league'] = player_league['name']
mainz_players2['league_id'] = player_league['id']
mainz_players2['age'] = df_p1['age']
mainz_players2['birth'] = player_birth['date']
mainz_players2['nationality'] = df_p1['nationality']
mainz_players2['app'] = player_games['appearences']
mainz_players2['mins'] = player_games['minutes']
mainz_players2['goals'] = player_goals['total']
mainz_players2['shots'] = player_shots['total']
mainz_players2['shots_on_target'] = player_shots['on']
mainz_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
mainz_players2['assists'] = player_goals['assists']
mainz_players2['passes'] = player_passes['total']
mainz_players2['passes_completed'] = player_passes['accuracy']
# mainz_players2['pass_accuracy_%'] = df_p1['name']
mainz_players2['dribbles'] = player_dribbles['attempts']
mainz_players2['dribbles_completed'] = player_dribbles['success']
mainz_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
mainz_players2['tackles'] = player_tackles['total']
mainz_players2['blocks'] = player_tackles['blocks']
mainz_players2['interceptions'] = player_tackles['interceptions']
mainz_players2['fouls_drawn'] = player_fouls['drawn']
mainz_players2['fouls_committed'] = player_fouls['committed']
mainz_players2['yellow_cards'] = player_cards['yellow']
mainz_players2['red_cards'] = player_cards['red']
mainz_players2['yellow_to_red_cards'] = player_cards['yellowred']
mainz_players2['sub_in'] = player_subs['in']
mainz_players2['sub_out'] = player_subs['out']

mainz_players2 = mainz_players2.fillna(0)


# Stage 3: Concatenate all data frames for the team's players
mainz_players = pd.concat([mainz_players1, mainz_players2])
mainz_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column



####### HERTHA BERLIN ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"159","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
hertha_berlin_players1 = pd.DataFrame()

hertha_berlin_players1['name'] = df_p1['name']
hertha_berlin_players1['first_name'] = df_p1['firstname']
hertha_berlin_players1['last_name'] = df_p1['lastname']
hertha_berlin_players1['id'] = df_p1['id']
hertha_berlin_players1['team'] = player_team['name']
hertha_berlin_players1['team_id'] = player_team['id']
hertha_berlin_players1['league'] = player_league['name']
hertha_berlin_players1['league_id'] = player_league['id']
hertha_berlin_players1['age'] = df_p1['age']
hertha_berlin_players1['birth'] = player_birth['date']
hertha_berlin_players1['nationality'] = df_p1['nationality']
hertha_berlin_players1['app'] = player_games['appearences']
hertha_berlin_players1['mins'] = player_games['minutes']
hertha_berlin_players1['goals'] = player_goals['total']
hertha_berlin_players1['shots'] = player_shots['total']
hertha_berlin_players1['shots_on_target'] = player_shots['on']
hertha_berlin_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
hertha_berlin_players1['assists'] = player_goals['assists']
hertha_berlin_players1['passes'] = player_passes['total']
hertha_berlin_players1['passes_completed'] = player_passes['accuracy']
# hertha_berlin_players1['pass_accuracy_%'] = df_p1['name']
hertha_berlin_players1['dribbles'] = player_dribbles['attempts']
hertha_berlin_players1['dribbles_completed'] = player_dribbles['success']
hertha_berlin_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
hertha_berlin_players1['tackles'] = player_tackles['total']
hertha_berlin_players1['blocks'] = player_tackles['blocks']
hertha_berlin_players1['interceptions'] = player_tackles['interceptions']
hertha_berlin_players1['fouls_drawn'] = player_fouls['drawn']
hertha_berlin_players1['fouls_committed'] = player_fouls['committed']
hertha_berlin_players1['yellow_cards'] = player_cards['yellow']
hertha_berlin_players1['red_cards'] = player_cards['red']
hertha_berlin_players1['yellow_to_red_cards'] = player_cards['yellowred']
hertha_berlin_players1['sub_in'] = player_subs['in']
hertha_berlin_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
hertha_berlin_players1 = hertha_berlin_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"159","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
hertha_berlin_players2 = pd.DataFrame()

hertha_berlin_players2['name'] = df_p1['name']
hertha_berlin_players2['first_name'] = df_p1['firstname']
hertha_berlin_players2['last_name'] = df_p1['lastname']
hertha_berlin_players2['id'] = df_p1['id']
hertha_berlin_players2['team'] = player_team['name']
hertha_berlin_players2['team_id'] = player_team['id']
hertha_berlin_players2['league'] = player_league['name']
hertha_berlin_players2['league_id'] = player_league['id']
hertha_berlin_players2['age'] = df_p1['age']
hertha_berlin_players2['birth'] = player_birth['date']
hertha_berlin_players2['nationality'] = df_p1['nationality']
hertha_berlin_players2['app'] = player_games['appearences']
hertha_berlin_players2['mins'] = player_games['minutes']
hertha_berlin_players2['goals'] = player_goals['total']
hertha_berlin_players2['shots'] = player_shots['total']
hertha_berlin_players2['shots_on_target'] = player_shots['on']
hertha_berlin_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
hertha_berlin_players2['assists'] = player_goals['assists']
hertha_berlin_players2['passes'] = player_passes['total']
hertha_berlin_players2['passes_completed'] = player_passes['accuracy']
# hertha_berlin_players2['pass_accuracy_%'] = df_p1['name']
hertha_berlin_players2['dribbles'] = player_dribbles['attempts']
hertha_berlin_players2['dribbles_completed'] = player_dribbles['success']
hertha_berlin_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
hertha_berlin_players2['tackles'] = player_tackles['total']
hertha_berlin_players2['blocks'] = player_tackles['blocks']
hertha_berlin_players2['interceptions'] = player_tackles['interceptions']
hertha_berlin_players2['fouls_drawn'] = player_fouls['drawn']
hertha_berlin_players2['fouls_committed'] = player_fouls['committed']
hertha_berlin_players2['yellow_cards'] = player_cards['yellow']
hertha_berlin_players2['red_cards'] = player_cards['red']
hertha_berlin_players2['yellow_to_red_cards'] = player_cards['yellowred']
hertha_berlin_players2['sub_in'] = player_subs['in']
hertha_berlin_players2['sub_out'] = player_subs['out']

hertha_berlin_players2 = hertha_berlin_players2.fillna(0)


# Stage 3: Concatenate all data frames for the team's players
hertha_berlin_players = pd.concat([hertha_berlin_players1, hertha_berlin_players2])
hertha_berlin_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### RP LEIPZIG ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"173","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
leipzig_players1 = pd.DataFrame()

leipzig_players1['name'] = df_p1['name']
leipzig_players1['first_name'] = df_p1['firstname']
leipzig_players1['last_name'] = df_p1['lastname']
leipzig_players1['id'] = df_p1['id']
leipzig_players1['team'] = player_team['name']
leipzig_players1['team_id'] = player_team['id']
leipzig_players1['league'] = player_league['name']
leipzig_players1['league_id'] = player_league['id']
leipzig_players1['age'] = df_p1['age']
leipzig_players1['birth'] = player_birth['date']
leipzig_players1['nationality'] = df_p1['nationality']
leipzig_players1['app'] = player_games['appearences']
leipzig_players1['mins'] = player_games['minutes']
leipzig_players1['goals'] = player_goals['total']
leipzig_players1['shots'] = player_shots['total']
leipzig_players1['shots_on_target'] = player_shots['on']
leipzig_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
leipzig_players1['assists'] = player_goals['assists']
leipzig_players1['passes'] = player_passes['total']
leipzig_players1['passes_completed'] = player_passes['accuracy']
# leipzig_players1['pass_accuracy_%'] = df_p1['name']
leipzig_players1['dribbles'] = player_dribbles['attempts']
leipzig_players1['dribbles_completed'] = player_dribbles['success']
leipzig_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
leipzig_players1['tackles'] = player_tackles['total']
leipzig_players1['blocks'] = player_tackles['blocks']
leipzig_players1['interceptions'] = player_tackles['interceptions']
leipzig_players1['fouls_drawn'] = player_fouls['drawn']
leipzig_players1['fouls_committed'] = player_fouls['committed']
leipzig_players1['yellow_cards'] = player_cards['yellow']
leipzig_players1['red_cards'] = player_cards['red']
leipzig_players1['yellow_to_red_cards'] = player_cards['yellowred']
leipzig_players1['sub_in'] = player_subs['in']
leipzig_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
leipzig_players1 = leipzig_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"173","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
leipzig_players2 = pd.DataFrame()

leipzig_players2['name'] = df_p1['name']
leipzig_players2['first_name'] = df_p1['firstname']
leipzig_players2['last_name'] = df_p1['lastname']
leipzig_players2['id'] = df_p1['id']
leipzig_players2['team'] = player_team['name']
leipzig_players2['team_id'] = player_team['id']
leipzig_players2['league'] = player_league['name']
leipzig_players2['league_id'] = player_league['id']
leipzig_players2['age'] = df_p1['age']
leipzig_players2['birth'] = player_birth['date']
leipzig_players2['nationality'] = df_p1['nationality']
leipzig_players2['app'] = player_games['appearences']
leipzig_players2['mins'] = player_games['minutes']
leipzig_players2['goals'] = player_goals['total']
leipzig_players2['shots'] = player_shots['total']
leipzig_players2['shots_on_target'] = player_shots['on']
leipzig_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
leipzig_players2['assists'] = player_goals['assists']
leipzig_players2['passes'] = player_passes['total']
leipzig_players2['passes_completed'] = player_passes['accuracy']
# leipzig_players2['pass_accuracy_%'] = df_p1['name']
leipzig_players2['dribbles'] = player_dribbles['attempts']
leipzig_players2['dribbles_completed'] = player_dribbles['success']
leipzig_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
leipzig_players2['tackles'] = player_tackles['total']
leipzig_players2['blocks'] = player_tackles['blocks']
leipzig_players2['interceptions'] = player_tackles['interceptions']
leipzig_players2['fouls_drawn'] = player_fouls['drawn']
leipzig_players2['fouls_committed'] = player_fouls['committed']
leipzig_players2['yellow_cards'] = player_cards['yellow']
leipzig_players2['red_cards'] = player_cards['red']
leipzig_players2['yellow_to_red_cards'] = player_cards['yellowred']
leipzig_players2['sub_in'] = player_subs['in']
leipzig_players2['sub_out'] = player_subs['out']

leipzig_players2 = leipzig_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
leipzig_players = pd.concat([leipzig_players1, leipzig_players2])
leipzig_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### SC FREIBURG ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"160","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
freiburg_players1 = pd.DataFrame()

freiburg_players1['name'] = df_p1['name']
freiburg_players1['first_name'] = df_p1['firstname']
freiburg_players1['last_name'] = df_p1['lastname']
freiburg_players1['id'] = df_p1['id']
freiburg_players1['team'] = player_team['name']
freiburg_players1['team_id'] = player_team['id']
freiburg_players1['league'] = player_league['name']
freiburg_players1['league_id'] = player_league['id']
freiburg_players1['age'] = df_p1['age']
freiburg_players1['birth'] = player_birth['date']
freiburg_players1['nationality'] = df_p1['nationality']
freiburg_players1['app'] = player_games['appearences']
freiburg_players1['mins'] = player_games['minutes']
freiburg_players1['goals'] = player_goals['total']
freiburg_players1['shots'] = player_shots['total']
freiburg_players1['shots_on_target'] = player_shots['on']
freiburg_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
freiburg_players1['assists'] = player_goals['assists']
freiburg_players1['passes'] = player_passes['total']
freiburg_players1['passes_completed'] = player_passes['accuracy']
# freiburg_players1['pass_accuracy_%'] = df_p1['name']
freiburg_players1['dribbles'] = player_dribbles['attempts']
freiburg_players1['dribbles_completed'] = player_dribbles['success']
freiburg_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
freiburg_players1['tackles'] = player_tackles['total']
freiburg_players1['blocks'] = player_tackles['blocks']
freiburg_players1['interceptions'] = player_tackles['interceptions']
freiburg_players1['fouls_drawn'] = player_fouls['drawn']
freiburg_players1['fouls_committed'] = player_fouls['committed']
freiburg_players1['yellow_cards'] = player_cards['yellow']
freiburg_players1['red_cards'] = player_cards['red']
freiburg_players1['yellow_to_red_cards'] = player_cards['yellowred']
freiburg_players1['sub_in'] = player_subs['in']
freiburg_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
freiburg_players1 = freiburg_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"160","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
freiburg_players2 = pd.DataFrame()

freiburg_players2['name'] = df_p1['name']
freiburg_players2['first_name'] = df_p1['firstname']
freiburg_players2['last_name'] = df_p1['lastname']
freiburg_players2['id'] = df_p1['id']
freiburg_players2['team'] = player_team['name']
freiburg_players2['team_id'] = player_team['id']
freiburg_players2['league'] = player_league['name']
freiburg_players2['league_id'] = player_league['id']
freiburg_players2['age'] = df_p1['age']
freiburg_players2['birth'] = player_birth['date']
freiburg_players2['nationality'] = df_p1['nationality']
freiburg_players2['app'] = player_games['appearences']
freiburg_players2['mins'] = player_games['minutes']
freiburg_players2['goals'] = player_goals['total']
freiburg_players2['shots'] = player_shots['total']
freiburg_players2['shots_on_target'] = player_shots['on']
freiburg_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
freiburg_players2['assists'] = player_goals['assists']
freiburg_players2['passes'] = player_passes['total']
freiburg_players2['passes_completed'] = player_passes['accuracy']
# freiburg_players2['pass_accuracy_%'] = df_p1['name']
freiburg_players2['dribbles'] = player_dribbles['attempts']
freiburg_players2['dribbles_completed'] = player_dribbles['success']
freiburg_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
freiburg_players2['tackles'] = player_tackles['total']
freiburg_players2['blocks'] = player_tackles['blocks']
freiburg_players2['interceptions'] = player_tackles['interceptions']
freiburg_players2['fouls_drawn'] = player_fouls['drawn']
freiburg_players2['fouls_committed'] = player_fouls['committed']
freiburg_players2['yellow_cards'] = player_cards['yellow']
freiburg_players2['red_cards'] = player_cards['red']
freiburg_players2['yellow_to_red_cards'] = player_cards['yellowred']
freiburg_players2['sub_in'] = player_subs['in']
freiburg_players2['sub_out'] = player_subs['out']

freiburg_players2 = freiburg_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
freiburg_players = pd.concat([freiburg_players1, freiburg_players2])
freiburg_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### SPVGG GREUTHER FURTH ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"178","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
greuther_furth_players1 = pd.DataFrame()

greuther_furth_players1['name'] = df_p1['name']
greuther_furth_players1['first_name'] = df_p1['firstname']
greuther_furth_players1['last_name'] = df_p1['lastname']
greuther_furth_players1['id'] = df_p1['id']
greuther_furth_players1['team'] = player_team['name']
greuther_furth_players1['team_id'] = player_team['id']
greuther_furth_players1['league'] = player_league['name']
greuther_furth_players1['league_id'] = player_league['id']
greuther_furth_players1['age'] = df_p1['age']
greuther_furth_players1['birth'] = player_birth['date']
greuther_furth_players1['nationality'] = df_p1['nationality']
greuther_furth_players1['app'] = player_games['appearences']
greuther_furth_players1['mins'] = player_games['minutes']
greuther_furth_players1['goals'] = player_goals['total']
greuther_furth_players1['shots'] = player_shots['total']
greuther_furth_players1['shots_on_target'] = player_shots['on']
greuther_furth_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
greuther_furth_players1['assists'] = player_goals['assists']
greuther_furth_players1['passes'] = player_passes['total']
greuther_furth_players1['passes_completed'] = player_passes['accuracy']
# greuther_furth_players1['pass_accuracy_%'] = df_p1['name']
greuther_furth_players1['dribbles'] = player_dribbles['attempts']
greuther_furth_players1['dribbles_completed'] = player_dribbles['success']
greuther_furth_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
greuther_furth_players1['tackles'] = player_tackles['total']
greuther_furth_players1['blocks'] = player_tackles['blocks']
greuther_furth_players1['interceptions'] = player_tackles['interceptions']
greuther_furth_players1['fouls_drawn'] = player_fouls['drawn']
greuther_furth_players1['fouls_committed'] = player_fouls['committed']
greuther_furth_players1['yellow_cards'] = player_cards['yellow']
greuther_furth_players1['red_cards'] = player_cards['red']
greuther_furth_players1['yellow_to_red_cards'] = player_cards['yellowred']
greuther_furth_players1['sub_in'] = player_subs['in']
greuther_furth_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
greuther_furth_players1 = greuther_furth_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"178","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
greuther_furth_players2 = pd.DataFrame()

greuther_furth_players2['name'] = df_p1['name']
greuther_furth_players2['first_name'] = df_p1['firstname']
greuther_furth_players2['last_name'] = df_p1['lastname']
greuther_furth_players2['id'] = df_p1['id']
greuther_furth_players2['team'] = player_team['name']
greuther_furth_players2['team_id'] = player_team['id']
greuther_furth_players2['league'] = player_league['name']
greuther_furth_players2['league_id'] = player_league['id']
greuther_furth_players2['age'] = df_p1['age']
greuther_furth_players2['birth'] = player_birth['date']
greuther_furth_players2['nationality'] = df_p1['nationality']
greuther_furth_players2['app'] = player_games['appearences']
greuther_furth_players2['mins'] = player_games['minutes']
greuther_furth_players2['goals'] = player_goals['total']
greuther_furth_players2['shots'] = player_shots['total']
greuther_furth_players2['shots_on_target'] = player_shots['on']
greuther_furth_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
greuther_furth_players2['assists'] = player_goals['assists']
greuther_furth_players2['passes'] = player_passes['total']
greuther_furth_players2['passes_completed'] = player_passes['accuracy']
# greuther_furth_players2['pass_accuracy_%'] = df_p1['name']
greuther_furth_players2['dribbles'] = player_dribbles['attempts']
greuther_furth_players2['dribbles_completed'] = player_dribbles['success']
greuther_furth_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
greuther_furth_players2['tackles'] = player_tackles['total']
greuther_furth_players2['blocks'] = player_tackles['blocks']
greuther_furth_players2['interceptions'] = player_tackles['interceptions']
greuther_furth_players2['fouls_drawn'] = player_fouls['drawn']
greuther_furth_players2['fouls_committed'] = player_fouls['committed']
greuther_furth_players2['yellow_cards'] = player_cards['yellow']
greuther_furth_players2['red_cards'] = player_cards['red']
greuther_furth_players2['yellow_to_red_cards'] = player_cards['yellowred']
greuther_furth_players2['sub_in'] = player_subs['in']
greuther_furth_players2['sub_out'] = player_subs['out']

greuther_furth_players2 = greuther_furth_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
greuther_furth_players = pd.concat([greuther_furth_players1, greuther_furth_players2])
greuther_furth_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### UNION BERLIN ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"182","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
union_berlin_players1 = pd.DataFrame()

union_berlin_players1['name'] = df_p1['name']
union_berlin_players1['first_name'] = df_p1['firstname']
union_berlin_players1['last_name'] = df_p1['lastname']
union_berlin_players1['id'] = df_p1['id']
union_berlin_players1['team'] = player_team['name']
union_berlin_players1['team_id'] = player_team['id']
union_berlin_players1['league'] = player_league['name']
union_berlin_players1['league_id'] = player_league['id']
union_berlin_players1['age'] = df_p1['age']
union_berlin_players1['birth'] = player_birth['date']
union_berlin_players1['nationality'] = df_p1['nationality']
union_berlin_players1['app'] = player_games['appearences']
union_berlin_players1['mins'] = player_games['minutes']
union_berlin_players1['goals'] = player_goals['total']
union_berlin_players1['shots'] = player_shots['total']
union_berlin_players1['shots_on_target'] = player_shots['on']
union_berlin_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
union_berlin_players1['assists'] = player_goals['assists']
union_berlin_players1['passes'] = player_passes['total']
union_berlin_players1['passes_completed'] = player_passes['accuracy']
# union_berlin_players1['pass_accuracy_%'] = df_p1['name']
union_berlin_players1['dribbles'] = player_dribbles['attempts']
union_berlin_players1['dribbles_completed'] = player_dribbles['success']
union_berlin_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
union_berlin_players1['tackles'] = player_tackles['total']
union_berlin_players1['blocks'] = player_tackles['blocks']
union_berlin_players1['interceptions'] = player_tackles['interceptions']
union_berlin_players1['fouls_drawn'] = player_fouls['drawn']
union_berlin_players1['fouls_committed'] = player_fouls['committed']
union_berlin_players1['yellow_cards'] = player_cards['yellow']
union_berlin_players1['red_cards'] = player_cards['red']
union_berlin_players1['yellow_to_red_cards'] = player_cards['yellowred']
union_berlin_players1['sub_in'] = player_subs['in']
union_berlin_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
union_berlin_players1 = union_berlin_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"182","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
union_berlin_players2 = pd.DataFrame()

union_berlin_players2['name'] = df_p1['name']
union_berlin_players2['first_name'] = df_p1['firstname']
union_berlin_players2['last_name'] = df_p1['lastname']
union_berlin_players2['id'] = df_p1['id']
union_berlin_players2['team'] = player_team['name']
union_berlin_players2['team_id'] = player_team['id']
union_berlin_players2['league'] = player_league['name']
union_berlin_players2['league_id'] = player_league['id']
union_berlin_players2['age'] = df_p1['age']
union_berlin_players2['birth'] = player_birth['date']
union_berlin_players2['nationality'] = df_p1['nationality']
union_berlin_players2['app'] = player_games['appearences']
union_berlin_players2['mins'] = player_games['minutes']
union_berlin_players2['goals'] = player_goals['total']
union_berlin_players2['shots'] = player_shots['total']
union_berlin_players2['shots_on_target'] = player_shots['on']
union_berlin_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
union_berlin_players2['assists'] = player_goals['assists']
union_berlin_players2['passes'] = player_passes['total']
union_berlin_players2['passes_completed'] = player_passes['accuracy']
# union_berlin_players2['pass_accuracy_%'] = df_p1['name']
union_berlin_players2['dribbles'] = player_dribbles['attempts']
union_berlin_players2['dribbles_completed'] = player_dribbles['success']
union_berlin_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
union_berlin_players2['tackles'] = player_tackles['total']
union_berlin_players2['blocks'] = player_tackles['blocks']
union_berlin_players2['interceptions'] = player_tackles['interceptions']
union_berlin_players2['fouls_drawn'] = player_fouls['drawn']
union_berlin_players2['fouls_committed'] = player_fouls['committed']
union_berlin_players2['yellow_cards'] = player_cards['yellow']
union_berlin_players2['red_cards'] = player_cards['red']
union_berlin_players2['yellow_to_red_cards'] = player_cards['yellowred']
union_berlin_players2['sub_in'] = player_subs['in']
union_berlin_players2['sub_out'] = player_subs['out']

union_berlin_players2 = union_berlin_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
union_berlin_players = pd.concat([union_berlin_players1, union_berlin_players2])
union_berlin_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### VFB STUTTGART ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"172","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
stuttgart_players1 = pd.DataFrame()

stuttgart_players1['name'] = df_p1['name']
stuttgart_players1['first_name'] = df_p1['firstname']
stuttgart_players1['last_name'] = df_p1['lastname']
stuttgart_players1['id'] = df_p1['id']
stuttgart_players1['team'] = player_team['name']
stuttgart_players1['team_id'] = player_team['id']
stuttgart_players1['league'] = player_league['name']
stuttgart_players1['league_id'] = player_league['id']
stuttgart_players1['age'] = df_p1['age']
stuttgart_players1['birth'] = player_birth['date']
stuttgart_players1['nationality'] = df_p1['nationality']
stuttgart_players1['app'] = player_games['appearences']
stuttgart_players1['mins'] = player_games['minutes']
stuttgart_players1['goals'] = player_goals['total']
stuttgart_players1['shots'] = player_shots['total']
stuttgart_players1['shots_on_target'] = player_shots['on']
stuttgart_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
stuttgart_players1['assists'] = player_goals['assists']
stuttgart_players1['passes'] = player_passes['total']
stuttgart_players1['passes_completed'] = player_passes['accuracy']
# stuttgart_players1['pass_accuracy_%'] = df_p1['name']
stuttgart_players1['dribbles'] = player_dribbles['attempts']
stuttgart_players1['dribbles_completed'] = player_dribbles['success']
stuttgart_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
stuttgart_players1['tackles'] = player_tackles['total']
stuttgart_players1['blocks'] = player_tackles['blocks']
stuttgart_players1['interceptions'] = player_tackles['interceptions']
stuttgart_players1['fouls_drawn'] = player_fouls['drawn']
stuttgart_players1['fouls_committed'] = player_fouls['committed']
stuttgart_players1['yellow_cards'] = player_cards['yellow']
stuttgart_players1['red_cards'] = player_cards['red']
stuttgart_players1['yellow_to_red_cards'] = player_cards['yellowred']
stuttgart_players1['sub_in'] = player_subs['in']
stuttgart_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
stuttgart_players1 = stuttgart_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"172","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
stuttgart_players2 = pd.DataFrame()

stuttgart_players2['name'] = df_p1['name']
stuttgart_players2['first_name'] = df_p1['firstname']
stuttgart_players2['last_name'] = df_p1['lastname']
stuttgart_players2['id'] = df_p1['id']
stuttgart_players2['team'] = player_team['name']
stuttgart_players2['team_id'] = player_team['id']
stuttgart_players2['league'] = player_league['name']
stuttgart_players2['league_id'] = player_league['id']
stuttgart_players2['age'] = df_p1['age']
stuttgart_players2['birth'] = player_birth['date']
stuttgart_players2['nationality'] = df_p1['nationality']
stuttgart_players2['app'] = player_games['appearences']
stuttgart_players2['mins'] = player_games['minutes']
stuttgart_players2['goals'] = player_goals['total']
stuttgart_players2['shots'] = player_shots['total']
stuttgart_players2['shots_on_target'] = player_shots['on']
stuttgart_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
stuttgart_players2['assists'] = player_goals['assists']
stuttgart_players2['passes'] = player_passes['total']
stuttgart_players2['passes_completed'] = player_passes['accuracy']
# stuttgart_players2['pass_accuracy_%'] = df_p1['name']
stuttgart_players2['dribbles'] = player_dribbles['attempts']
stuttgart_players2['dribbles_completed'] = player_dribbles['success']
stuttgart_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
stuttgart_players2['tackles'] = player_tackles['total']
stuttgart_players2['blocks'] = player_tackles['blocks']
stuttgart_players2['interceptions'] = player_tackles['interceptions']
stuttgart_players2['fouls_drawn'] = player_fouls['drawn']
stuttgart_players2['fouls_committed'] = player_fouls['committed']
stuttgart_players2['yellow_cards'] = player_cards['yellow']
stuttgart_players2['red_cards'] = player_cards['red']
stuttgart_players2['yellow_to_red_cards'] = player_cards['yellowred']
stuttgart_players2['sub_in'] = player_subs['in']
stuttgart_players2['sub_out'] = player_subs['out']

stuttgart_players2 = stuttgart_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
stuttgart_players = pd.concat([stuttgart_players1, stuttgart_players2])
stuttgart_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column







####### VFL BOCHUM ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"176","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
vfl_bochum_players1 = pd.DataFrame()

vfl_bochum_players1['name'] = df_p1['name']
vfl_bochum_players1['first_name'] = df_p1['firstname']
vfl_bochum_players1['last_name'] = df_p1['lastname']
vfl_bochum_players1['id'] = df_p1['id']
vfl_bochum_players1['team'] = player_team['name']
vfl_bochum_players1['team_id'] = player_team['id']
vfl_bochum_players1['league'] = player_league['name']
vfl_bochum_players1['league_id'] = player_league['id']
vfl_bochum_players1['age'] = df_p1['age']
vfl_bochum_players1['birth'] = player_birth['date']
vfl_bochum_players1['nationality'] = df_p1['nationality']
vfl_bochum_players1['app'] = player_games['appearences']
vfl_bochum_players1['mins'] = player_games['minutes']
vfl_bochum_players1['goals'] = player_goals['total']
vfl_bochum_players1['shots'] = player_shots['total']
vfl_bochum_players1['shots_on_target'] = player_shots['on']
vfl_bochum_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
vfl_bochum_players1['assists'] = player_goals['assists']
vfl_bochum_players1['passes'] = player_passes['total']
vfl_bochum_players1['passes_completed'] = player_passes['accuracy']
# vfl_bochum_players1['pass_accuracy_%'] = df_p1['name']
vfl_bochum_players1['dribbles'] = player_dribbles['attempts']
vfl_bochum_players1['dribbles_completed'] = player_dribbles['success']
vfl_bochum_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
vfl_bochum_players1['tackles'] = player_tackles['total']
vfl_bochum_players1['blocks'] = player_tackles['blocks']
vfl_bochum_players1['interceptions'] = player_tackles['interceptions']
vfl_bochum_players1['fouls_drawn'] = player_fouls['drawn']
vfl_bochum_players1['fouls_committed'] = player_fouls['committed']
vfl_bochum_players1['yellow_cards'] = player_cards['yellow']
vfl_bochum_players1['red_cards'] = player_cards['red']
vfl_bochum_players1['yellow_to_red_cards'] = player_cards['yellowred']
vfl_bochum_players1['sub_in'] = player_subs['in']
vfl_bochum_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
vfl_bochum_players1 = vfl_bochum_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"176","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
vfl_bochum_players2 = pd.DataFrame()

vfl_bochum_players2['name'] = df_p1['name']
vfl_bochum_players2['first_name'] = df_p1['firstname']
vfl_bochum_players2['last_name'] = df_p1['lastname']
vfl_bochum_players2['id'] = df_p1['id']
vfl_bochum_players2['team'] = player_team['name']
vfl_bochum_players2['team_id'] = player_team['id']
vfl_bochum_players2['league'] = player_league['name']
vfl_bochum_players2['league_id'] = player_league['id']
vfl_bochum_players2['age'] = df_p1['age']
vfl_bochum_players2['birth'] = player_birth['date']
vfl_bochum_players2['nationality'] = df_p1['nationality']
vfl_bochum_players2['app'] = player_games['appearences']
vfl_bochum_players2['mins'] = player_games['minutes']
vfl_bochum_players2['goals'] = player_goals['total']
vfl_bochum_players2['shots'] = player_shots['total']
vfl_bochum_players2['shots_on_target'] = player_shots['on']
vfl_bochum_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
vfl_bochum_players2['assists'] = player_goals['assists']
vfl_bochum_players2['passes'] = player_passes['total']
vfl_bochum_players2['passes_completed'] = player_passes['accuracy']
# vfl_bochum_players2['pass_accuracy_%'] = df_p1['name']
vfl_bochum_players2['dribbles'] = player_dribbles['attempts']
vfl_bochum_players2['dribbles_completed'] = player_dribbles['success']
vfl_bochum_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
vfl_bochum_players2['tackles'] = player_tackles['total']
vfl_bochum_players2['blocks'] = player_tackles['blocks']
vfl_bochum_players2['interceptions'] = player_tackles['interceptions']
vfl_bochum_players2['fouls_drawn'] = player_fouls['drawn']
vfl_bochum_players2['fouls_committed'] = player_fouls['committed']
vfl_bochum_players2['yellow_cards'] = player_cards['yellow']
vfl_bochum_players2['red_cards'] = player_cards['red']
vfl_bochum_players2['yellow_to_red_cards'] = player_cards['yellowred']
vfl_bochum_players2['sub_in'] = player_subs['in']
vfl_bochum_players2['sub_out'] = player_subs['out']

vfl_bochum_players2 = vfl_bochum_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
vfl_bochum_players = pd.concat([vfl_bochum_players1, vfl_bochum_players2])
vfl_bochum_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### VFL WOLFSBURG ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"161","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1' , 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
wolfsburg_players1 = pd.DataFrame()

wolfsburg_players1['name'] = df_p1['name']
wolfsburg_players1['first_name'] = df_p1['firstname']
wolfsburg_players1['last_name'] = df_p1['lastname']
wolfsburg_players1['id'] = df_p1['id']
wolfsburg_players1['team'] = player_team['name']
wolfsburg_players1['team_id'] = player_team['id']
wolfsburg_players1['league'] = player_league['name']
wolfsburg_players1['league_id'] = player_league['id']
wolfsburg_players1['age'] = df_p1['age']
wolfsburg_players1['birth'] = player_birth['date']
wolfsburg_players1['nationality'] = df_p1['nationality']
wolfsburg_players1['app'] = player_games['appearences']
wolfsburg_players1['mins'] = player_games['minutes']
wolfsburg_players1['goals'] = player_goals['total']
wolfsburg_players1['shots'] = player_shots['total']
wolfsburg_players1['shots_on_target'] = player_shots['on']
wolfsburg_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
wolfsburg_players1['assists'] = player_goals['assists']
wolfsburg_players1['passes'] = player_passes['total']
wolfsburg_players1['passes_completed'] = player_passes['accuracy']
# wolfsburg_players1['pass_accuracy_%'] = df_p1['name']
wolfsburg_players1['dribbles'] = player_dribbles['attempts']
wolfsburg_players1['dribbles_completed'] = player_dribbles['success']
wolfsburg_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
wolfsburg_players1['tackles'] = player_tackles['total']
wolfsburg_players1['blocks'] = player_tackles['blocks']
wolfsburg_players1['interceptions'] = player_tackles['interceptions']
wolfsburg_players1['fouls_drawn'] = player_fouls['drawn']
wolfsburg_players1['fouls_committed'] = player_fouls['committed']
wolfsburg_players1['yellow_cards'] = player_cards['yellow']
wolfsburg_players1['red_cards'] = player_cards['red']
wolfsburg_players1['yellow_to_red_cards'] = player_cards['yellowred']
wolfsburg_players1['sub_in'] = player_subs['in']
wolfsburg_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
wolfsburg_players1 = wolfsburg_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"161","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
wolfsburg_players2 = pd.DataFrame()

wolfsburg_players2['name'] = df_p1['name']
wolfsburg_players2['first_name'] = df_p1['firstname']
wolfsburg_players2['last_name'] = df_p1['lastname']
wolfsburg_players2['id'] = df_p1['id']
wolfsburg_players2['team'] = player_team['name']
wolfsburg_players2['team_id'] = player_team['id']
wolfsburg_players2['league'] = player_league['name']
wolfsburg_players2['league_id'] = player_league['id']
wolfsburg_players2['age'] = df_p1['age']
wolfsburg_players2['birth'] = player_birth['date']
wolfsburg_players2['nationality'] = df_p1['nationality']
wolfsburg_players2['app'] = player_games['appearences']
wolfsburg_players2['mins'] = player_games['minutes']
wolfsburg_players2['goals'] = player_goals['total']
wolfsburg_players2['shots'] = player_shots['total']
wolfsburg_players2['shots_on_target'] = player_shots['on']
wolfsburg_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
wolfsburg_players2['assists'] = player_goals['assists']
wolfsburg_players2['passes'] = player_passes['total']
wolfsburg_players2['passes_completed'] = player_passes['accuracy']
# wolfsburg_players2['pass_accuracy_%'] = df_p1['name']
wolfsburg_players2['dribbles'] = player_dribbles['attempts']
wolfsburg_players2['dribbles_completed'] = player_dribbles['success']
wolfsburg_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
wolfsburg_players2['tackles'] = player_tackles['total']
wolfsburg_players2['blocks'] = player_tackles['blocks']
wolfsburg_players2['interceptions'] = player_tackles['interceptions']
wolfsburg_players2['fouls_drawn'] = player_fouls['drawn']
wolfsburg_players2['fouls_committed'] = player_fouls['committed']
wolfsburg_players2['yellow_cards'] = player_cards['yellow']
wolfsburg_players2['red_cards'] = player_cards['red']
wolfsburg_players2['yellow_to_red_cards'] = player_cards['yellowred']
wolfsburg_players2['sub_in'] = player_subs['in']
wolfsburg_players2['sub_out'] = player_subs['out']

wolfsburg_players2 = wolfsburg_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
wolfsburg_players = pd.concat([wolfsburg_players1, wolfsburg_players2])
wolfsburg_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




# Combine players from all teams in the league into a single data frame
bundesliga_players = pd.concat([hoffenheim_players,
						bielefeld_players,
						leverkusen_players,
						bayern_munich_players,
						dortmund_players,
						monchengladbach_players,
						frankfurt_players,
						augsburg_players,
						koln_players,
						mainz_players,
						hertha_berlin_players,
						leipzig_players,
						freiburg_players,
						greuther_furth_players,
						union_berlin_players,
						stuttgart_players,
						vfl_bochum_players,
						wolfsburg_players
						], ignore_index = True)




####################################### 3. LA LIGA ##############################################


####### ALAVES ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"542","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
alaves_players1 = pd.DataFrame()

alaves_players1['name'] = df_p1['name']
alaves_players1['first_name'] = df_p1['firstname']
alaves_players1['last_name'] = df_p1['lastname']
alaves_players1['id'] = df_p1['id']
alaves_players1['team'] = player_team['name']
alaves_players1['team_id'] = player_team['id']
alaves_players1['league'] = player_league['name']
alaves_players1['league_id'] = player_league['id']
alaves_players1['age'] = df_p1['age']
alaves_players1['birth'] = player_birth['date']
alaves_players1['nationality'] = df_p1['nationality']
alaves_players1['app'] = player_games['appearences']
alaves_players1['mins'] = player_games['minutes']
alaves_players1['goals'] = player_goals['total']
alaves_players1['shots'] = player_shots['total']
alaves_players1['shots_on_target'] = player_shots['on']
alaves_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
alaves_players1['assists'] = player_goals['assists']
alaves_players1['passes'] = player_passes['total']
alaves_players1['passes_completed'] = player_passes['accuracy']
# alaves_players1['pass_accuracy_%'] = df_p1['name']
alaves_players1['dribbles'] = player_dribbles['attempts']
alaves_players1['dribbles_completed'] = player_dribbles['success']
alaves_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
alaves_players1['tackles'] = player_tackles['total']
alaves_players1['blocks'] = player_tackles['blocks']
alaves_players1['interceptions'] = player_tackles['interceptions']
alaves_players1['fouls_drawn'] = player_fouls['drawn']
alaves_players1['fouls_committed'] = player_fouls['committed']
alaves_players1['yellow_cards'] = player_cards['yellow']
alaves_players1['red_cards'] = player_cards['red']
alaves_players1['yellow_to_red_cards'] = player_cards['yellowred']
alaves_players1['sub_in'] = player_subs['in']
alaves_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
alaves_players1 = alaves_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"542","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
alaves_players2 = pd.DataFrame()

alaves_players2['name'] = df_p1['name']
alaves_players2['first_name'] = df_p1['firstname']
alaves_players2['last_name'] = df_p1['lastname']
alaves_players2['id'] = df_p1['id']
alaves_players2['team'] = player_team['name']
alaves_players2['team_id'] = player_team['id']
alaves_players2['league'] = player_league['name']
alaves_players2['league_id'] = player_league['id']
alaves_players2['age'] = df_p1['age']
alaves_players2['birth'] = player_birth['date']
alaves_players2['nationality'] = df_p1['nationality']
alaves_players2['app'] = player_games['appearences']
alaves_players2['mins'] = player_games['minutes']
alaves_players2['goals'] = player_goals['total']
alaves_players2['shots'] = player_shots['total']
alaves_players2['shots_on_target'] = player_shots['on']
alaves_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
alaves_players2['assists'] = player_goals['assists']
alaves_players2['passes'] = player_passes['total']
alaves_players2['passes_completed'] = player_passes['accuracy']
# alaves_players2['pass_accuracy_%'] = df_p1['name']
alaves_players2['dribbles'] = player_dribbles['attempts']
alaves_players2['dribbles_completed'] = player_dribbles['success']
alaves_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
alaves_players2['tackles'] = player_tackles['total']
alaves_players2['blocks'] = player_tackles['blocks']
alaves_players2['interceptions'] = player_tackles['interceptions']
alaves_players2['fouls_drawn'] = player_fouls['drawn']
alaves_players2['fouls_committed'] = player_fouls['committed']
alaves_players2['yellow_cards'] = player_cards['yellow']
alaves_players2['red_cards'] = player_cards['red']
alaves_players2['yellow_to_red_cards'] = player_cards['yellowred']
alaves_players2['sub_in'] = player_subs['in']
alaves_players2['sub_out'] = player_subs['out']

alaves_players2 = alaves_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
alaves_players = pd.concat([alaves_players1, alaves_players2])
alaves_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### ATHLETIC CLUB ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"531","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
athletic_club_players1 = pd.DataFrame()

athletic_club_players1['name'] = df_p1['name']
athletic_club_players1['first_name'] = df_p1['firstname']
athletic_club_players1['last_name'] = df_p1['lastname']
athletic_club_players1['id'] = df_p1['id']
athletic_club_players1['team'] = player_team['name']
athletic_club_players1['team_id'] = player_team['id']
athletic_club_players1['league'] = player_league['name']
athletic_club_players1['league_id'] = player_league['id']
athletic_club_players1['age'] = df_p1['age']
athletic_club_players1['birth'] = player_birth['date']
athletic_club_players1['nationality'] = df_p1['nationality']
athletic_club_players1['app'] = player_games['appearences']
athletic_club_players1['mins'] = player_games['minutes']
athletic_club_players1['goals'] = player_goals['total']
athletic_club_players1['shots'] = player_shots['total']
athletic_club_players1['shots_on_target'] = player_shots['on']
athletic_club_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
athletic_club_players1['assists'] = player_goals['assists']
athletic_club_players1['passes'] = player_passes['total']
athletic_club_players1['passes_completed'] = player_passes['accuracy']
# athletic_club_players1['pass_accuracy_%'] = df_p1['name']
athletic_club_players1['dribbles'] = player_dribbles['attempts']
athletic_club_players1['dribbles_completed'] = player_dribbles['success']
athletic_club_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
athletic_club_players1['tackles'] = player_tackles['total']
athletic_club_players1['blocks'] = player_tackles['blocks']
athletic_club_players1['interceptions'] = player_tackles['interceptions']
athletic_club_players1['fouls_drawn'] = player_fouls['drawn']
athletic_club_players1['fouls_committed'] = player_fouls['committed']
athletic_club_players1['yellow_cards'] = player_cards['yellow']
athletic_club_players1['red_cards'] = player_cards['red']
athletic_club_players1['yellow_to_red_cards'] = player_cards['yellowred']
athletic_club_players1['sub_in'] = player_subs['in']
athletic_club_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
athletic_club_players1 = athletic_club_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"531","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
athletic_club_players2 = pd.DataFrame()

athletic_club_players2['name'] = df_p1['name']
athletic_club_players2['first_name'] = df_p1['firstname']
athletic_club_players2['last_name'] = df_p1['lastname']
athletic_club_players2['id'] = df_p1['id']
athletic_club_players2['team'] = player_team['name']
athletic_club_players2['team_id'] = player_team['id']
athletic_club_players2['league'] = player_league['name']
athletic_club_players2['league_id'] = player_league['id']
athletic_club_players2['age'] = df_p1['age']
athletic_club_players2['birth'] = player_birth['date']
athletic_club_players2['nationality'] = df_p1['nationality']
athletic_club_players2['app'] = player_games['appearences']
athletic_club_players2['mins'] = player_games['minutes']
athletic_club_players2['goals'] = player_goals['total']
athletic_club_players2['shots'] = player_shots['total']
athletic_club_players2['shots_on_target'] = player_shots['on']
athletic_club_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
athletic_club_players2['assists'] = player_goals['assists']
athletic_club_players2['passes'] = player_passes['total']
athletic_club_players2['passes_completed'] = player_passes['accuracy']
# athletic_club_players2['pass_accuracy_%'] = df_p1['name']
athletic_club_players2['dribbles'] = player_dribbles['attempts']
athletic_club_players2['dribbles_completed'] = player_dribbles['success']
athletic_club_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
athletic_club_players2['tackles'] = player_tackles['total']
athletic_club_players2['blocks'] = player_tackles['blocks']
athletic_club_players2['interceptions'] = player_tackles['interceptions']
athletic_club_players2['fouls_drawn'] = player_fouls['drawn']
athletic_club_players2['fouls_committed'] = player_fouls['committed']
athletic_club_players2['yellow_cards'] = player_cards['yellow']
athletic_club_players2['red_cards'] = player_cards['red']
athletic_club_players2['yellow_to_red_cards'] = player_cards['yellowred']
athletic_club_players2['sub_in'] = player_subs['in']
athletic_club_players2['sub_out'] = player_subs['out']

athletic_club_players2 = athletic_club_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
athletic_club_players = pd.concat([athletic_club_players1, athletic_club_players2])
athletic_club_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column









####### ATHLETICO MADRID ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"530","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
athletico_madrid_players1 = pd.DataFrame()

athletico_madrid_players1['name'] = df_p1['name']
athletico_madrid_players1['first_name'] = df_p1['firstname']
athletico_madrid_players1['last_name'] = df_p1['lastname']
athletico_madrid_players1['id'] = df_p1['id']
athletico_madrid_players1['team'] = player_team['name']
athletico_madrid_players1['team_id'] = player_team['id']
athletico_madrid_players1['league'] = player_league['name']
athletico_madrid_players1['league_id'] = player_league['id']
athletico_madrid_players1['age'] = df_p1['age']
athletico_madrid_players1['birth'] = player_birth['date']
athletico_madrid_players1['nationality'] = df_p1['nationality']
athletico_madrid_players1['app'] = player_games['appearences']
athletico_madrid_players1['mins'] = player_games['minutes']
athletico_madrid_players1['goals'] = player_goals['total']
athletico_madrid_players1['shots'] = player_shots['total']
athletico_madrid_players1['shots_on_target'] = player_shots['on']
athletico_madrid_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
athletico_madrid_players1['assists'] = player_goals['assists']
athletico_madrid_players1['passes'] = player_passes['total']
athletico_madrid_players1['passes_completed'] = player_passes['accuracy']
# athletico_madrid_players1['pass_accuracy_%'] = df_p1['name']
athletico_madrid_players1['dribbles'] = player_dribbles['attempts']
athletico_madrid_players1['dribbles_completed'] = player_dribbles['success']
athletico_madrid_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
athletico_madrid_players1['tackles'] = player_tackles['total']
athletico_madrid_players1['blocks'] = player_tackles['blocks']
athletico_madrid_players1['interceptions'] = player_tackles['interceptions']
athletico_madrid_players1['fouls_drawn'] = player_fouls['drawn']
athletico_madrid_players1['fouls_committed'] = player_fouls['committed']
athletico_madrid_players1['yellow_cards'] = player_cards['yellow']
athletico_madrid_players1['red_cards'] = player_cards['red']
athletico_madrid_players1['yellow_to_red_cards'] = player_cards['yellowred']
athletico_madrid_players1['sub_in'] = player_subs['in']
athletico_madrid_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
athletico_madrid_players1 = athletico_madrid_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"530","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
athletico_madrid_players2 = pd.DataFrame()

athletico_madrid_players2['name'] = df_p1['name']
athletico_madrid_players2['first_name'] = df_p1['firstname']
athletico_madrid_players2['last_name'] = df_p1['lastname']
athletico_madrid_players2['id'] = df_p1['id']
athletico_madrid_players2['team'] = player_team['name']
athletico_madrid_players2['team_id'] = player_team['id']
athletico_madrid_players2['league'] = player_league['name']
athletico_madrid_players2['league_id'] = player_league['id']
athletico_madrid_players2['age'] = df_p1['age']
athletico_madrid_players2['birth'] = player_birth['date']
athletico_madrid_players2['nationality'] = df_p1['nationality']
athletico_madrid_players2['app'] = player_games['appearences']
athletico_madrid_players2['mins'] = player_games['minutes']
athletico_madrid_players2['goals'] = player_goals['total']
athletico_madrid_players2['shots'] = player_shots['total']
athletico_madrid_players2['shots_on_target'] = player_shots['on']
athletico_madrid_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
athletico_madrid_players2['assists'] = player_goals['assists']
athletico_madrid_players2['passes'] = player_passes['total']
athletico_madrid_players2['passes_completed'] = player_passes['accuracy']
# athletico_madrid_players2['pass_accuracy_%'] = df_p1['name']
athletico_madrid_players2['dribbles'] = player_dribbles['attempts']
athletico_madrid_players2['dribbles_completed'] = player_dribbles['success']
athletico_madrid_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
athletico_madrid_players2['tackles'] = player_tackles['total']
athletico_madrid_players2['blocks'] = player_tackles['blocks']
athletico_madrid_players2['interceptions'] = player_tackles['interceptions']
athletico_madrid_players2['fouls_drawn'] = player_fouls['drawn']
athletico_madrid_players2['fouls_committed'] = player_fouls['committed']
athletico_madrid_players2['yellow_cards'] = player_cards['yellow']
athletico_madrid_players2['red_cards'] = player_cards['red']
athletico_madrid_players2['yellow_to_red_cards'] = player_cards['yellowred']
athletico_madrid_players2['sub_in'] = player_subs['in']
athletico_madrid_players2['sub_out'] = player_subs['out']

athletico_madrid_players2 = athletico_madrid_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
athletico_madrid_players = pd.concat([athletico_madrid_players1, athletico_madrid_players2])
athletico_madrid_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### BARCELONA ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"529","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
barcelona_players1 = pd.DataFrame()

barcelona_players1['name'] = df_p1['name']
barcelona_players1['first_name'] = df_p1['firstname']
barcelona_players1['last_name'] = df_p1['lastname']
barcelona_players1['id'] = df_p1['id']
barcelona_players1['team'] = player_team['name']
barcelona_players1['team_id'] = player_team['id']
barcelona_players1['league'] = player_league['name']
barcelona_players1['league_id'] = player_league['id']
barcelona_players1['age'] = df_p1['age']
barcelona_players1['birth'] = player_birth['date']
barcelona_players1['nationality'] = df_p1['nationality']
barcelona_players1['app'] = player_games['appearences']
barcelona_players1['mins'] = player_games['minutes']
barcelona_players1['goals'] = player_goals['total']
barcelona_players1['shots'] = player_shots['total']
barcelona_players1['shots_on_target'] = player_shots['on']
barcelona_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
barcelona_players1['assists'] = player_goals['assists']
barcelona_players1['passes'] = player_passes['total']
barcelona_players1['passes_completed'] = player_passes['accuracy']
# barcelona_players1['pass_accuracy_%'] = df_p1['name']
barcelona_players1['dribbles'] = player_dribbles['attempts']
barcelona_players1['dribbles_completed'] = player_dribbles['success']
barcelona_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
barcelona_players1['tackles'] = player_tackles['total']
barcelona_players1['blocks'] = player_tackles['blocks']
barcelona_players1['interceptions'] = player_tackles['interceptions']
barcelona_players1['fouls_drawn'] = player_fouls['drawn']
barcelona_players1['fouls_committed'] = player_fouls['committed']
barcelona_players1['yellow_cards'] = player_cards['yellow']
barcelona_players1['red_cards'] = player_cards['red']
barcelona_players1['yellow_to_red_cards'] = player_cards['yellowred']
barcelona_players1['sub_in'] = player_subs['in']
barcelona_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
barcelona_players1 = barcelona_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"529","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
barcelona_players2 = pd.DataFrame()

barcelona_players2['name'] = df_p1['name']
barcelona_players2['first_name'] = df_p1['firstname']
barcelona_players2['last_name'] = df_p1['lastname']
barcelona_players2['id'] = df_p1['id']
barcelona_players2['team'] = player_team['name']
barcelona_players2['team_id'] = player_team['id']
barcelona_players2['league'] = player_league['name']
barcelona_players2['league_id'] = player_league['id']
barcelona_players2['age'] = df_p1['age']
barcelona_players2['birth'] = player_birth['date']
barcelona_players2['nationality'] = df_p1['nationality']
barcelona_players2['app'] = player_games['appearences']
barcelona_players2['mins'] = player_games['minutes']
barcelona_players2['goals'] = player_goals['total']
barcelona_players2['shots'] = player_shots['total']
barcelona_players2['shots_on_target'] = player_shots['on']
barcelona_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
barcelona_players2['assists'] = player_goals['assists']
barcelona_players2['passes'] = player_passes['total']
barcelona_players2['passes_completed'] = player_passes['accuracy']
# barcelona_players2['pass_accuracy_%'] = df_p1['name']
barcelona_players2['dribbles'] = player_dribbles['attempts']
barcelona_players2['dribbles_completed'] = player_dribbles['success']
barcelona_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
barcelona_players2['tackles'] = player_tackles['total']
barcelona_players2['blocks'] = player_tackles['blocks']
barcelona_players2['interceptions'] = player_tackles['interceptions']
barcelona_players2['fouls_drawn'] = player_fouls['drawn']
barcelona_players2['fouls_committed'] = player_fouls['committed']
barcelona_players2['yellow_cards'] = player_cards['yellow']
barcelona_players2['red_cards'] = player_cards['red']
barcelona_players2['yellow_to_red_cards'] = player_cards['yellowred']
barcelona_players2['sub_in'] = player_subs['in']
barcelona_players2['sub_out'] = player_subs['out']

barcelona_players2 = barcelona_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
barcelona_players = pd.concat([barcelona_players1, barcelona_players2])
barcelona_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column







####### CADIZ ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"724","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
cadiz_players1 = pd.DataFrame()

cadiz_players1['name'] = df_p1['name']
cadiz_players1['first_name'] = df_p1['firstname']
cadiz_players1['last_name'] = df_p1['lastname']
cadiz_players1['id'] = df_p1['id']
cadiz_players1['team'] = player_team['name']
cadiz_players1['team_id'] = player_team['id']
cadiz_players1['league'] = player_league['name']
cadiz_players1['league_id'] = player_league['id']
cadiz_players1['age'] = df_p1['age']
cadiz_players1['birth'] = player_birth['date']
cadiz_players1['nationality'] = df_p1['nationality']
cadiz_players1['app'] = player_games['appearences']
cadiz_players1['mins'] = player_games['minutes']
cadiz_players1['goals'] = player_goals['total']
cadiz_players1['shots'] = player_shots['total']
cadiz_players1['shots_on_target'] = player_shots['on']
cadiz_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
cadiz_players1['assists'] = player_goals['assists']
cadiz_players1['passes'] = player_passes['total']
cadiz_players1['passes_completed'] = player_passes['accuracy']
# cadiz_players1['pass_accuracy_%'] = df_p1['name']
cadiz_players1['dribbles'] = player_dribbles['attempts']
cadiz_players1['dribbles_completed'] = player_dribbles['success']
cadiz_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
cadiz_players1['tackles'] = player_tackles['total']
cadiz_players1['blocks'] = player_tackles['blocks']
cadiz_players1['interceptions'] = player_tackles['interceptions']
cadiz_players1['fouls_drawn'] = player_fouls['drawn']
cadiz_players1['fouls_committed'] = player_fouls['committed']
cadiz_players1['yellow_cards'] = player_cards['yellow']
cadiz_players1['red_cards'] = player_cards['red']
cadiz_players1['yellow_to_red_cards'] = player_cards['yellowred']
cadiz_players1['sub_in'] = player_subs['in']
cadiz_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
cadiz_players1 = cadiz_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"724","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
cadiz_players2 = pd.DataFrame()

cadiz_players2['name'] = df_p1['name']
cadiz_players2['first_name'] = df_p1['firstname']
cadiz_players2['last_name'] = df_p1['lastname']
cadiz_players2['id'] = df_p1['id']
cadiz_players2['team'] = player_team['name']
cadiz_players2['team_id'] = player_team['id']
cadiz_players2['league'] = player_league['name']
cadiz_players2['league_id'] = player_league['id']
cadiz_players2['age'] = df_p1['age']
cadiz_players2['birth'] = player_birth['date']
cadiz_players2['nationality'] = df_p1['nationality']
cadiz_players2['app'] = player_games['appearences']
cadiz_players2['mins'] = player_games['minutes']
cadiz_players2['goals'] = player_goals['total']
cadiz_players2['shots'] = player_shots['total']
cadiz_players2['shots_on_target'] = player_shots['on']
cadiz_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
cadiz_players2['assists'] = player_goals['assists']
cadiz_players2['passes'] = player_passes['total']
cadiz_players2['passes_completed'] = player_passes['accuracy']
# cadiz_players2['pass_accuracy_%'] = df_p1['name']
cadiz_players2['dribbles'] = player_dribbles['attempts']
cadiz_players2['dribbles_completed'] = player_dribbles['success']
cadiz_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
cadiz_players2['tackles'] = player_tackles['total']
cadiz_players2['blocks'] = player_tackles['blocks']
cadiz_players2['interceptions'] = player_tackles['interceptions']
cadiz_players2['fouls_drawn'] = player_fouls['drawn']
cadiz_players2['fouls_committed'] = player_fouls['committed']
cadiz_players2['yellow_cards'] = player_cards['yellow']
cadiz_players2['red_cards'] = player_cards['red']
cadiz_players2['yellow_to_red_cards'] = player_cards['yellowred']
cadiz_players2['sub_in'] = player_subs['in']
cadiz_players2['sub_out'] = player_subs['out']

cadiz_players2 = cadiz_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
cadiz_players = pd.concat([cadiz_players1, cadiz_players2])
cadiz_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### CELTA VIGO ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"538","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
celta_vigo_players1 = pd.DataFrame()

celta_vigo_players1['name'] = df_p1['name']
celta_vigo_players1['first_name'] = df_p1['firstname']
celta_vigo_players1['last_name'] = df_p1['lastname']
celta_vigo_players1['id'] = df_p1['id']
celta_vigo_players1['team'] = player_team['name']
celta_vigo_players1['team_id'] = player_team['id']
celta_vigo_players1['league'] = player_league['name']
celta_vigo_players1['league_id'] = player_league['id']
celta_vigo_players1['age'] = df_p1['age']
celta_vigo_players1['birth'] = player_birth['date']
celta_vigo_players1['nationality'] = df_p1['nationality']
celta_vigo_players1['app'] = player_games['appearences']
celta_vigo_players1['mins'] = player_games['minutes']
celta_vigo_players1['goals'] = player_goals['total']
celta_vigo_players1['shots'] = player_shots['total']
celta_vigo_players1['shots_on_target'] = player_shots['on']
celta_vigo_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
celta_vigo_players1['assists'] = player_goals['assists']
celta_vigo_players1['passes'] = player_passes['total']
celta_vigo_players1['passes_completed'] = player_passes['accuracy']
# celta_vigo_players1['pass_accuracy_%'] = df_p1['name']
celta_vigo_players1['dribbles'] = player_dribbles['attempts']
celta_vigo_players1['dribbles_completed'] = player_dribbles['success']
celta_vigo_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
celta_vigo_players1['tackles'] = player_tackles['total']
celta_vigo_players1['blocks'] = player_tackles['blocks']
celta_vigo_players1['interceptions'] = player_tackles['interceptions']
celta_vigo_players1['fouls_drawn'] = player_fouls['drawn']
celta_vigo_players1['fouls_committed'] = player_fouls['committed']
celta_vigo_players1['yellow_cards'] = player_cards['yellow']
celta_vigo_players1['red_cards'] = player_cards['red']
celta_vigo_players1['yellow_to_red_cards'] = player_cards['yellowred']
celta_vigo_players1['sub_in'] = player_subs['in']
celta_vigo_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
celta_vigo_players1 = celta_vigo_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"538","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
celta_vigo_players2 = pd.DataFrame()

celta_vigo_players2['name'] = df_p1['name']
celta_vigo_players2['first_name'] = df_p1['firstname']
celta_vigo_players2['last_name'] = df_p1['lastname']
celta_vigo_players2['id'] = df_p1['id']
celta_vigo_players2['team'] = player_team['name']
celta_vigo_players2['team_id'] = player_team['id']
celta_vigo_players2['league'] = player_league['name']
celta_vigo_players2['league_id'] = player_league['id']
celta_vigo_players2['age'] = df_p1['age']
celta_vigo_players2['birth'] = player_birth['date']
celta_vigo_players2['nationality'] = df_p1['nationality']
celta_vigo_players2['app'] = player_games['appearences']
celta_vigo_players2['mins'] = player_games['minutes']
celta_vigo_players2['goals'] = player_goals['total']
celta_vigo_players2['shots'] = player_shots['total']
celta_vigo_players2['shots_on_target'] = player_shots['on']
celta_vigo_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
celta_vigo_players2['assists'] = player_goals['assists']
celta_vigo_players2['passes'] = player_passes['total']
celta_vigo_players2['passes_completed'] = player_passes['accuracy']
# celta_vigo_players2['pass_accuracy_%'] = df_p1['name']
celta_vigo_players2['dribbles'] = player_dribbles['attempts']
celta_vigo_players2['dribbles_completed'] = player_dribbles['success']
celta_vigo_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
celta_vigo_players2['tackles'] = player_tackles['total']
celta_vigo_players2['blocks'] = player_tackles['blocks']
celta_vigo_players2['interceptions'] = player_tackles['interceptions']
celta_vigo_players2['fouls_drawn'] = player_fouls['drawn']
celta_vigo_players2['fouls_committed'] = player_fouls['committed']
celta_vigo_players2['yellow_cards'] = player_cards['yellow']
celta_vigo_players2['red_cards'] = player_cards['red']
celta_vigo_players2['yellow_to_red_cards'] = player_cards['yellowred']
celta_vigo_players2['sub_in'] = player_subs['in']
celta_vigo_players2['sub_out'] = player_subs['out']

celta_vigo_players2 = celta_vigo_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
celta_vigo_players = pd.concat([celta_vigo_players1, celta_vigo_players2])
celta_vigo_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column










####### ELCHE ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"797","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
elche_players1 = pd.DataFrame()

elche_players1['name'] = df_p1['name']
elche_players1['first_name'] = df_p1['firstname']
elche_players1['last_name'] = df_p1['lastname']
elche_players1['id'] = df_p1['id']
elche_players1['team'] = player_team['name']
elche_players1['team_id'] = player_team['id']
elche_players1['league'] = player_league['name']
elche_players1['league_id'] = player_league['id']
elche_players1['age'] = df_p1['age']
elche_players1['birth'] = player_birth['date']
elche_players1['nationality'] = df_p1['nationality']
elche_players1['app'] = player_games['appearences']
elche_players1['mins'] = player_games['minutes']
elche_players1['goals'] = player_goals['total']
elche_players1['shots'] = player_shots['total']
elche_players1['shots_on_target'] = player_shots['on']
elche_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
elche_players1['assists'] = player_goals['assists']
elche_players1['passes'] = player_passes['total']
elche_players1['passes_completed'] = player_passes['accuracy']
# elche_players1['pass_accuracy_%'] = df_p1['name']
elche_players1['dribbles'] = player_dribbles['attempts']
elche_players1['dribbles_completed'] = player_dribbles['success']
elche_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
elche_players1['tackles'] = player_tackles['total']
elche_players1['blocks'] = player_tackles['blocks']
elche_players1['interceptions'] = player_tackles['interceptions']
elche_players1['fouls_drawn'] = player_fouls['drawn']
elche_players1['fouls_committed'] = player_fouls['committed']
elche_players1['yellow_cards'] = player_cards['yellow']
elche_players1['red_cards'] = player_cards['red']
elche_players1['yellow_to_red_cards'] = player_cards['yellowred']
elche_players1['sub_in'] = player_subs['in']
elche_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
elche_players1 = elche_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"797","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
elche_players2 = pd.DataFrame()

elche_players2['name'] = df_p1['name']
elche_players2['first_name'] = df_p1['firstname']
elche_players2['last_name'] = df_p1['lastname']
elche_players2['id'] = df_p1['id']
elche_players2['team'] = player_team['name']
elche_players2['team_id'] = player_team['id']
elche_players2['league'] = player_league['name']
elche_players2['league_id'] = player_league['id']
elche_players2['age'] = df_p1['age']
elche_players2['birth'] = player_birth['date']
elche_players2['nationality'] = df_p1['nationality']
elche_players2['app'] = player_games['appearences']
elche_players2['mins'] = player_games['minutes']
elche_players2['goals'] = player_goals['total']
elche_players2['shots'] = player_shots['total']
elche_players2['shots_on_target'] = player_shots['on']
elche_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
elche_players2['assists'] = player_goals['assists']
elche_players2['passes'] = player_passes['total']
elche_players2['passes_completed'] = player_passes['accuracy']
# elche_players2['pass_accuracy_%'] = df_p1['name']
elche_players2['dribbles'] = player_dribbles['attempts']
elche_players2['dribbles_completed'] = player_dribbles['success']
elche_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
elche_players2['tackles'] = player_tackles['total']
elche_players2['blocks'] = player_tackles['blocks']
elche_players2['interceptions'] = player_tackles['interceptions']
elche_players2['fouls_drawn'] = player_fouls['drawn']
elche_players2['fouls_committed'] = player_fouls['committed']
elche_players2['yellow_cards'] = player_cards['yellow']
elche_players2['red_cards'] = player_cards['red']
elche_players2['yellow_to_red_cards'] = player_cards['yellowred']
elche_players2['sub_in'] = player_subs['in']
elche_players2['sub_out'] = player_subs['out']

elche_players2 = elche_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
elche_players = pd.concat([elche_players1, elche_players2])
elche_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### ESPANYOL ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"540","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
espanyol_players1 = pd.DataFrame()

espanyol_players1['name'] = df_p1['name']
espanyol_players1['first_name'] = df_p1['firstname']
espanyol_players1['last_name'] = df_p1['lastname']
espanyol_players1['id'] = df_p1['id']
espanyol_players1['team'] = player_team['name']
espanyol_players1['team_id'] = player_team['id']
espanyol_players1['league'] = player_league['name']
espanyol_players1['league_id'] = player_league['id']
espanyol_players1['age'] = df_p1['age']
espanyol_players1['birth'] = player_birth['date']
espanyol_players1['nationality'] = df_p1['nationality']
espanyol_players1['app'] = player_games['appearences']
espanyol_players1['mins'] = player_games['minutes']
espanyol_players1['goals'] = player_goals['total']
espanyol_players1['shots'] = player_shots['total']
espanyol_players1['shots_on_target'] = player_shots['on']
espanyol_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
espanyol_players1['assists'] = player_goals['assists']
espanyol_players1['passes'] = player_passes['total']
espanyol_players1['passes_completed'] = player_passes['accuracy']
# espanyol_players1['pass_accuracy_%'] = df_p1['name']
espanyol_players1['dribbles'] = player_dribbles['attempts']
espanyol_players1['dribbles_completed'] = player_dribbles['success']
espanyol_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
espanyol_players1['tackles'] = player_tackles['total']
espanyol_players1['blocks'] = player_tackles['blocks']
espanyol_players1['interceptions'] = player_tackles['interceptions']
espanyol_players1['fouls_drawn'] = player_fouls['drawn']
espanyol_players1['fouls_committed'] = player_fouls['committed']
espanyol_players1['yellow_cards'] = player_cards['yellow']
espanyol_players1['red_cards'] = player_cards['red']
espanyol_players1['yellow_to_red_cards'] = player_cards['yellowred']
espanyol_players1['sub_in'] = player_subs['in']
espanyol_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
espanyol_players1 = espanyol_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"540","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
espanyol_players2 = pd.DataFrame()

espanyol_players2['name'] = df_p1['name']
espanyol_players2['first_name'] = df_p1['firstname']
espanyol_players2['last_name'] = df_p1['lastname']
espanyol_players2['id'] = df_p1['id']
espanyol_players2['team'] = player_team['name']
espanyol_players2['team_id'] = player_team['id']
espanyol_players2['league'] = player_league['name']
espanyol_players2['league_id'] = player_league['id']
espanyol_players2['age'] = df_p1['age']
espanyol_players2['birth'] = player_birth['date']
espanyol_players2['nationality'] = df_p1['nationality']
espanyol_players2['app'] = player_games['appearences']
espanyol_players2['mins'] = player_games['minutes']
espanyol_players2['goals'] = player_goals['total']
espanyol_players2['shots'] = player_shots['total']
espanyol_players2['shots_on_target'] = player_shots['on']
espanyol_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
espanyol_players2['assists'] = player_goals['assists']
espanyol_players2['passes'] = player_passes['total']
espanyol_players2['passes_completed'] = player_passes['accuracy']
# espanyol_players2['pass_accuracy_%'] = df_p1['name']
espanyol_players2['dribbles'] = player_dribbles['attempts']
espanyol_players2['dribbles_completed'] = player_dribbles['success']
espanyol_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
espanyol_players2['tackles'] = player_tackles['total']
espanyol_players2['blocks'] = player_tackles['blocks']
espanyol_players2['interceptions'] = player_tackles['interceptions']
espanyol_players2['fouls_drawn'] = player_fouls['drawn']
espanyol_players2['fouls_committed'] = player_fouls['committed']
espanyol_players2['yellow_cards'] = player_cards['yellow']
espanyol_players2['red_cards'] = player_cards['red']
espanyol_players2['yellow_to_red_cards'] = player_cards['yellowred']
espanyol_players2['sub_in'] = player_subs['in']
espanyol_players2['sub_out'] = player_subs['out']

espanyol_players2 = espanyol_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
espanyol_players = pd.concat([espanyol_players1, espanyol_players2])
espanyol_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### GETAFE ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"546","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
getafe_players1 = pd.DataFrame()

getafe_players1['name'] = df_p1['name']
getafe_players1['first_name'] = df_p1['firstname']
getafe_players1['last_name'] = df_p1['lastname']
getafe_players1['id'] = df_p1['id']
getafe_players1['team'] = player_team['name']
getafe_players1['team_id'] = player_team['id']
getafe_players1['league'] = player_league['name']
getafe_players1['league_id'] = player_league['id']
getafe_players1['age'] = df_p1['age']
getafe_players1['birth'] = player_birth['date']
getafe_players1['nationality'] = df_p1['nationality']
getafe_players1['app'] = player_games['appearences']
getafe_players1['mins'] = player_games['minutes']
getafe_players1['goals'] = player_goals['total']
getafe_players1['shots'] = player_shots['total']
getafe_players1['shots_on_target'] = player_shots['on']
getafe_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
getafe_players1['assists'] = player_goals['assists']
getafe_players1['passes'] = player_passes['total']
getafe_players1['passes_completed'] = player_passes['accuracy']
# getafe_players1['pass_accuracy_%'] = df_p1['name']
getafe_players1['dribbles'] = player_dribbles['attempts']
getafe_players1['dribbles_completed'] = player_dribbles['success']
getafe_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
getafe_players1['tackles'] = player_tackles['total']
getafe_players1['blocks'] = player_tackles['blocks']
getafe_players1['interceptions'] = player_tackles['interceptions']
getafe_players1['fouls_drawn'] = player_fouls['drawn']
getafe_players1['fouls_committed'] = player_fouls['committed']
getafe_players1['yellow_cards'] = player_cards['yellow']
getafe_players1['red_cards'] = player_cards['red']
getafe_players1['yellow_to_red_cards'] = player_cards['yellowred']
getafe_players1['sub_in'] = player_subs['in']
getafe_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
getafe_players1 = getafe_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"546","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
getafe_players2 = pd.DataFrame()

getafe_players2['name'] = df_p1['name']
getafe_players2['first_name'] = df_p1['firstname']
getafe_players2['last_name'] = df_p1['lastname']
getafe_players2['id'] = df_p1['id']
getafe_players2['team'] = player_team['name']
getafe_players2['team_id'] = player_team['id']
getafe_players2['league'] = player_league['name']
getafe_players2['league_id'] = player_league['id']
getafe_players2['age'] = df_p1['age']
getafe_players2['birth'] = player_birth['date']
getafe_players2['nationality'] = df_p1['nationality']
getafe_players2['app'] = player_games['appearences']
getafe_players2['mins'] = player_games['minutes']
getafe_players2['goals'] = player_goals['total']
getafe_players2['shots'] = player_shots['total']
getafe_players2['shots_on_target'] = player_shots['on']
getafe_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
getafe_players2['assists'] = player_goals['assists']
getafe_players2['passes'] = player_passes['total']
getafe_players2['passes_completed'] = player_passes['accuracy']
# getafe_players2['pass_accuracy_%'] = df_p1['name']
getafe_players2['dribbles'] = player_dribbles['attempts']
getafe_players2['dribbles_completed'] = player_dribbles['success']
getafe_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
getafe_players2['tackles'] = player_tackles['total']
getafe_players2['blocks'] = player_tackles['blocks']
getafe_players2['interceptions'] = player_tackles['interceptions']
getafe_players2['fouls_drawn'] = player_fouls['drawn']
getafe_players2['fouls_committed'] = player_fouls['committed']
getafe_players2['yellow_cards'] = player_cards['yellow']
getafe_players2['red_cards'] = player_cards['red']
getafe_players2['yellow_to_red_cards'] = player_cards['yellowred']
getafe_players2['sub_in'] = player_subs['in']
getafe_players2['sub_out'] = player_subs['out']

getafe_players2 = getafe_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
getafe_players = pd.concat([getafe_players1, getafe_players2])
getafe_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column














####### GRANADA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"715","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
granada_players1 = pd.DataFrame()

granada_players1['name'] = df_p1['name']
granada_players1['first_name'] = df_p1['firstname']
granada_players1['last_name'] = df_p1['lastname']
granada_players1['id'] = df_p1['id']
granada_players1['team'] = player_team['name']
granada_players1['team_id'] = player_team['id']
granada_players1['league'] = player_league['name']
granada_players1['league_id'] = player_league['id']
granada_players1['age'] = df_p1['age']
granada_players1['birth'] = player_birth['date']
granada_players1['nationality'] = df_p1['nationality']
granada_players1['app'] = player_games['appearences']
granada_players1['mins'] = player_games['minutes']
granada_players1['goals'] = player_goals['total']
granada_players1['shots'] = player_shots['total']
granada_players1['shots_on_target'] = player_shots['on']
granada_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
granada_players1['assists'] = player_goals['assists']
granada_players1['passes'] = player_passes['total']
granada_players1['passes_completed'] = player_passes['accuracy']
# granada_players1['pass_accuracy_%'] = df_p1['name']
granada_players1['dribbles'] = player_dribbles['attempts']
granada_players1['dribbles_completed'] = player_dribbles['success']
granada_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
granada_players1['tackles'] = player_tackles['total']
granada_players1['blocks'] = player_tackles['blocks']
granada_players1['interceptions'] = player_tackles['interceptions']
granada_players1['fouls_drawn'] = player_fouls['drawn']
granada_players1['fouls_committed'] = player_fouls['committed']
granada_players1['yellow_cards'] = player_cards['yellow']
granada_players1['red_cards'] = player_cards['red']
granada_players1['yellow_to_red_cards'] = player_cards['yellowred']
granada_players1['sub_in'] = player_subs['in']
granada_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
granada_players1 = granada_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"715","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
granada_players2 = pd.DataFrame()

granada_players2['name'] = df_p1['name']
granada_players2['first_name'] = df_p1['firstname']
granada_players2['last_name'] = df_p1['lastname']
granada_players2['id'] = df_p1['id']
granada_players2['team'] = player_team['name']
granada_players2['team_id'] = player_team['id']
granada_players2['league'] = player_league['name']
granada_players2['league_id'] = player_league['id']
granada_players2['age'] = df_p1['age']
granada_players2['birth'] = player_birth['date']
granada_players2['nationality'] = df_p1['nationality']
granada_players2['app'] = player_games['appearences']
granada_players2['mins'] = player_games['minutes']
granada_players2['goals'] = player_goals['total']
granada_players2['shots'] = player_shots['total']
granada_players2['shots_on_target'] = player_shots['on']
granada_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
granada_players2['assists'] = player_goals['assists']
granada_players2['passes'] = player_passes['total']
granada_players2['passes_completed'] = player_passes['accuracy']
# granada_players2['pass_accuracy_%'] = df_p1['name']
granada_players2['dribbles'] = player_dribbles['attempts']
granada_players2['dribbles_completed'] = player_dribbles['success']
granada_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
granada_players2['tackles'] = player_tackles['total']
granada_players2['blocks'] = player_tackles['blocks']
granada_players2['interceptions'] = player_tackles['interceptions']
granada_players2['fouls_drawn'] = player_fouls['drawn']
granada_players2['fouls_committed'] = player_fouls['committed']
granada_players2['yellow_cards'] = player_cards['yellow']
granada_players2['red_cards'] = player_cards['red']
granada_players2['yellow_to_red_cards'] = player_cards['yellowred']
granada_players2['sub_in'] = player_subs['in']
granada_players2['sub_out'] = player_subs['out']

granada_players2 = granada_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
granada_players = pd.concat([granada_players1, granada_players2])
granada_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### LEVANTE  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"539","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
levante_players1 = pd.DataFrame()

levante_players1['name'] = df_p1['name']
levante_players1['first_name'] = df_p1['firstname']
levante_players1['last_name'] = df_p1['lastname']
levante_players1['id'] = df_p1['id']
levante_players1['team'] = player_team['name']
levante_players1['team_id'] = player_team['id']
levante_players1['league'] = player_league['name']
levante_players1['league_id'] = player_league['id']
levante_players1['age'] = df_p1['age']
levante_players1['birth'] = player_birth['date']
levante_players1['nationality'] = df_p1['nationality']
levante_players1['app'] = player_games['appearences']
levante_players1['mins'] = player_games['minutes']
levante_players1['goals'] = player_goals['total']
levante_players1['shots'] = player_shots['total']
levante_players1['shots_on_target'] = player_shots['on']
levante_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
levante_players1['assists'] = player_goals['assists']
levante_players1['passes'] = player_passes['total']
levante_players1['passes_completed'] = player_passes['accuracy']
# levante_players1['pass_accuracy_%'] = df_p1['name']
levante_players1['dribbles'] = player_dribbles['attempts']
levante_players1['dribbles_completed'] = player_dribbles['success']
levante_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
levante_players1['tackles'] = player_tackles['total']
levante_players1['blocks'] = player_tackles['blocks']
levante_players1['interceptions'] = player_tackles['interceptions']
levante_players1['fouls_drawn'] = player_fouls['drawn']
levante_players1['fouls_committed'] = player_fouls['committed']
levante_players1['yellow_cards'] = player_cards['yellow']
levante_players1['red_cards'] = player_cards['red']
levante_players1['yellow_to_red_cards'] = player_cards['yellowred']
levante_players1['sub_in'] = player_subs['in']
levante_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
levante_players1 = levante_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"539","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
levante_players2 = pd.DataFrame()

levante_players2['name'] = df_p1['name']
levante_players2['first_name'] = df_p1['firstname']
levante_players2['last_name'] = df_p1['lastname']
levante_players2['id'] = df_p1['id']
levante_players2['team'] = player_team['name']
levante_players2['team_id'] = player_team['id']
levante_players2['league'] = player_league['name']
levante_players2['league_id'] = player_league['id']
levante_players2['age'] = df_p1['age']
levante_players2['birth'] = player_birth['date']
levante_players2['nationality'] = df_p1['nationality']
levante_players2['app'] = player_games['appearences']
levante_players2['mins'] = player_games['minutes']
levante_players2['goals'] = player_goals['total']
levante_players2['shots'] = player_shots['total']
levante_players2['shots_on_target'] = player_shots['on']
levante_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
levante_players2['assists'] = player_goals['assists']
levante_players2['passes'] = player_passes['total']
levante_players2['passes_completed'] = player_passes['accuracy']
# levante_players2['pass_accuracy_%'] = df_p1['name']
levante_players2['dribbles'] = player_dribbles['attempts']
levante_players2['dribbles_completed'] = player_dribbles['success']
levante_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
levante_players2['tackles'] = player_tackles['total']
levante_players2['blocks'] = player_tackles['blocks']
levante_players2['interceptions'] = player_tackles['interceptions']
levante_players2['fouls_drawn'] = player_fouls['drawn']
levante_players2['fouls_committed'] = player_fouls['committed']
levante_players2['yellow_cards'] = player_cards['yellow']
levante_players2['red_cards'] = player_cards['red']
levante_players2['yellow_to_red_cards'] = player_cards['yellowred']
levante_players2['sub_in'] = player_subs['in']
levante_players2['sub_out'] = player_subs['out']

levante_players2 = levante_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
levante_players = pd.concat([levante_players1, levante_players2])
levante_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### MALLORCA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"798","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
mallorca_players1 = pd.DataFrame()

mallorca_players1['name'] = df_p1['name']
mallorca_players1['first_name'] = df_p1['firstname']
mallorca_players1['last_name'] = df_p1['lastname']
mallorca_players1['id'] = df_p1['id']
mallorca_players1['team'] = player_team['name']
mallorca_players1['team_id'] = player_team['id']
mallorca_players1['league'] = player_league['name']
mallorca_players1['league_id'] = player_league['id']
mallorca_players1['age'] = df_p1['age']
mallorca_players1['birth'] = player_birth['date']
mallorca_players1['nationality'] = df_p1['nationality']
mallorca_players1['app'] = player_games['appearences']
mallorca_players1['mins'] = player_games['minutes']
mallorca_players1['goals'] = player_goals['total']
mallorca_players1['shots'] = player_shots['total']
mallorca_players1['shots_on_target'] = player_shots['on']
mallorca_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
mallorca_players1['assists'] = player_goals['assists']
mallorca_players1['passes'] = player_passes['total']
mallorca_players1['passes_completed'] = player_passes['accuracy']
# mallorca_players1['pass_accuracy_%'] = df_p1['name']
mallorca_players1['dribbles'] = player_dribbles['attempts']
mallorca_players1['dribbles_completed'] = player_dribbles['success']
mallorca_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
mallorca_players1['tackles'] = player_tackles['total']
mallorca_players1['blocks'] = player_tackles['blocks']
mallorca_players1['interceptions'] = player_tackles['interceptions']
mallorca_players1['fouls_drawn'] = player_fouls['drawn']
mallorca_players1['fouls_committed'] = player_fouls['committed']
mallorca_players1['yellow_cards'] = player_cards['yellow']
mallorca_players1['red_cards'] = player_cards['red']
mallorca_players1['yellow_to_red_cards'] = player_cards['yellowred']
mallorca_players1['sub_in'] = player_subs['in']
mallorca_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
mallorca_players1 = mallorca_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"798","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
mallorca_players2 = pd.DataFrame()

mallorca_players2['name'] = df_p1['name']
mallorca_players2['first_name'] = df_p1['firstname']
mallorca_players2['last_name'] = df_p1['lastname']
mallorca_players2['id'] = df_p1['id']
mallorca_players2['team'] = player_team['name']
mallorca_players2['team_id'] = player_team['id']
mallorca_players2['league'] = player_league['name']
mallorca_players2['league_id'] = player_league['id']
mallorca_players2['age'] = df_p1['age']
mallorca_players2['birth'] = player_birth['date']
mallorca_players2['nationality'] = df_p1['nationality']
mallorca_players2['app'] = player_games['appearences']
mallorca_players2['mins'] = player_games['minutes']
mallorca_players2['goals'] = player_goals['total']
mallorca_players2['shots'] = player_shots['total']
mallorca_players2['shots_on_target'] = player_shots['on']
mallorca_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
mallorca_players2['assists'] = player_goals['assists']
mallorca_players2['passes'] = player_passes['total']
mallorca_players2['passes_completed'] = player_passes['accuracy']
# mallorca_players2['pass_accuracy_%'] = df_p1['name']
mallorca_players2['dribbles'] = player_dribbles['attempts']
mallorca_players2['dribbles_completed'] = player_dribbles['success']
mallorca_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
mallorca_players2['tackles'] = player_tackles['total']
mallorca_players2['blocks'] = player_tackles['blocks']
mallorca_players2['interceptions'] = player_tackles['interceptions']
mallorca_players2['fouls_drawn'] = player_fouls['drawn']
mallorca_players2['fouls_committed'] = player_fouls['committed']
mallorca_players2['yellow_cards'] = player_cards['yellow']
mallorca_players2['red_cards'] = player_cards['red']
mallorca_players2['yellow_to_red_cards'] = player_cards['yellowred']
mallorca_players2['sub_in'] = player_subs['in']
mallorca_players2['sub_out'] = player_subs['out']

mallorca_players2 = mallorca_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
mallorca_players = pd.concat([mallorca_players1, mallorca_players2])
mallorca_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### OSASUNA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"727","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
osasuna_players1 = pd.DataFrame()

osasuna_players1['name'] = df_p1['name']
osasuna_players1['first_name'] = df_p1['firstname']
osasuna_players1['last_name'] = df_p1['lastname']
osasuna_players1['id'] = df_p1['id']
osasuna_players1['team'] = player_team['name']
osasuna_players1['team_id'] = player_team['id']
osasuna_players1['league'] = player_league['name']
osasuna_players1['league_id'] = player_league['id']
osasuna_players1['age'] = df_p1['age']
osasuna_players1['birth'] = player_birth['date']
osasuna_players1['nationality'] = df_p1['nationality']
osasuna_players1['app'] = player_games['appearences']
osasuna_players1['mins'] = player_games['minutes']
osasuna_players1['goals'] = player_goals['total']
osasuna_players1['shots'] = player_shots['total']
osasuna_players1['shots_on_target'] = player_shots['on']
osasuna_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
osasuna_players1['assists'] = player_goals['assists']
osasuna_players1['passes'] = player_passes['total']
osasuna_players1['passes_completed'] = player_passes['accuracy']
# osasuna_players1['pass_accuracy_%'] = df_p1['name']
osasuna_players1['dribbles'] = player_dribbles['attempts']
osasuna_players1['dribbles_completed'] = player_dribbles['success']
osasuna_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
osasuna_players1['tackles'] = player_tackles['total']
osasuna_players1['blocks'] = player_tackles['blocks']
osasuna_players1['interceptions'] = player_tackles['interceptions']
osasuna_players1['fouls_drawn'] = player_fouls['drawn']
osasuna_players1['fouls_committed'] = player_fouls['committed']
osasuna_players1['yellow_cards'] = player_cards['yellow']
osasuna_players1['red_cards'] = player_cards['red']
osasuna_players1['yellow_to_red_cards'] = player_cards['yellowred']
osasuna_players1['sub_in'] = player_subs['in']
osasuna_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
osasuna_players1 = osasuna_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"727","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
osasuna_players2 = pd.DataFrame()

osasuna_players2['name'] = df_p1['name']
osasuna_players2['first_name'] = df_p1['firstname']
osasuna_players2['last_name'] = df_p1['lastname']
osasuna_players2['id'] = df_p1['id']
osasuna_players2['team'] = player_team['name']
osasuna_players2['team_id'] = player_team['id']
osasuna_players2['league'] = player_league['name']
osasuna_players2['league_id'] = player_league['id']
osasuna_players2['age'] = df_p1['age']
osasuna_players2['birth'] = player_birth['date']
osasuna_players2['nationality'] = df_p1['nationality']
osasuna_players2['app'] = player_games['appearences']
osasuna_players2['mins'] = player_games['minutes']
osasuna_players2['goals'] = player_goals['total']
osasuna_players2['shots'] = player_shots['total']
osasuna_players2['shots_on_target'] = player_shots['on']
osasuna_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
osasuna_players2['assists'] = player_goals['assists']
osasuna_players2['passes'] = player_passes['total']
osasuna_players2['passes_completed'] = player_passes['accuracy']
# osasuna_players2['pass_accuracy_%'] = df_p1['name']
osasuna_players2['dribbles'] = player_dribbles['attempts']
osasuna_players2['dribbles_completed'] = player_dribbles['success']
osasuna_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
osasuna_players2['tackles'] = player_tackles['total']
osasuna_players2['blocks'] = player_tackles['blocks']
osasuna_players2['interceptions'] = player_tackles['interceptions']
osasuna_players2['fouls_drawn'] = player_fouls['drawn']
osasuna_players2['fouls_committed'] = player_fouls['committed']
osasuna_players2['yellow_cards'] = player_cards['yellow']
osasuna_players2['red_cards'] = player_cards['red']
osasuna_players2['yellow_to_red_cards'] = player_cards['yellowred']
osasuna_players2['sub_in'] = player_subs['in']
osasuna_players2['sub_out'] = player_subs['out']

osasuna_players2 = osasuna_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
osasuna_players = pd.concat([osasuna_players1, osasuna_players2])
osasuna_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column









####### RAYO VALLECANO  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"728","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
rayo_vallecano_players1 = pd.DataFrame()

rayo_vallecano_players1['name'] = df_p1['name']
rayo_vallecano_players1['first_name'] = df_p1['firstname']
rayo_vallecano_players1['last_name'] = df_p1['lastname']
rayo_vallecano_players1['id'] = df_p1['id']
rayo_vallecano_players1['team'] = player_team['name']
rayo_vallecano_players1['team_id'] = player_team['id']
rayo_vallecano_players1['league'] = player_league['name']
rayo_vallecano_players1['league_id'] = player_league['id']
rayo_vallecano_players1['age'] = df_p1['age']
rayo_vallecano_players1['birth'] = player_birth['date']
rayo_vallecano_players1['nationality'] = df_p1['nationality']
rayo_vallecano_players1['app'] = player_games['appearences']
rayo_vallecano_players1['mins'] = player_games['minutes']
rayo_vallecano_players1['goals'] = player_goals['total']
rayo_vallecano_players1['shots'] = player_shots['total']
rayo_vallecano_players1['shots_on_target'] = player_shots['on']
rayo_vallecano_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
rayo_vallecano_players1['assists'] = player_goals['assists']
rayo_vallecano_players1['passes'] = player_passes['total']
rayo_vallecano_players1['passes_completed'] = player_passes['accuracy']
# rayo_vallecano_players1['pass_accuracy_%'] = df_p1['name']
rayo_vallecano_players1['dribbles'] = player_dribbles['attempts']
rayo_vallecano_players1['dribbles_completed'] = player_dribbles['success']
rayo_vallecano_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
rayo_vallecano_players1['tackles'] = player_tackles['total']
rayo_vallecano_players1['blocks'] = player_tackles['blocks']
rayo_vallecano_players1['interceptions'] = player_tackles['interceptions']
rayo_vallecano_players1['fouls_drawn'] = player_fouls['drawn']
rayo_vallecano_players1['fouls_committed'] = player_fouls['committed']
rayo_vallecano_players1['yellow_cards'] = player_cards['yellow']
rayo_vallecano_players1['red_cards'] = player_cards['red']
rayo_vallecano_players1['yellow_to_red_cards'] = player_cards['yellowred']
rayo_vallecano_players1['sub_in'] = player_subs['in']
rayo_vallecano_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
rayo_vallecano_players1 = rayo_vallecano_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"728","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
rayo_vallecano_players2 = pd.DataFrame()

rayo_vallecano_players2['name'] = df_p1['name']
rayo_vallecano_players2['first_name'] = df_p1['firstname']
rayo_vallecano_players2['last_name'] = df_p1['lastname']
rayo_vallecano_players2['id'] = df_p1['id']
rayo_vallecano_players2['team'] = player_team['name']
rayo_vallecano_players2['team_id'] = player_team['id']
rayo_vallecano_players2['league'] = player_league['name']
rayo_vallecano_players2['league_id'] = player_league['id']
rayo_vallecano_players2['age'] = df_p1['age']
rayo_vallecano_players2['birth'] = player_birth['date']
rayo_vallecano_players2['nationality'] = df_p1['nationality']
rayo_vallecano_players2['app'] = player_games['appearences']
rayo_vallecano_players2['mins'] = player_games['minutes']
rayo_vallecano_players2['goals'] = player_goals['total']
rayo_vallecano_players2['shots'] = player_shots['total']
rayo_vallecano_players2['shots_on_target'] = player_shots['on']
rayo_vallecano_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
rayo_vallecano_players2['assists'] = player_goals['assists']
rayo_vallecano_players2['passes'] = player_passes['total']
rayo_vallecano_players2['passes_completed'] = player_passes['accuracy']
# rayo_vallecano_players2['pass_accuracy_%'] = df_p1['name']
rayo_vallecano_players2['dribbles'] = player_dribbles['attempts']
rayo_vallecano_players2['dribbles_completed'] = player_dribbles['success']
rayo_vallecano_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
rayo_vallecano_players2['tackles'] = player_tackles['total']
rayo_vallecano_players2['blocks'] = player_tackles['blocks']
rayo_vallecano_players2['interceptions'] = player_tackles['interceptions']
rayo_vallecano_players2['fouls_drawn'] = player_fouls['drawn']
rayo_vallecano_players2['fouls_committed'] = player_fouls['committed']
rayo_vallecano_players2['yellow_cards'] = player_cards['yellow']
rayo_vallecano_players2['red_cards'] = player_cards['red']
rayo_vallecano_players2['yellow_to_red_cards'] = player_cards['yellowred']
rayo_vallecano_players2['sub_in'] = player_subs['in']
rayo_vallecano_players2['sub_out'] = player_subs['out']

rayo_vallecano_players2 = rayo_vallecano_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
rayo_vallecano_players = pd.concat([rayo_vallecano_players1, rayo_vallecano_players2])
rayo_vallecano_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### REAL BETIS  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"543","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
real_betis_players1 = pd.DataFrame()

real_betis_players1['name'] = df_p1['name']
real_betis_players1['first_name'] = df_p1['firstname']
real_betis_players1['last_name'] = df_p1['lastname']
real_betis_players1['id'] = df_p1['id']
real_betis_players1['team'] = player_team['name']
real_betis_players1['team_id'] = player_team['id']
real_betis_players1['league'] = player_league['name']
real_betis_players1['league_id'] = player_league['id']
real_betis_players1['age'] = df_p1['age']
real_betis_players1['birth'] = player_birth['date']
real_betis_players1['nationality'] = df_p1['nationality']
real_betis_players1['app'] = player_games['appearences']
real_betis_players1['mins'] = player_games['minutes']
real_betis_players1['goals'] = player_goals['total']
real_betis_players1['shots'] = player_shots['total']
real_betis_players1['shots_on_target'] = player_shots['on']
real_betis_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
real_betis_players1['assists'] = player_goals['assists']
real_betis_players1['passes'] = player_passes['total']
real_betis_players1['passes_completed'] = player_passes['accuracy']
# real_betis_players1['pass_accuracy_%'] = df_p1['name']
real_betis_players1['dribbles'] = player_dribbles['attempts']
real_betis_players1['dribbles_completed'] = player_dribbles['success']
real_betis_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
real_betis_players1['tackles'] = player_tackles['total']
real_betis_players1['blocks'] = player_tackles['blocks']
real_betis_players1['interceptions'] = player_tackles['interceptions']
real_betis_players1['fouls_drawn'] = player_fouls['drawn']
real_betis_players1['fouls_committed'] = player_fouls['committed']
real_betis_players1['yellow_cards'] = player_cards['yellow']
real_betis_players1['red_cards'] = player_cards['red']
real_betis_players1['yellow_to_red_cards'] = player_cards['yellowred']
real_betis_players1['sub_in'] = player_subs['in']
real_betis_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
real_betis_players1 = real_betis_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"543","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
real_betis_players2 = pd.DataFrame()

real_betis_players2['name'] = df_p1['name']
real_betis_players2['first_name'] = df_p1['firstname']
real_betis_players2['last_name'] = df_p1['lastname']
real_betis_players2['id'] = df_p1['id']
real_betis_players2['team'] = player_team['name']
real_betis_players2['team_id'] = player_team['id']
real_betis_players2['league'] = player_league['name']
real_betis_players2['league_id'] = player_league['id']
real_betis_players2['age'] = df_p1['age']
real_betis_players2['birth'] = player_birth['date']
real_betis_players2['nationality'] = df_p1['nationality']
real_betis_players2['app'] = player_games['appearences']
real_betis_players2['mins'] = player_games['minutes']
real_betis_players2['goals'] = player_goals['total']
real_betis_players2['shots'] = player_shots['total']
real_betis_players2['shots_on_target'] = player_shots['on']
real_betis_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
real_betis_players2['assists'] = player_goals['assists']
real_betis_players2['passes'] = player_passes['total']
real_betis_players2['passes_completed'] = player_passes['accuracy']
# real_betis_players2['pass_accuracy_%'] = df_p1['name']
real_betis_players2['dribbles'] = player_dribbles['attempts']
real_betis_players2['dribbles_completed'] = player_dribbles['success']
real_betis_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
real_betis_players2['tackles'] = player_tackles['total']
real_betis_players2['blocks'] = player_tackles['blocks']
real_betis_players2['interceptions'] = player_tackles['interceptions']
real_betis_players2['fouls_drawn'] = player_fouls['drawn']
real_betis_players2['fouls_committed'] = player_fouls['committed']
real_betis_players2['yellow_cards'] = player_cards['yellow']
real_betis_players2['red_cards'] = player_cards['red']
real_betis_players2['yellow_to_red_cards'] = player_cards['yellowred']
real_betis_players2['sub_in'] = player_subs['in']
real_betis_players2['sub_out'] = player_subs['out']

real_betis_players2 = real_betis_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
real_betis_players = pd.concat([real_betis_players1, real_betis_players2])
real_betis_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### REAL MADRID  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"541","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
real_madrid_players1 = pd.DataFrame()

real_madrid_players1['name'] = df_p1['name']
real_madrid_players1['first_name'] = df_p1['firstname']
real_madrid_players1['last_name'] = df_p1['lastname']
real_madrid_players1['id'] = df_p1['id']
real_madrid_players1['team'] = player_team['name']
real_madrid_players1['team_id'] = player_team['id']
real_madrid_players1['league'] = player_league['name']
real_madrid_players1['league_id'] = player_league['id']
real_madrid_players1['age'] = df_p1['age']
real_madrid_players1['birth'] = player_birth['date']
real_madrid_players1['nationality'] = df_p1['nationality']
real_madrid_players1['app'] = player_games['appearences']
real_madrid_players1['mins'] = player_games['minutes']
real_madrid_players1['goals'] = player_goals['total']
real_madrid_players1['shots'] = player_shots['total']
real_madrid_players1['shots_on_target'] = player_shots['on']
real_madrid_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
real_madrid_players1['assists'] = player_goals['assists']
real_madrid_players1['passes'] = player_passes['total']
real_madrid_players1['passes_completed'] = player_passes['accuracy']
# real_madrid_players1['pass_accuracy_%'] = df_p1['name']
real_madrid_players1['dribbles'] = player_dribbles['attempts']
real_madrid_players1['dribbles_completed'] = player_dribbles['success']
real_madrid_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
real_madrid_players1['tackles'] = player_tackles['total']
real_madrid_players1['blocks'] = player_tackles['blocks']
real_madrid_players1['interceptions'] = player_tackles['interceptions']
real_madrid_players1['fouls_drawn'] = player_fouls['drawn']
real_madrid_players1['fouls_committed'] = player_fouls['committed']
real_madrid_players1['yellow_cards'] = player_cards['yellow']
real_madrid_players1['red_cards'] = player_cards['red']
real_madrid_players1['yellow_to_red_cards'] = player_cards['yellowred']
real_madrid_players1['sub_in'] = player_subs['in']
real_madrid_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
real_madrid_players1 = real_madrid_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"541","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
real_madrid_players2 = pd.DataFrame()

real_madrid_players2['name'] = df_p1['name']
real_madrid_players2['first_name'] = df_p1['firstname']
real_madrid_players2['last_name'] = df_p1['lastname']
real_madrid_players2['id'] = df_p1['id']
real_madrid_players2['team'] = player_team['name']
real_madrid_players2['team_id'] = player_team['id']
real_madrid_players2['league'] = player_league['name']
real_madrid_players2['league_id'] = player_league['id']
real_madrid_players2['age'] = df_p1['age']
real_madrid_players2['birth'] = player_birth['date']
real_madrid_players2['nationality'] = df_p1['nationality']
real_madrid_players2['app'] = player_games['appearences']
real_madrid_players2['mins'] = player_games['minutes']
real_madrid_players2['goals'] = player_goals['total']
real_madrid_players2['shots'] = player_shots['total']
real_madrid_players2['shots_on_target'] = player_shots['on']
real_madrid_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
real_madrid_players2['assists'] = player_goals['assists']
real_madrid_players2['passes'] = player_passes['total']
real_madrid_players2['passes_completed'] = player_passes['accuracy']
# real_madrid_players2['pass_accuracy_%'] = df_p1['name']
real_madrid_players2['dribbles'] = player_dribbles['attempts']
real_madrid_players2['dribbles_completed'] = player_dribbles['success']
real_madrid_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
real_madrid_players2['tackles'] = player_tackles['total']
real_madrid_players2['blocks'] = player_tackles['blocks']
real_madrid_players2['interceptions'] = player_tackles['interceptions']
real_madrid_players2['fouls_drawn'] = player_fouls['drawn']
real_madrid_players2['fouls_committed'] = player_fouls['committed']
real_madrid_players2['yellow_cards'] = player_cards['yellow']
real_madrid_players2['red_cards'] = player_cards['red']
real_madrid_players2['yellow_to_red_cards'] = player_cards['yellowred']
real_madrid_players2['sub_in'] = player_subs['in']
real_madrid_players2['sub_out'] = player_subs['out']

real_madrid_players2 = real_madrid_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
real_madrid_players = pd.concat([real_madrid_players1, real_madrid_players2])
real_madrid_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### REAL SOCIEDAD  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"548","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
real_sociedad_players1 = pd.DataFrame()

real_sociedad_players1['name'] = df_p1['name']
real_sociedad_players1['first_name'] = df_p1['firstname']
real_sociedad_players1['last_name'] = df_p1['lastname']
real_sociedad_players1['id'] = df_p1['id']
real_sociedad_players1['team'] = player_team['name']
real_sociedad_players1['team_id'] = player_team['id']
real_sociedad_players1['league'] = player_league['name']
real_sociedad_players1['league_id'] = player_league['id']
real_sociedad_players1['age'] = df_p1['age']
real_sociedad_players1['birth'] = player_birth['date']
real_sociedad_players1['nationality'] = df_p1['nationality']
real_sociedad_players1['app'] = player_games['appearences']
real_sociedad_players1['mins'] = player_games['minutes']
real_sociedad_players1['goals'] = player_goals['total']
real_sociedad_players1['shots'] = player_shots['total']
real_sociedad_players1['shots_on_target'] = player_shots['on']
real_sociedad_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
real_sociedad_players1['assists'] = player_goals['assists']
real_sociedad_players1['passes'] = player_passes['total']
real_sociedad_players1['passes_completed'] = player_passes['accuracy']
# real_sociedad_players1['pass_accuracy_%'] = df_p1['name']
real_sociedad_players1['dribbles'] = player_dribbles['attempts']
real_sociedad_players1['dribbles_completed'] = player_dribbles['success']
real_sociedad_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
real_sociedad_players1['tackles'] = player_tackles['total']
real_sociedad_players1['blocks'] = player_tackles['blocks']
real_sociedad_players1['interceptions'] = player_tackles['interceptions']
real_sociedad_players1['fouls_drawn'] = player_fouls['drawn']
real_sociedad_players1['fouls_committed'] = player_fouls['committed']
real_sociedad_players1['yellow_cards'] = player_cards['yellow']
real_sociedad_players1['red_cards'] = player_cards['red']
real_sociedad_players1['yellow_to_red_cards'] = player_cards['yellowred']
real_sociedad_players1['sub_in'] = player_subs['in']
real_sociedad_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
real_sociedad_players1 = real_sociedad_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"548","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
real_sociedad_players2 = pd.DataFrame()

real_sociedad_players2['name'] = df_p1['name']
real_sociedad_players2['first_name'] = df_p1['firstname']
real_sociedad_players2['last_name'] = df_p1['lastname']
real_sociedad_players2['id'] = df_p1['id']
real_sociedad_players2['team'] = player_team['name']
real_sociedad_players2['team_id'] = player_team['id']
real_sociedad_players2['league'] = player_league['name']
real_sociedad_players2['league_id'] = player_league['id']
real_sociedad_players2['age'] = df_p1['age']
real_sociedad_players2['birth'] = player_birth['date']
real_sociedad_players2['nationality'] = df_p1['nationality']
real_sociedad_players2['app'] = player_games['appearences']
real_sociedad_players2['mins'] = player_games['minutes']
real_sociedad_players2['goals'] = player_goals['total']
real_sociedad_players2['shots'] = player_shots['total']
real_sociedad_players2['shots_on_target'] = player_shots['on']
real_sociedad_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
real_sociedad_players2['assists'] = player_goals['assists']
real_sociedad_players2['passes'] = player_passes['total']
real_sociedad_players2['passes_completed'] = player_passes['accuracy']
# real_sociedad_players2['pass_accuracy_%'] = df_p1['name']
real_sociedad_players2['dribbles'] = player_dribbles['attempts']
real_sociedad_players2['dribbles_completed'] = player_dribbles['success']
real_sociedad_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
real_sociedad_players2['tackles'] = player_tackles['total']
real_sociedad_players2['blocks'] = player_tackles['blocks']
real_sociedad_players2['interceptions'] = player_tackles['interceptions']
real_sociedad_players2['fouls_drawn'] = player_fouls['drawn']
real_sociedad_players2['fouls_committed'] = player_fouls['committed']
real_sociedad_players2['yellow_cards'] = player_cards['yellow']
real_sociedad_players2['red_cards'] = player_cards['red']
real_sociedad_players2['yellow_to_red_cards'] = player_cards['yellowred']
real_sociedad_players2['sub_in'] = player_subs['in']
real_sociedad_players2['sub_out'] = player_subs['out']

real_sociedad_players2 = real_sociedad_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
real_sociedad_players = pd.concat([real_sociedad_players1, real_sociedad_players2])
real_sociedad_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### SEVILLA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"536","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
sevilla_players1 = pd.DataFrame()

sevilla_players1['name'] = df_p1['name']
sevilla_players1['first_name'] = df_p1['firstname']
sevilla_players1['last_name'] = df_p1['lastname']
sevilla_players1['id'] = df_p1['id']
sevilla_players1['team'] = player_team['name']
sevilla_players1['team_id'] = player_team['id']
sevilla_players1['league'] = player_league['name']
sevilla_players1['league_id'] = player_league['id']
sevilla_players1['age'] = df_p1['age']
sevilla_players1['birth'] = player_birth['date']
sevilla_players1['nationality'] = df_p1['nationality']
sevilla_players1['app'] = player_games['appearences']
sevilla_players1['mins'] = player_games['minutes']
sevilla_players1['goals'] = player_goals['total']
sevilla_players1['shots'] = player_shots['total']
sevilla_players1['shots_on_target'] = player_shots['on']
sevilla_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
sevilla_players1['assists'] = player_goals['assists']
sevilla_players1['passes'] = player_passes['total']
sevilla_players1['passes_completed'] = player_passes['accuracy']
# sevilla_players1['pass_accuracy_%'] = df_p1['name']
sevilla_players1['dribbles'] = player_dribbles['attempts']
sevilla_players1['dribbles_completed'] = player_dribbles['success']
sevilla_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
sevilla_players1['tackles'] = player_tackles['total']
sevilla_players1['blocks'] = player_tackles['blocks']
sevilla_players1['interceptions'] = player_tackles['interceptions']
sevilla_players1['fouls_drawn'] = player_fouls['drawn']
sevilla_players1['fouls_committed'] = player_fouls['committed']
sevilla_players1['yellow_cards'] = player_cards['yellow']
sevilla_players1['red_cards'] = player_cards['red']
sevilla_players1['yellow_to_red_cards'] = player_cards['yellowred']
sevilla_players1['sub_in'] = player_subs['in']
sevilla_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
sevilla_players1 = sevilla_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"536","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
sevilla_players2 = pd.DataFrame()

sevilla_players2['name'] = df_p1['name']
sevilla_players2['first_name'] = df_p1['firstname']
sevilla_players2['last_name'] = df_p1['lastname']
sevilla_players2['id'] = df_p1['id']
sevilla_players2['team'] = player_team['name']
sevilla_players2['team_id'] = player_team['id']
sevilla_players2['league'] = player_league['name']
sevilla_players2['league_id'] = player_league['id']
sevilla_players2['age'] = df_p1['age']
sevilla_players2['birth'] = player_birth['date']
sevilla_players2['nationality'] = df_p1['nationality']
sevilla_players2['app'] = player_games['appearences']
sevilla_players2['mins'] = player_games['minutes']
sevilla_players2['goals'] = player_goals['total']
sevilla_players2['shots'] = player_shots['total']
sevilla_players2['shots_on_target'] = player_shots['on']
sevilla_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
sevilla_players2['assists'] = player_goals['assists']
sevilla_players2['passes'] = player_passes['total']
sevilla_players2['passes_completed'] = player_passes['accuracy']
# sevilla_players2['pass_accuracy_%'] = df_p1['name']
sevilla_players2['dribbles'] = player_dribbles['attempts']
sevilla_players2['dribbles_completed'] = player_dribbles['success']
sevilla_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
sevilla_players2['tackles'] = player_tackles['total']
sevilla_players2['blocks'] = player_tackles['blocks']
sevilla_players2['interceptions'] = player_tackles['interceptions']
sevilla_players2['fouls_drawn'] = player_fouls['drawn']
sevilla_players2['fouls_committed'] = player_fouls['committed']
sevilla_players2['yellow_cards'] = player_cards['yellow']
sevilla_players2['red_cards'] = player_cards['red']
sevilla_players2['yellow_to_red_cards'] = player_cards['yellowred']
sevilla_players2['sub_in'] = player_subs['in']
sevilla_players2['sub_out'] = player_subs['out']

sevilla_players2 = sevilla_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
sevilla_players = pd.concat([sevilla_players1, sevilla_players2])
sevilla_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### VALENCIA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"532","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
valencia_players1 = pd.DataFrame()

valencia_players1['name'] = df_p1['name']
valencia_players1['first_name'] = df_p1['firstname']
valencia_players1['last_name'] = df_p1['lastname']
valencia_players1['id'] = df_p1['id']
valencia_players1['team'] = player_team['name']
valencia_players1['team_id'] = player_team['id']
valencia_players1['league'] = player_league['name']
valencia_players1['league_id'] = player_league['id']
valencia_players1['age'] = df_p1['age']
valencia_players1['birth'] = player_birth['date']
valencia_players1['nationality'] = df_p1['nationality']
valencia_players1['app'] = player_games['appearences']
valencia_players1['mins'] = player_games['minutes']
valencia_players1['goals'] = player_goals['total']
valencia_players1['shots'] = player_shots['total']
valencia_players1['shots_on_target'] = player_shots['on']
valencia_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
valencia_players1['assists'] = player_goals['assists']
valencia_players1['passes'] = player_passes['total']
valencia_players1['passes_completed'] = player_passes['accuracy']
# valencia_players1['pass_accuracy_%'] = df_p1['name']
valencia_players1['dribbles'] = player_dribbles['attempts']
valencia_players1['dribbles_completed'] = player_dribbles['success']
valencia_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
valencia_players1['tackles'] = player_tackles['total']
valencia_players1['blocks'] = player_tackles['blocks']
valencia_players1['interceptions'] = player_tackles['interceptions']
valencia_players1['fouls_drawn'] = player_fouls['drawn']
valencia_players1['fouls_committed'] = player_fouls['committed']
valencia_players1['yellow_cards'] = player_cards['yellow']
valencia_players1['red_cards'] = player_cards['red']
valencia_players1['yellow_to_red_cards'] = player_cards['yellowred']
valencia_players1['sub_in'] = player_subs['in']
valencia_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
valencia_players1 = valencia_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"532","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
valencia_players2 = pd.DataFrame()

valencia_players2['name'] = df_p1['name']
valencia_players2['first_name'] = df_p1['firstname']
valencia_players2['last_name'] = df_p1['lastname']
valencia_players2['id'] = df_p1['id']
valencia_players2['team'] = player_team['name']
valencia_players2['team_id'] = player_team['id']
valencia_players2['league'] = player_league['name']
valencia_players2['league_id'] = player_league['id']
valencia_players2['age'] = df_p1['age']
valencia_players2['birth'] = player_birth['date']
valencia_players2['nationality'] = df_p1['nationality']
valencia_players2['app'] = player_games['appearences']
valencia_players2['mins'] = player_games['minutes']
valencia_players2['goals'] = player_goals['total']
valencia_players2['shots'] = player_shots['total']
valencia_players2['shots_on_target'] = player_shots['on']
valencia_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
valencia_players2['assists'] = player_goals['assists']
valencia_players2['passes'] = player_passes['total']
valencia_players2['passes_completed'] = player_passes['accuracy']
# valencia_players2['pass_accuracy_%'] = df_p1['name']
valencia_players2['dribbles'] = player_dribbles['attempts']
valencia_players2['dribbles_completed'] = player_dribbles['success']
valencia_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
valencia_players2['tackles'] = player_tackles['total']
valencia_players2['blocks'] = player_tackles['blocks']
valencia_players2['interceptions'] = player_tackles['interceptions']
valencia_players2['fouls_drawn'] = player_fouls['drawn']
valencia_players2['fouls_committed'] = player_fouls['committed']
valencia_players2['yellow_cards'] = player_cards['yellow']
valencia_players2['red_cards'] = player_cards['red']
valencia_players2['yellow_to_red_cards'] = player_cards['yellowred']
valencia_players2['sub_in'] = player_subs['in']
valencia_players2['sub_out'] = player_subs['out']

valencia_players2 = valencia_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
valencia_players = pd.concat([valencia_players1, valencia_players2])
valencia_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### VILLAREAL  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"533","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
villareal_players1 = pd.DataFrame()

villareal_players1['name'] = df_p1['name']
villareal_players1['first_name'] = df_p1['firstname']
villareal_players1['last_name'] = df_p1['lastname']
villareal_players1['id'] = df_p1['id']
villareal_players1['team'] = player_team['name']
villareal_players1['team_id'] = player_team['id']
villareal_players1['league'] = player_league['name']
villareal_players1['league_id'] = player_league['id']
villareal_players1['age'] = df_p1['age']
villareal_players1['birth'] = player_birth['date']
villareal_players1['nationality'] = df_p1['nationality']
villareal_players1['app'] = player_games['appearences']
villareal_players1['mins'] = player_games['minutes']
villareal_players1['goals'] = player_goals['total']
villareal_players1['shots'] = player_shots['total']
villareal_players1['shots_on_target'] = player_shots['on']
villareal_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
villareal_players1['assists'] = player_goals['assists']
villareal_players1['passes'] = player_passes['total']
villareal_players1['passes_completed'] = player_passes['accuracy']
# villareal_players1['pass_accuracy_%'] = df_p1['name']
villareal_players1['dribbles'] = player_dribbles['attempts']
villareal_players1['dribbles_completed'] = player_dribbles['success']
villareal_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
villareal_players1['tackles'] = player_tackles['total']
villareal_players1['blocks'] = player_tackles['blocks']
villareal_players1['interceptions'] = player_tackles['interceptions']
villareal_players1['fouls_drawn'] = player_fouls['drawn']
villareal_players1['fouls_committed'] = player_fouls['committed']
villareal_players1['yellow_cards'] = player_cards['yellow']
villareal_players1['red_cards'] = player_cards['red']
villareal_players1['yellow_to_red_cards'] = player_cards['yellowred']
villareal_players1['sub_in'] = player_subs['in']
villareal_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
villareal_players1 = villareal_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"533","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
villareal_players2 = pd.DataFrame()

villareal_players2['name'] = df_p1['name']
villareal_players2['first_name'] = df_p1['firstname']
villareal_players2['last_name'] = df_p1['lastname']
villareal_players2['id'] = df_p1['id']
villareal_players2['team'] = player_team['name']
villareal_players2['team_id'] = player_team['id']
villareal_players2['league'] = player_league['name']
villareal_players2['league_id'] = player_league['id']
villareal_players2['age'] = df_p1['age']
villareal_players2['birth'] = player_birth['date']
villareal_players2['nationality'] = df_p1['nationality']
villareal_players2['app'] = player_games['appearences']
villareal_players2['mins'] = player_games['minutes']
villareal_players2['goals'] = player_goals['total']
villareal_players2['shots'] = player_shots['total']
villareal_players2['shots_on_target'] = player_shots['on']
villareal_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
villareal_players2['assists'] = player_goals['assists']
villareal_players2['passes'] = player_passes['total']
villareal_players2['passes_completed'] = player_passes['accuracy']
# villareal_players2['pass_accuracy_%'] = df_p1['name']
villareal_players2['dribbles'] = player_dribbles['attempts']
villareal_players2['dribbles_completed'] = player_dribbles['success']
villareal_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
villareal_players2['tackles'] = player_tackles['total']
villareal_players2['blocks'] = player_tackles['blocks']
villareal_players2['interceptions'] = player_tackles['interceptions']
villareal_players2['fouls_drawn'] = player_fouls['drawn']
villareal_players2['fouls_committed'] = player_fouls['committed']
villareal_players2['yellow_cards'] = player_cards['yellow']
villareal_players2['red_cards'] = player_cards['red']
villareal_players2['yellow_to_red_cards'] = player_cards['yellowred']
villareal_players2['sub_in'] = player_subs['in']
villareal_players2['sub_out'] = player_subs['out']

villareal_players2 = villareal_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
villareal_players = pd.concat([villareal_players1, villareal_players2])
villareal_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column







# Combine players from all teams in the league into a single data frame
la_liga_players = pd.concat([alaves_players,
					athletic_club_players,
					athletico_madrid_players,
					barcelona_players,
					cadiz_players,
					celta_vigo_players,
					elche_players,
					espanyol_players,
					getafe_players,
					granada_players,
					levante_players,
					mallorca_players,
					osasuna_players,
					rayo_vallecano_players,
					real_betis_players,
					real_madrid_players,
					real_sociedad_players,
					sevilla_players,
					valencia_players,
					villareal_players
					], ignore_index=True)




####################################### 4. SERIE A ##############################################







####### AC MILAN  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"489","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3', 'data4', 'data5']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
ac_milan_players1 = pd.DataFrame()

ac_milan_players1['name'] = df_p1['name']
ac_milan_players1['first_name'] = df_p1['firstname']
ac_milan_players1['last_name'] = df_p1['lastname']
ac_milan_players1['id'] = df_p1['id']
ac_milan_players1['team'] = player_team['name']
ac_milan_players1['team_id'] = player_team['id']
ac_milan_players1['league'] = player_league['name']
ac_milan_players1['league_id'] = player_league['id']
ac_milan_players1['age'] = df_p1['age']
ac_milan_players1['birth'] = player_birth['date']
ac_milan_players1['nationality'] = df_p1['nationality']
ac_milan_players1['app'] = player_games['appearences']
ac_milan_players1['mins'] = player_games['minutes']
ac_milan_players1['goals'] = player_goals['total']
ac_milan_players1['shots'] = player_shots['total']
ac_milan_players1['shots_on_target'] = player_shots['on']
ac_milan_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
ac_milan_players1['assists'] = player_goals['assists']
ac_milan_players1['passes'] = player_passes['total']
ac_milan_players1['passes_completed'] = player_passes['accuracy']
# ac_milan_players1['pass_accuracy_%'] = df_p1['name']
ac_milan_players1['dribbles'] = player_dribbles['attempts']
ac_milan_players1['dribbles_completed'] = player_dribbles['success']
ac_milan_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
ac_milan_players1['tackles'] = player_tackles['total']
ac_milan_players1['blocks'] = player_tackles['blocks']
ac_milan_players1['interceptions'] = player_tackles['interceptions']
ac_milan_players1['fouls_drawn'] = player_fouls['drawn']
ac_milan_players1['fouls_committed'] = player_fouls['committed']
ac_milan_players1['yellow_cards'] = player_cards['yellow']
ac_milan_players1['red_cards'] = player_cards['red']
ac_milan_players1['yellow_to_red_cards'] = player_cards['yellowred']
ac_milan_players1['sub_in'] = player_subs['in']
ac_milan_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
ac_milan_players1 = ac_milan_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"489","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3', 'data4', 'data5']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
ac_milan_players2 = pd.DataFrame()

ac_milan_players2['name'] = df_p1['name']
ac_milan_players2['first_name'] = df_p1['firstname']
ac_milan_players2['last_name'] = df_p1['lastname']
ac_milan_players2['id'] = df_p1['id']
ac_milan_players2['team'] = player_team['name']
ac_milan_players2['team_id'] = player_team['id']
ac_milan_players2['league'] = player_league['name']
ac_milan_players2['league_id'] = player_league['id']
ac_milan_players2['age'] = df_p1['age']
ac_milan_players2['birth'] = player_birth['date']
ac_milan_players2['nationality'] = df_p1['nationality']
ac_milan_players2['app'] = player_games['appearences']
ac_milan_players2['mins'] = player_games['minutes']
ac_milan_players2['goals'] = player_goals['total']
ac_milan_players2['shots'] = player_shots['total']
ac_milan_players2['shots_on_target'] = player_shots['on']
ac_milan_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
ac_milan_players2['assists'] = player_goals['assists']
ac_milan_players2['passes'] = player_passes['total']
ac_milan_players2['passes_completed'] = player_passes['accuracy']
# ac_milan_players2['pass_accuracy_%'] = df_p1['name']
ac_milan_players2['dribbles'] = player_dribbles['attempts']
ac_milan_players2['dribbles_completed'] = player_dribbles['success']
ac_milan_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
ac_milan_players2['tackles'] = player_tackles['total']
ac_milan_players2['blocks'] = player_tackles['blocks']
ac_milan_players2['interceptions'] = player_tackles['interceptions']
ac_milan_players2['fouls_drawn'] = player_fouls['drawn']
ac_milan_players2['fouls_committed'] = player_fouls['committed']
ac_milan_players2['yellow_cards'] = player_cards['yellow']
ac_milan_players2['red_cards'] = player_cards['red']
ac_milan_players2['yellow_to_red_cards'] = player_cards['yellowred']
ac_milan_players2['sub_in'] = player_subs['in']
ac_milan_players2['sub_out'] = player_subs['out']

ac_milan_players2 = ac_milan_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
ac_milan_players = pd.concat([ac_milan_players1, ac_milan_players2])
ac_milan_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### AS ROMA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"497","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
roma_players1 = pd.DataFrame()

roma_players1['name'] = df_p1['name']
roma_players1['first_name'] = df_p1['firstname']
roma_players1['last_name'] = df_p1['lastname']
roma_players1['id'] = df_p1['id']
roma_players1['team'] = player_team['name']
roma_players1['team_id'] = player_team['id']
roma_players1['league'] = player_league['name']
roma_players1['league_id'] = player_league['id']
roma_players1['age'] = df_p1['age']
roma_players1['birth'] = player_birth['date']
roma_players1['nationality'] = df_p1['nationality']
roma_players1['app'] = player_games['appearences']
roma_players1['mins'] = player_games['minutes']
roma_players1['goals'] = player_goals['total']
roma_players1['shots'] = player_shots['total']
roma_players1['shots_on_target'] = player_shots['on']
roma_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
roma_players1['assists'] = player_goals['assists']
roma_players1['passes'] = player_passes['total']
roma_players1['passes_completed'] = player_passes['accuracy']
# roma_players1['pass_accuracy_%'] = df_p1['name']
roma_players1['dribbles'] = player_dribbles['attempts']
roma_players1['dribbles_completed'] = player_dribbles['success']
roma_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
roma_players1['tackles'] = player_tackles['total']
roma_players1['blocks'] = player_tackles['blocks']
roma_players1['interceptions'] = player_tackles['interceptions']
roma_players1['fouls_drawn'] = player_fouls['drawn']
roma_players1['fouls_committed'] = player_fouls['committed']
roma_players1['yellow_cards'] = player_cards['yellow']
roma_players1['red_cards'] = player_cards['red']
roma_players1['yellow_to_red_cards'] = player_cards['yellowred']
roma_players1['sub_in'] = player_subs['in']
roma_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
roma_players1 = roma_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"497","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns =['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
roma_players2 = pd.DataFrame()

roma_players2['name'] = df_p1['name']
roma_players2['first_name'] = df_p1['firstname']
roma_players2['last_name'] = df_p1['lastname']
roma_players2['id'] = df_p1['id']
roma_players2['team'] = player_team['name']
roma_players2['team_id'] = player_team['id']
roma_players2['league'] = player_league['name']
roma_players2['league_id'] = player_league['id']
roma_players2['age'] = df_p1['age']
roma_players2['birth'] = player_birth['date']
roma_players2['nationality'] = df_p1['nationality']
roma_players2['app'] = player_games['appearences']
roma_players2['mins'] = player_games['minutes']
roma_players2['goals'] = player_goals['total']
roma_players2['shots'] = player_shots['total']
roma_players2['shots_on_target'] = player_shots['on']
roma_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
roma_players2['assists'] = player_goals['assists']
roma_players2['passes'] = player_passes['total']
roma_players2['passes_completed'] = player_passes['accuracy']
# roma_players2['pass_accuracy_%'] = df_p1['name']
roma_players2['dribbles'] = player_dribbles['attempts']
roma_players2['dribbles_completed'] = player_dribbles['success']
roma_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
roma_players2['tackles'] = player_tackles['total']
roma_players2['blocks'] = player_tackles['blocks']
roma_players2['interceptions'] = player_tackles['interceptions']
roma_players2['fouls_drawn'] = player_fouls['drawn']
roma_players2['fouls_committed'] = player_fouls['committed']
roma_players2['yellow_cards'] = player_cards['yellow']
roma_players2['red_cards'] = player_cards['red']
roma_players2['yellow_to_red_cards'] = player_cards['yellowred']
roma_players2['sub_in'] = player_subs['in']
roma_players2['sub_out'] = player_subs['out']

roma_players2 = roma_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
roma_players = pd.concat([roma_players1, roma_players2])
roma_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### ATALANTA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"499","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns =['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
atalanta_players1 = pd.DataFrame()

atalanta_players1['name'] = df_p1['name']
atalanta_players1['first_name'] = df_p1['firstname']
atalanta_players1['last_name'] = df_p1['lastname']
atalanta_players1['id'] = df_p1['id']
atalanta_players1['team'] = player_team['name']
atalanta_players1['team_id'] = player_team['id']
atalanta_players1['league'] = player_league['name']
atalanta_players1['league_id'] = player_league['id']
atalanta_players1['age'] = df_p1['age']
atalanta_players1['birth'] = player_birth['date']
atalanta_players1['nationality'] = df_p1['nationality']
atalanta_players1['app'] = player_games['appearences']
atalanta_players1['mins'] = player_games['minutes']
atalanta_players1['goals'] = player_goals['total']
atalanta_players1['shots'] = player_shots['total']
atalanta_players1['shots_on_target'] = player_shots['on']
atalanta_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
atalanta_players1['assists'] = player_goals['assists']
atalanta_players1['passes'] = player_passes['total']
atalanta_players1['passes_completed'] = player_passes['accuracy']
# atalanta_players1['pass_accuracy_%'] = df_p1['name']
atalanta_players1['dribbles'] = player_dribbles['attempts']
atalanta_players1['dribbles_completed'] = player_dribbles['success']
atalanta_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
atalanta_players1['tackles'] = player_tackles['total']
atalanta_players1['blocks'] = player_tackles['blocks']
atalanta_players1['interceptions'] = player_tackles['interceptions']
atalanta_players1['fouls_drawn'] = player_fouls['drawn']
atalanta_players1['fouls_committed'] = player_fouls['committed']
atalanta_players1['yellow_cards'] = player_cards['yellow']
atalanta_players1['red_cards'] = player_cards['red']
atalanta_players1['yellow_to_red_cards'] = player_cards['yellowred']
atalanta_players1['sub_in'] = player_subs['in']
atalanta_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
atalanta_players1 = atalanta_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"499","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns =['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
atalanta_players2 = pd.DataFrame()

atalanta_players2['name'] = df_p1['name']
atalanta_players2['first_name'] = df_p1['firstname']
atalanta_players2['last_name'] = df_p1['lastname']
atalanta_players2['id'] = df_p1['id']
atalanta_players2['team'] = player_team['name']
atalanta_players2['team_id'] = player_team['id']
atalanta_players2['league'] = player_league['name']
atalanta_players2['league_id'] = player_league['id']
atalanta_players2['age'] = df_p1['age']
atalanta_players2['birth'] = player_birth['date']
atalanta_players2['nationality'] = df_p1['nationality']
atalanta_players2['app'] = player_games['appearences']
atalanta_players2['mins'] = player_games['minutes']
atalanta_players2['goals'] = player_goals['total']
atalanta_players2['shots'] = player_shots['total']
atalanta_players2['shots_on_target'] = player_shots['on']
atalanta_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
atalanta_players2['assists'] = player_goals['assists']
atalanta_players2['passes'] = player_passes['total']
atalanta_players2['passes_completed'] = player_passes['accuracy']
# atalanta_players2['pass_accuracy_%'] = df_p1['name']
atalanta_players2['dribbles'] = player_dribbles['attempts']
atalanta_players2['dribbles_completed'] = player_dribbles['success']
atalanta_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
atalanta_players2['tackles'] = player_tackles['total']
atalanta_players2['blocks'] = player_tackles['blocks']
atalanta_players2['interceptions'] = player_tackles['interceptions']
atalanta_players2['fouls_drawn'] = player_fouls['drawn']
atalanta_players2['fouls_committed'] = player_fouls['committed']
atalanta_players2['yellow_cards'] = player_cards['yellow']
atalanta_players2['red_cards'] = player_cards['red']
atalanta_players2['yellow_to_red_cards'] = player_cards['yellowred']
atalanta_players2['sub_in'] = player_subs['in']
atalanta_players2['sub_out'] = player_subs['out']

atalanta_players2 = atalanta_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
atalanta_players = pd.concat([atalanta_players1, atalanta_players2])
atalanta_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column







####### BOLOGNA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"500","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns =['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
bologna_players1 = pd.DataFrame()

bologna_players1['name'] = df_p1['name']
bologna_players1['first_name'] = df_p1['firstname']
bologna_players1['last_name'] = df_p1['lastname']
bologna_players1['id'] = df_p1['id']
bologna_players1['team'] = player_team['name']
bologna_players1['team_id'] = player_team['id']
bologna_players1['league'] = player_league['name']
bologna_players1['league_id'] = player_league['id']
bologna_players1['age'] = df_p1['age']
bologna_players1['birth'] = player_birth['date']
bologna_players1['nationality'] = df_p1['nationality']
bologna_players1['app'] = player_games['appearences']
bologna_players1['mins'] = player_games['minutes']
bologna_players1['goals'] = player_goals['total']
bologna_players1['shots'] = player_shots['total']
bologna_players1['shots_on_target'] = player_shots['on']
bologna_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
bologna_players1['assists'] = player_goals['assists']
bologna_players1['passes'] = player_passes['total']
bologna_players1['passes_completed'] = player_passes['accuracy']
# bologna_players1['pass_accuracy_%'] = df_p1['name']
bologna_players1['dribbles'] = player_dribbles['attempts']
bologna_players1['dribbles_completed'] = player_dribbles['success']
bologna_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
bologna_players1['tackles'] = player_tackles['total']
bologna_players1['blocks'] = player_tackles['blocks']
bologna_players1['interceptions'] = player_tackles['interceptions']
bologna_players1['fouls_drawn'] = player_fouls['drawn']
bologna_players1['fouls_committed'] = player_fouls['committed']
bologna_players1['yellow_cards'] = player_cards['yellow']
bologna_players1['red_cards'] = player_cards['red']
bologna_players1['yellow_to_red_cards'] = player_cards['yellowred']
bologna_players1['sub_in'] = player_subs['in']
bologna_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
bologna_players1 = bologna_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"500","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns =['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
bologna_players2 = pd.DataFrame()

bologna_players2['name'] = df_p1['name']
bologna_players2['first_name'] = df_p1['firstname']
bologna_players2['last_name'] = df_p1['lastname']
bologna_players2['id'] = df_p1['id']
bologna_players2['team'] = player_team['name']
bologna_players2['team_id'] = player_team['id']
bologna_players2['league'] = player_league['name']
bologna_players2['league_id'] = player_league['id']
bologna_players2['age'] = df_p1['age']
bologna_players2['birth'] = player_birth['date']
bologna_players2['nationality'] = df_p1['nationality']
bologna_players2['app'] = player_games['appearences']
bologna_players2['mins'] = player_games['minutes']
bologna_players2['goals'] = player_goals['total']
bologna_players2['shots'] = player_shots['total']
bologna_players2['shots_on_target'] = player_shots['on']
bologna_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
bologna_players2['assists'] = player_goals['assists']
bologna_players2['passes'] = player_passes['total']
bologna_players2['passes_completed'] = player_passes['accuracy']
# bologna_players2['pass_accuracy_%'] = df_p1['name']
bologna_players2['dribbles'] = player_dribbles['attempts']
bologna_players2['dribbles_completed'] = player_dribbles['success']
bologna_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
bologna_players2['tackles'] = player_tackles['total']
bologna_players2['blocks'] = player_tackles['blocks']
bologna_players2['interceptions'] = player_tackles['interceptions']
bologna_players2['fouls_drawn'] = player_fouls['drawn']
bologna_players2['fouls_committed'] = player_fouls['committed']
bologna_players2['yellow_cards'] = player_cards['yellow']
bologna_players2['red_cards'] = player_cards['red']
bologna_players2['yellow_to_red_cards'] = player_cards['yellowred']
bologna_players2['sub_in'] = player_subs['in']
bologna_players2['sub_out'] = player_subs['out']

bologna_players2 = bologna_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
bologna_players = pd.concat([bologna_players1, bologna_players2])
bologna_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### CAGLIARI  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"490","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
cagliari_players1 = pd.DataFrame()

cagliari_players1['name'] = df_p1['name']
cagliari_players1['first_name'] = df_p1['firstname']
cagliari_players1['last_name'] = df_p1['lastname']
cagliari_players1['id'] = df_p1['id']
cagliari_players1['team'] = player_team['name']
cagliari_players1['team_id'] = player_team['id']
cagliari_players1['league'] = player_league['name']
cagliari_players1['league_id'] = player_league['id']
cagliari_players1['age'] = df_p1['age']
cagliari_players1['birth'] = player_birth['date']
cagliari_players1['nationality'] = df_p1['nationality']
cagliari_players1['app'] = player_games['appearences']
cagliari_players1['mins'] = player_games['minutes']
cagliari_players1['goals'] = player_goals['total']
cagliari_players1['shots'] = player_shots['total']
cagliari_players1['shots_on_target'] = player_shots['on']
cagliari_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
cagliari_players1['assists'] = player_goals['assists']
cagliari_players1['passes'] = player_passes['total']
cagliari_players1['passes_completed'] = player_passes['accuracy']
# cagliari_players1['pass_accuracy_%'] = df_p1['name']
cagliari_players1['dribbles'] = player_dribbles['attempts']
cagliari_players1['dribbles_completed'] = player_dribbles['success']
cagliari_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
cagliari_players1['tackles'] = player_tackles['total']
cagliari_players1['blocks'] = player_tackles['blocks']
cagliari_players1['interceptions'] = player_tackles['interceptions']
cagliari_players1['fouls_drawn'] = player_fouls['drawn']
cagliari_players1['fouls_committed'] = player_fouls['committed']
cagliari_players1['yellow_cards'] = player_cards['yellow']
cagliari_players1['red_cards'] = player_cards['red']
cagliari_players1['yellow_to_red_cards'] = player_cards['yellowred']
cagliari_players1['sub_in'] = player_subs['in']
cagliari_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
cagliari_players1 = cagliari_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"490","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
cagliari_players2 = pd.DataFrame()

cagliari_players2['name'] = df_p1['name']
cagliari_players2['first_name'] = df_p1['firstname']
cagliari_players2['last_name'] = df_p1['lastname']
cagliari_players2['id'] = df_p1['id']
cagliari_players2['team'] = player_team['name']
cagliari_players2['team_id'] = player_team['id']
cagliari_players2['league'] = player_league['name']
cagliari_players2['league_id'] = player_league['id']
cagliari_players2['age'] = df_p1['age']
cagliari_players2['birth'] = player_birth['date']
cagliari_players2['nationality'] = df_p1['nationality']
cagliari_players2['app'] = player_games['appearences']
cagliari_players2['mins'] = player_games['minutes']
cagliari_players2['goals'] = player_goals['total']
cagliari_players2['shots'] = player_shots['total']
cagliari_players2['shots_on_target'] = player_shots['on']
cagliari_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
cagliari_players2['assists'] = player_goals['assists']
cagliari_players2['passes'] = player_passes['total']
cagliari_players2['passes_completed'] = player_passes['accuracy']
# cagliari_players2['pass_accuracy_%'] = df_p1['name']
cagliari_players2['dribbles'] = player_dribbles['attempts']
cagliari_players2['dribbles_completed'] = player_dribbles['success']
cagliari_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
cagliari_players2['tackles'] = player_tackles['total']
cagliari_players2['blocks'] = player_tackles['blocks']
cagliari_players2['interceptions'] = player_tackles['interceptions']
cagliari_players2['fouls_drawn'] = player_fouls['drawn']
cagliari_players2['fouls_committed'] = player_fouls['committed']
cagliari_players2['yellow_cards'] = player_cards['yellow']
cagliari_players2['red_cards'] = player_cards['red']
cagliari_players2['yellow_to_red_cards'] = player_cards['yellowred']
cagliari_players2['sub_in'] = player_subs['in']
cagliari_players2['sub_out'] = player_subs['out']

cagliari_players2 = cagliari_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
cagliari_players = pd.concat([cagliari_players1, cagliari_players2])
cagliari_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### EMPOLI  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"511","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
empoli_players1 = pd.DataFrame()

empoli_players1['name'] = df_p1['name']
empoli_players1['first_name'] = df_p1['firstname']
empoli_players1['last_name'] = df_p1['lastname']
empoli_players1['id'] = df_p1['id']
empoli_players1['team'] = player_team['name']
empoli_players1['team_id'] = player_team['id']
empoli_players1['league'] = player_league['name']
empoli_players1['league_id'] = player_league['id']
empoli_players1['age'] = df_p1['age']
empoli_players1['birth'] = player_birth['date']
empoli_players1['nationality'] = df_p1['nationality']
empoli_players1['app'] = player_games['appearences']
empoli_players1['mins'] = player_games['minutes']
empoli_players1['goals'] = player_goals['total']
empoli_players1['shots'] = player_shots['total']
empoli_players1['shots_on_target'] = player_shots['on']
empoli_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
empoli_players1['assists'] = player_goals['assists']
empoli_players1['passes'] = player_passes['total']
empoli_players1['passes_completed'] = player_passes['accuracy']
# empoli_players1['pass_accuracy_%'] = df_p1['name']
empoli_players1['dribbles'] = player_dribbles['attempts']
empoli_players1['dribbles_completed'] = player_dribbles['success']
empoli_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
empoli_players1['tackles'] = player_tackles['total']
empoli_players1['blocks'] = player_tackles['blocks']
empoli_players1['interceptions'] = player_tackles['interceptions']
empoli_players1['fouls_drawn'] = player_fouls['drawn']
empoli_players1['fouls_committed'] = player_fouls['committed']
empoli_players1['yellow_cards'] = player_cards['yellow']
empoli_players1['red_cards'] = player_cards['red']
empoli_players1['yellow_to_red_cards'] = player_cards['yellowred']
empoli_players1['sub_in'] = player_subs['in']
empoli_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
empoli_players1 = empoli_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"511","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
empoli_players2 = pd.DataFrame()

empoli_players2['name'] = df_p1['name']
empoli_players2['first_name'] = df_p1['firstname']
empoli_players2['last_name'] = df_p1['lastname']
empoli_players2['id'] = df_p1['id']
empoli_players2['team'] = player_team['name']
empoli_players2['team_id'] = player_team['id']
empoli_players2['league'] = player_league['name']
empoli_players2['league_id'] = player_league['id']
empoli_players2['age'] = df_p1['age']
empoli_players2['birth'] = player_birth['date']
empoli_players2['nationality'] = df_p1['nationality']
empoli_players2['app'] = player_games['appearences']
empoli_players2['mins'] = player_games['minutes']
empoli_players2['goals'] = player_goals['total']
empoli_players2['shots'] = player_shots['total']
empoli_players2['shots_on_target'] = player_shots['on']
empoli_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
empoli_players2['assists'] = player_goals['assists']
empoli_players2['passes'] = player_passes['total']
empoli_players2['passes_completed'] = player_passes['accuracy']
# empoli_players2['pass_accuracy_%'] = df_p1['name']
empoli_players2['dribbles'] = player_dribbles['attempts']
empoli_players2['dribbles_completed'] = player_dribbles['success']
empoli_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
empoli_players2['tackles'] = player_tackles['total']
empoli_players2['blocks'] = player_tackles['blocks']
empoli_players2['interceptions'] = player_tackles['interceptions']
empoli_players2['fouls_drawn'] = player_fouls['drawn']
empoli_players2['fouls_committed'] = player_fouls['committed']
empoli_players2['yellow_cards'] = player_cards['yellow']
empoli_players2['red_cards'] = player_cards['red']
empoli_players2['yellow_to_red_cards'] = player_cards['yellowred']
empoli_players2['sub_in'] = player_subs['in']
empoli_players2['sub_out'] = player_subs['out']

empoli_players2 = empoli_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
empoli_players = pd.concat([empoli_players1, empoli_players2])
empoli_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### FIORENTINA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"502","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
fiorentina_players1 = pd.DataFrame()

fiorentina_players1['name'] = df_p1['name']
fiorentina_players1['first_name'] = df_p1['firstname']
fiorentina_players1['last_name'] = df_p1['lastname']
fiorentina_players1['id'] = df_p1['id']
fiorentina_players1['team'] = player_team['name']
fiorentina_players1['team_id'] = player_team['id']
fiorentina_players1['league'] = player_league['name']
fiorentina_players1['league_id'] = player_league['id']
fiorentina_players1['age'] = df_p1['age']
fiorentina_players1['birth'] = player_birth['date']
fiorentina_players1['nationality'] = df_p1['nationality']
fiorentina_players1['app'] = player_games['appearences']
fiorentina_players1['mins'] = player_games['minutes']
fiorentina_players1['goals'] = player_goals['total']
fiorentina_players1['shots'] = player_shots['total']
fiorentina_players1['shots_on_target'] = player_shots['on']
fiorentina_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
fiorentina_players1['assists'] = player_goals['assists']
fiorentina_players1['passes'] = player_passes['total']
fiorentina_players1['passes_completed'] = player_passes['accuracy']
# fiorentina_players1['pass_accuracy_%'] = df_p1['name']
fiorentina_players1['dribbles'] = player_dribbles['attempts']
fiorentina_players1['dribbles_completed'] = player_dribbles['success']
fiorentina_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
fiorentina_players1['tackles'] = player_tackles['total']
fiorentina_players1['blocks'] = player_tackles['blocks']
fiorentina_players1['interceptions'] = player_tackles['interceptions']
fiorentina_players1['fouls_drawn'] = player_fouls['drawn']
fiorentina_players1['fouls_committed'] = player_fouls['committed']
fiorentina_players1['yellow_cards'] = player_cards['yellow']
fiorentina_players1['red_cards'] = player_cards['red']
fiorentina_players1['yellow_to_red_cards'] = player_cards['yellowred']
fiorentina_players1['sub_in'] = player_subs['in']
fiorentina_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
fiorentina_players1 = fiorentina_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"502","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
fiorentina_players2 = pd.DataFrame()

fiorentina_players2['name'] = df_p1['name']
fiorentina_players2['first_name'] = df_p1['firstname']
fiorentina_players2['last_name'] = df_p1['lastname']
fiorentina_players2['id'] = df_p1['id']
fiorentina_players2['team'] = player_team['name']
fiorentina_players2['team_id'] = player_team['id']
fiorentina_players2['league'] = player_league['name']
fiorentina_players2['league_id'] = player_league['id']
fiorentina_players2['age'] = df_p1['age']
fiorentina_players2['birth'] = player_birth['date']
fiorentina_players2['nationality'] = df_p1['nationality']
fiorentina_players2['app'] = player_games['appearences']
fiorentina_players2['mins'] = player_games['minutes']
fiorentina_players2['goals'] = player_goals['total']
fiorentina_players2['shots'] = player_shots['total']
fiorentina_players2['shots_on_target'] = player_shots['on']
fiorentina_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
fiorentina_players2['assists'] = player_goals['assists']
fiorentina_players2['passes'] = player_passes['total']
fiorentina_players2['passes_completed'] = player_passes['accuracy']
# fiorentina_players2['pass_accuracy_%'] = df_p1['name']
fiorentina_players2['dribbles'] = player_dribbles['attempts']
fiorentina_players2['dribbles_completed'] = player_dribbles['success']
fiorentina_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
fiorentina_players2['tackles'] = player_tackles['total']
fiorentina_players2['blocks'] = player_tackles['blocks']
fiorentina_players2['interceptions'] = player_tackles['interceptions']
fiorentina_players2['fouls_drawn'] = player_fouls['drawn']
fiorentina_players2['fouls_committed'] = player_fouls['committed']
fiorentina_players2['yellow_cards'] = player_cards['yellow']
fiorentina_players2['red_cards'] = player_cards['red']
fiorentina_players2['yellow_to_red_cards'] = player_cards['yellowred']
fiorentina_players2['sub_in'] = player_subs['in']
fiorentina_players2['sub_out'] = player_subs['out']

fiorentina_players2 = fiorentina_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
fiorentina_players = pd.concat([fiorentina_players1, fiorentina_players2])
fiorentina_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### GENOA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"495","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
genoa_players1 = pd.DataFrame()

genoa_players1['name'] = df_p1['name']
genoa_players1['first_name'] = df_p1['firstname']
genoa_players1['last_name'] = df_p1['lastname']
genoa_players1['id'] = df_p1['id']
genoa_players1['team'] = player_team['name']
genoa_players1['team_id'] = player_team['id']
genoa_players1['league'] = player_league['name']
genoa_players1['league_id'] = player_league['id']
genoa_players1['age'] = df_p1['age']
genoa_players1['birth'] = player_birth['date']
genoa_players1['nationality'] = df_p1['nationality']
genoa_players1['app'] = player_games['appearences']
genoa_players1['mins'] = player_games['minutes']
genoa_players1['goals'] = player_goals['total']
genoa_players1['shots'] = player_shots['total']
genoa_players1['shots_on_target'] = player_shots['on']
genoa_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
genoa_players1['assists'] = player_goals['assists']
genoa_players1['passes'] = player_passes['total']
genoa_players1['passes_completed'] = player_passes['accuracy']
# genoa_players1['pass_accuracy_%'] = df_p1['name']
genoa_players1['dribbles'] = player_dribbles['attempts']
genoa_players1['dribbles_completed'] = player_dribbles['success']
genoa_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
genoa_players1['tackles'] = player_tackles['total']
genoa_players1['blocks'] = player_tackles['blocks']
genoa_players1['interceptions'] = player_tackles['interceptions']
genoa_players1['fouls_drawn'] = player_fouls['drawn']
genoa_players1['fouls_committed'] = player_fouls['committed']
genoa_players1['yellow_cards'] = player_cards['yellow']
genoa_players1['red_cards'] = player_cards['red']
genoa_players1['yellow_to_red_cards'] = player_cards['yellowred']
genoa_players1['sub_in'] = player_subs['in']
genoa_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
genoa_players1 = genoa_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"495","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
genoa_players2 = pd.DataFrame()

genoa_players2['name'] = df_p1['name']
genoa_players2['first_name'] = df_p1['firstname']
genoa_players2['last_name'] = df_p1['lastname']
genoa_players2['id'] = df_p1['id']
genoa_players2['team'] = player_team['name']
genoa_players2['team_id'] = player_team['id']
genoa_players2['league'] = player_league['name']
genoa_players2['league_id'] = player_league['id']
genoa_players2['age'] = df_p1['age']
genoa_players2['birth'] = player_birth['date']
genoa_players2['nationality'] = df_p1['nationality']
genoa_players2['app'] = player_games['appearences']
genoa_players2['mins'] = player_games['minutes']
genoa_players2['goals'] = player_goals['total']
genoa_players2['shots'] = player_shots['total']
genoa_players2['shots_on_target'] = player_shots['on']
genoa_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
genoa_players2['assists'] = player_goals['assists']
genoa_players2['passes'] = player_passes['total']
genoa_players2['passes_completed'] = player_passes['accuracy']
# genoa_players2['pass_accuracy_%'] = df_p1['name']
genoa_players2['dribbles'] = player_dribbles['attempts']
genoa_players2['dribbles_completed'] = player_dribbles['success']
genoa_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
genoa_players2['tackles'] = player_tackles['total']
genoa_players2['blocks'] = player_tackles['blocks']
genoa_players2['interceptions'] = player_tackles['interceptions']
genoa_players2['fouls_drawn'] = player_fouls['drawn']
genoa_players2['fouls_committed'] = player_fouls['committed']
genoa_players2['yellow_cards'] = player_cards['yellow']
genoa_players2['red_cards'] = player_cards['red']
genoa_players2['yellow_to_red_cards'] = player_cards['yellowred']
genoa_players2['sub_in'] = player_subs['in']
genoa_players2['sub_out'] = player_subs['out']

genoa_players2 = genoa_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
genoa_players = pd.concat([genoa_players1, genoa_players2])
genoa_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column









####### INTER MILAN  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"505","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3', 'data4', 'data5']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
inter_milan_players1 = pd.DataFrame()

inter_milan_players1['name'] = df_p1['name']
inter_milan_players1['first_name'] = df_p1['firstname']
inter_milan_players1['last_name'] = df_p1['lastname']
inter_milan_players1['id'] = df_p1['id']
inter_milan_players1['team'] = player_team['name']
inter_milan_players1['team_id'] = player_team['id']
inter_milan_players1['league'] = player_league['name']
inter_milan_players1['league_id'] = player_league['id']
inter_milan_players1['age'] = df_p1['age']
inter_milan_players1['birth'] = player_birth['date']
inter_milan_players1['nationality'] = df_p1['nationality']
inter_milan_players1['app'] = player_games['appearences']
inter_milan_players1['mins'] = player_games['minutes']
inter_milan_players1['goals'] = player_goals['total']
inter_milan_players1['shots'] = player_shots['total']
inter_milan_players1['shots_on_target'] = player_shots['on']
inter_milan_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
inter_milan_players1['assists'] = player_goals['assists']
inter_milan_players1['passes'] = player_passes['total']
inter_milan_players1['passes_completed'] = player_passes['accuracy']
# inter_milan_players1['pass_accuracy_%'] = df_p1['name']
inter_milan_players1['dribbles'] = player_dribbles['attempts']
inter_milan_players1['dribbles_completed'] = player_dribbles['success']
inter_milan_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
inter_milan_players1['tackles'] = player_tackles['total']
inter_milan_players1['blocks'] = player_tackles['blocks']
inter_milan_players1['interceptions'] = player_tackles['interceptions']
inter_milan_players1['fouls_drawn'] = player_fouls['drawn']
inter_milan_players1['fouls_committed'] = player_fouls['committed']
inter_milan_players1['yellow_cards'] = player_cards['yellow']
inter_milan_players1['red_cards'] = player_cards['red']
inter_milan_players1['yellow_to_red_cards'] = player_cards['yellowred']
inter_milan_players1['sub_in'] = player_subs['in']
inter_milan_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
inter_milan_players1 = inter_milan_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"505","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
inter_milan_players2 = pd.DataFrame()

inter_milan_players2['name'] = df_p1['name']
inter_milan_players2['first_name'] = df_p1['firstname']
inter_milan_players2['last_name'] = df_p1['lastname']
inter_milan_players2['id'] = df_p1['id']
inter_milan_players2['team'] = player_team['name']
inter_milan_players2['team_id'] = player_team['id']
inter_milan_players2['league'] = player_league['name']
inter_milan_players2['league_id'] = player_league['id']
inter_milan_players2['age'] = df_p1['age']
inter_milan_players2['birth'] = player_birth['date']
inter_milan_players2['nationality'] = df_p1['nationality']
inter_milan_players2['app'] = player_games['appearences']
inter_milan_players2['mins'] = player_games['minutes']
inter_milan_players2['goals'] = player_goals['total']
inter_milan_players2['shots'] = player_shots['total']
inter_milan_players2['shots_on_target'] = player_shots['on']
inter_milan_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
inter_milan_players2['assists'] = player_goals['assists']
inter_milan_players2['passes'] = player_passes['total']
inter_milan_players2['passes_completed'] = player_passes['accuracy']
# inter_milan_players2['pass_accuracy_%'] = df_p1['name']
inter_milan_players2['dribbles'] = player_dribbles['attempts']
inter_milan_players2['dribbles_completed'] = player_dribbles['success']
inter_milan_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
inter_milan_players2['tackles'] = player_tackles['total']
inter_milan_players2['blocks'] = player_tackles['blocks']
inter_milan_players2['interceptions'] = player_tackles['interceptions']
inter_milan_players2['fouls_drawn'] = player_fouls['drawn']
inter_milan_players2['fouls_committed'] = player_fouls['committed']
inter_milan_players2['yellow_cards'] = player_cards['yellow']
inter_milan_players2['red_cards'] = player_cards['red']
inter_milan_players2['yellow_to_red_cards'] = player_cards['yellowred']
inter_milan_players2['sub_in'] = player_subs['in']
inter_milan_players2['sub_out'] = player_subs['out']

inter_milan_players2 = inter_milan_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
inter_milan_players = pd.concat([inter_milan_players1, inter_milan_players2])
inter_milan_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### JUVENTUS  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"496","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
juventus_players1 = pd.DataFrame()

juventus_players1['name'] = df_p1['name']
juventus_players1['first_name'] = df_p1['firstname']
juventus_players1['last_name'] = df_p1['lastname']
juventus_players1['id'] = df_p1['id']
juventus_players1['team'] = player_team['name']
juventus_players1['team_id'] = player_team['id']
juventus_players1['league'] = player_league['name']
juventus_players1['league_id'] = player_league['id']
juventus_players1['age'] = df_p1['age']
juventus_players1['birth'] = player_birth['date']
juventus_players1['nationality'] = df_p1['nationality']
juventus_players1['app'] = player_games['appearences']
juventus_players1['mins'] = player_games['minutes']
juventus_players1['goals'] = player_goals['total']
juventus_players1['shots'] = player_shots['total']
juventus_players1['shots_on_target'] = player_shots['on']
juventus_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
juventus_players1['assists'] = player_goals['assists']
juventus_players1['passes'] = player_passes['total']
juventus_players1['passes_completed'] = player_passes['accuracy']
# juventus_players1['pass_accuracy_%'] = df_p1['name']
juventus_players1['dribbles'] = player_dribbles['attempts']
juventus_players1['dribbles_completed'] = player_dribbles['success']
juventus_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
juventus_players1['tackles'] = player_tackles['total']
juventus_players1['blocks'] = player_tackles['blocks']
juventus_players1['interceptions'] = player_tackles['interceptions']
juventus_players1['fouls_drawn'] = player_fouls['drawn']
juventus_players1['fouls_committed'] = player_fouls['committed']
juventus_players1['yellow_cards'] = player_cards['yellow']
juventus_players1['red_cards'] = player_cards['red']
juventus_players1['yellow_to_red_cards'] = player_cards['yellowred']
juventus_players1['sub_in'] = player_subs['in']
juventus_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
juventus_players1 = juventus_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"496","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
juventus_players2 = pd.DataFrame()

juventus_players2['name'] = df_p1['name']
juventus_players2['first_name'] = df_p1['firstname']
juventus_players2['last_name'] = df_p1['lastname']
juventus_players2['id'] = df_p1['id']
juventus_players2['team'] = player_team['name']
juventus_players2['team_id'] = player_team['id']
juventus_players2['league'] = player_league['name']
juventus_players2['league_id'] = player_league['id']
juventus_players2['age'] = df_p1['age']
juventus_players2['birth'] = player_birth['date']
juventus_players2['nationality'] = df_p1['nationality']
juventus_players2['app'] = player_games['appearences']
juventus_players2['mins'] = player_games['minutes']
juventus_players2['goals'] = player_goals['total']
juventus_players2['shots'] = player_shots['total']
juventus_players2['shots_on_target'] = player_shots['on']
juventus_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
juventus_players2['assists'] = player_goals['assists']
juventus_players2['passes'] = player_passes['total']
juventus_players2['passes_completed'] = player_passes['accuracy']
# juventus_players2['pass_accuracy_%'] = df_p1['name']
juventus_players2['dribbles'] = player_dribbles['attempts']
juventus_players2['dribbles_completed'] = player_dribbles['success']
juventus_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
juventus_players2['tackles'] = player_tackles['total']
juventus_players2['blocks'] = player_tackles['blocks']
juventus_players2['interceptions'] = player_tackles['interceptions']
juventus_players2['fouls_drawn'] = player_fouls['drawn']
juventus_players2['fouls_committed'] = player_fouls['committed']
juventus_players2['yellow_cards'] = player_cards['yellow']
juventus_players2['red_cards'] = player_cards['red']
juventus_players2['yellow_to_red_cards'] = player_cards['yellowred']
juventus_players2['sub_in'] = player_subs['in']
juventus_players2['sub_out'] = player_subs['out']

juventus_players2 = juventus_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
juventus_players = pd.concat([juventus_players1, juventus_players2])
juventus_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column











####### LAZIO  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"487","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
lazio_players1 = pd.DataFrame()

lazio_players1['name'] = df_p1['name']
lazio_players1['first_name'] = df_p1['firstname']
lazio_players1['last_name'] = df_p1['lastname']
lazio_players1['id'] = df_p1['id']
lazio_players1['team'] = player_team['name']
lazio_players1['team_id'] = player_team['id']
lazio_players1['league'] = player_league['name']
lazio_players1['league_id'] = player_league['id']
lazio_players1['age'] = df_p1['age']
lazio_players1['birth'] = player_birth['date']
lazio_players1['nationality'] = df_p1['nationality']
lazio_players1['app'] = player_games['appearences']
lazio_players1['mins'] = player_games['minutes']
lazio_players1['goals'] = player_goals['total']
lazio_players1['shots'] = player_shots['total']
lazio_players1['shots_on_target'] = player_shots['on']
lazio_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
lazio_players1['assists'] = player_goals['assists']
lazio_players1['passes'] = player_passes['total']
lazio_players1['passes_completed'] = player_passes['accuracy']
# lazio_players1['pass_accuracy_%'] = df_p1['name']
lazio_players1['dribbles'] = player_dribbles['attempts']
lazio_players1['dribbles_completed'] = player_dribbles['success']
lazio_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
lazio_players1['tackles'] = player_tackles['total']
lazio_players1['blocks'] = player_tackles['blocks']
lazio_players1['interceptions'] = player_tackles['interceptions']
lazio_players1['fouls_drawn'] = player_fouls['drawn']
lazio_players1['fouls_committed'] = player_fouls['committed']
lazio_players1['yellow_cards'] = player_cards['yellow']
lazio_players1['red_cards'] = player_cards['red']
lazio_players1['yellow_to_red_cards'] = player_cards['yellowred']
lazio_players1['sub_in'] = player_subs['in']
lazio_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
lazio_players1 = lazio_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"487","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3', 'data4']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
lazio_players2 = pd.DataFrame()

lazio_players2['name'] = df_p1['name']
lazio_players2['first_name'] = df_p1['firstname']
lazio_players2['last_name'] = df_p1['lastname']
lazio_players2['id'] = df_p1['id']
lazio_players2['team'] = player_team['name']
lazio_players2['team_id'] = player_team['id']
lazio_players2['league'] = player_league['name']
lazio_players2['league_id'] = player_league['id']
lazio_players2['age'] = df_p1['age']
lazio_players2['birth'] = player_birth['date']
lazio_players2['nationality'] = df_p1['nationality']
lazio_players2['app'] = player_games['appearences']
lazio_players2['mins'] = player_games['minutes']
lazio_players2['goals'] = player_goals['total']
lazio_players2['shots'] = player_shots['total']
lazio_players2['shots_on_target'] = player_shots['on']
lazio_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
lazio_players2['assists'] = player_goals['assists']
lazio_players2['passes'] = player_passes['total']
lazio_players2['passes_completed'] = player_passes['accuracy']
# lazio_players2['pass_accuracy_%'] = df_p1['name']
lazio_players2['dribbles'] = player_dribbles['attempts']
lazio_players2['dribbles_completed'] = player_dribbles['success']
lazio_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
lazio_players2['tackles'] = player_tackles['total']
lazio_players2['blocks'] = player_tackles['blocks']
lazio_players2['interceptions'] = player_tackles['interceptions']
lazio_players2['fouls_drawn'] = player_fouls['drawn']
lazio_players2['fouls_committed'] = player_fouls['committed']
lazio_players2['yellow_cards'] = player_cards['yellow']
lazio_players2['red_cards'] = player_cards['red']
lazio_players2['yellow_to_red_cards'] = player_cards['yellowred']
lazio_players2['sub_in'] = player_subs['in']
lazio_players2['sub_out'] = player_subs['out']

lazio_players2 = lazio_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
lazio_players = pd.concat([lazio_players1, lazio_players2])
lazio_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### NAPOLI  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"492","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3', 'data4']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
napoli_players1 = pd.DataFrame()

napoli_players1['name'] = df_p1['name']
napoli_players1['first_name'] = df_p1['firstname']
napoli_players1['last_name'] = df_p1['lastname']
napoli_players1['id'] = df_p1['id']
napoli_players1['team'] = player_team['name']
napoli_players1['team_id'] = player_team['id']
napoli_players1['league'] = player_league['name']
napoli_players1['league_id'] = player_league['id']
napoli_players1['age'] = df_p1['age']
napoli_players1['birth'] = player_birth['date']
napoli_players1['nationality'] = df_p1['nationality']
napoli_players1['app'] = player_games['appearences']
napoli_players1['mins'] = player_games['minutes']
napoli_players1['goals'] = player_goals['total']
napoli_players1['shots'] = player_shots['total']
napoli_players1['shots_on_target'] = player_shots['on']
napoli_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
napoli_players1['assists'] = player_goals['assists']
napoli_players1['passes'] = player_passes['total']
napoli_players1['passes_completed'] = player_passes['accuracy']
# napoli_players1['pass_accuracy_%'] = df_p1['name']
napoli_players1['dribbles'] = player_dribbles['attempts']
napoli_players1['dribbles_completed'] = player_dribbles['success']
napoli_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
napoli_players1['tackles'] = player_tackles['total']
napoli_players1['blocks'] = player_tackles['blocks']
napoli_players1['interceptions'] = player_tackles['interceptions']
napoli_players1['fouls_drawn'] = player_fouls['drawn']
napoli_players1['fouls_committed'] = player_fouls['committed']
napoli_players1['yellow_cards'] = player_cards['yellow']
napoli_players1['red_cards'] = player_cards['red']
napoli_players1['yellow_to_red_cards'] = player_cards['yellowred']
napoli_players1['sub_in'] = player_subs['in']
napoli_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
napoli_players1 = napoli_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"492","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3', 'data4']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
napoli_players2 = pd.DataFrame()

napoli_players2['name'] = df_p1['name']
napoli_players2['first_name'] = df_p1['firstname']
napoli_players2['last_name'] = df_p1['lastname']
napoli_players2['id'] = df_p1['id']
napoli_players2['team'] = player_team['name']
napoli_players2['team_id'] = player_team['id']
napoli_players2['league'] = player_league['name']
napoli_players2['league_id'] = player_league['id']
napoli_players2['age'] = df_p1['age']
napoli_players2['birth'] = player_birth['date']
napoli_players2['nationality'] = df_p1['nationality']
napoli_players2['app'] = player_games['appearences']
napoli_players2['mins'] = player_games['minutes']
napoli_players2['goals'] = player_goals['total']
napoli_players2['shots'] = player_shots['total']
napoli_players2['shots_on_target'] = player_shots['on']
napoli_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
napoli_players2['assists'] = player_goals['assists']
napoli_players2['passes'] = player_passes['total']
napoli_players2['passes_completed'] = player_passes['accuracy']
# napoli_players2['pass_accuracy_%'] = df_p1['name']
napoli_players2['dribbles'] = player_dribbles['attempts']
napoli_players2['dribbles_completed'] = player_dribbles['success']
napoli_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
napoli_players2['tackles'] = player_tackles['total']
napoli_players2['blocks'] = player_tackles['blocks']
napoli_players2['interceptions'] = player_tackles['interceptions']
napoli_players2['fouls_drawn'] = player_fouls['drawn']
napoli_players2['fouls_committed'] = player_fouls['committed']
napoli_players2['yellow_cards'] = player_cards['yellow']
napoli_players2['red_cards'] = player_cards['red']
napoli_players2['yellow_to_red_cards'] = player_cards['yellowred']
napoli_players2['sub_in'] = player_subs['in']
napoli_players2['sub_out'] = player_subs['out']

napoli_players2 = napoli_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
napoli_players = pd.concat([napoli_players1, napoli_players2])
napoli_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column









####### SALERNITANA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"514","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
salernitana_players1 = pd.DataFrame()

salernitana_players1['name'] = df_p1['name']
salernitana_players1['first_name'] = df_p1['firstname']
salernitana_players1['last_name'] = df_p1['lastname']
salernitana_players1['id'] = df_p1['id']
salernitana_players1['team'] = player_team['name']
salernitana_players1['team_id'] = player_team['id']
salernitana_players1['league'] = player_league['name']
salernitana_players1['league_id'] = player_league['id']
salernitana_players1['age'] = df_p1['age']
salernitana_players1['birth'] = player_birth['date']
salernitana_players1['nationality'] = df_p1['nationality']
salernitana_players1['app'] = player_games['appearences']
salernitana_players1['mins'] = player_games['minutes']
salernitana_players1['goals'] = player_goals['total']
salernitana_players1['shots'] = player_shots['total']
salernitana_players1['shots_on_target'] = player_shots['on']
salernitana_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
salernitana_players1['assists'] = player_goals['assists']
salernitana_players1['passes'] = player_passes['total']
salernitana_players1['passes_completed'] = player_passes['accuracy']
# salernitana_players1['pass_accuracy_%'] = df_p1['name']
salernitana_players1['dribbles'] = player_dribbles['attempts']
salernitana_players1['dribbles_completed'] = player_dribbles['success']
salernitana_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
salernitana_players1['tackles'] = player_tackles['total']
salernitana_players1['blocks'] = player_tackles['blocks']
salernitana_players1['interceptions'] = player_tackles['interceptions']
salernitana_players1['fouls_drawn'] = player_fouls['drawn']
salernitana_players1['fouls_committed'] = player_fouls['committed']
salernitana_players1['yellow_cards'] = player_cards['yellow']
salernitana_players1['red_cards'] = player_cards['red']
salernitana_players1['yellow_to_red_cards'] = player_cards['yellowred']
salernitana_players1['sub_in'] = player_subs['in']
salernitana_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
salernitana_players1 = salernitana_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"514","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
salernitana_players2 = pd.DataFrame()

salernitana_players2['name'] = df_p1['name']
salernitana_players2['first_name'] = df_p1['firstname']
salernitana_players2['last_name'] = df_p1['lastname']
salernitana_players2['id'] = df_p1['id']
salernitana_players2['team'] = player_team['name']
salernitana_players2['team_id'] = player_team['id']
salernitana_players2['league'] = player_league['name']
salernitana_players2['league_id'] = player_league['id']
salernitana_players2['age'] = df_p1['age']
salernitana_players2['birth'] = player_birth['date']
salernitana_players2['nationality'] = df_p1['nationality']
salernitana_players2['app'] = player_games['appearences']
salernitana_players2['mins'] = player_games['minutes']
salernitana_players2['goals'] = player_goals['total']
salernitana_players2['shots'] = player_shots['total']
salernitana_players2['shots_on_target'] = player_shots['on']
salernitana_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
salernitana_players2['assists'] = player_goals['assists']
salernitana_players2['passes'] = player_passes['total']
salernitana_players2['passes_completed'] = player_passes['accuracy']
# salernitana_players2['pass_accuracy_%'] = df_p1['name']
salernitana_players2['dribbles'] = player_dribbles['attempts']
salernitana_players2['dribbles_completed'] = player_dribbles['success']
salernitana_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
salernitana_players2['tackles'] = player_tackles['total']
salernitana_players2['blocks'] = player_tackles['blocks']
salernitana_players2['interceptions'] = player_tackles['interceptions']
salernitana_players2['fouls_drawn'] = player_fouls['drawn']
salernitana_players2['fouls_committed'] = player_fouls['committed']
salernitana_players2['yellow_cards'] = player_cards['yellow']
salernitana_players2['red_cards'] = player_cards['red']
salernitana_players2['yellow_to_red_cards'] = player_cards['yellowred']
salernitana_players2['sub_in'] = player_subs['in']
salernitana_players2['sub_out'] = player_subs['out']

salernitana_players2 = salernitana_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
salernitana_players = pd.concat([salernitana_players1, salernitana_players2])
salernitana_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### SAMPDORIA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"498","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
sampdoria_players1 = pd.DataFrame()

sampdoria_players1['name'] = df_p1['name']
sampdoria_players1['first_name'] = df_p1['firstname']
sampdoria_players1['last_name'] = df_p1['lastname']
sampdoria_players1['id'] = df_p1['id']
sampdoria_players1['team'] = player_team['name']
sampdoria_players1['team_id'] = player_team['id']
sampdoria_players1['league'] = player_league['name']
sampdoria_players1['league_id'] = player_league['id']
sampdoria_players1['age'] = df_p1['age']
sampdoria_players1['birth'] = player_birth['date']
sampdoria_players1['nationality'] = df_p1['nationality']
sampdoria_players1['app'] = player_games['appearences']
sampdoria_players1['mins'] = player_games['minutes']
sampdoria_players1['goals'] = player_goals['total']
sampdoria_players1['shots'] = player_shots['total']
sampdoria_players1['shots_on_target'] = player_shots['on']
sampdoria_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
sampdoria_players1['assists'] = player_goals['assists']
sampdoria_players1['passes'] = player_passes['total']
sampdoria_players1['passes_completed'] = player_passes['accuracy']
# sampdoria_players1['pass_accuracy_%'] = df_p1['name']
sampdoria_players1['dribbles'] = player_dribbles['attempts']
sampdoria_players1['dribbles_completed'] = player_dribbles['success']
sampdoria_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
sampdoria_players1['tackles'] = player_tackles['total']
sampdoria_players1['blocks'] = player_tackles['blocks']
sampdoria_players1['interceptions'] = player_tackles['interceptions']
sampdoria_players1['fouls_drawn'] = player_fouls['drawn']
sampdoria_players1['fouls_committed'] = player_fouls['committed']
sampdoria_players1['yellow_cards'] = player_cards['yellow']
sampdoria_players1['red_cards'] = player_cards['red']
sampdoria_players1['yellow_to_red_cards'] = player_cards['yellowred']
sampdoria_players1['sub_in'] = player_subs['in']
sampdoria_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
sampdoria_players1 = sampdoria_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"498","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
sampdoria_players2 = pd.DataFrame()

sampdoria_players2['name'] = df_p1['name']
sampdoria_players2['first_name'] = df_p1['firstname']
sampdoria_players2['last_name'] = df_p1['lastname']
sampdoria_players2['id'] = df_p1['id']
sampdoria_players2['team'] = player_team['name']
sampdoria_players2['team_id'] = player_team['id']
sampdoria_players2['league'] = player_league['name']
sampdoria_players2['league_id'] = player_league['id']
sampdoria_players2['age'] = df_p1['age']
sampdoria_players2['birth'] = player_birth['date']
sampdoria_players2['nationality'] = df_p1['nationality']
sampdoria_players2['app'] = player_games['appearences']
sampdoria_players2['mins'] = player_games['minutes']
sampdoria_players2['goals'] = player_goals['total']
sampdoria_players2['shots'] = player_shots['total']
sampdoria_players2['shots_on_target'] = player_shots['on']
sampdoria_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
sampdoria_players2['assists'] = player_goals['assists']
sampdoria_players2['passes'] = player_passes['total']
sampdoria_players2['passes_completed'] = player_passes['accuracy']
# sampdoria_players2['pass_accuracy_%'] = df_p1['name']
sampdoria_players2['dribbles'] = player_dribbles['attempts']
sampdoria_players2['dribbles_completed'] = player_dribbles['success']
sampdoria_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
sampdoria_players2['tackles'] = player_tackles['total']
sampdoria_players2['blocks'] = player_tackles['blocks']
sampdoria_players2['interceptions'] = player_tackles['interceptions']
sampdoria_players2['fouls_drawn'] = player_fouls['drawn']
sampdoria_players2['fouls_committed'] = player_fouls['committed']
sampdoria_players2['yellow_cards'] = player_cards['yellow']
sampdoria_players2['red_cards'] = player_cards['red']
sampdoria_players2['yellow_to_red_cards'] = player_cards['yellowred']
sampdoria_players2['sub_in'] = player_subs['in']
sampdoria_players2['sub_out'] = player_subs['out']

sampdoria_players2 = sampdoria_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
sampdoria_players = pd.concat([sampdoria_players1, sampdoria_players2])
sampdoria_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### SASSUOLO  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"488","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
sassuolo_players1 = pd.DataFrame()

sassuolo_players1['name'] = df_p1['name']
sassuolo_players1['first_name'] = df_p1['firstname']
sassuolo_players1['last_name'] = df_p1['lastname']
sassuolo_players1['id'] = df_p1['id']
sassuolo_players1['team'] = player_team['name']
sassuolo_players1['team_id'] = player_team['id']
sassuolo_players1['league'] = player_league['name']
sassuolo_players1['league_id'] = player_league['id']
sassuolo_players1['age'] = df_p1['age']
sassuolo_players1['birth'] = player_birth['date']
sassuolo_players1['nationality'] = df_p1['nationality']
sassuolo_players1['app'] = player_games['appearences']
sassuolo_players1['mins'] = player_games['minutes']
sassuolo_players1['goals'] = player_goals['total']
sassuolo_players1['shots'] = player_shots['total']
sassuolo_players1['shots_on_target'] = player_shots['on']
sassuolo_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
sassuolo_players1['assists'] = player_goals['assists']
sassuolo_players1['passes'] = player_passes['total']
sassuolo_players1['passes_completed'] = player_passes['accuracy']
# sassuolo_players1['pass_accuracy_%'] = df_p1['name']
sassuolo_players1['dribbles'] = player_dribbles['attempts']
sassuolo_players1['dribbles_completed'] = player_dribbles['success']
sassuolo_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
sassuolo_players1['tackles'] = player_tackles['total']
sassuolo_players1['blocks'] = player_tackles['blocks']
sassuolo_players1['interceptions'] = player_tackles['interceptions']
sassuolo_players1['fouls_drawn'] = player_fouls['drawn']
sassuolo_players1['fouls_committed'] = player_fouls['committed']
sassuolo_players1['yellow_cards'] = player_cards['yellow']
sassuolo_players1['red_cards'] = player_cards['red']
sassuolo_players1['yellow_to_red_cards'] = player_cards['yellowred']
sassuolo_players1['sub_in'] = player_subs['in']
sassuolo_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
sassuolo_players1 = sassuolo_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"488","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
sassuolo_players2 = pd.DataFrame()

sassuolo_players2['name'] = df_p1['name']
sassuolo_players2['first_name'] = df_p1['firstname']
sassuolo_players2['last_name'] = df_p1['lastname']
sassuolo_players2['id'] = df_p1['id']
sassuolo_players2['team'] = player_team['name']
sassuolo_players2['team_id'] = player_team['id']
sassuolo_players2['league'] = player_league['name']
sassuolo_players2['league_id'] = player_league['id']
sassuolo_players2['age'] = df_p1['age']
sassuolo_players2['birth'] = player_birth['date']
sassuolo_players2['nationality'] = df_p1['nationality']
sassuolo_players2['app'] = player_games['appearences']
sassuolo_players2['mins'] = player_games['minutes']
sassuolo_players2['goals'] = player_goals['total']
sassuolo_players2['shots'] = player_shots['total']
sassuolo_players2['shots_on_target'] = player_shots['on']
sassuolo_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
sassuolo_players2['assists'] = player_goals['assists']
sassuolo_players2['passes'] = player_passes['total']
sassuolo_players2['passes_completed'] = player_passes['accuracy']
# sassuolo_players2['pass_accuracy_%'] = df_p1['name']
sassuolo_players2['dribbles'] = player_dribbles['attempts']
sassuolo_players2['dribbles_completed'] = player_dribbles['success']
sassuolo_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
sassuolo_players2['tackles'] = player_tackles['total']
sassuolo_players2['blocks'] = player_tackles['blocks']
sassuolo_players2['interceptions'] = player_tackles['interceptions']
sassuolo_players2['fouls_drawn'] = player_fouls['drawn']
sassuolo_players2['fouls_committed'] = player_fouls['committed']
sassuolo_players2['yellow_cards'] = player_cards['yellow']
sassuolo_players2['red_cards'] = player_cards['red']
sassuolo_players2['yellow_to_red_cards'] = player_cards['yellowred']
sassuolo_players2['sub_in'] = player_subs['in']
sassuolo_players2['sub_out'] = player_subs['out']

sassuolo_players2 = sassuolo_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
sassuolo_players = pd.concat([sassuolo_players1, sassuolo_players2])
sassuolo_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### SPEZIA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"515","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
spezia_players1 = pd.DataFrame()

spezia_players1['name'] = df_p1['name']
spezia_players1['first_name'] = df_p1['firstname']
spezia_players1['last_name'] = df_p1['lastname']
spezia_players1['id'] = df_p1['id']
spezia_players1['team'] = player_team['name']
spezia_players1['team_id'] = player_team['id']
spezia_players1['league'] = player_league['name']
spezia_players1['league_id'] = player_league['id']
spezia_players1['age'] = df_p1['age']
spezia_players1['birth'] = player_birth['date']
spezia_players1['nationality'] = df_p1['nationality']
spezia_players1['app'] = player_games['appearences']
spezia_players1['mins'] = player_games['minutes']
spezia_players1['goals'] = player_goals['total']
spezia_players1['shots'] = player_shots['total']
spezia_players1['shots_on_target'] = player_shots['on']
spezia_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
spezia_players1['assists'] = player_goals['assists']
spezia_players1['passes'] = player_passes['total']
spezia_players1['passes_completed'] = player_passes['accuracy']
# spezia_players1['pass_accuracy_%'] = df_p1['name']
spezia_players1['dribbles'] = player_dribbles['attempts']
spezia_players1['dribbles_completed'] = player_dribbles['success']
spezia_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
spezia_players1['tackles'] = player_tackles['total']
spezia_players1['blocks'] = player_tackles['blocks']
spezia_players1['interceptions'] = player_tackles['interceptions']
spezia_players1['fouls_drawn'] = player_fouls['drawn']
spezia_players1['fouls_committed'] = player_fouls['committed']
spezia_players1['yellow_cards'] = player_cards['yellow']
spezia_players1['red_cards'] = player_cards['red']
spezia_players1['yellow_to_red_cards'] = player_cards['yellowred']
spezia_players1['sub_in'] = player_subs['in']
spezia_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
spezia_players1 = spezia_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"515","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
spezia_players2 = pd.DataFrame()

spezia_players2['name'] = df_p1['name']
spezia_players2['first_name'] = df_p1['firstname']
spezia_players2['last_name'] = df_p1['lastname']
spezia_players2['id'] = df_p1['id']
spezia_players2['team'] = player_team['name']
spezia_players2['team_id'] = player_team['id']
spezia_players2['league'] = player_league['name']
spezia_players2['league_id'] = player_league['id']
spezia_players2['age'] = df_p1['age']
spezia_players2['birth'] = player_birth['date']
spezia_players2['nationality'] = df_p1['nationality']
spezia_players2['app'] = player_games['appearences']
spezia_players2['mins'] = player_games['minutes']
spezia_players2['goals'] = player_goals['total']
spezia_players2['shots'] = player_shots['total']
spezia_players2['shots_on_target'] = player_shots['on']
spezia_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
spezia_players2['assists'] = player_goals['assists']
spezia_players2['passes'] = player_passes['total']
spezia_players2['passes_completed'] = player_passes['accuracy']
# spezia_players2['pass_accuracy_%'] = df_p1['name']
spezia_players2['dribbles'] = player_dribbles['attempts']
spezia_players2['dribbles_completed'] = player_dribbles['success']
spezia_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
spezia_players2['tackles'] = player_tackles['total']
spezia_players2['blocks'] = player_tackles['blocks']
spezia_players2['interceptions'] = player_tackles['interceptions']
spezia_players2['fouls_drawn'] = player_fouls['drawn']
spezia_players2['fouls_committed'] = player_fouls['committed']
spezia_players2['yellow_cards'] = player_cards['yellow']
spezia_players2['red_cards'] = player_cards['red']
spezia_players2['yellow_to_red_cards'] = player_cards['yellowred']
spezia_players2['sub_in'] = player_subs['in']
spezia_players2['sub_out'] = player_subs['out']

spezia_players2 = spezia_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
spezia_players = pd.concat([spezia_players1, spezia_players2])
spezia_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### TORINO  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"503","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
torino_players1 = pd.DataFrame()

torino_players1['name'] = df_p1['name']
torino_players1['first_name'] = df_p1['firstname']
torino_players1['last_name'] = df_p1['lastname']
torino_players1['id'] = df_p1['id']
torino_players1['team'] = player_team['name']
torino_players1['team_id'] = player_team['id']
torino_players1['league'] = player_league['name']
torino_players1['league_id'] = player_league['id']
torino_players1['age'] = df_p1['age']
torino_players1['birth'] = player_birth['date']
torino_players1['nationality'] = df_p1['nationality']
torino_players1['app'] = player_games['appearences']
torino_players1['mins'] = player_games['minutes']
torino_players1['goals'] = player_goals['total']
torino_players1['shots'] = player_shots['total']
torino_players1['shots_on_target'] = player_shots['on']
torino_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
torino_players1['assists'] = player_goals['assists']
torino_players1['passes'] = player_passes['total']
torino_players1['passes_completed'] = player_passes['accuracy']
# torino_players1['pass_accuracy_%'] = df_p1['name']
torino_players1['dribbles'] = player_dribbles['attempts']
torino_players1['dribbles_completed'] = player_dribbles['success']
torino_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
torino_players1['tackles'] = player_tackles['total']
torino_players1['blocks'] = player_tackles['blocks']
torino_players1['interceptions'] = player_tackles['interceptions']
torino_players1['fouls_drawn'] = player_fouls['drawn']
torino_players1['fouls_committed'] = player_fouls['committed']
torino_players1['yellow_cards'] = player_cards['yellow']
torino_players1['red_cards'] = player_cards['red']
torino_players1['yellow_to_red_cards'] = player_cards['yellowred']
torino_players1['sub_in'] = player_subs['in']
torino_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
torino_players1 = torino_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"503","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2', 'data3']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
torino_players2 = pd.DataFrame()

torino_players2['name'] = df_p1['name']
torino_players2['first_name'] = df_p1['firstname']
torino_players2['last_name'] = df_p1['lastname']
torino_players2['id'] = df_p1['id']
torino_players2['team'] = player_team['name']
torino_players2['team_id'] = player_team['id']
torino_players2['league'] = player_league['name']
torino_players2['league_id'] = player_league['id']
torino_players2['age'] = df_p1['age']
torino_players2['birth'] = player_birth['date']
torino_players2['nationality'] = df_p1['nationality']
torino_players2['app'] = player_games['appearences']
torino_players2['mins'] = player_games['minutes']
torino_players2['goals'] = player_goals['total']
torino_players2['shots'] = player_shots['total']
torino_players2['shots_on_target'] = player_shots['on']
torino_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
torino_players2['assists'] = player_goals['assists']
torino_players2['passes'] = player_passes['total']
torino_players2['passes_completed'] = player_passes['accuracy']
# torino_players2['pass_accuracy_%'] = df_p1['name']
torino_players2['dribbles'] = player_dribbles['attempts']
torino_players2['dribbles_completed'] = player_dribbles['success']
torino_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
torino_players2['tackles'] = player_tackles['total']
torino_players2['blocks'] = player_tackles['blocks']
torino_players2['interceptions'] = player_tackles['interceptions']
torino_players2['fouls_drawn'] = player_fouls['drawn']
torino_players2['fouls_committed'] = player_fouls['committed']
torino_players2['yellow_cards'] = player_cards['yellow']
torino_players2['red_cards'] = player_cards['red']
torino_players2['yellow_to_red_cards'] = player_cards['yellowred']
torino_players2['sub_in'] = player_subs['in']
torino_players2['sub_out'] = player_subs['out']

torino_players2 = torino_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
torino_players = pd.concat([torino_players1, torino_players2])
torino_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### UDINESE  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"494","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
udinese_players1 = pd.DataFrame()

udinese_players1['name'] = df_p1['name']
udinese_players1['first_name'] = df_p1['firstname']
udinese_players1['last_name'] = df_p1['lastname']
udinese_players1['id'] = df_p1['id']
udinese_players1['team'] = player_team['name']
udinese_players1['team_id'] = player_team['id']
udinese_players1['league'] = player_league['name']
udinese_players1['league_id'] = player_league['id']
udinese_players1['age'] = df_p1['age']
udinese_players1['birth'] = player_birth['date']
udinese_players1['nationality'] = df_p1['nationality']
udinese_players1['app'] = player_games['appearences']
udinese_players1['mins'] = player_games['minutes']
udinese_players1['goals'] = player_goals['total']
udinese_players1['shots'] = player_shots['total']
udinese_players1['shots_on_target'] = player_shots['on']
udinese_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
udinese_players1['assists'] = player_goals['assists']
udinese_players1['passes'] = player_passes['total']
udinese_players1['passes_completed'] = player_passes['accuracy']
# udinese_players1['pass_accuracy_%'] = df_p1['name']
udinese_players1['dribbles'] = player_dribbles['attempts']
udinese_players1['dribbles_completed'] = player_dribbles['success']
udinese_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
udinese_players1['tackles'] = player_tackles['total']
udinese_players1['blocks'] = player_tackles['blocks']
udinese_players1['interceptions'] = player_tackles['interceptions']
udinese_players1['fouls_drawn'] = player_fouls['drawn']
udinese_players1['fouls_committed'] = player_fouls['committed']
udinese_players1['yellow_cards'] = player_cards['yellow']
udinese_players1['red_cards'] = player_cards['red']
udinese_players1['yellow_to_red_cards'] = player_cards['yellowred']
udinese_players1['sub_in'] = player_subs['in']
udinese_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
udinese_players1 = udinese_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"494","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
udinese_players2 = pd.DataFrame()

udinese_players2['name'] = df_p1['name']
udinese_players2['first_name'] = df_p1['firstname']
udinese_players2['last_name'] = df_p1['lastname']
udinese_players2['id'] = df_p1['id']
udinese_players2['team'] = player_team['name']
udinese_players2['team_id'] = player_team['id']
udinese_players2['league'] = player_league['name']
udinese_players2['league_id'] = player_league['id']
udinese_players2['age'] = df_p1['age']
udinese_players2['birth'] = player_birth['date']
udinese_players2['nationality'] = df_p1['nationality']
udinese_players2['app'] = player_games['appearences']
udinese_players2['mins'] = player_games['minutes']
udinese_players2['goals'] = player_goals['total']
udinese_players2['shots'] = player_shots['total']
udinese_players2['shots_on_target'] = player_shots['on']
udinese_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
udinese_players2['assists'] = player_goals['assists']
udinese_players2['passes'] = player_passes['total']
udinese_players2['passes_completed'] = player_passes['accuracy']
# udinese_players2['pass_accuracy_%'] = df_p1['name']
udinese_players2['dribbles'] = player_dribbles['attempts']
udinese_players2['dribbles_completed'] = player_dribbles['success']
udinese_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
udinese_players2['tackles'] = player_tackles['total']
udinese_players2['blocks'] = player_tackles['blocks']
udinese_players2['interceptions'] = player_tackles['interceptions']
udinese_players2['fouls_drawn'] = player_fouls['drawn']
udinese_players2['fouls_committed'] = player_fouls['committed']
udinese_players2['yellow_cards'] = player_cards['yellow']
udinese_players2['red_cards'] = player_cards['red']
udinese_players2['yellow_to_red_cards'] = player_cards['yellowred']
udinese_players2['sub_in'] = player_subs['in']
udinese_players2['sub_out'] = player_subs['out']

udinese_players2 = udinese_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
udinese_players = pd.concat([udinese_players1, udinese_players2])
udinese_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### VENEZIA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"517","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
venezia_players1 = pd.DataFrame()

venezia_players1['name'] = df_p1['name']
venezia_players1['first_name'] = df_p1['firstname']
venezia_players1['last_name'] = df_p1['lastname']
venezia_players1['id'] = df_p1['id']
venezia_players1['team'] = player_team['name']
venezia_players1['team_id'] = player_team['id']
venezia_players1['league'] = player_league['name']
venezia_players1['league_id'] = player_league['id']
venezia_players1['age'] = df_p1['age']
venezia_players1['birth'] = player_birth['date']
venezia_players1['nationality'] = df_p1['nationality']
venezia_players1['app'] = player_games['appearences']
venezia_players1['mins'] = player_games['minutes']
venezia_players1['goals'] = player_goals['total']
venezia_players1['shots'] = player_shots['total']
venezia_players1['shots_on_target'] = player_shots['on']
venezia_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
venezia_players1['assists'] = player_goals['assists']
venezia_players1['passes'] = player_passes['total']
venezia_players1['passes_completed'] = player_passes['accuracy']
# venezia_players1['pass_accuracy_%'] = df_p1['name']
venezia_players1['dribbles'] = player_dribbles['attempts']
venezia_players1['dribbles_completed'] = player_dribbles['success']
venezia_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
venezia_players1['tackles'] = player_tackles['total']
venezia_players1['blocks'] = player_tackles['blocks']
venezia_players1['interceptions'] = player_tackles['interceptions']
venezia_players1['fouls_drawn'] = player_fouls['drawn']
venezia_players1['fouls_committed'] = player_fouls['committed']
venezia_players1['yellow_cards'] = player_cards['yellow']
venezia_players1['red_cards'] = player_cards['red']
venezia_players1['yellow_to_red_cards'] = player_cards['yellowred']
venezia_players1['sub_in'] = player_subs['in']
venezia_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
venezia_players1 = venezia_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"517","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
venezia_players2 = pd.DataFrame()

venezia_players2['name'] = df_p1['name']
venezia_players2['first_name'] = df_p1['firstname']
venezia_players2['last_name'] = df_p1['lastname']
venezia_players2['id'] = df_p1['id']
venezia_players2['team'] = player_team['name']
venezia_players2['team_id'] = player_team['id']
venezia_players2['league'] = player_league['name']
venezia_players2['league_id'] = player_league['id']
venezia_players2['age'] = df_p1['age']
venezia_players2['birth'] = player_birth['date']
venezia_players2['nationality'] = df_p1['nationality']
venezia_players2['app'] = player_games['appearences']
venezia_players2['mins'] = player_games['minutes']
venezia_players2['goals'] = player_goals['total']
venezia_players2['shots'] = player_shots['total']
venezia_players2['shots_on_target'] = player_shots['on']
venezia_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
venezia_players2['assists'] = player_goals['assists']
venezia_players2['passes'] = player_passes['total']
venezia_players2['passes_completed'] = player_passes['accuracy']
# venezia_players2['pass_accuracy_%'] = df_p1['name']
venezia_players2['dribbles'] = player_dribbles['attempts']
venezia_players2['dribbles_completed'] = player_dribbles['success']
venezia_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
venezia_players2['tackles'] = player_tackles['total']
venezia_players2['blocks'] = player_tackles['blocks']
venezia_players2['interceptions'] = player_tackles['interceptions']
venezia_players2['fouls_drawn'] = player_fouls['drawn']
venezia_players2['fouls_committed'] = player_fouls['committed']
venezia_players2['yellow_cards'] = player_cards['yellow']
venezia_players2['red_cards'] = player_cards['red']
venezia_players2['yellow_to_red_cards'] = player_cards['yellowred']
venezia_players2['sub_in'] = player_subs['in']
venezia_players2['sub_out'] = player_subs['out']

venezia_players2 = venezia_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
venezia_players = pd.concat([venezia_players1, venezia_players2])
venezia_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column







####### VERONA  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"504","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
verona_players1 = pd.DataFrame()

verona_players1['name'] = df_p1['name']
verona_players1['first_name'] = df_p1['firstname']
verona_players1['last_name'] = df_p1['lastname']
verona_players1['id'] = df_p1['id']
verona_players1['team'] = player_team['name']
verona_players1['team_id'] = player_team['id']
verona_players1['league'] = player_league['name']
verona_players1['league_id'] = player_league['id']
verona_players1['age'] = df_p1['age']
verona_players1['birth'] = player_birth['date']
verona_players1['nationality'] = df_p1['nationality']
verona_players1['app'] = player_games['appearences']
verona_players1['mins'] = player_games['minutes']
verona_players1['goals'] = player_goals['total']
verona_players1['shots'] = player_shots['total']
verona_players1['shots_on_target'] = player_shots['on']
verona_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
verona_players1['assists'] = player_goals['assists']
verona_players1['passes'] = player_passes['total']
verona_players1['passes_completed'] = player_passes['accuracy']
# verona_players1['pass_accuracy_%'] = df_p1['name']
verona_players1['dribbles'] = player_dribbles['attempts']
verona_players1['dribbles_completed'] = player_dribbles['success']
verona_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
verona_players1['tackles'] = player_tackles['total']
verona_players1['blocks'] = player_tackles['blocks']
verona_players1['interceptions'] = player_tackles['interceptions']
verona_players1['fouls_drawn'] = player_fouls['drawn']
verona_players1['fouls_committed'] = player_fouls['committed']
verona_players1['yellow_cards'] = player_cards['yellow']
verona_players1['red_cards'] = player_cards['red']
verona_players1['yellow_to_red_cards'] = player_cards['yellowred']
verona_players1['sub_in'] = player_subs['in']
verona_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
verona_players1 = verona_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"504","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
verona_players2 = pd.DataFrame()

verona_players2['name'] = df_p1['name']
verona_players2['first_name'] = df_p1['firstname']
verona_players2['last_name'] = df_p1['lastname']
verona_players2['id'] = df_p1['id']
verona_players2['team'] = player_team['name']
verona_players2['team_id'] = player_team['id']
verona_players2['league'] = player_league['name']
verona_players2['league_id'] = player_league['id']
verona_players2['age'] = df_p1['age']
verona_players2['birth'] = player_birth['date']
verona_players2['nationality'] = df_p1['nationality']
verona_players2['app'] = player_games['appearences']
verona_players2['mins'] = player_games['minutes']
verona_players2['goals'] = player_goals['total']
verona_players2['shots'] = player_shots['total']
verona_players2['shots_on_target'] = player_shots['on']
verona_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
verona_players2['assists'] = player_goals['assists']
verona_players2['passes'] = player_passes['total']
verona_players2['passes_completed'] = player_passes['accuracy']
# verona_players2['pass_accuracy_%'] = df_p1['name']
verona_players2['dribbles'] = player_dribbles['attempts']
verona_players2['dribbles_completed'] = player_dribbles['success']
verona_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
verona_players2['tackles'] = player_tackles['total']
verona_players2['blocks'] = player_tackles['blocks']
verona_players2['interceptions'] = player_tackles['interceptions']
verona_players2['fouls_drawn'] = player_fouls['drawn']
verona_players2['fouls_committed'] = player_fouls['committed']
verona_players2['yellow_cards'] = player_cards['yellow']
verona_players2['red_cards'] = player_cards['red']
verona_players2['yellow_to_red_cards'] = player_cards['yellowred']
verona_players2['sub_in'] = player_subs['in']
verona_players2['sub_out'] = player_subs['out']

verona_players2 = verona_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
verona_players = pd.concat([verona_players1, verona_players2])
verona_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




# Combine players from all teams in the league into a single data frame
serie_a_players = pd.concat([ac_milan_players,
					roma_players,
					atalanta_players,
					bologna_players,
					cagliari_players,
					empoli_players,
					fiorentina_players,
					genoa_players,
					inter_milan_players,
					juventus_players,
					lazio_players,
					napoli_players,
					salernitana_players,
					sampdoria_players,
					sassuolo_players,
					spezia_players,
					torino_players,
					udinese_players,
					venezia_players,
					verona_players
					], ignore_index=True)





####################################### 5. LIGUE 1 ##############################################


####### ANGERS  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"504","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
angers_players1 = pd.DataFrame()

angers_players1['name'] = df_p1['name']
angers_players1['first_name'] = df_p1['firstname']
angers_players1['last_name'] = df_p1['lastname']
angers_players1['id'] = df_p1['id']
angers_players1['team'] = player_team['name']
angers_players1['team_id'] = player_team['id']
angers_players1['league'] = player_league['name']
angers_players1['league_id'] = player_league['id']
angers_players1['age'] = df_p1['age']
angers_players1['birth'] = player_birth['date']
angers_players1['nationality'] = df_p1['nationality']
angers_players1['app'] = player_games['appearences']
angers_players1['mins'] = player_games['minutes']
angers_players1['goals'] = player_goals['total']
angers_players1['shots'] = player_shots['total']
angers_players1['shots_on_target'] = player_shots['on']
angers_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
angers_players1['assists'] = player_goals['assists']
angers_players1['passes'] = player_passes['total']
angers_players1['passes_completed'] = player_passes['accuracy']
# angers_players1['pass_accuracy_%'] = df_p1['name']
angers_players1['dribbles'] = player_dribbles['attempts']
angers_players1['dribbles_completed'] = player_dribbles['success']
angers_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
angers_players1['tackles'] = player_tackles['total']
angers_players1['blocks'] = player_tackles['blocks']
angers_players1['interceptions'] = player_tackles['interceptions']
angers_players1['fouls_drawn'] = player_fouls['drawn']
angers_players1['fouls_committed'] = player_fouls['committed']
angers_players1['yellow_cards'] = player_cards['yellow']
angers_players1['red_cards'] = player_cards['red']
angers_players1['yellow_to_red_cards'] = player_cards['yellowred']
angers_players1['sub_in'] = player_subs['in']
angers_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
angers_players1 = angers_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"504","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
angers_players2 = pd.DataFrame()

angers_players2['name'] = df_p1['name']
angers_players2['first_name'] = df_p1['firstname']
angers_players2['last_name'] = df_p1['lastname']
angers_players2['id'] = df_p1['id']
angers_players2['team'] = player_team['name']
angers_players2['team_id'] = player_team['id']
angers_players2['league'] = player_league['name']
angers_players2['league_id'] = player_league['id']
angers_players2['age'] = df_p1['age']
angers_players2['birth'] = player_birth['date']
angers_players2['nationality'] = df_p1['nationality']
angers_players2['app'] = player_games['appearences']
angers_players2['mins'] = player_games['minutes']
angers_players2['goals'] = player_goals['total']
angers_players2['shots'] = player_shots['total']
angers_players2['shots_on_target'] = player_shots['on']
angers_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
angers_players2['assists'] = player_goals['assists']
angers_players2['passes'] = player_passes['total']
angers_players2['passes_completed'] = player_passes['accuracy']
# angers_players2['pass_accuracy_%'] = df_p1['name']
angers_players2['dribbles'] = player_dribbles['attempts']
angers_players2['dribbles_completed'] = player_dribbles['success']
angers_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
angers_players2['tackles'] = player_tackles['total']
angers_players2['blocks'] = player_tackles['blocks']
angers_players2['interceptions'] = player_tackles['interceptions']
angers_players2['fouls_drawn'] = player_fouls['drawn']
angers_players2['fouls_committed'] = player_fouls['committed']
angers_players2['yellow_cards'] = player_cards['yellow']
angers_players2['red_cards'] = player_cards['red']
angers_players2['yellow_to_red_cards'] = player_cards['yellowred']
angers_players2['sub_in'] = player_subs['in']
angers_players2['sub_out'] = player_subs['out']

angers_players2 = angers_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
angers_players = pd.concat([angers_players1, angers_players2])
angers_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### BORDEAUX  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"78","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
bordeaux_players1 = pd.DataFrame()

bordeaux_players1['name'] = df_p1['name']
bordeaux_players1['first_name'] = df_p1['firstname']
bordeaux_players1['last_name'] = df_p1['lastname']
bordeaux_players1['id'] = df_p1['id']
bordeaux_players1['team'] = player_team['name']
bordeaux_players1['team_id'] = player_team['id']
bordeaux_players1['league'] = player_league['name']
bordeaux_players1['league_id'] = player_league['id']
bordeaux_players1['age'] = df_p1['age']
bordeaux_players1['birth'] = player_birth['date']
bordeaux_players1['nationality'] = df_p1['nationality']
bordeaux_players1['app'] = player_games['appearences']
bordeaux_players1['mins'] = player_games['minutes']
bordeaux_players1['goals'] = player_goals['total']
bordeaux_players1['shots'] = player_shots['total']
bordeaux_players1['shots_on_target'] = player_shots['on']
bordeaux_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
bordeaux_players1['assists'] = player_goals['assists']
bordeaux_players1['passes'] = player_passes['total']
bordeaux_players1['passes_completed'] = player_passes['accuracy']
# bordeaux_players1['pass_accuracy_%'] = df_p1['name']
bordeaux_players1['dribbles'] = player_dribbles['attempts']
bordeaux_players1['dribbles_completed'] = player_dribbles['success']
bordeaux_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
bordeaux_players1['tackles'] = player_tackles['total']
bordeaux_players1['blocks'] = player_tackles['blocks']
bordeaux_players1['interceptions'] = player_tackles['interceptions']
bordeaux_players1['fouls_drawn'] = player_fouls['drawn']
bordeaux_players1['fouls_committed'] = player_fouls['committed']
bordeaux_players1['yellow_cards'] = player_cards['yellow']
bordeaux_players1['red_cards'] = player_cards['red']
bordeaux_players1['yellow_to_red_cards'] = player_cards['yellowred']
bordeaux_players1['sub_in'] = player_subs['in']
bordeaux_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
bordeaux_players1 = bordeaux_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"78","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
bordeaux_players2 = pd.DataFrame()

bordeaux_players2['name'] = df_p1['name']
bordeaux_players2['first_name'] = df_p1['firstname']
bordeaux_players2['last_name'] = df_p1['lastname']
bordeaux_players2['id'] = df_p1['id']
bordeaux_players2['team'] = player_team['name']
bordeaux_players2['team_id'] = player_team['id']
bordeaux_players2['league'] = player_league['name']
bordeaux_players2['league_id'] = player_league['id']
bordeaux_players2['age'] = df_p1['age']
bordeaux_players2['birth'] = player_birth['date']
bordeaux_players2['nationality'] = df_p1['nationality']
bordeaux_players2['app'] = player_games['appearences']
bordeaux_players2['mins'] = player_games['minutes']
bordeaux_players2['goals'] = player_goals['total']
bordeaux_players2['shots'] = player_shots['total']
bordeaux_players2['shots_on_target'] = player_shots['on']
bordeaux_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
bordeaux_players2['assists'] = player_goals['assists']
bordeaux_players2['passes'] = player_passes['total']
bordeaux_players2['passes_completed'] = player_passes['accuracy']
# bordeaux_players2['pass_accuracy_%'] = df_p1['name']
bordeaux_players2['dribbles'] = player_dribbles['attempts']
bordeaux_players2['dribbles_completed'] = player_dribbles['success']
bordeaux_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
bordeaux_players2['tackles'] = player_tackles['total']
bordeaux_players2['blocks'] = player_tackles['blocks']
bordeaux_players2['interceptions'] = player_tackles['interceptions']
bordeaux_players2['fouls_drawn'] = player_fouls['drawn']
bordeaux_players2['fouls_committed'] = player_fouls['committed']
bordeaux_players2['yellow_cards'] = player_cards['yellow']
bordeaux_players2['red_cards'] = player_cards['red']
bordeaux_players2['yellow_to_red_cards'] = player_cards['yellowred']
bordeaux_players2['sub_in'] = player_subs['in']
bordeaux_players2['sub_out'] = player_subs['out']

bordeaux_players2 = bordeaux_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
bordeaux_players = pd.concat([bordeaux_players1, bordeaux_players2])
bordeaux_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### CLERMONT FOOT  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"99","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
clermont_foot_players1 = pd.DataFrame()

clermont_foot_players1['name'] = df_p1['name']
clermont_foot_players1['first_name'] = df_p1['firstname']
clermont_foot_players1['last_name'] = df_p1['lastname']
clermont_foot_players1['id'] = df_p1['id']
clermont_foot_players1['team'] = player_team['name']
clermont_foot_players1['team_id'] = player_team['id']
clermont_foot_players1['league'] = player_league['name']
clermont_foot_players1['league_id'] = player_league['id']
clermont_foot_players1['age'] = df_p1['age']
clermont_foot_players1['birth'] = player_birth['date']
clermont_foot_players1['nationality'] = df_p1['nationality']
clermont_foot_players1['app'] = player_games['appearences']
clermont_foot_players1['mins'] = player_games['minutes']
clermont_foot_players1['goals'] = player_goals['total']
clermont_foot_players1['shots'] = player_shots['total']
clermont_foot_players1['shots_on_target'] = player_shots['on']
clermont_foot_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
clermont_foot_players1['assists'] = player_goals['assists']
clermont_foot_players1['passes'] = player_passes['total']
clermont_foot_players1['passes_completed'] = player_passes['accuracy']
# clermont_foot_players1['pass_accuracy_%'] = df_p1['name']
clermont_foot_players1['dribbles'] = player_dribbles['attempts']
clermont_foot_players1['dribbles_completed'] = player_dribbles['success']
clermont_foot_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
clermont_foot_players1['tackles'] = player_tackles['total']
clermont_foot_players1['blocks'] = player_tackles['blocks']
clermont_foot_players1['interceptions'] = player_tackles['interceptions']
clermont_foot_players1['fouls_drawn'] = player_fouls['drawn']
clermont_foot_players1['fouls_committed'] = player_fouls['committed']
clermont_foot_players1['yellow_cards'] = player_cards['yellow']
clermont_foot_players1['red_cards'] = player_cards['red']
clermont_foot_players1['yellow_to_red_cards'] = player_cards['yellowred']
clermont_foot_players1['sub_in'] = player_subs['in']
clermont_foot_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
clermont_foot_players1 = clermont_foot_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"99","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
clermont_foot_players2 = pd.DataFrame()

clermont_foot_players2['name'] = df_p1['name']
clermont_foot_players2['first_name'] = df_p1['firstname']
clermont_foot_players2['last_name'] = df_p1['lastname']
clermont_foot_players2['id'] = df_p1['id']
clermont_foot_players2['team'] = player_team['name']
clermont_foot_players2['team_id'] = player_team['id']
clermont_foot_players2['league'] = player_league['name']
clermont_foot_players2['league_id'] = player_league['id']
clermont_foot_players2['age'] = df_p1['age']
clermont_foot_players2['birth'] = player_birth['date']
clermont_foot_players2['nationality'] = df_p1['nationality']
clermont_foot_players2['app'] = player_games['appearences']
clermont_foot_players2['mins'] = player_games['minutes']
clermont_foot_players2['goals'] = player_goals['total']
clermont_foot_players2['shots'] = player_shots['total']
clermont_foot_players2['shots_on_target'] = player_shots['on']
clermont_foot_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
clermont_foot_players2['assists'] = player_goals['assists']
clermont_foot_players2['passes'] = player_passes['total']
clermont_foot_players2['passes_completed'] = player_passes['accuracy']
# clermont_foot_players2['pass_accuracy_%'] = df_p1['name']
clermont_foot_players2['dribbles'] = player_dribbles['attempts']
clermont_foot_players2['dribbles_completed'] = player_dribbles['success']
clermont_foot_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
clermont_foot_players2['tackles'] = player_tackles['total']
clermont_foot_players2['blocks'] = player_tackles['blocks']
clermont_foot_players2['interceptions'] = player_tackles['interceptions']
clermont_foot_players2['fouls_drawn'] = player_fouls['drawn']
clermont_foot_players2['fouls_committed'] = player_fouls['committed']
clermont_foot_players2['yellow_cards'] = player_cards['yellow']
clermont_foot_players2['red_cards'] = player_cards['red']
clermont_foot_players2['yellow_to_red_cards'] = player_cards['yellowred']
clermont_foot_players2['sub_in'] = player_subs['in']
clermont_foot_players2['sub_out'] = player_subs['out']

clermont_foot_players2 = clermont_foot_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
clermont_foot_players = pd.concat([clermont_foot_players1, clermont_foot_players2])
clermont_foot_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column







####### ESTAC TROYES  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"110","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
estac_troyes_players1 = pd.DataFrame()

estac_troyes_players1['name'] = df_p1['name']
estac_troyes_players1['first_name'] = df_p1['firstname']
estac_troyes_players1['last_name'] = df_p1['lastname']
estac_troyes_players1['id'] = df_p1['id']
estac_troyes_players1['team'] = player_team['name']
estac_troyes_players1['team_id'] = player_team['id']
estac_troyes_players1['league'] = player_league['name']
estac_troyes_players1['league_id'] = player_league['id']
estac_troyes_players1['age'] = df_p1['age']
estac_troyes_players1['birth'] = player_birth['date']
estac_troyes_players1['nationality'] = df_p1['nationality']
estac_troyes_players1['app'] = player_games['appearences']
estac_troyes_players1['mins'] = player_games['minutes']
estac_troyes_players1['goals'] = player_goals['total']
estac_troyes_players1['shots'] = player_shots['total']
estac_troyes_players1['shots_on_target'] = player_shots['on']
estac_troyes_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
estac_troyes_players1['assists'] = player_goals['assists']
estac_troyes_players1['passes'] = player_passes['total']
estac_troyes_players1['passes_completed'] = player_passes['accuracy']
# estac_troyes_players1['pass_accuracy_%'] = df_p1['name']
estac_troyes_players1['dribbles'] = player_dribbles['attempts']
estac_troyes_players1['dribbles_completed'] = player_dribbles['success']
estac_troyes_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
estac_troyes_players1['tackles'] = player_tackles['total']
estac_troyes_players1['blocks'] = player_tackles['blocks']
estac_troyes_players1['interceptions'] = player_tackles['interceptions']
estac_troyes_players1['fouls_drawn'] = player_fouls['drawn']
estac_troyes_players1['fouls_committed'] = player_fouls['committed']
estac_troyes_players1['yellow_cards'] = player_cards['yellow']
estac_troyes_players1['red_cards'] = player_cards['red']
estac_troyes_players1['yellow_to_red_cards'] = player_cards['yellowred']
estac_troyes_players1['sub_in'] = player_subs['in']
estac_troyes_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
estac_troyes_players1 = estac_troyes_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"110","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
estac_troyes_players2 = pd.DataFrame()

estac_troyes_players2['name'] = df_p1['name']
estac_troyes_players2['first_name'] = df_p1['firstname']
estac_troyes_players2['last_name'] = df_p1['lastname']
estac_troyes_players2['id'] = df_p1['id']
estac_troyes_players2['team'] = player_team['name']
estac_troyes_players2['team_id'] = player_team['id']
estac_troyes_players2['league'] = player_league['name']
estac_troyes_players2['league_id'] = player_league['id']
estac_troyes_players2['age'] = df_p1['age']
estac_troyes_players2['birth'] = player_birth['date']
estac_troyes_players2['nationality'] = df_p1['nationality']
estac_troyes_players2['app'] = player_games['appearences']
estac_troyes_players2['mins'] = player_games['minutes']
estac_troyes_players2['goals'] = player_goals['total']
estac_troyes_players2['shots'] = player_shots['total']
estac_troyes_players2['shots_on_target'] = player_shots['on']
estac_troyes_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
estac_troyes_players2['assists'] = player_goals['assists']
estac_troyes_players2['passes'] = player_passes['total']
estac_troyes_players2['passes_completed'] = player_passes['accuracy']
# estac_troyes_players2['pass_accuracy_%'] = df_p1['name']
estac_troyes_players2['dribbles'] = player_dribbles['attempts']
estac_troyes_players2['dribbles_completed'] = player_dribbles['success']
estac_troyes_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
estac_troyes_players2['tackles'] = player_tackles['total']
estac_troyes_players2['blocks'] = player_tackles['blocks']
estac_troyes_players2['interceptions'] = player_tackles['interceptions']
estac_troyes_players2['fouls_drawn'] = player_fouls['drawn']
estac_troyes_players2['fouls_committed'] = player_fouls['committed']
estac_troyes_players2['yellow_cards'] = player_cards['yellow']
estac_troyes_players2['red_cards'] = player_cards['red']
estac_troyes_players2['yellow_to_red_cards'] = player_cards['yellowred']
estac_troyes_players2['sub_in'] = player_subs['in']
estac_troyes_players2['sub_out'] = player_subs['out']

estac_troyes_players2 = estac_troyes_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
estac_troyes_players = pd.concat([estac_troyes_players1, estac_troyes_players2])
estac_troyes_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column




####### LENS  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"116","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
lens_players1 = pd.DataFrame()

lens_players1['name'] = df_p1['name']
lens_players1['first_name'] = df_p1['firstname']
lens_players1['last_name'] = df_p1['lastname']
lens_players1['id'] = df_p1['id']
lens_players1['team'] = player_team['name']
lens_players1['team_id'] = player_team['id']
lens_players1['league'] = player_league['name']
lens_players1['league_id'] = player_league['id']
lens_players1['age'] = df_p1['age']
lens_players1['birth'] = player_birth['date']
lens_players1['nationality'] = df_p1['nationality']
lens_players1['app'] = player_games['appearences']
lens_players1['mins'] = player_games['minutes']
lens_players1['goals'] = player_goals['total']
lens_players1['shots'] = player_shots['total']
lens_players1['shots_on_target'] = player_shots['on']
lens_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
lens_players1['assists'] = player_goals['assists']
lens_players1['passes'] = player_passes['total']
lens_players1['passes_completed'] = player_passes['accuracy']
# lens_players1['pass_accuracy_%'] = df_p1['name']
lens_players1['dribbles'] = player_dribbles['attempts']
lens_players1['dribbles_completed'] = player_dribbles['success']
lens_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
lens_players1['tackles'] = player_tackles['total']
lens_players1['blocks'] = player_tackles['blocks']
lens_players1['interceptions'] = player_tackles['interceptions']
lens_players1['fouls_drawn'] = player_fouls['drawn']
lens_players1['fouls_committed'] = player_fouls['committed']
lens_players1['yellow_cards'] = player_cards['yellow']
lens_players1['red_cards'] = player_cards['red']
lens_players1['yellow_to_red_cards'] = player_cards['yellowred']
lens_players1['sub_in'] = player_subs['in']
lens_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
lens_players1 = lens_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"116","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
lens_players2 = pd.DataFrame()

lens_players2['name'] = df_p1['name']
lens_players2['first_name'] = df_p1['firstname']
lens_players2['last_name'] = df_p1['lastname']
lens_players2['id'] = df_p1['id']
lens_players2['team'] = player_team['name']
lens_players2['team_id'] = player_team['id']
lens_players2['league'] = player_league['name']
lens_players2['league_id'] = player_league['id']
lens_players2['age'] = df_p1['age']
lens_players2['birth'] = player_birth['date']
lens_players2['nationality'] = df_p1['nationality']
lens_players2['app'] = player_games['appearences']
lens_players2['mins'] = player_games['minutes']
lens_players2['goals'] = player_goals['total']
lens_players2['shots'] = player_shots['total']
lens_players2['shots_on_target'] = player_shots['on']
lens_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
lens_players2['assists'] = player_goals['assists']
lens_players2['passes'] = player_passes['total']
lens_players2['passes_completed'] = player_passes['accuracy']
# lens_players2['pass_accuracy_%'] = df_p1['name']
lens_players2['dribbles'] = player_dribbles['attempts']
lens_players2['dribbles_completed'] = player_dribbles['success']
lens_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
lens_players2['tackles'] = player_tackles['total']
lens_players2['blocks'] = player_tackles['blocks']
lens_players2['interceptions'] = player_tackles['interceptions']
lens_players2['fouls_drawn'] = player_fouls['drawn']
lens_players2['fouls_committed'] = player_fouls['committed']
lens_players2['yellow_cards'] = player_cards['yellow']
lens_players2['red_cards'] = player_cards['red']
lens_players2['yellow_to_red_cards'] = player_cards['yellowred']
lens_players2['sub_in'] = player_subs['in']
lens_players2['sub_out'] = player_subs['out']

lens_players2 = lens_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
lens_players = pd.concat([lens_players1, lens_players2])
lens_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column









####### LILLE  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"79","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
lille_players1 = pd.DataFrame()

lille_players1['name'] = df_p1['name']
lille_players1['first_name'] = df_p1['firstname']
lille_players1['last_name'] = df_p1['lastname']
lille_players1['id'] = df_p1['id']
lille_players1['team'] = player_team['name']
lille_players1['team_id'] = player_team['id']
lille_players1['league'] = player_league['name']
lille_players1['league_id'] = player_league['id']
lille_players1['age'] = df_p1['age']
lille_players1['birth'] = player_birth['date']
lille_players1['nationality'] = df_p1['nationality']
lille_players1['app'] = player_games['appearences']
lille_players1['mins'] = player_games['minutes']
lille_players1['goals'] = player_goals['total']
lille_players1['shots'] = player_shots['total']
lille_players1['shots_on_target'] = player_shots['on']
lille_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
lille_players1['assists'] = player_goals['assists']
lille_players1['passes'] = player_passes['total']
lille_players1['passes_completed'] = player_passes['accuracy']
# lille_players1['pass_accuracy_%'] = df_p1['name']
lille_players1['dribbles'] = player_dribbles['attempts']
lille_players1['dribbles_completed'] = player_dribbles['success']
lille_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
lille_players1['tackles'] = player_tackles['total']
lille_players1['blocks'] = player_tackles['blocks']
lille_players1['interceptions'] = player_tackles['interceptions']
lille_players1['fouls_drawn'] = player_fouls['drawn']
lille_players1['fouls_committed'] = player_fouls['committed']
lille_players1['yellow_cards'] = player_cards['yellow']
lille_players1['red_cards'] = player_cards['red']
lille_players1['yellow_to_red_cards'] = player_cards['yellowred']
lille_players1['sub_in'] = player_subs['in']
lille_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
lille_players1 = lille_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"79","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
lille_players2 = pd.DataFrame()

lille_players2['name'] = df_p1['name']
lille_players2['first_name'] = df_p1['firstname']
lille_players2['last_name'] = df_p1['lastname']
lille_players2['id'] = df_p1['id']
lille_players2['team'] = player_team['name']
lille_players2['team_id'] = player_team['id']
lille_players2['league'] = player_league['name']
lille_players2['league_id'] = player_league['id']
lille_players2['age'] = df_p1['age']
lille_players2['birth'] = player_birth['date']
lille_players2['nationality'] = df_p1['nationality']
lille_players2['app'] = player_games['appearences']
lille_players2['mins'] = player_games['minutes']
lille_players2['goals'] = player_goals['total']
lille_players2['shots'] = player_shots['total']
lille_players2['shots_on_target'] = player_shots['on']
lille_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
lille_players2['assists'] = player_goals['assists']
lille_players2['passes'] = player_passes['total']
lille_players2['passes_completed'] = player_passes['accuracy']
# lille_players2['pass_accuracy_%'] = df_p1['name']
lille_players2['dribbles'] = player_dribbles['attempts']
lille_players2['dribbles_completed'] = player_dribbles['success']
lille_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
lille_players2['tackles'] = player_tackles['total']
lille_players2['blocks'] = player_tackles['blocks']
lille_players2['interceptions'] = player_tackles['interceptions']
lille_players2['fouls_drawn'] = player_fouls['drawn']
lille_players2['fouls_committed'] = player_fouls['committed']
lille_players2['yellow_cards'] = player_cards['yellow']
lille_players2['red_cards'] = player_cards['red']
lille_players2['yellow_to_red_cards'] = player_cards['yellowred']
lille_players2['sub_in'] = player_subs['in']
lille_players2['sub_out'] = player_subs['out']

lille_players2 = lille_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
lille_players = pd.concat([lille_players1, lille_players2])
lille_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column







####### LORIENT  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"97","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
lorient_players1 = pd.DataFrame()

lorient_players1['name'] = df_p1['name']
lorient_players1['first_name'] = df_p1['firstname']
lorient_players1['last_name'] = df_p1['lastname']
lorient_players1['id'] = df_p1['id']
lorient_players1['team'] = player_team['name']
lorient_players1['team_id'] = player_team['id']
lorient_players1['league'] = player_league['name']
lorient_players1['league_id'] = player_league['id']
lorient_players1['age'] = df_p1['age']
lorient_players1['birth'] = player_birth['date']
lorient_players1['nationality'] = df_p1['nationality']
lorient_players1['app'] = player_games['appearences']
lorient_players1['mins'] = player_games['minutes']
lorient_players1['goals'] = player_goals['total']
lorient_players1['shots'] = player_shots['total']
lorient_players1['shots_on_target'] = player_shots['on']
lorient_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
lorient_players1['assists'] = player_goals['assists']
lorient_players1['passes'] = player_passes['total']
lorient_players1['passes_completed'] = player_passes['accuracy']
# lorient_players1['pass_accuracy_%'] = df_p1['name']
lorient_players1['dribbles'] = player_dribbles['attempts']
lorient_players1['dribbles_completed'] = player_dribbles['success']
lorient_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
lorient_players1['tackles'] = player_tackles['total']
lorient_players1['blocks'] = player_tackles['blocks']
lorient_players1['interceptions'] = player_tackles['interceptions']
lorient_players1['fouls_drawn'] = player_fouls['drawn']
lorient_players1['fouls_committed'] = player_fouls['committed']
lorient_players1['yellow_cards'] = player_cards['yellow']
lorient_players1['red_cards'] = player_cards['red']
lorient_players1['yellow_to_red_cards'] = player_cards['yellowred']
lorient_players1['sub_in'] = player_subs['in']
lorient_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
lorient_players1 = lorient_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"97","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
lorient_players2 = pd.DataFrame()

lorient_players2['name'] = df_p1['name']
lorient_players2['first_name'] = df_p1['firstname']
lorient_players2['last_name'] = df_p1['lastname']
lorient_players2['id'] = df_p1['id']
lorient_players2['team'] = player_team['name']
lorient_players2['team_id'] = player_team['id']
lorient_players2['league'] = player_league['name']
lorient_players2['league_id'] = player_league['id']
lorient_players2['age'] = df_p1['age']
lorient_players2['birth'] = player_birth['date']
lorient_players2['nationality'] = df_p1['nationality']
lorient_players2['app'] = player_games['appearences']
lorient_players2['mins'] = player_games['minutes']
lorient_players2['goals'] = player_goals['total']
lorient_players2['shots'] = player_shots['total']
lorient_players2['shots_on_target'] = player_shots['on']
lorient_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
lorient_players2['assists'] = player_goals['assists']
lorient_players2['passes'] = player_passes['total']
lorient_players2['passes_completed'] = player_passes['accuracy']
# lorient_players2['pass_accuracy_%'] = df_p1['name']
lorient_players2['dribbles'] = player_dribbles['attempts']
lorient_players2['dribbles_completed'] = player_dribbles['success']
lorient_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
lorient_players2['tackles'] = player_tackles['total']
lorient_players2['blocks'] = player_tackles['blocks']
lorient_players2['interceptions'] = player_tackles['interceptions']
lorient_players2['fouls_drawn'] = player_fouls['drawn']
lorient_players2['fouls_committed'] = player_fouls['committed']
lorient_players2['yellow_cards'] = player_cards['yellow']
lorient_players2['red_cards'] = player_cards['red']
lorient_players2['yellow_to_red_cards'] = player_cards['yellowred']
lorient_players2['sub_in'] = player_subs['in']
lorient_players2['sub_out'] = player_subs['out']

lorient_players2 = lorient_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
lorient_players = pd.concat([lorient_players1, lorient_players2])
lorient_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### LYON  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"80","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
lyon_players1 = pd.DataFrame()

lyon_players1['name'] = df_p1['name']
lyon_players1['first_name'] = df_p1['firstname']
lyon_players1['last_name'] = df_p1['lastname']
lyon_players1['id'] = df_p1['id']
lyon_players1['team'] = player_team['name']
lyon_players1['team_id'] = player_team['id']
lyon_players1['league'] = player_league['name']
lyon_players1['league_id'] = player_league['id']
lyon_players1['age'] = df_p1['age']
lyon_players1['birth'] = player_birth['date']
lyon_players1['nationality'] = df_p1['nationality']
lyon_players1['app'] = player_games['appearences']
lyon_players1['mins'] = player_games['minutes']
lyon_players1['goals'] = player_goals['total']
lyon_players1['shots'] = player_shots['total']
lyon_players1['shots_on_target'] = player_shots['on']
lyon_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
lyon_players1['assists'] = player_goals['assists']
lyon_players1['passes'] = player_passes['total']
lyon_players1['passes_completed'] = player_passes['accuracy']
# lyon_players1['pass_accuracy_%'] = df_p1['name']
lyon_players1['dribbles'] = player_dribbles['attempts']
lyon_players1['dribbles_completed'] = player_dribbles['success']
lyon_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
lyon_players1['tackles'] = player_tackles['total']
lyon_players1['blocks'] = player_tackles['blocks']
lyon_players1['interceptions'] = player_tackles['interceptions']
lyon_players1['fouls_drawn'] = player_fouls['drawn']
lyon_players1['fouls_committed'] = player_fouls['committed']
lyon_players1['yellow_cards'] = player_cards['yellow']
lyon_players1['red_cards'] = player_cards['red']
lyon_players1['yellow_to_red_cards'] = player_cards['yellowred']
lyon_players1['sub_in'] = player_subs['in']
lyon_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
lyon_players1 = lyon_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"80","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
lyon_players2 = pd.DataFrame()

lyon_players2['name'] = df_p1['name']
lyon_players2['first_name'] = df_p1['firstname']
lyon_players2['last_name'] = df_p1['lastname']
lyon_players2['id'] = df_p1['id']
lyon_players2['team'] = player_team['name']
lyon_players2['team_id'] = player_team['id']
lyon_players2['league'] = player_league['name']
lyon_players2['league_id'] = player_league['id']
lyon_players2['age'] = df_p1['age']
lyon_players2['birth'] = player_birth['date']
lyon_players2['nationality'] = df_p1['nationality']
lyon_players2['app'] = player_games['appearences']
lyon_players2['mins'] = player_games['minutes']
lyon_players2['goals'] = player_goals['total']
lyon_players2['shots'] = player_shots['total']
lyon_players2['shots_on_target'] = player_shots['on']
lyon_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
lyon_players2['assists'] = player_goals['assists']
lyon_players2['passes'] = player_passes['total']
lyon_players2['passes_completed'] = player_passes['accuracy']
# lyon_players2['pass_accuracy_%'] = df_p1['name']
lyon_players2['dribbles'] = player_dribbles['attempts']
lyon_players2['dribbles_completed'] = player_dribbles['success']
lyon_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
lyon_players2['tackles'] = player_tackles['total']
lyon_players2['blocks'] = player_tackles['blocks']
lyon_players2['interceptions'] = player_tackles['interceptions']
lyon_players2['fouls_drawn'] = player_fouls['drawn']
lyon_players2['fouls_committed'] = player_fouls['committed']
lyon_players2['yellow_cards'] = player_cards['yellow']
lyon_players2['red_cards'] = player_cards['red']
lyon_players2['yellow_to_red_cards'] = player_cards['yellowred']
lyon_players2['sub_in'] = player_subs['in']
lyon_players2['sub_out'] = player_subs['out']

lyon_players2 = lyon_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
lyon_players = pd.concat([lyon_players1, lyon_players2])
lyon_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column









####### MARSEILLE  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"81","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
marseille_players1 = pd.DataFrame()

marseille_players1['name'] = df_p1['name']
marseille_players1['first_name'] = df_p1['firstname']
marseille_players1['last_name'] = df_p1['lastname']
marseille_players1['id'] = df_p1['id']
marseille_players1['team'] = player_team['name']
marseille_players1['team_id'] = player_team['id']
marseille_players1['league'] = player_league['name']
marseille_players1['league_id'] = player_league['id']
marseille_players1['age'] = df_p1['age']
marseille_players1['birth'] = player_birth['date']
marseille_players1['nationality'] = df_p1['nationality']
marseille_players1['app'] = player_games['appearences']
marseille_players1['mins'] = player_games['minutes']
marseille_players1['goals'] = player_goals['total']
marseille_players1['shots'] = player_shots['total']
marseille_players1['shots_on_target'] = player_shots['on']
marseille_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
marseille_players1['assists'] = player_goals['assists']
marseille_players1['passes'] = player_passes['total']
marseille_players1['passes_completed'] = player_passes['accuracy']
# marseille_players1['pass_accuracy_%'] = df_p1['name']
marseille_players1['dribbles'] = player_dribbles['attempts']
marseille_players1['dribbles_completed'] = player_dribbles['success']
marseille_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
marseille_players1['tackles'] = player_tackles['total']
marseille_players1['blocks'] = player_tackles['blocks']
marseille_players1['interceptions'] = player_tackles['interceptions']
marseille_players1['fouls_drawn'] = player_fouls['drawn']
marseille_players1['fouls_committed'] = player_fouls['committed']
marseille_players1['yellow_cards'] = player_cards['yellow']
marseille_players1['red_cards'] = player_cards['red']
marseille_players1['yellow_to_red_cards'] = player_cards['yellowred']
marseille_players1['sub_in'] = player_subs['in']
marseille_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
marseille_players1 = marseille_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"81","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
marseille_players2 = pd.DataFrame()

marseille_players2['name'] = df_p1['name']
marseille_players2['first_name'] = df_p1['firstname']
marseille_players2['last_name'] = df_p1['lastname']
marseille_players2['id'] = df_p1['id']
marseille_players2['team'] = player_team['name']
marseille_players2['team_id'] = player_team['id']
marseille_players2['league'] = player_league['name']
marseille_players2['league_id'] = player_league['id']
marseille_players2['age'] = df_p1['age']
marseille_players2['birth'] = player_birth['date']
marseille_players2['nationality'] = df_p1['nationality']
marseille_players2['app'] = player_games['appearences']
marseille_players2['mins'] = player_games['minutes']
marseille_players2['goals'] = player_goals['total']
marseille_players2['shots'] = player_shots['total']
marseille_players2['shots_on_target'] = player_shots['on']
marseille_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
marseille_players2['assists'] = player_goals['assists']
marseille_players2['passes'] = player_passes['total']
marseille_players2['passes_completed'] = player_passes['accuracy']
# marseille_players2['pass_accuracy_%'] = df_p1['name']
marseille_players2['dribbles'] = player_dribbles['attempts']
marseille_players2['dribbles_completed'] = player_dribbles['success']
marseille_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
marseille_players2['tackles'] = player_tackles['total']
marseille_players2['blocks'] = player_tackles['blocks']
marseille_players2['interceptions'] = player_tackles['interceptions']
marseille_players2['fouls_drawn'] = player_fouls['drawn']
marseille_players2['fouls_committed'] = player_fouls['committed']
marseille_players2['yellow_cards'] = player_cards['yellow']
marseille_players2['red_cards'] = player_cards['red']
marseille_players2['yellow_to_red_cards'] = player_cards['yellowred']
marseille_players2['sub_in'] = player_subs['in']
marseille_players2['sub_out'] = player_subs['out']

marseille_players2 = marseille_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
marseille_players = pd.concat([marseille_players1, marseille_players2])
marseille_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column







####### METZ  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"112","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
metz_players1 = pd.DataFrame()

metz_players1['name'] = df_p1['name']
metz_players1['first_name'] = df_p1['firstname']
metz_players1['last_name'] = df_p1['lastname']
metz_players1['id'] = df_p1['id']
metz_players1['team'] = player_team['name']
metz_players1['team_id'] = player_team['id']
metz_players1['league'] = player_league['name']
metz_players1['league_id'] = player_league['id']
metz_players1['age'] = df_p1['age']
metz_players1['birth'] = player_birth['date']
metz_players1['nationality'] = df_p1['nationality']
metz_players1['app'] = player_games['appearences']
metz_players1['mins'] = player_games['minutes']
metz_players1['goals'] = player_goals['total']
metz_players1['shots'] = player_shots['total']
metz_players1['shots_on_target'] = player_shots['on']
metz_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
metz_players1['assists'] = player_goals['assists']
metz_players1['passes'] = player_passes['total']
metz_players1['passes_completed'] = player_passes['accuracy']
# metz_players1['pass_accuracy_%'] = df_p1['name']
metz_players1['dribbles'] = player_dribbles['attempts']
metz_players1['dribbles_completed'] = player_dribbles['success']
metz_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
metz_players1['tackles'] = player_tackles['total']
metz_players1['blocks'] = player_tackles['blocks']
metz_players1['interceptions'] = player_tackles['interceptions']
metz_players1['fouls_drawn'] = player_fouls['drawn']
metz_players1['fouls_committed'] = player_fouls['committed']
metz_players1['yellow_cards'] = player_cards['yellow']
metz_players1['red_cards'] = player_cards['red']
metz_players1['yellow_to_red_cards'] = player_cards['yellowred']
metz_players1['sub_in'] = player_subs['in']
metz_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
metz_players1 = metz_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"112","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
metz_players2 = pd.DataFrame()

metz_players2['name'] = df_p1['name']
metz_players2['first_name'] = df_p1['firstname']
metz_players2['last_name'] = df_p1['lastname']
metz_players2['id'] = df_p1['id']
metz_players2['team'] = player_team['name']
metz_players2['team_id'] = player_team['id']
metz_players2['league'] = player_league['name']
metz_players2['league_id'] = player_league['id']
metz_players2['age'] = df_p1['age']
metz_players2['birth'] = player_birth['date']
metz_players2['nationality'] = df_p1['nationality']
metz_players2['app'] = player_games['appearences']
metz_players2['mins'] = player_games['minutes']
metz_players2['goals'] = player_goals['total']
metz_players2['shots'] = player_shots['total']
metz_players2['shots_on_target'] = player_shots['on']
metz_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
metz_players2['assists'] = player_goals['assists']
metz_players2['passes'] = player_passes['total']
metz_players2['passes_completed'] = player_passes['accuracy']
# metz_players2['pass_accuracy_%'] = df_p1['name']
metz_players2['dribbles'] = player_dribbles['attempts']
metz_players2['dribbles_completed'] = player_dribbles['success']
metz_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
metz_players2['tackles'] = player_tackles['total']
metz_players2['blocks'] = player_tackles['blocks']
metz_players2['interceptions'] = player_tackles['interceptions']
metz_players2['fouls_drawn'] = player_fouls['drawn']
metz_players2['fouls_committed'] = player_fouls['committed']
metz_players2['yellow_cards'] = player_cards['yellow']
metz_players2['red_cards'] = player_cards['red']
metz_players2['yellow_to_red_cards'] = player_cards['yellowred']
metz_players2['sub_in'] = player_subs['in']
metz_players2['sub_out'] = player_subs['out']

metz_players2 = metz_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
metz_players = pd.concat([metz_players1, metz_players2])
metz_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column










####### MONACO  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"91","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
monaco_players1 = pd.DataFrame()

monaco_players1['name'] = df_p1['name']
monaco_players1['first_name'] = df_p1['firstname']
monaco_players1['last_name'] = df_p1['lastname']
monaco_players1['id'] = df_p1['id']
monaco_players1['team'] = player_team['name']
monaco_players1['team_id'] = player_team['id']
monaco_players1['league'] = player_league['name']
monaco_players1['league_id'] = player_league['id']
monaco_players1['age'] = df_p1['age']
monaco_players1['birth'] = player_birth['date']
monaco_players1['nationality'] = df_p1['nationality']
monaco_players1['app'] = player_games['appearences']
monaco_players1['mins'] = player_games['minutes']
monaco_players1['goals'] = player_goals['total']
monaco_players1['shots'] = player_shots['total']
monaco_players1['shots_on_target'] = player_shots['on']
monaco_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
monaco_players1['assists'] = player_goals['assists']
monaco_players1['passes'] = player_passes['total']
monaco_players1['passes_completed'] = player_passes['accuracy']
# monaco_players1['pass_accuracy_%'] = df_p1['name']
monaco_players1['dribbles'] = player_dribbles['attempts']
monaco_players1['dribbles_completed'] = player_dribbles['success']
monaco_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
monaco_players1['tackles'] = player_tackles['total']
monaco_players1['blocks'] = player_tackles['blocks']
monaco_players1['interceptions'] = player_tackles['interceptions']
monaco_players1['fouls_drawn'] = player_fouls['drawn']
monaco_players1['fouls_committed'] = player_fouls['committed']
monaco_players1['yellow_cards'] = player_cards['yellow']
monaco_players1['red_cards'] = player_cards['red']
monaco_players1['yellow_to_red_cards'] = player_cards['yellowred']
monaco_players1['sub_in'] = player_subs['in']
monaco_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
monaco_players1 = monaco_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"91","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
monaco_players2 = pd.DataFrame()

monaco_players2['name'] = df_p1['name']
monaco_players2['first_name'] = df_p1['firstname']
monaco_players2['last_name'] = df_p1['lastname']
monaco_players2['id'] = df_p1['id']
monaco_players2['team'] = player_team['name']
monaco_players2['team_id'] = player_team['id']
monaco_players2['league'] = player_league['name']
monaco_players2['league_id'] = player_league['id']
monaco_players2['age'] = df_p1['age']
monaco_players2['birth'] = player_birth['date']
monaco_players2['nationality'] = df_p1['nationality']
monaco_players2['app'] = player_games['appearences']
monaco_players2['mins'] = player_games['minutes']
monaco_players2['goals'] = player_goals['total']
monaco_players2['shots'] = player_shots['total']
monaco_players2['shots_on_target'] = player_shots['on']
monaco_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
monaco_players2['assists'] = player_goals['assists']
monaco_players2['passes'] = player_passes['total']
monaco_players2['passes_completed'] = player_passes['accuracy']
# monaco_players2['pass_accuracy_%'] = df_p1['name']
monaco_players2['dribbles'] = player_dribbles['attempts']
monaco_players2['dribbles_completed'] = player_dribbles['success']
monaco_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
monaco_players2['tackles'] = player_tackles['total']
monaco_players2['blocks'] = player_tackles['blocks']
monaco_players2['interceptions'] = player_tackles['interceptions']
monaco_players2['fouls_drawn'] = player_fouls['drawn']
monaco_players2['fouls_committed'] = player_fouls['committed']
monaco_players2['yellow_cards'] = player_cards['yellow']
monaco_players2['red_cards'] = player_cards['red']
monaco_players2['yellow_to_red_cards'] = player_cards['yellowred']
monaco_players2['sub_in'] = player_subs['in']
monaco_players2['sub_out'] = player_subs['out']

monaco_players2 = monaco_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
monaco_players = pd.concat([monaco_players1, monaco_players2])
monaco_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### MONTPELLIER  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"82","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
montpellier_players1 = pd.DataFrame()

montpellier_players1['name'] = df_p1['name']
montpellier_players1['first_name'] = df_p1['firstname']
montpellier_players1['last_name'] = df_p1['lastname']
montpellier_players1['id'] = df_p1['id']
montpellier_players1['team'] = player_team['name']
montpellier_players1['team_id'] = player_team['id']
montpellier_players1['league'] = player_league['name']
montpellier_players1['league_id'] = player_league['id']
montpellier_players1['age'] = df_p1['age']
montpellier_players1['birth'] = player_birth['date']
montpellier_players1['nationality'] = df_p1['nationality']
montpellier_players1['app'] = player_games['appearences']
montpellier_players1['mins'] = player_games['minutes']
montpellier_players1['goals'] = player_goals['total']
montpellier_players1['shots'] = player_shots['total']
montpellier_players1['shots_on_target'] = player_shots['on']
montpellier_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
montpellier_players1['assists'] = player_goals['assists']
montpellier_players1['passes'] = player_passes['total']
montpellier_players1['passes_completed'] = player_passes['accuracy']
# montpellier_players1['pass_accuracy_%'] = df_p1['name']
montpellier_players1['dribbles'] = player_dribbles['attempts']
montpellier_players1['dribbles_completed'] = player_dribbles['success']
montpellier_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
montpellier_players1['tackles'] = player_tackles['total']
montpellier_players1['blocks'] = player_tackles['blocks']
montpellier_players1['interceptions'] = player_tackles['interceptions']
montpellier_players1['fouls_drawn'] = player_fouls['drawn']
montpellier_players1['fouls_committed'] = player_fouls['committed']
montpellier_players1['yellow_cards'] = player_cards['yellow']
montpellier_players1['red_cards'] = player_cards['red']
montpellier_players1['yellow_to_red_cards'] = player_cards['yellowred']
montpellier_players1['sub_in'] = player_subs['in']
montpellier_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
montpellier_players1 = montpellier_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"82","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
montpellier_players2 = pd.DataFrame()

montpellier_players2['name'] = df_p1['name']
montpellier_players2['first_name'] = df_p1['firstname']
montpellier_players2['last_name'] = df_p1['lastname']
montpellier_players2['id'] = df_p1['id']
montpellier_players2['team'] = player_team['name']
montpellier_players2['team_id'] = player_team['id']
montpellier_players2['league'] = player_league['name']
montpellier_players2['league_id'] = player_league['id']
montpellier_players2['age'] = df_p1['age']
montpellier_players2['birth'] = player_birth['date']
montpellier_players2['nationality'] = df_p1['nationality']
montpellier_players2['app'] = player_games['appearences']
montpellier_players2['mins'] = player_games['minutes']
montpellier_players2['goals'] = player_goals['total']
montpellier_players2['shots'] = player_shots['total']
montpellier_players2['shots_on_target'] = player_shots['on']
montpellier_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
montpellier_players2['assists'] = player_goals['assists']
montpellier_players2['passes'] = player_passes['total']
montpellier_players2['passes_completed'] = player_passes['accuracy']
# montpellier_players2['pass_accuracy_%'] = df_p1['name']
montpellier_players2['dribbles'] = player_dribbles['attempts']
montpellier_players2['dribbles_completed'] = player_dribbles['success']
montpellier_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
montpellier_players2['tackles'] = player_tackles['total']
montpellier_players2['blocks'] = player_tackles['blocks']
montpellier_players2['interceptions'] = player_tackles['interceptions']
montpellier_players2['fouls_drawn'] = player_fouls['drawn']
montpellier_players2['fouls_committed'] = player_fouls['committed']
montpellier_players2['yellow_cards'] = player_cards['yellow']
montpellier_players2['red_cards'] = player_cards['red']
montpellier_players2['yellow_to_red_cards'] = player_cards['yellowred']
montpellier_players2['sub_in'] = player_subs['in']
montpellier_players2['sub_out'] = player_subs['out']

montpellier_players2 = montpellier_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
montpellier_players = pd.concat([montpellier_players1, montpellier_players2])
montpellier_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### NANTES  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"83","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
nantes_players1 = pd.DataFrame()

nantes_players1['name'] = df_p1['name']
nantes_players1['first_name'] = df_p1['firstname']
nantes_players1['last_name'] = df_p1['lastname']
nantes_players1['id'] = df_p1['id']
nantes_players1['team'] = player_team['name']
nantes_players1['team_id'] = player_team['id']
nantes_players1['league'] = player_league['name']
nantes_players1['league_id'] = player_league['id']
nantes_players1['age'] = df_p1['age']
nantes_players1['birth'] = player_birth['date']
nantes_players1['nationality'] = df_p1['nationality']
nantes_players1['app'] = player_games['appearences']
nantes_players1['mins'] = player_games['minutes']
nantes_players1['goals'] = player_goals['total']
nantes_players1['shots'] = player_shots['total']
nantes_players1['shots_on_target'] = player_shots['on']
nantes_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
nantes_players1['assists'] = player_goals['assists']
nantes_players1['passes'] = player_passes['total']
nantes_players1['passes_completed'] = player_passes['accuracy']
# nantes_players1['pass_accuracy_%'] = df_p1['name']
nantes_players1['dribbles'] = player_dribbles['attempts']
nantes_players1['dribbles_completed'] = player_dribbles['success']
nantes_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
nantes_players1['tackles'] = player_tackles['total']
nantes_players1['blocks'] = player_tackles['blocks']
nantes_players1['interceptions'] = player_tackles['interceptions']
nantes_players1['fouls_drawn'] = player_fouls['drawn']
nantes_players1['fouls_committed'] = player_fouls['committed']
nantes_players1['yellow_cards'] = player_cards['yellow']
nantes_players1['red_cards'] = player_cards['red']
nantes_players1['yellow_to_red_cards'] = player_cards['yellowred']
nantes_players1['sub_in'] = player_subs['in']
nantes_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
nantes_players1 = nantes_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"83","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
nantes_players2 = pd.DataFrame()

nantes_players2['name'] = df_p1['name']
nantes_players2['first_name'] = df_p1['firstname']
nantes_players2['last_name'] = df_p1['lastname']
nantes_players2['id'] = df_p1['id']
nantes_players2['team'] = player_team['name']
nantes_players2['team_id'] = player_team['id']
nantes_players2['league'] = player_league['name']
nantes_players2['league_id'] = player_league['id']
nantes_players2['age'] = df_p1['age']
nantes_players2['birth'] = player_birth['date']
nantes_players2['nationality'] = df_p1['nationality']
nantes_players2['app'] = player_games['appearences']
nantes_players2['mins'] = player_games['minutes']
nantes_players2['goals'] = player_goals['total']
nantes_players2['shots'] = player_shots['total']
nantes_players2['shots_on_target'] = player_shots['on']
nantes_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
nantes_players2['assists'] = player_goals['assists']
nantes_players2['passes'] = player_passes['total']
nantes_players2['passes_completed'] = player_passes['accuracy']
# nantes_players2['pass_accuracy_%'] = df_p1['name']
nantes_players2['dribbles'] = player_dribbles['attempts']
nantes_players2['dribbles_completed'] = player_dribbles['success']
nantes_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
nantes_players2['tackles'] = player_tackles['total']
nantes_players2['blocks'] = player_tackles['blocks']
nantes_players2['interceptions'] = player_tackles['interceptions']
nantes_players2['fouls_drawn'] = player_fouls['drawn']
nantes_players2['fouls_committed'] = player_fouls['committed']
nantes_players2['yellow_cards'] = player_cards['yellow']
nantes_players2['red_cards'] = player_cards['red']
nantes_players2['yellow_to_red_cards'] = player_cards['yellowred']
nantes_players2['sub_in'] = player_subs['in']
nantes_players2['sub_out'] = player_subs['out']

nantes_players2 = nantes_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
nantes_players = pd.concat([nantes_players1, nantes_players2])
nantes_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### NICE  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"84","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1', 'data2']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
nice_players1 = pd.DataFrame()

nice_players1['name'] = df_p1['name']
nice_players1['first_name'] = df_p1['firstname']
nice_players1['last_name'] = df_p1['lastname']
nice_players1['id'] = df_p1['id']
nice_players1['team'] = player_team['name']
nice_players1['team_id'] = player_team['id']
nice_players1['league'] = player_league['name']
nice_players1['league_id'] = player_league['id']
nice_players1['age'] = df_p1['age']
nice_players1['birth'] = player_birth['date']
nice_players1['nationality'] = df_p1['nationality']
nice_players1['app'] = player_games['appearences']
nice_players1['mins'] = player_games['minutes']
nice_players1['goals'] = player_goals['total']
nice_players1['shots'] = player_shots['total']
nice_players1['shots_on_target'] = player_shots['on']
nice_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
nice_players1['assists'] = player_goals['assists']
nice_players1['passes'] = player_passes['total']
nice_players1['passes_completed'] = player_passes['accuracy']
# nice_players1['pass_accuracy_%'] = df_p1['name']
nice_players1['dribbles'] = player_dribbles['attempts']
nice_players1['dribbles_completed'] = player_dribbles['success']
nice_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
nice_players1['tackles'] = player_tackles['total']
nice_players1['blocks'] = player_tackles['blocks']
nice_players1['interceptions'] = player_tackles['interceptions']
nice_players1['fouls_drawn'] = player_fouls['drawn']
nice_players1['fouls_committed'] = player_fouls['committed']
nice_players1['yellow_cards'] = player_cards['yellow']
nice_players1['red_cards'] = player_cards['red']
nice_players1['yellow_to_red_cards'] = player_cards['yellowred']
nice_players1['sub_in'] = player_subs['in']
nice_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
nice_players1 = nice_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"84","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
nice_players2 = pd.DataFrame()

nice_players2['name'] = df_p1['name']
nice_players2['first_name'] = df_p1['firstname']
nice_players2['last_name'] = df_p1['lastname']
nice_players2['id'] = df_p1['id']
nice_players2['team'] = player_team['name']
nice_players2['team_id'] = player_team['id']
nice_players2['league'] = player_league['name']
nice_players2['league_id'] = player_league['id']
nice_players2['age'] = df_p1['age']
nice_players2['birth'] = player_birth['date']
nice_players2['nationality'] = df_p1['nationality']
nice_players2['app'] = player_games['appearences']
nice_players2['mins'] = player_games['minutes']
nice_players2['goals'] = player_goals['total']
nice_players2['shots'] = player_shots['total']
nice_players2['shots_on_target'] = player_shots['on']
nice_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
nice_players2['assists'] = player_goals['assists']
nice_players2['passes'] = player_passes['total']
nice_players2['passes_completed'] = player_passes['accuracy']
# nice_players2['pass_accuracy_%'] = df_p1['name']
nice_players2['dribbles'] = player_dribbles['attempts']
nice_players2['dribbles_completed'] = player_dribbles['success']
nice_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
nice_players2['tackles'] = player_tackles['total']
nice_players2['blocks'] = player_tackles['blocks']
nice_players2['interceptions'] = player_tackles['interceptions']
nice_players2['fouls_drawn'] = player_fouls['drawn']
nice_players2['fouls_committed'] = player_fouls['committed']
nice_players2['yellow_cards'] = player_cards['yellow']
nice_players2['red_cards'] = player_cards['red']
nice_players2['yellow_to_red_cards'] = player_cards['yellowred']
nice_players2['sub_in'] = player_subs['in']
nice_players2['sub_out'] = player_subs['out']

nice_players2 = nice_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
nice_players = pd.concat([nice_players1, nice_players2])
nice_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column










####### PARIS SAINT GERMAIN  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"85","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
psg_players1 = pd.DataFrame()

psg_players1['name'] = df_p1['name']
psg_players1['first_name'] = df_p1['firstname']
psg_players1['last_name'] = df_p1['lastname']
psg_players1['id'] = df_p1['id']
psg_players1['team'] = player_team['name']
psg_players1['team_id'] = player_team['id']
psg_players1['league'] = player_league['name']
psg_players1['league_id'] = player_league['id']
psg_players1['age'] = df_p1['age']
psg_players1['birth'] = player_birth['date']
psg_players1['nationality'] = df_p1['nationality']
psg_players1['app'] = player_games['appearences']
psg_players1['mins'] = player_games['minutes']
psg_players1['goals'] = player_goals['total']
psg_players1['shots'] = player_shots['total']
psg_players1['shots_on_target'] = player_shots['on']
psg_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
psg_players1['assists'] = player_goals['assists']
psg_players1['passes'] = player_passes['total']
psg_players1['passes_completed'] = player_passes['accuracy']
# psg_players1['pass_accuracy_%'] = df_p1['name']
psg_players1['dribbles'] = player_dribbles['attempts']
psg_players1['dribbles_completed'] = player_dribbles['success']
psg_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
psg_players1['tackles'] = player_tackles['total']
psg_players1['blocks'] = player_tackles['blocks']
psg_players1['interceptions'] = player_tackles['interceptions']
psg_players1['fouls_drawn'] = player_fouls['drawn']
psg_players1['fouls_committed'] = player_fouls['committed']
psg_players1['yellow_cards'] = player_cards['yellow']
psg_players1['red_cards'] = player_cards['red']
psg_players1['yellow_to_red_cards'] = player_cards['yellowred']
psg_players1['sub_in'] = player_subs['in']
psg_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
psg_players1 = psg_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"85","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data', 'data1']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
psg_players2 = pd.DataFrame()

psg_players2['name'] = df_p1['name']
psg_players2['first_name'] = df_p1['firstname']
psg_players2['last_name'] = df_p1['lastname']
psg_players2['id'] = df_p1['id']
psg_players2['team'] = player_team['name']
psg_players2['team_id'] = player_team['id']
psg_players2['league'] = player_league['name']
psg_players2['league_id'] = player_league['id']
psg_players2['age'] = df_p1['age']
psg_players2['birth'] = player_birth['date']
psg_players2['nationality'] = df_p1['nationality']
psg_players2['app'] = player_games['appearences']
psg_players2['mins'] = player_games['minutes']
psg_players2['goals'] = player_goals['total']
psg_players2['shots'] = player_shots['total']
psg_players2['shots_on_target'] = player_shots['on']
psg_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
psg_players2['assists'] = player_goals['assists']
psg_players2['passes'] = player_passes['total']
psg_players2['passes_completed'] = player_passes['accuracy']
# psg_players2['pass_accuracy_%'] = df_p1['name']
psg_players2['dribbles'] = player_dribbles['attempts']
psg_players2['dribbles_completed'] = player_dribbles['success']
psg_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
psg_players2['tackles'] = player_tackles['total']
psg_players2['blocks'] = player_tackles['blocks']
psg_players2['interceptions'] = player_tackles['interceptions']
psg_players2['fouls_drawn'] = player_fouls['drawn']
psg_players2['fouls_committed'] = player_fouls['committed']
psg_players2['yellow_cards'] = player_cards['yellow']
psg_players2['red_cards'] = player_cards['red']
psg_players2['yellow_to_red_cards'] = player_cards['yellowred']
psg_players2['sub_in'] = player_subs['in']
psg_players2['sub_out'] = player_subs['out']

psg_players2 = psg_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
psg_players = pd.concat([psg_players1, psg_players2])
psg_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column








####### REIMS  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"93","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
reims_players1 = pd.DataFrame()

reims_players1['name'] = df_p1['name']
reims_players1['first_name'] = df_p1['firstname']
reims_players1['last_name'] = df_p1['lastname']
reims_players1['id'] = df_p1['id']
reims_players1['team'] = player_team['name']
reims_players1['team_id'] = player_team['id']
reims_players1['league'] = player_league['name']
reims_players1['league_id'] = player_league['id']
reims_players1['age'] = df_p1['age']
reims_players1['birth'] = player_birth['date']
reims_players1['nationality'] = df_p1['nationality']
reims_players1['app'] = player_games['appearences']
reims_players1['mins'] = player_games['minutes']
reims_players1['goals'] = player_goals['total']
reims_players1['shots'] = player_shots['total']
reims_players1['shots_on_target'] = player_shots['on']
reims_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
reims_players1['assists'] = player_goals['assists']
reims_players1['passes'] = player_passes['total']
reims_players1['passes_completed'] = player_passes['accuracy']
# reims_players1['pass_accuracy_%'] = df_p1['name']
reims_players1['dribbles'] = player_dribbles['attempts']
reims_players1['dribbles_completed'] = player_dribbles['success']
reims_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
reims_players1['tackles'] = player_tackles['total']
reims_players1['blocks'] = player_tackles['blocks']
reims_players1['interceptions'] = player_tackles['interceptions']
reims_players1['fouls_drawn'] = player_fouls['drawn']
reims_players1['fouls_committed'] = player_fouls['committed']
reims_players1['yellow_cards'] = player_cards['yellow']
reims_players1['red_cards'] = player_cards['red']
reims_players1['yellow_to_red_cards'] = player_cards['yellowred']
reims_players1['sub_in'] = player_subs['in']
reims_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
reims_players1 = reims_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"93","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
reims_players2 = pd.DataFrame()

reims_players2['name'] = df_p1['name']
reims_players2['first_name'] = df_p1['firstname']
reims_players2['last_name'] = df_p1['lastname']
reims_players2['id'] = df_p1['id']
reims_players2['team'] = player_team['name']
reims_players2['team_id'] = player_team['id']
reims_players2['league'] = player_league['name']
reims_players2['league_id'] = player_league['id']
reims_players2['age'] = df_p1['age']
reims_players2['birth'] = player_birth['date']
reims_players2['nationality'] = df_p1['nationality']
reims_players2['app'] = player_games['appearences']
reims_players2['mins'] = player_games['minutes']
reims_players2['goals'] = player_goals['total']
reims_players2['shots'] = player_shots['total']
reims_players2['shots_on_target'] = player_shots['on']
reims_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
reims_players2['assists'] = player_goals['assists']
reims_players2['passes'] = player_passes['total']
reims_players2['passes_completed'] = player_passes['accuracy']
# reims_players2['pass_accuracy_%'] = df_p1['name']
reims_players2['dribbles'] = player_dribbles['attempts']
reims_players2['dribbles_completed'] = player_dribbles['success']
reims_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
reims_players2['tackles'] = player_tackles['total']
reims_players2['blocks'] = player_tackles['blocks']
reims_players2['interceptions'] = player_tackles['interceptions']
reims_players2['fouls_drawn'] = player_fouls['drawn']
reims_players2['fouls_committed'] = player_fouls['committed']
reims_players2['yellow_cards'] = player_cards['yellow']
reims_players2['red_cards'] = player_cards['red']
reims_players2['yellow_to_red_cards'] = player_cards['yellowred']
reims_players2['sub_in'] = player_subs['in']
reims_players2['sub_out'] = player_subs['out']

reims_players2 = reims_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
reims_players = pd.concat([reims_players1, reims_players2])
reims_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column





####### RENNES  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"94","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
rennes_players1 = pd.DataFrame()

rennes_players1['name'] = df_p1['name']
rennes_players1['first_name'] = df_p1['firstname']
rennes_players1['last_name'] = df_p1['lastname']
rennes_players1['id'] = df_p1['id']
rennes_players1['team'] = player_team['name']
rennes_players1['team_id'] = player_team['id']
rennes_players1['league'] = player_league['name']
rennes_players1['league_id'] = player_league['id']
rennes_players1['age'] = df_p1['age']
rennes_players1['birth'] = player_birth['date']
rennes_players1['nationality'] = df_p1['nationality']
rennes_players1['app'] = player_games['appearences']
rennes_players1['mins'] = player_games['minutes']
rennes_players1['goals'] = player_goals['total']
rennes_players1['shots'] = player_shots['total']
rennes_players1['shots_on_target'] = player_shots['on']
rennes_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
rennes_players1['assists'] = player_goals['assists']
rennes_players1['passes'] = player_passes['total']
rennes_players1['passes_completed'] = player_passes['accuracy']
# rennes_players1['pass_accuracy_%'] = df_p1['name']
rennes_players1['dribbles'] = player_dribbles['attempts']
rennes_players1['dribbles_completed'] = player_dribbles['success']
rennes_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
rennes_players1['tackles'] = player_tackles['total']
rennes_players1['blocks'] = player_tackles['blocks']
rennes_players1['interceptions'] = player_tackles['interceptions']
rennes_players1['fouls_drawn'] = player_fouls['drawn']
rennes_players1['fouls_committed'] = player_fouls['committed']
rennes_players1['yellow_cards'] = player_cards['yellow']
rennes_players1['red_cards'] = player_cards['red']
rennes_players1['yellow_to_red_cards'] = player_cards['yellowred']
rennes_players1['sub_in'] = player_subs['in']
rennes_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
rennes_players1 = rennes_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"94","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
rennes_players2 = pd.DataFrame()

rennes_players2['name'] = df_p1['name']
rennes_players2['first_name'] = df_p1['firstname']
rennes_players2['last_name'] = df_p1['lastname']
rennes_players2['id'] = df_p1['id']
rennes_players2['team'] = player_team['name']
rennes_players2['team_id'] = player_team['id']
rennes_players2['league'] = player_league['name']
rennes_players2['league_id'] = player_league['id']
rennes_players2['age'] = df_p1['age']
rennes_players2['birth'] = player_birth['date']
rennes_players2['nationality'] = df_p1['nationality']
rennes_players2['app'] = player_games['appearences']
rennes_players2['mins'] = player_games['minutes']
rennes_players2['goals'] = player_goals['total']
rennes_players2['shots'] = player_shots['total']
rennes_players2['shots_on_target'] = player_shots['on']
rennes_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
rennes_players2['assists'] = player_goals['assists']
rennes_players2['passes'] = player_passes['total']
rennes_players2['passes_completed'] = player_passes['accuracy']
# rennes_players2['pass_accuracy_%'] = df_p1['name']
rennes_players2['dribbles'] = player_dribbles['attempts']
rennes_players2['dribbles_completed'] = player_dribbles['success']
rennes_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
rennes_players2['tackles'] = player_tackles['total']
rennes_players2['blocks'] = player_tackles['blocks']
rennes_players2['interceptions'] = player_tackles['interceptions']
rennes_players2['fouls_drawn'] = player_fouls['drawn']
rennes_players2['fouls_committed'] = player_fouls['committed']
rennes_players2['yellow_cards'] = player_cards['yellow']
rennes_players2['red_cards'] = player_cards['red']
rennes_players2['yellow_to_red_cards'] = player_cards['yellowred']
rennes_players2['sub_in'] = player_subs['in']
rennes_players2['sub_out'] = player_subs['out']

rennes_players2 = rennes_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
rennes_players = pd.concat([rennes_players1, rennes_players2])
rennes_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### SAINT ETIENNE  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"1063","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
saint_etienne_players1 = pd.DataFrame()

saint_etienne_players1['name'] = df_p1['name']
saint_etienne_players1['first_name'] = df_p1['firstname']
saint_etienne_players1['last_name'] = df_p1['lastname']
saint_etienne_players1['id'] = df_p1['id']
saint_etienne_players1['team'] = player_team['name']
saint_etienne_players1['team_id'] = player_team['id']
saint_etienne_players1['league'] = player_league['name']
saint_etienne_players1['league_id'] = player_league['id']
saint_etienne_players1['age'] = df_p1['age']
saint_etienne_players1['birth'] = player_birth['date']
saint_etienne_players1['nationality'] = df_p1['nationality']
saint_etienne_players1['app'] = player_games['appearences']
saint_etienne_players1['mins'] = player_games['minutes']
saint_etienne_players1['goals'] = player_goals['total']
saint_etienne_players1['shots'] = player_shots['total']
saint_etienne_players1['shots_on_target'] = player_shots['on']
saint_etienne_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
saint_etienne_players1['assists'] = player_goals['assists']
saint_etienne_players1['passes'] = player_passes['total']
saint_etienne_players1['passes_completed'] = player_passes['accuracy']
# saint_etienne_players1['pass_accuracy_%'] = df_p1['name']
saint_etienne_players1['dribbles'] = player_dribbles['attempts']
saint_etienne_players1['dribbles_completed'] = player_dribbles['success']
saint_etienne_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
saint_etienne_players1['tackles'] = player_tackles['total']
saint_etienne_players1['blocks'] = player_tackles['blocks']
saint_etienne_players1['interceptions'] = player_tackles['interceptions']
saint_etienne_players1['fouls_drawn'] = player_fouls['drawn']
saint_etienne_players1['fouls_committed'] = player_fouls['committed']
saint_etienne_players1['yellow_cards'] = player_cards['yellow']
saint_etienne_players1['red_cards'] = player_cards['red']
saint_etienne_players1['yellow_to_red_cards'] = player_cards['yellowred']
saint_etienne_players1['sub_in'] = player_subs['in']
saint_etienne_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
saint_etienne_players1 = saint_etienne_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"1063","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
saint_etienne_players2 = pd.DataFrame()

saint_etienne_players2['name'] = df_p1['name']
saint_etienne_players2['first_name'] = df_p1['firstname']
saint_etienne_players2['last_name'] = df_p1['lastname']
saint_etienne_players2['id'] = df_p1['id']
saint_etienne_players2['team'] = player_team['name']
saint_etienne_players2['team_id'] = player_team['id']
saint_etienne_players2['league'] = player_league['name']
saint_etienne_players2['league_id'] = player_league['id']
saint_etienne_players2['age'] = df_p1['age']
saint_etienne_players2['birth'] = player_birth['date']
saint_etienne_players2['nationality'] = df_p1['nationality']
saint_etienne_players2['app'] = player_games['appearences']
saint_etienne_players2['mins'] = player_games['minutes']
saint_etienne_players2['goals'] = player_goals['total']
saint_etienne_players2['shots'] = player_shots['total']
saint_etienne_players2['shots_on_target'] = player_shots['on']
saint_etienne_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
saint_etienne_players2['assists'] = player_goals['assists']
saint_etienne_players2['passes'] = player_passes['total']
saint_etienne_players2['passes_completed'] = player_passes['accuracy']
# saint_etienne_players2['pass_accuracy_%'] = df_p1['name']
saint_etienne_players2['dribbles'] = player_dribbles['attempts']
saint_etienne_players2['dribbles_completed'] = player_dribbles['success']
saint_etienne_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
saint_etienne_players2['tackles'] = player_tackles['total']
saint_etienne_players2['blocks'] = player_tackles['blocks']
saint_etienne_players2['interceptions'] = player_tackles['interceptions']
saint_etienne_players2['fouls_drawn'] = player_fouls['drawn']
saint_etienne_players2['fouls_committed'] = player_fouls['committed']
saint_etienne_players2['yellow_cards'] = player_cards['yellow']
saint_etienne_players2['red_cards'] = player_cards['red']
saint_etienne_players2['yellow_to_red_cards'] = player_cards['yellowred']
saint_etienne_players2['sub_in'] = player_subs['in']
saint_etienne_players2['sub_out'] = player_subs['out']

saint_etienne_players2 = saint_etienne_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
saint_etienne_players = pd.concat([saint_etienne_players1, saint_etienne_players2])
saint_etienne_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column






####### STADE BRESTOIS  ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"106","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
stade_brestois_players1 = pd.DataFrame()

stade_brestois_players1['name'] = df_p1['name']
stade_brestois_players1['first_name'] = df_p1['firstname']
stade_brestois_players1['last_name'] = df_p1['lastname']
stade_brestois_players1['id'] = df_p1['id']
stade_brestois_players1['team'] = player_team['name']
stade_brestois_players1['team_id'] = player_team['id']
stade_brestois_players1['league'] = player_league['name']
stade_brestois_players1['league_id'] = player_league['id']
stade_brestois_players1['age'] = df_p1['age']
stade_brestois_players1['birth'] = player_birth['date']
stade_brestois_players1['nationality'] = df_p1['nationality']
stade_brestois_players1['app'] = player_games['appearences']
stade_brestois_players1['mins'] = player_games['minutes']
stade_brestois_players1['goals'] = player_goals['total']
stade_brestois_players1['shots'] = player_shots['total']
stade_brestois_players1['shots_on_target'] = player_shots['on']
stade_brestois_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
stade_brestois_players1['assists'] = player_goals['assists']
stade_brestois_players1['passes'] = player_passes['total']
stade_brestois_players1['passes_completed'] = player_passes['accuracy']
# stade_brestois_players1['pass_accuracy_%'] = df_p1['name']
stade_brestois_players1['dribbles'] = player_dribbles['attempts']
stade_brestois_players1['dribbles_completed'] = player_dribbles['success']
stade_brestois_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
stade_brestois_players1['tackles'] = player_tackles['total']
stade_brestois_players1['blocks'] = player_tackles['blocks']
stade_brestois_players1['interceptions'] = player_tackles['interceptions']
stade_brestois_players1['fouls_drawn'] = player_fouls['drawn']
stade_brestois_players1['fouls_committed'] = player_fouls['committed']
stade_brestois_players1['yellow_cards'] = player_cards['yellow']
stade_brestois_players1['red_cards'] = player_cards['red']
stade_brestois_players1['yellow_to_red_cards'] = player_cards['yellowred']
stade_brestois_players1['sub_in'] = player_subs['in']
stade_brestois_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
stade_brestois_players1 = stade_brestois_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"106","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
stade_brestois_players2 = pd.DataFrame()

stade_brestois_players2['name'] = df_p1['name']
stade_brestois_players2['first_name'] = df_p1['firstname']
stade_brestois_players2['last_name'] = df_p1['lastname']
stade_brestois_players2['id'] = df_p1['id']
stade_brestois_players2['team'] = player_team['name']
stade_brestois_players2['team_id'] = player_team['id']
stade_brestois_players2['league'] = player_league['name']
stade_brestois_players2['league_id'] = player_league['id']
stade_brestois_players2['age'] = df_p1['age']
stade_brestois_players2['birth'] = player_birth['date']
stade_brestois_players2['nationality'] = df_p1['nationality']
stade_brestois_players2['app'] = player_games['appearences']
stade_brestois_players2['mins'] = player_games['minutes']
stade_brestois_players2['goals'] = player_goals['total']
stade_brestois_players2['shots'] = player_shots['total']
stade_brestois_players2['shots_on_target'] = player_shots['on']
stade_brestois_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
stade_brestois_players2['assists'] = player_goals['assists']
stade_brestois_players2['passes'] = player_passes['total']
stade_brestois_players2['passes_completed'] = player_passes['accuracy']
# stade_brestois_players2['pass_accuracy_%'] = df_p1['name']
stade_brestois_players2['dribbles'] = player_dribbles['attempts']
stade_brestois_players2['dribbles_completed'] = player_dribbles['success']
stade_brestois_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
stade_brestois_players2['tackles'] = player_tackles['total']
stade_brestois_players2['blocks'] = player_tackles['blocks']
stade_brestois_players2['interceptions'] = player_tackles['interceptions']
stade_brestois_players2['fouls_drawn'] = player_fouls['drawn']
stade_brestois_players2['fouls_committed'] = player_fouls['committed']
stade_brestois_players2['yellow_cards'] = player_cards['yellow']
stade_brestois_players2['red_cards'] = player_cards['red']
stade_brestois_players2['yellow_to_red_cards'] = player_cards['yellowred']
stade_brestois_players2['sub_in'] = player_subs['in']
stade_brestois_players2['sub_out'] = player_subs['out']

stade_brestois_players2 = stade_brestois_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
stade_brestois_players = pd.concat([stade_brestois_players1, stade_brestois_players2])
stade_brestois_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column










####### STRASBOURG   ######



# Stage 1: Import Players' Data via API call

## Players per League

# Get the list of players per team in each European league 

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"95","season":"2021","page":"1"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)


# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players
df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)



# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics
df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)


# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)



# Create data frame for the first set of imported players 
strasbourg_players1 = pd.DataFrame()

strasbourg_players1['name'] = df_p1['name']
strasbourg_players1['first_name'] = df_p1['firstname']
strasbourg_players1['last_name'] = df_p1['lastname']
strasbourg_players1['id'] = df_p1['id']
strasbourg_players1['team'] = player_team['name']
strasbourg_players1['team_id'] = player_team['id']
strasbourg_players1['league'] = player_league['name']
strasbourg_players1['league_id'] = player_league['id']
strasbourg_players1['age'] = df_p1['age']
strasbourg_players1['birth'] = player_birth['date']
strasbourg_players1['nationality'] = df_p1['nationality']
strasbourg_players1['app'] = player_games['appearences']
strasbourg_players1['mins'] = player_games['minutes']
strasbourg_players1['goals'] = player_goals['total']
strasbourg_players1['shots'] = player_shots['total']
strasbourg_players1['shots_on_target'] = player_shots['on']
strasbourg_players1['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
strasbourg_players1['assists'] = player_goals['assists']
strasbourg_players1['passes'] = player_passes['total']
strasbourg_players1['passes_completed'] = player_passes['accuracy']
# strasbourg_players1['pass_accuracy_%'] = df_p1['name']
strasbourg_players1['dribbles'] = player_dribbles['attempts']
strasbourg_players1['dribbles_completed'] = player_dribbles['success']
strasbourg_players1['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
strasbourg_players1['tackles'] = player_tackles['total']
strasbourg_players1['blocks'] = player_tackles['blocks']
strasbourg_players1['interceptions'] = player_tackles['interceptions']
strasbourg_players1['fouls_drawn'] = player_fouls['drawn']
strasbourg_players1['fouls_committed'] = player_fouls['committed']
strasbourg_players1['yellow_cards'] = player_cards['yellow']
strasbourg_players1['red_cards'] = player_cards['red']
strasbourg_players1['yellow_to_red_cards'] = player_cards['yellowred']
strasbourg_players1['sub_in'] = player_subs['in']
strasbourg_players1['sub_out'] = player_subs['out']


# Replace 'NaN' values with '0'
strasbourg_players1 = strasbourg_players1.fillna(0)



# Stage 2: Append New Players' Data   
#### Append the other team mates into the main players' data frame



API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/players"
querystring = {"team":"95","season":"2021","page":"2"} # change page no to find other players per team 

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# The JSON response contains each team nested in a JSON format
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Players

df_p = pd.DataFrame(temp)
df_p1 = df_p['player'].apply(pd.Series)

# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
# Statistics

df_p2 = df_p['statistics'].apply(pd.Series)
df_p2.columns = ['data']
df_p3 = df_p2['data'].apply(pd.Series)

# Create mini data frames to feed our sub-dataframe
player_team = df_p3['team'].apply(pd.Series)
player_league = df_p3['league'].apply(pd.Series)
player_games = df_p3['games'].apply(pd.Series)
player_subs = df_p3['substitutes'].apply(pd.Series)
player_shots = df_p3['shots'].apply(pd.Series)
player_goals = df_p3['goals'].apply(pd.Series)
player_passes = df_p3['passes'].apply(pd.Series)
player_dribbles = df_p3['dribbles'].apply(pd.Series)
player_tackles = df_p3['tackles'].apply(pd.Series)
player_duels = df_p3['duels'].apply(pd.Series)
player_fouls = df_p3['fouls'].apply(pd.Series)
player_cards = df_p3['cards'].apply(pd.Series)
player_penalties = df_p3['penalty'].apply(pd.Series)
player_birth = df_p1['birth'].apply(pd.Series)





# Create data frame for the first set of imported players 
strasbourg_players2 = pd.DataFrame()

strasbourg_players2['name'] = df_p1['name']
strasbourg_players2['first_name'] = df_p1['firstname']
strasbourg_players2['last_name'] = df_p1['lastname']
strasbourg_players2['id'] = df_p1['id']
strasbourg_players2['team'] = player_team['name']
strasbourg_players2['team_id'] = player_team['id']
strasbourg_players2['league'] = player_league['name']
strasbourg_players2['league_id'] = player_league['id']
strasbourg_players2['age'] = df_p1['age']
strasbourg_players2['birth'] = player_birth['date']
strasbourg_players2['nationality'] = df_p1['nationality']
strasbourg_players2['app'] = player_games['appearences']
strasbourg_players2['mins'] = player_games['minutes']
strasbourg_players2['goals'] = player_goals['total']
strasbourg_players2['shots'] = player_shots['total']
strasbourg_players2['shots_on_target'] = player_shots['on']
strasbourg_players2['shot_accuracy_%'] = player_shots['on'] % player_shots['total']
strasbourg_players2['assists'] = player_goals['assists']
strasbourg_players2['passes'] = player_passes['total']
strasbourg_players2['passes_completed'] = player_passes['accuracy']
# strasbourg_players2['pass_accuracy_%'] = df_p1['name']
strasbourg_players2['dribbles'] = player_dribbles['attempts']
strasbourg_players2['dribbles_completed'] = player_dribbles['success']
strasbourg_players2['dribble_accuracy'] = player_dribbles['success'] % player_dribbles['attempts']
strasbourg_players2['tackles'] = player_tackles['total']
strasbourg_players2['blocks'] = player_tackles['blocks']
strasbourg_players2['interceptions'] = player_tackles['interceptions']
strasbourg_players2['fouls_drawn'] = player_fouls['drawn']
strasbourg_players2['fouls_committed'] = player_fouls['committed']
strasbourg_players2['yellow_cards'] = player_cards['yellow']
strasbourg_players2['red_cards'] = player_cards['red']
strasbourg_players2['yellow_to_red_cards'] = player_cards['yellowred']
strasbourg_players2['sub_in'] = player_subs['in']
strasbourg_players2['sub_out'] = player_subs['out']

strasbourg_players2 = strasbourg_players2.fillna(0)





# Stage 3: Concatenate all data frames for the team's players
strasbourg_players = pd.concat([strasbourg_players1, strasbourg_players2])
strasbourg_players.reset_index(inplace=True, drop=True) # the index will keep restarting for each df, so restart it and drop the original index column







# Combine players from all teams in the league into a single data frame
ligue_1_players = pd.concat([angers_players,
					bordeaux_players,
					clermont_foot_players,
					estac_troyes_players,
					lens_players,
					lille_players,
					lorient_players,
					lyon_players,
					marseille_players,
					metz_players,
					monaco_players,
					montpellier_players,
					nantes_players,
					nice_players,
					psg_players,
					reims_players,
					rennes_players,
					saint_etienne_players,
					stade_brestois_players,
					strasbourg_players
					], ignore_index=True)



# Combine all players together into one data frame 
players = pd.concat([prem_league_players, 
                     bundesliga_players, 
                     la_liga_players, 
                     serie_a_players, 
                     ligue_1_players
                     ], ignore_index=True)













