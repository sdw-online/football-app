# -*- coding: utf-8 -*-
"""
Author: Stephen David-Williams
Purpose: To extract general team stats from RapidAPI via API call.


"""


#--------------------------------------------------------TEAMS--------------------------------------------------------------


#### Let's begin pulling the teams into Python to add to our app

import requests
import pandas as pd
import explode
import csv
import os

## Teams per League



####################################### 1. ENGLISH PREMIER LEAGUE ##############################################



# Get the list of teams in England's top flight

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/teams"
querystring = {"league":"39","season":"2021"}

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# Pass the json response to a variable 
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
df_t = pd.DataFrame(temp)


# Premier League Teams
prem_teams = df_t['team'].apply(pd.Series)
prem_teams = prem_teams.sort_values(by='name')
print(prem_teams.to_string(index=False))   # to hide row index

# Premier League Clubs' Venues
prem_venues = df_t['venue'].apply(pd.Series)






####### ARSENAL ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"42"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
arsenal = pd.DataFrame()

arsenal['team_name'] = temp1['team.name']
arsenal['team_id'] = temp1['team.id']
arsenal['league_name'] = temp1['league.name']
arsenal['league_id'] = temp1['league.id']
arsenal['fixtures.played'] = fixtures['total']
arsenal['fixtures.home'] = fixtures['home']
arsenal['fixtures.away'] = fixtures['away']
arsenal['goals'] = goals['total']
arsenal['goals_home'] = goals['home']
arsenal['goals_away'] = goals['away']
arsenal['most_goals_scored'] = b_goals_scored['total']
arsenal['most_goals_conceded'] = b_goals_conceded['total']
arsenal['clean_sheets'] = temp1['clean_sheet.total']
arsenal['penalties_scored'] = pens_scored['total']
arsenal['penalties_missed'] = pens_missed['total']
arsenal['yellow_cards'] = y_cards_final['total']
arsenal['red_cards'] = r_cards_final['total']






####### ASTON VILLA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"66"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
aston_villa = pd.DataFrame()

aston_villa['team_name'] = temp1['team.name']
aston_villa['team_id'] = temp1['team.id']
aston_villa['league_name'] = temp1['league.name']
aston_villa['league_id'] = temp1['league.id']
aston_villa['fixtures.played'] = fixtures['total']
aston_villa['fixtures.home'] = fixtures['home']
aston_villa['fixtures.away'] = fixtures['away']
aston_villa['goals'] = goals['total']
aston_villa['goals_home'] = goals['home']
aston_villa['goals_away'] = goals['away']
aston_villa['most_goals_scored'] = b_goals_scored['total']
aston_villa['most_goals_conceded'] = b_goals_conceded['total']
aston_villa['clean_sheets'] = temp1['clean_sheet.total']
aston_villa['penalties_scored'] = pens_scored['total']
aston_villa['penalties_missed'] = pens_missed['total']
aston_villa['yellow_cards'] = y_cards_final['total']
aston_villa['red_cards'] = r_cards_final['total']





####### BRENTFORD ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"55"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
brentford = pd.DataFrame()

brentford['team_name'] = temp1['team.name']
brentford['team_id'] = temp1['team.id']
brentford['league_name'] = temp1['league.name']
brentford['league_id'] = temp1['league.id']
brentford['fixtures.played'] = fixtures['total']
brentford['fixtures.home'] = fixtures['home']
brentford['fixtures.away'] = fixtures['away']
brentford['goals'] = goals['total']
brentford['goals_home'] = goals['home']
brentford['goals_away'] = goals['away']
brentford['most_goals_scored'] = b_goals_scored['total']
brentford['most_goals_conceded'] = b_goals_conceded['total']
brentford['clean_sheets'] = temp1['clean_sheet.total']
brentford['penalties_scored'] = pens_scored['total']
brentford['penalties_missed'] = pens_missed['total']
brentford['yellow_cards'] = y_cards_final['total']
brentford['red_cards'] = r_cards_final['total']





####### BRIGHTON ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"51"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
brighton = pd.DataFrame()

brighton['team_name'] = temp1['team.name']
brighton['team_id'] = temp1['team.id']
brighton['league_name'] = temp1['league.name']
brighton['league_id'] = temp1['league.id']
brighton['fixtures.played'] = fixtures['total']
brighton['fixtures.home'] = fixtures['home']
brighton['fixtures.away'] = fixtures['away']
brighton['goals'] = goals['total']
brighton['goals_home'] = goals['home']
brighton['goals_away'] = goals['away']
brighton['most_goals_scored'] = b_goals_scored['total']
brighton['most_goals_conceded'] = b_goals_conceded['total']
brighton['clean_sheets'] = temp1['clean_sheet.total']
brighton['penalties_scored'] = pens_scored['total']
brighton['penalties_missed'] = pens_missed['total']
brighton['yellow_cards'] = y_cards_final['total']
brighton['red_cards'] = r_cards_final['total']




####### BURNLEY ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"44"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
burnley = pd.DataFrame()

burnley['team_name'] = temp1['team.name']
burnley['team_id'] = temp1['team.id']
burnley['league_name'] = temp1['league.name']
burnley['league_id'] = temp1['league.id']
burnley['fixtures.played'] = fixtures['total']
burnley['fixtures.home'] = fixtures['home']
burnley['fixtures.away'] = fixtures['away']
burnley['goals'] = goals['total']
burnley['goals_home'] = goals['home']
burnley['goals_away'] = goals['away']
burnley['most_goals_scored'] = b_goals_scored['total']
burnley['most_goals_conceded'] = b_goals_conceded['total']
burnley['clean_sheets'] = temp1['clean_sheet.total']
burnley['penalties_scored'] = pens_scored['total']
burnley['penalties_missed'] = pens_missed['total']
burnley['yellow_cards'] = y_cards_final['total']
burnley['red_cards'] = r_cards_final['total']





####### CHELSEA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"49"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
chelsea = pd.DataFrame()

chelsea['team_name'] = temp1['team.name']
chelsea['team_id'] = temp1['team.id']
chelsea['league_name'] = temp1['league.name']
chelsea['league_id'] = temp1['league.id']
chelsea['fixtures.played'] = fixtures['total']
chelsea['fixtures.home'] = fixtures['home']
chelsea['fixtures.away'] = fixtures['away']
chelsea['goals'] = goals['total']
chelsea['goals_home'] = goals['home']
chelsea['goals_away'] = goals['away']
chelsea['most_goals_scored'] = b_goals_scored['total']
chelsea['most_goals_conceded'] = b_goals_conceded['total']
chelsea['clean_sheets'] = temp1['clean_sheet.total']
chelsea['penalties_scored'] = pens_scored['total']
chelsea['penalties_missed'] = pens_missed['total']
chelsea['yellow_cards'] = y_cards_final['total']
chelsea['red_cards'] = r_cards_final['total']





####### CRYSTAL PALACE ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"52"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
crystal_palace = pd.DataFrame()

crystal_palace['team_name'] = temp1['team.name']
crystal_palace['team_id'] = temp1['team.id']
crystal_palace['league_name'] = temp1['league.name']
crystal_palace['league_id'] = temp1['league.id']
crystal_palace['fixtures.played'] = fixtures['total']
crystal_palace['fixtures.home'] = fixtures['home']
crystal_palace['fixtures.away'] = fixtures['away']
crystal_palace['goals'] = goals['total']
crystal_palace['goals_home'] = goals['home']
crystal_palace['goals_away'] = goals['away']
crystal_palace['most_goals_scored'] = b_goals_scored['total']
crystal_palace['most_goals_conceded'] = b_goals_conceded['total']
crystal_palace['clean_sheets'] = temp1['clean_sheet.total']
crystal_palace['penalties_scored'] = pens_scored['total']
crystal_palace['penalties_missed'] = pens_missed['total']
crystal_palace['yellow_cards'] = y_cards_final['total']
crystal_palace['red_cards'] = r_cards_final['total']





####### EVERTON ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"45"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
everton = pd.DataFrame()

everton['team_name'] = temp1['team.name']
everton['team_id'] = temp1['team.id']
everton['league_name'] = temp1['league.name']
everton['league_id'] = temp1['league.id']
everton['fixtures.played'] = fixtures['total']
everton['fixtures.home'] = fixtures['home']
everton['fixtures.away'] = fixtures['away']
everton['goals'] = goals['total']
everton['goals_home'] = goals['home']
everton['goals_away'] = goals['away']
everton['most_goals_scored'] = b_goals_scored['total']
everton['most_goals_conceded'] = b_goals_conceded['total']
everton['clean_sheets'] = temp1['clean_sheet.total']
everton['penalties_scored'] = pens_scored['total']
everton['penalties_missed'] = pens_missed['total']
everton['yellow_cards'] = y_cards_final['total']
everton['red_cards'] = r_cards_final['total']






####### LEEDS ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"63"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
leeds = pd.DataFrame()

leeds['team_name'] = temp1['team.name']
leeds['team_id'] = temp1['team.id']
leeds['league_name'] = temp1['league.name']
leeds['league_id'] = temp1['league.id']
leeds['fixtures.played'] = fixtures['total']
leeds['fixtures.home'] = fixtures['home']
leeds['fixtures.away'] = fixtures['away']
leeds['goals'] = goals['total']
leeds['goals_home'] = goals['home']
leeds['goals_away'] = goals['away']
leeds['most_goals_scored'] = b_goals_scored['total']
leeds['most_goals_conceded'] = b_goals_conceded['total']
leeds['clean_sheets'] = temp1['clean_sheet.total']
leeds['penalties_scored'] = pens_scored['total']
leeds['penalties_missed'] = pens_missed['total']
leeds['yellow_cards'] = y_cards_final['total']
leeds['red_cards'] = r_cards_final['total']





####### LEICESTER CITY ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"46"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
leicester = pd.DataFrame()

leicester['team_name'] = temp1['team.name']
leicester['team_id'] = temp1['team.id']
leicester['league_name'] = temp1['league.name']
leicester['league_id'] = temp1['league.id']
leicester['fixtures.played'] = fixtures['total']
leicester['fixtures.home'] = fixtures['home']
leicester['fixtures.away'] = fixtures['away']
leicester['goals'] = goals['total']
leicester['goals_home'] = goals['home']
leicester['goals_away'] = goals['away']
leicester['most_goals_scored'] = b_goals_scored['total']
leicester['most_goals_conceded'] = b_goals_conceded['total']
leicester['clean_sheets'] = temp1['clean_sheet.total']
leicester['penalties_scored'] = pens_scored['total']
leicester['penalties_missed'] = pens_missed['total']
leicester['yellow_cards'] = y_cards_final['total']
leicester['red_cards'] = r_cards_final['total']





####### LIVERPOOL ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"40"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
liverpool = pd.DataFrame()

liverpool['team_name'] = temp1['team.name']
liverpool['team_id'] = temp1['team.id']
liverpool['league_name'] = temp1['league.name']
liverpool['league_id'] = temp1['league.id']
liverpool['fixtures.played'] = fixtures['total']
liverpool['fixtures.home'] = fixtures['home']
liverpool['fixtures.away'] = fixtures['away']
liverpool['goals'] = goals['total']
liverpool['goals_home'] = goals['home']
liverpool['goals_away'] = goals['away']
liverpool['most_goals_scored'] = b_goals_scored['total']
liverpool['most_goals_conceded'] = b_goals_conceded['total']
liverpool['clean_sheets'] = temp1['clean_sheet.total']
liverpool['penalties_scored'] = pens_scored['total']
liverpool['penalties_missed'] = pens_missed['total']
liverpool['yellow_cards'] = y_cards_final['total']
liverpool['red_cards'] = r_cards_final['total']





####### MANCHESTER CITY ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"50"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
man_city = pd.DataFrame()

man_city['team_name'] = temp1['team.name']
man_city['team_id'] = temp1['team.id']
man_city['league_name'] = temp1['league.name']
man_city['league_id'] = temp1['league.id']
man_city['fixtures.played'] = fixtures['total']
man_city['fixtures.home'] = fixtures['home']
man_city['fixtures.away'] = fixtures['away']
man_city['goals'] = goals['total']
man_city['goals_home'] = goals['home']
man_city['goals_away'] = goals['away']
man_city['most_goals_scored'] = b_goals_scored['total']
man_city['most_goals_conceded'] = b_goals_conceded['total']
man_city['clean_sheets'] = temp1['clean_sheet.total']
man_city['penalties_scored'] = pens_scored['total']
man_city['penalties_missed'] = pens_missed['total']
man_city['yellow_cards'] = y_cards_final['total']
man_city['red_cards'] = r_cards_final['total']






####### MANCHESTER UTD ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"33"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
man_utd = pd.DataFrame()

man_utd['team_name'] = temp1['team.name']
man_utd['team_id'] = temp1['team.id']
man_utd['league_name'] = temp1['league.name']
man_utd['league_id'] = temp1['league.id']
man_utd['fixtures.played'] = fixtures['total']
man_utd['fixtures.home'] = fixtures['home']
man_utd['fixtures.away'] = fixtures['away']
man_utd['goals'] = goals['total']
man_utd['goals_home'] = goals['home']
man_utd['goals_away'] = goals['away']
man_utd['most_goals_scored'] = b_goals_scored['total']
man_utd['most_goals_conceded'] = b_goals_conceded['total']
man_utd['clean_sheets'] = temp1['clean_sheet.total']
man_utd['penalties_scored'] = pens_scored['total']
man_utd['penalties_missed'] = pens_missed['total']
man_utd['yellow_cards'] = y_cards_final['total']
man_utd['red_cards'] = r_cards_final['total']






####### NEWCASTLE UTD ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"34"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
newcastle = pd.DataFrame()

newcastle['team_name'] = temp1['team.name']
newcastle['team_id'] = temp1['team.id']
newcastle['league_name'] = temp1['league.name']
newcastle['league_id'] = temp1['league.id']
newcastle['fixtures.played'] = fixtures['total']
newcastle['fixtures.home'] = fixtures['home']
newcastle['fixtures.away'] = fixtures['away']
newcastle['goals'] = goals['total']
newcastle['goals_home'] = goals['home']
newcastle['goals_away'] = goals['away']
newcastle['most_goals_scored'] = b_goals_scored['total']
newcastle['most_goals_conceded'] = b_goals_conceded['total']
newcastle['clean_sheets'] = temp1['clean_sheet.total']
newcastle['penalties_scored'] = pens_scored['total']
newcastle['penalties_missed'] = pens_missed['total']
newcastle['yellow_cards'] = y_cards_final['total']
newcastle['red_cards'] = r_cards_final['total']






####### NORWICH  ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"71"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
norwich = pd.DataFrame()

norwich['team_name'] = temp1['team.name']
norwich['team_id'] = temp1['team.id']
norwich['league_name'] = temp1['league.name']
norwich['league_id'] = temp1['league.id']
norwich['fixtures.played'] = fixtures['total']
norwich['fixtures.home'] = fixtures['home']
norwich['fixtures.away'] = fixtures['away']
norwich['goals'] = goals['total']
norwich['goals_home'] = goals['home']
norwich['goals_away'] = goals['away']
norwich['most_goals_scored'] = b_goals_scored['total']
norwich['most_goals_conceded'] = b_goals_conceded['total']
norwich['clean_sheets'] = temp1['clean_sheet.total']
norwich['penalties_scored'] = pens_scored['total']
norwich['penalties_missed'] = pens_missed['total']
norwich['yellow_cards'] = y_cards_final['total']
norwich['red_cards'] = r_cards_final['total']





####### SOUTHAMPTON  ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"41"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
southampton = pd.DataFrame()

southampton['team_name'] = temp1['team.name']
southampton['team_id'] = temp1['team.id']
southampton['league_name'] = temp1['league.name']
southampton['league_id'] = temp1['league.id']
southampton['fixtures.played'] = fixtures['total']
southampton['fixtures.home'] = fixtures['home']
southampton['fixtures.away'] = fixtures['away']
southampton['goals'] = goals['total']
southampton['goals_home'] = goals['home']
southampton['goals_away'] = goals['away']
southampton['most_goals_scored'] = b_goals_scored['total']
southampton['most_goals_conceded'] = b_goals_conceded['total']
southampton['clean_sheets'] = temp1['clean_sheet.total']
southampton['penalties_scored'] = pens_scored['total']
southampton['penalties_missed'] = pens_missed['total']
southampton['yellow_cards'] = y_cards_final['total']
southampton['red_cards'] = r_cards_final['total']




####### SPURS  ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"47"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
spurs = pd.DataFrame()

spurs['team_name'] = temp1['team.name']
spurs['team_id'] = temp1['team.id']
spurs['league_name'] = temp1['league.name']
spurs['league_id'] = temp1['league.id']
spurs['fixtures.played'] = fixtures['total']
spurs['fixtures.home'] = fixtures['home']
spurs['fixtures.away'] = fixtures['away']
spurs['goals'] = goals['total']
spurs['goals_home'] = goals['home']
spurs['goals_away'] = goals['away']
spurs['most_goals_scored'] = b_goals_scored['total']
spurs['most_goals_conceded'] = b_goals_conceded['total']
spurs['clean_sheets'] = temp1['clean_sheet.total']
spurs['penalties_scored'] = pens_scored['total']
spurs['penalties_missed'] = pens_missed['total']
spurs['yellow_cards'] = y_cards_final['total']
spurs['red_cards'] = r_cards_final['total']





####### WATFORD ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"38"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
watford = pd.DataFrame()

watford['team_name'] = temp1['team.name']
watford['team_id'] = temp1['team.id']
watford['league_name'] = temp1['league.name']
watford['league_id'] = temp1['league.id']
watford['fixtures.played'] = fixtures['total']
watford['fixtures.home'] = fixtures['home']
watford['fixtures.away'] = fixtures['away']
watford['goals'] = goals['total']
watford['goals_home'] = goals['home']
watford['goals_away'] = goals['away']
watford['most_goals_scored'] = b_goals_scored['total']
watford['most_goals_conceded'] = b_goals_conceded['total']
watford['clean_sheets'] = temp1['clean_sheet.total']
watford['penalties_scored'] = pens_scored['total']
watford['penalties_missed'] = pens_missed['total']
watford['yellow_cards'] = y_cards_final['total']
watford['red_cards'] = r_cards_final['total']





####### WEST HAM ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"48"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
west_ham = pd.DataFrame()

west_ham['team_name'] = temp1['team.name']
west_ham['team_id'] = temp1['team.id']
west_ham['league_name'] = temp1['league.name']
west_ham['league_id'] = temp1['league.id']
west_ham['fixtures.played'] = fixtures['total']
west_ham['fixtures.home'] = fixtures['home']
west_ham['fixtures.away'] = fixtures['away']
west_ham['goals'] = goals['total']
west_ham['goals_home'] = goals['home']
west_ham['goals_away'] = goals['away']
west_ham['most_goals_scored'] = b_goals_scored['total']
west_ham['most_goals_conceded'] = b_goals_conceded['total']
west_ham['clean_sheets'] = temp1['clean_sheet.total']
west_ham['penalties_scored'] = pens_scored['total']
west_ham['penalties_missed'] = pens_missed['total']
west_ham['yellow_cards'] = y_cards_final['total']
west_ham['red_cards'] = r_cards_final['total']






####### WOLVERHAMPTON  ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"39","season":"2021","team":"39"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
wolves = pd.DataFrame()

wolves['team_name'] = temp1['team.name']
wolves['team_id'] = temp1['team.id']
wolves['league_name'] = temp1['league.name']
wolves['league_id'] = temp1['league.id']
wolves['fixtures.played'] = fixtures['total']
wolves['fixtures.home'] = fixtures['home']
wolves['fixtures.away'] = fixtures['away']
wolves['goals'] = goals['total']
wolves['goals_home'] = goals['home']
wolves['goals_away'] = goals['away']
wolves['most_goals_scored'] = b_goals_scored['total']
wolves['most_goals_conceded'] = b_goals_conceded['total']
wolves['clean_sheets'] = temp1['clean_sheet.total']
wolves['penalties_scored'] = pens_scored['total']
wolves['penalties_missed'] = pens_missed['total']
wolves['yellow_cards'] = y_cards_final['total']
wolves['red_cards'] = r_cards_final['total']




############################################################################################################################################################################################

# Append all the TEAMS in this league to ONE data frame

prem_league = pd.concat([arsenal, aston_villa, brentford, brighton, burnley, chelsea, crystal_palace, everton, leeds, leicester, liverpool, man_city, man_utd, newcastle, norwich, southampton, spurs, watford, wolves], ignore_index=True)



# Data frames to list
#prem_league = [arsenal.columns.values.tolist()] 
#arsenal_list =  arsenal.values.tolist()
#aston_villa_list = aston_villa.values.tolist()
#spurs_list = spurs.values.tolist()
#wolves_list = wolves.values.tolist()
#prem_league.append(arsenal_list)












####################################### 2. BUNDESLIGA ##############################################



# Get the list of teams in Germany's top flight

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/teams"
querystring = {"league":"78","season":"2021"}

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# Pass the json response to a variable 
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
df_t = pd.DataFrame(temp)


# Bundesliga teams
bundesliga_teams = df_t['team'].apply(pd.Series)
bundesliga_teams = bundesliga_teams.sort_values(by='name')
print(bundesliga_teams.to_string(index=False))   # to hide row index

# Bundesliga clubs' venues
bundesliga_venues = df_t['venue'].apply(pd.Series)







####### 1899 HOFFENHEIM ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"167"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
hoffenheim = pd.DataFrame()

hoffenheim['team_name'] = temp1['team.name']
hoffenheim['team_id'] = temp1['team.id']
hoffenheim['league_name'] = 'Bundesliga'
hoffenheim['league_id'] = temp1['league.id']
hoffenheim['fixtures.played'] = fixtures['total']
hoffenheim['fixtures.home'] = fixtures['home']
hoffenheim['fixtures.away'] = fixtures['away']
hoffenheim['goals'] = goals['total']
hoffenheim['goals_home'] = goals['home']
hoffenheim['goals_away'] = goals['away']
hoffenheim['most_goals_scored'] = b_goals_scored['total']
hoffenheim['most_goals_conceded'] = b_goals_conceded['total']
hoffenheim['clean_sheets'] = temp1['clean_sheet.total']
hoffenheim['penalties_scored'] = pens_scored['total']
hoffenheim['penalties_missed'] = pens_missed['total']
hoffenheim['yellow_cards'] = y_cards_final['total']
hoffenheim['red_cards'] = r_cards_final['total']




####### BIELEFELD ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"188"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
bielefeld = pd.DataFrame()

bielefeld['team_name'] = temp1['team.name']
bielefeld['team_id'] = temp1['team.id']
bielefeld['league_name'] = 'Bundesliga'
bielefeld['league_id'] = temp1['league.id']
bielefeld['fixtures.played'] = fixtures['total']
bielefeld['fixtures.home'] = fixtures['home']
bielefeld['fixtures.away'] = fixtures['away']
bielefeld['goals'] = goals['total']
bielefeld['goals_home'] = goals['home']
bielefeld['goals_away'] = goals['away']
bielefeld['most_goals_scored'] = b_goals_scored['total']
bielefeld['most_goals_conceded'] = b_goals_conceded['total']
bielefeld['clean_sheets'] = temp1['clean_sheet.total']
bielefeld['penalties_scored'] = pens_scored['total']
bielefeld['penalties_missed'] = pens_missed['total']
bielefeld['yellow_cards'] = y_cards_final['total']
bielefeld['red_cards'] = r_cards_final['total']




####### BAYERN LEVERKUSEN ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"168"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
leverkusen = pd.DataFrame()

leverkusen['team_name'] = temp1['team.name']
leverkusen['team_id'] = temp1['team.id']
leverkusen['league_name'] = 'Bundesliga'
leverkusen['league_id'] = temp1['league.id']
leverkusen['fixtures.played'] = fixtures['total']
leverkusen['fixtures.home'] = fixtures['home']
leverkusen['fixtures.away'] = fixtures['away']
leverkusen['goals'] = goals['total']
leverkusen['goals_home'] = goals['home']
leverkusen['goals_away'] = goals['away']
leverkusen['most_goals_scored'] = b_goals_scored['total']
leverkusen['most_goals_conceded'] = b_goals_conceded['total']
leverkusen['clean_sheets'] = temp1['clean_sheet.total']
leverkusen['penalties_scored'] = pens_scored['total']
leverkusen['penalties_missed'] = pens_missed['total']
leverkusen['yellow_cards'] = y_cards_final['total']
leverkusen['red_cards'] = r_cards_final['total']





####### BAYERN MUNICH ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"157"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
bayern_munich = pd.DataFrame()

bayern_munich['team_name'] = temp1['team.name']
bayern_munich['team_id'] = temp1['team.id']
bayern_munich['league_name'] = 'Bundesliga'
bayern_munich['league_id'] = temp1['league.id']
bayern_munich['fixtures.played'] = fixtures['total']
bayern_munich['fixtures.home'] = fixtures['home']
bayern_munich['fixtures.away'] = fixtures['away']
bayern_munich['goals'] = goals['total']
bayern_munich['goals_home'] = goals['home']
bayern_munich['goals_away'] = goals['away']
bayern_munich['most_goals_scored'] = b_goals_scored['total']
bayern_munich['most_goals_conceded'] = b_goals_conceded['total']
bayern_munich['clean_sheets'] = temp1['clean_sheet.total']
bayern_munich['penalties_scored'] = pens_scored['total']
bayern_munich['penalties_missed'] = pens_missed['total']
bayern_munich['yellow_cards'] = y_cards_final['total']
bayern_munich['red_cards'] = r_cards_final['total']






####### BORUSSIA DORTMUND ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"165"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
dortmund = pd.DataFrame()

dortmund['team_name'] = temp1['team.name']
dortmund['team_id'] = temp1['team.id']
dortmund['league_name'] = 'Bundesliga'
dortmund['league_id'] = temp1['league.id']
dortmund['fixtures.played'] = fixtures['total']
dortmund['fixtures.home'] = fixtures['home']
dortmund['fixtures.away'] = fixtures['away']
dortmund['goals'] = goals['total']
dortmund['goals_home'] = goals['home']
dortmund['goals_away'] = goals['away']
dortmund['most_goals_scored'] = b_goals_scored['total']
dortmund['most_goals_conceded'] = b_goals_conceded['total']
dortmund['clean_sheets'] = temp1['clean_sheet.total']
dortmund['penalties_scored'] = pens_scored['total']
dortmund['penalties_missed'] = pens_missed['total']
dortmund['yellow_cards'] = y_cards_final['total']
dortmund['red_cards'] = r_cards_final['total']



####### BORUSSIA MONCHENGLADBACH ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"163"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
monchengladbach = pd.DataFrame()

monchengladbach['team_name'] = temp1['team.name']
monchengladbach['team_id'] = temp1['team.id']
monchengladbach['league_name'] = 'Bundesliga'
monchengladbach['league_id'] = temp1['league.id']
monchengladbach['fixtures.played'] = fixtures['total']
monchengladbach['fixtures.home'] = fixtures['home']
monchengladbach['fixtures.away'] = fixtures['away']
monchengladbach['goals'] = goals['total']
monchengladbach['goals_home'] = goals['home']
monchengladbach['goals_away'] = goals['away']
monchengladbach['most_goals_scored'] = b_goals_scored['total']
monchengladbach['most_goals_conceded'] = b_goals_conceded['total']
monchengladbach['clean_sheets'] = temp1['clean_sheet.total']
monchengladbach['penalties_scored'] = pens_scored['total']
monchengladbach['penalties_missed'] = pens_missed['total']
monchengladbach['yellow_cards'] = y_cards_final['total']
monchengladbach['red_cards'] = r_cards_final['total']





####### FRANKFURT ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"169"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
frankfurt = pd.DataFrame()

frankfurt['team_name'] = temp1['team.name']
frankfurt['team_id'] = temp1['team.id']
frankfurt['league_name'] = 'Bundesliga'
frankfurt['league_id'] = temp1['league.id']
frankfurt['fixtures.played'] = fixtures['total']
frankfurt['fixtures.home'] = fixtures['home']
frankfurt['fixtures.away'] = fixtures['away']
frankfurt['goals'] = goals['total']
frankfurt['goals_home'] = goals['home']
frankfurt['goals_away'] = goals['away']
frankfurt['most_goals_scored'] = b_goals_scored['total']
frankfurt['most_goals_conceded'] = b_goals_conceded['total']
frankfurt['clean_sheets'] = temp1['clean_sheet.total']
frankfurt['penalties_scored'] = pens_scored['total']
frankfurt['penalties_missed'] = pens_missed['total']
frankfurt['yellow_cards'] = y_cards_final['total']
frankfurt['red_cards'] = r_cards_final['total']





####### FC AUGSBURG ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"170"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
augsburg = pd.DataFrame()

augsburg['team_name'] = temp1['team.name']
augsburg['team_id'] = temp1['team.id']
augsburg['league_name'] = 'Bundesliga'
augsburg['league_id'] = temp1['league.id']
augsburg['fixtures.played'] = fixtures['total']
augsburg['fixtures.home'] = fixtures['home']
augsburg['fixtures.away'] = fixtures['away']
augsburg['goals'] = goals['total']
augsburg['goals_home'] = goals['home']
augsburg['goals_away'] = goals['away']
augsburg['most_goals_scored'] = b_goals_scored['total']
augsburg['most_goals_conceded'] = b_goals_conceded['total']
augsburg['clean_sheets'] = temp1['clean_sheet.total']
augsburg['penalties_scored'] = pens_scored['total']
augsburg['penalties_missed'] = pens_missed['total']
augsburg['yellow_cards'] = y_cards_final['total']
augsburg['red_cards'] = r_cards_final['total']






####### FC KOLN ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"192"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
koln = pd.DataFrame()

koln['team_name'] = temp1['team.name']
koln['team_id'] = temp1['team.id']
koln['league_name'] = 'Bundesliga'
koln['league_id'] = temp1['league.id']
koln['fixtures.played'] = fixtures['total']
koln['fixtures.home'] = fixtures['home']
koln['fixtures.away'] = fixtures['away']
koln['goals'] = goals['total']
koln['goals_home'] = goals['home']
koln['goals_away'] = goals['away']
koln['most_goals_scored'] = b_goals_scored['total']
koln['most_goals_conceded'] = b_goals_conceded['total']
koln['clean_sheets'] = temp1['clean_sheet.total']
koln['penalties_scored'] = pens_scored['total']
koln['penalties_missed'] = pens_missed['total']
koln['yellow_cards'] = y_cards_final['total']
koln['red_cards'] = r_cards_final['total']





####### FSV MAINZ ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"164"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
mainz = pd.DataFrame()

mainz['team_name'] = temp1['team.name']
mainz['team_id'] = temp1['team.id']
mainz['league_name'] = 'Bundesliga'
mainz['league_id'] = temp1['league.id']
mainz['fixtures.played'] = fixtures['total']
mainz['fixtures.home'] = fixtures['home']
mainz['fixtures.away'] = fixtures['away']
mainz['goals'] = goals['total']
mainz['goals_home'] = goals['home']
mainz['goals_away'] = goals['away']
mainz['most_goals_scored'] = b_goals_scored['total']
mainz['most_goals_conceded'] = b_goals_conceded['total']
mainz['clean_sheets'] = temp1['clean_sheet.total']
mainz['penalties_scored'] = pens_scored['total']
mainz['penalties_missed'] = pens_missed['total']
mainz['yellow_cards'] = y_cards_final['total']
mainz['red_cards'] = r_cards_final['total']






####### HERTHA BERLIN ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"159"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
hertha_berlin = pd.DataFrame()

hertha_berlin['team_name'] = temp1['team.name']
hertha_berlin['team_id'] = temp1['team.id']
hertha_berlin['league_name'] = 'Bundesliga'
hertha_berlin['league_id'] = temp1['league.id']
hertha_berlin['fixtures.played'] = fixtures['total']
hertha_berlin['fixtures.home'] = fixtures['home']
hertha_berlin['fixtures.away'] = fixtures['away']
hertha_berlin['goals'] = goals['total']
hertha_berlin['goals_home'] = goals['home']
hertha_berlin['goals_away'] = goals['away']
hertha_berlin['most_goals_scored'] = b_goals_scored['total']
hertha_berlin['most_goals_conceded'] = b_goals_conceded['total']
hertha_berlin['clean_sheets'] = temp1['clean_sheet.total']
hertha_berlin['penalties_scored'] = pens_scored['total']
hertha_berlin['penalties_missed'] = pens_missed['total']
hertha_berlin['yellow_cards'] = y_cards_final['total']
hertha_berlin['red_cards'] = r_cards_final['total']






####### RB LEIPZIG ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"173"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
leipzig = pd.DataFrame()

leipzig['team_name'] = temp1['team.name']
leipzig['team_id'] = temp1['team.id']
leipzig['league_name'] = 'Bundesliga'
leipzig['league_id'] = temp1['league.id']
leipzig['fixtures.played'] = fixtures['total']
leipzig['fixtures.home'] = fixtures['home']
leipzig['fixtures.away'] = fixtures['away']
leipzig['goals'] = goals['total']
leipzig['goals_home'] = goals['home']
leipzig['goals_away'] = goals['away']
leipzig['most_goals_scored'] = b_goals_scored['total']
leipzig['most_goals_conceded'] = b_goals_conceded['total']
leipzig['clean_sheets'] = temp1['clean_sheet.total']
leipzig['penalties_scored'] = pens_scored['total']
leipzig['penalties_missed'] = pens_missed['total']
leipzig['yellow_cards'] = y_cards_final['total']
leipzig['red_cards'] = r_cards_final['total']






####### SC FREIBURG ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"160"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
freiburg = pd.DataFrame()

freiburg['team_name'] = temp1['team.name']
freiburg['team_id'] = temp1['team.id']
freiburg['league_name'] = 'Bundesliga'
freiburg['league_id'] = temp1['league.id']
freiburg['fixtures.played'] = fixtures['total']
freiburg['fixtures.home'] = fixtures['home']
freiburg['fixtures.away'] = fixtures['away']
freiburg['goals'] = goals['total']
freiburg['goals_home'] = goals['home']
freiburg['goals_away'] = goals['away']
freiburg['most_goals_scored'] = b_goals_scored['total']
freiburg['most_goals_conceded'] = b_goals_conceded['total']
freiburg['clean_sheets'] = temp1['clean_sheet.total']
freiburg['penalties_scored'] = pens_scored['total']
freiburg['penalties_missed'] = pens_missed['total']
freiburg['yellow_cards'] = y_cards_final['total']
freiburg['red_cards'] = r_cards_final['total']






####### SPVGG GREUTHER FURTH ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"178"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
greuther_furth = pd.DataFrame()

greuther_furth['team_name'] = temp1['team.name']
greuther_furth['team_id'] = temp1['team.id']
greuther_furth['league_name'] = 'Bundesliga'
greuther_furth['league_id'] = temp1['league.id']
greuther_furth['fixtures.played'] = fixtures['total']
greuther_furth['fixtures.home'] = fixtures['home']
greuther_furth['fixtures.away'] = fixtures['away']
greuther_furth['goals'] = goals['total']
greuther_furth['goals_home'] = goals['home']
greuther_furth['goals_away'] = goals['away']
greuther_furth['most_goals_scored'] = b_goals_scored['total']
greuther_furth['most_goals_conceded'] = b_goals_conceded['total']
greuther_furth['clean_sheets'] = temp1['clean_sheet.total']
greuther_furth['penalties_scored'] = pens_scored['total']
greuther_furth['penalties_missed'] = pens_missed['total']
greuther_furth['yellow_cards'] = y_cards_final['total']
greuther_furth['red_cards'] = r_cards_final['total']






####### UNION BERLIN ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"182"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
union_berlin = pd.DataFrame()

union_berlin['team_name'] = temp1['team.name']
union_berlin['team_id'] = temp1['team.id']
union_berlin['league_name'] = 'Bundesliga'
union_berlin['league_id'] = temp1['league.id']
union_berlin['fixtures.played'] = fixtures['total']
union_berlin['fixtures.home'] = fixtures['home']
union_berlin['fixtures.away'] = fixtures['away']
union_berlin['goals'] = goals['total']
union_berlin['goals_home'] = goals['home']
union_berlin['goals_away'] = goals['away']
union_berlin['most_goals_scored'] = b_goals_scored['total']
union_berlin['most_goals_conceded'] = b_goals_conceded['total']
union_berlin['clean_sheets'] = temp1['clean_sheet.total']
union_berlin['penalties_scored'] = pens_scored['total']
union_berlin['penalties_missed'] = pens_missed['total']
union_berlin['yellow_cards'] = y_cards_final['total']
union_berlin['red_cards'] = r_cards_final['total']






####### VFB STUTTGART ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"172"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
stuttgart = pd.DataFrame()

stuttgart['team_name'] = temp1['team.name']
stuttgart['team_id'] = temp1['team.id']
stuttgart['league_name'] = 'Bundesliga'
stuttgart['league_id'] = temp1['league.id']
stuttgart['fixtures.played'] = fixtures['total']
stuttgart['fixtures.home'] = fixtures['home']
stuttgart['fixtures.away'] = fixtures['away']
stuttgart['goals'] = goals['total']
stuttgart['goals_home'] = goals['home']
stuttgart['goals_away'] = goals['away']
stuttgart['most_goals_scored'] = b_goals_scored['total']
stuttgart['most_goals_conceded'] = b_goals_conceded['total']
stuttgart['clean_sheets'] = temp1['clean_sheet.total']
stuttgart['penalties_scored'] = pens_scored['total']
stuttgart['penalties_missed'] = pens_missed['total']
stuttgart['yellow_cards'] = y_cards_final['total']
stuttgart['red_cards'] = r_cards_final['total']






####### VFL BOCHUM ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"176"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
vfl_bochum = pd.DataFrame()

vfl_bochum['team_name'] = temp1['team.name']
vfl_bochum['team_id'] = temp1['team.id']
vfl_bochum['league_name'] = 'Bundesliga'
vfl_bochum['league_id'] = temp1['league.id']
vfl_bochum['fixtures.played'] = fixtures['total']
vfl_bochum['fixtures.home'] = fixtures['home']
vfl_bochum['fixtures.away'] = fixtures['away']
vfl_bochum['goals'] = goals['total']
vfl_bochum['goals_home'] = goals['home']
vfl_bochum['goals_away'] = goals['away']
vfl_bochum['most_goals_scored'] = b_goals_scored['total']
vfl_bochum['most_goals_conceded'] = b_goals_conceded['total']
vfl_bochum['clean_sheets'] = temp1['clean_sheet.total']
vfl_bochum['penalties_scored'] = pens_scored['total']
vfl_bochum['penalties_missed'] = pens_missed['total']
vfl_bochum['yellow_cards'] = y_cards_final['total']
vfl_bochum['red_cards'] = r_cards_final['total']






####### VFL WOLFSBURG ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"78","season":"2021","team":"161"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
wolfsburg = pd.DataFrame()

wolfsburg['team_name'] = temp1['team.name']
wolfsburg['team_id'] = temp1['team.id']
wolfsburg['league_name'] = 'Bundesliga'
wolfsburg['league_id'] = temp1['league.id']
wolfsburg['fixtures.played'] = fixtures['total']
wolfsburg['fixtures.home'] = fixtures['home']
wolfsburg['fixtures.away'] = fixtures['away']
wolfsburg['goals'] = goals['total']
wolfsburg['goals_home'] = goals['home']
wolfsburg['goals_away'] = goals['away']
wolfsburg['most_goals_scored'] = b_goals_scored['total']
wolfsburg['most_goals_conceded'] = b_goals_conceded['total']
wolfsburg['clean_sheets'] = temp1['clean_sheet.total']
wolfsburg['penalties_scored'] = pens_scored['total']
wolfsburg['penalties_missed'] = pens_missed['total']
wolfsburg['yellow_cards'] = y_cards_final['total']
wolfsburg['red_cards'] = r_cards_final['total']




############################################################################################################################################################################################

# Append all the TEAMS in this league to ONE data frame

prem_league = pd.concat([arsenal,
							aston_villa,
							brentford,
							burnley,
							brighton,
							chelsea,
							crystal_palace,
							everton,
							leeds,
							leicester,
							liverpool,
							man_city,
							man_utd,
							newcastle,
							norwich,
							southampton,
							spurs,
							watford,
							west_ham,
							wolves
							], ignore_index=True)



# Data frames to list
#prem_league = [arsenal.columns.values.tolist()] 
#arsenal_list =  arsenal.values.tolist()
#aston_villa_list = aston_villa.values.tolist()
#spurs_list = spurs.values.tolist()
#wolves_list = wolves.values.tolist()
#prem_league.append(arsenal_list)

bundesliga = pd.concat([hoffenheim,
						bielefeld,
						leverkusen,
						bayern_munich,
						dortmund,
						monchengladbach,
						frankfurt,
						augsburg,
						koln,
						mainz,
						hertha_berlin,
						leipzig,
						freiburg,
						greuther_furth,
						union_berlin,
						stuttgart,
						vfl_bochum,
						wolfsburg
 
						], ignore_index = True)






						
						
						
						
						



####################################### 3. LA LIGA ##############################################



# Get the list of teams in Spain's top flight

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/teams"
querystring = {"league":"140","season":"2021"}

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# Pass the json response to a variable 
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
df_t = pd.DataFrame(temp)


# Premier League Teams
prem_teams = df_t['team'].apply(pd.Series)
prem_teams = prem_teams.sort_values(by='name')
print(prem_teams.to_string(index=False))   # to hide row index

# Premier League Clubs' Venues
prem_venues = df_t['venue'].apply(pd.Series)






####### ALAVES ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"542"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
alaves = pd.DataFrame()

alaves['team_name'] = temp1['team.name']
alaves['team_id'] = temp1['team.id']
alaves['league_name'] = temp1['league.name']
alaves['league_id'] = temp1['league.id']
alaves['fixtures.played'] = fixtures['total']
alaves['fixtures.home'] = fixtures['home']
alaves['fixtures.away'] = fixtures['away']
alaves['goals'] = goals['total']
alaves['goals_home'] = goals['home']
alaves['goals_away'] = goals['away']
alaves['most_goals_scored'] = b_goals_scored['total']
alaves['most_goals_conceded'] = b_goals_conceded['total']
alaves['clean_sheets'] = temp1['clean_sheet.total']
alaves['penalties_scored'] = pens_scored['total']
alaves['penalties_missed'] = pens_missed['total']
alaves['yellow_cards'] = y_cards_final['total']
alaves['red_cards'] = r_cards_final['total']










####### ATHLETIC CLUB ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"531"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
athletic_club = pd.DataFrame()

athletic_club['team_name'] = temp1['team.name']
athletic_club['team_id'] = temp1['team.id']
athletic_club['league_name'] = temp1['league.name']
athletic_club['league_id'] = temp1['league.id']
athletic_club['fixtures.played'] = fixtures['total']
athletic_club['fixtures.home'] = fixtures['home']
athletic_club['fixtures.away'] = fixtures['away']
athletic_club['goals'] = goals['total']
athletic_club['goals_home'] = goals['home']
athletic_club['goals_away'] = goals['away']
athletic_club['most_goals_scored'] = b_goals_scored['total']
athletic_club['most_goals_conceded'] = b_goals_conceded['total']
athletic_club['clean_sheets'] = temp1['clean_sheet.total']
athletic_club['penalties_scored'] = pens_scored['total']
athletic_club['penalties_missed'] = pens_missed['total']
athletic_club['yellow_cards'] = y_cards_final['total']
athletic_club['red_cards'] = r_cards_final['total']









####### ATHLETICO MADRID ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"530"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
athletico_madrid = pd.DataFrame()

athletico_madrid['team_name'] = temp1['team.name']
athletico_madrid['team_id'] = temp1['team.id']
athletico_madrid['league_name'] = temp1['league.name']
athletico_madrid['league_id'] = temp1['league.id']
athletico_madrid['fixtures.played'] = fixtures['total']
athletico_madrid['fixtures.home'] = fixtures['home']
athletico_madrid['fixtures.away'] = fixtures['away']
athletico_madrid['goals'] = goals['total']
athletico_madrid['goals_home'] = goals['home']
athletico_madrid['goals_away'] = goals['away']
athletico_madrid['most_goals_scored'] = b_goals_scored['total']
athletico_madrid['most_goals_conceded'] = b_goals_conceded['total']
athletico_madrid['clean_sheets'] = temp1['clean_sheet.total']
athletico_madrid['penalties_scored'] = pens_scored['total']
athletico_madrid['penalties_missed'] = pens_missed['total']
athletico_madrid['yellow_cards'] = y_cards_final['total']
athletico_madrid['red_cards'] = r_cards_final['total']






####### BARCELONA FC ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"529"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
barcelona = pd.DataFrame()

barcelona['team_name'] = temp1['team.name']
barcelona['team_id'] = temp1['team.id']
barcelona['league_name'] = temp1['league.name']
barcelona['league_id'] = temp1['league.id']
barcelona['fixtures.played'] = fixtures['total']
barcelona['fixtures.home'] = fixtures['home']
barcelona['fixtures.away'] = fixtures['away']
barcelona['goals'] = goals['total']
barcelona['goals_home'] = goals['home']
barcelona['goals_away'] = goals['away']
barcelona['most_goals_scored'] = b_goals_scored['total']
barcelona['most_goals_conceded'] = b_goals_conceded['total']
barcelona['clean_sheets'] = temp1['clean_sheet.total']
barcelona['penalties_scored'] = pens_scored['total']
barcelona['penalties_missed'] = pens_missed['total']
barcelona['yellow_cards'] = y_cards_final['total']
barcelona['red_cards'] = r_cards_final['total']






####### CADIZ ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"724"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
cadiz = pd.DataFrame()

cadiz['team_name'] = temp1['team.name']
cadiz['team_id'] = temp1['team.id']
cadiz['league_name'] = temp1['league.name']
cadiz['league_id'] = temp1['league.id']
cadiz['fixtures.played'] = fixtures['total']
cadiz['fixtures.home'] = fixtures['home']
cadiz['fixtures.away'] = fixtures['away']
cadiz['goals'] = goals['total']
cadiz['goals_home'] = goals['home']
cadiz['goals_away'] = goals['away']
cadiz['most_goals_scored'] = b_goals_scored['total']
cadiz['most_goals_conceded'] = b_goals_conceded['total']
cadiz['clean_sheets'] = temp1['clean_sheet.total']
cadiz['penalties_scored'] = pens_scored['total']
cadiz['penalties_missed'] = pens_missed['total']
cadiz['yellow_cards'] = y_cards_final['total']
cadiz['red_cards'] = r_cards_final['total']






####### CELTA VIGO ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"538"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
celta_vigo = pd.DataFrame()

celta_vigo['team_name'] = temp1['team.name']
celta_vigo['team_id'] = temp1['team.id']
celta_vigo['league_name'] = temp1['league.name']
celta_vigo['league_id'] = temp1['league.id']
celta_vigo['fixtures.played'] = fixtures['total']
celta_vigo['fixtures.home'] = fixtures['home']
celta_vigo['fixtures.away'] = fixtures['away']
celta_vigo['goals'] = goals['total']
celta_vigo['goals_home'] = goals['home']
celta_vigo['goals_away'] = goals['away']
celta_vigo['most_goals_scored'] = b_goals_scored['total']
celta_vigo['most_goals_conceded'] = b_goals_conceded['total']
celta_vigo['clean_sheets'] = temp1['clean_sheet.total']
celta_vigo['penalties_scored'] = pens_scored['total']
celta_vigo['penalties_missed'] = pens_missed['total']
celta_vigo['yellow_cards'] = y_cards_final['total']
celta_vigo['red_cards'] = r_cards_final['total']






####### ELCHE ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"797"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
elche = pd.DataFrame()

elche['team_name'] = temp1['team.name']
elche['team_id'] = temp1['team.id']
elche['league_name'] = temp1['league.name']
elche['league_id'] = temp1['league.id']
elche['fixtures.played'] = fixtures['total']
elche['fixtures.home'] = fixtures['home']
elche['fixtures.away'] = fixtures['away']
elche['goals'] = goals['total']
elche['goals_home'] = goals['home']
elche['goals_away'] = goals['away']
elche['most_goals_scored'] = b_goals_scored['total']
elche['most_goals_conceded'] = b_goals_conceded['total']
elche['clean_sheets'] = temp1['clean_sheet.total']
elche['penalties_scored'] = pens_scored['total']
elche['penalties_missed'] = pens_missed['total']
elche['yellow_cards'] = y_cards_final['total']
elche['red_cards'] = r_cards_final['total']






####### ESPANYOL ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"540"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
espanyol = pd.DataFrame()

espanyol['team_name'] = temp1['team.name']
espanyol['team_id'] = temp1['team.id']
espanyol['league_name'] = temp1['league.name']
espanyol['league_id'] = temp1['league.id']
espanyol['fixtures.played'] = fixtures['total']
espanyol['fixtures.home'] = fixtures['home']
espanyol['fixtures.away'] = fixtures['away']
espanyol['goals'] = goals['total']
espanyol['goals_home'] = goals['home']
espanyol['goals_away'] = goals['away']
espanyol['most_goals_scored'] = b_goals_scored['total']
espanyol['most_goals_conceded'] = b_goals_conceded['total']
espanyol['clean_sheets'] = temp1['clean_sheet.total']
espanyol['penalties_scored'] = pens_scored['total']
espanyol['penalties_missed'] = pens_missed['total']
espanyol['yellow_cards'] = y_cards_final['total']
espanyol['red_cards'] = r_cards_final['total']






####### GETAFE ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"546"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
getafe = pd.DataFrame()

getafe['team_name'] = temp1['team.name']
getafe['team_id'] = temp1['team.id']
getafe['league_name'] = temp1['league.name']
getafe['league_id'] = temp1['league.id']
getafe['fixtures.played'] = fixtures['total']
getafe['fixtures.home'] = fixtures['home']
getafe['fixtures.away'] = fixtures['away']
getafe['goals'] = goals['total']
getafe['goals_home'] = goals['home']
getafe['goals_away'] = goals['away']
getafe['most_goals_scored'] = b_goals_scored['total']
getafe['most_goals_conceded'] = b_goals_conceded['total']
getafe['clean_sheets'] = temp1['clean_sheet.total']
getafe['penalties_scored'] = pens_scored['total']
getafe['penalties_missed'] = pens_missed['total']
getafe['yellow_cards'] = y_cards_final['total']
getafe['red_cards'] = r_cards_final['total']






####### GRANADA CF ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"715"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
granada = pd.DataFrame()

granada['team_name'] = temp1['team.name']
granada['team_id'] = temp1['team.id']
granada['league_name'] = temp1['league.name']
granada['league_id'] = temp1['league.id']
granada['fixtures.played'] = fixtures['total']
granada['fixtures.home'] = fixtures['home']
granada['fixtures.away'] = fixtures['away']
granada['goals'] = goals['total']
granada['goals_home'] = goals['home']
granada['goals_away'] = goals['away']
granada['most_goals_scored'] = b_goals_scored['total']
granada['most_goals_conceded'] = b_goals_conceded['total']
granada['clean_sheets'] = temp1['clean_sheet.total']
granada['penalties_scored'] = pens_scored['total']
granada['penalties_missed'] = pens_missed['total']
granada['yellow_cards'] = y_cards_final['total']
granada['red_cards'] = r_cards_final['total']






####### LEVANTE ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"539"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
levante = pd.DataFrame()

levante['team_name'] = temp1['team.name']
levante['team_id'] = temp1['team.id']
levante['league_name'] = temp1['league.name']
levante['league_id'] = temp1['league.id']
levante['fixtures.played'] = fixtures['total']
levante['fixtures.home'] = fixtures['home']
levante['fixtures.away'] = fixtures['away']
levante['goals'] = goals['total']
levante['goals_home'] = goals['home']
levante['goals_away'] = goals['away']
levante['most_goals_scored'] = b_goals_scored['total']
levante['most_goals_conceded'] = b_goals_conceded['total']
levante['clean_sheets'] = temp1['clean_sheet.total']
levante['penalties_scored'] = pens_scored['total']
levante['penalties_missed'] = pens_missed['total']
levante['yellow_cards'] = y_cards_final['total']
levante['red_cards'] = r_cards_final['total']






####### MALLORCA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"798"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
mallorca = pd.DataFrame()

mallorca['team_name'] = temp1['team.name']
mallorca['team_id'] = temp1['team.id']
mallorca['league_name'] = temp1['league.name']
mallorca['league_id'] = temp1['league.id']
mallorca['fixtures.played'] = fixtures['total']
mallorca['fixtures.home'] = fixtures['home']
mallorca['fixtures.away'] = fixtures['away']
mallorca['goals'] = goals['total']
mallorca['goals_home'] = goals['home']
mallorca['goals_away'] = goals['away']
mallorca['most_goals_scored'] = b_goals_scored['total']
mallorca['most_goals_conceded'] = b_goals_conceded['total']
mallorca['clean_sheets'] = temp1['clean_sheet.total']
mallorca['penalties_scored'] = pens_scored['total']
mallorca['penalties_missed'] = pens_missed['total']
mallorca['yellow_cards'] = y_cards_final['total']
mallorca['red_cards'] = r_cards_final['total']






####### OSASUNA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"727"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
osasuna = pd.DataFrame()

osasuna['team_name'] = temp1['team.name']
osasuna['team_id'] = temp1['team.id']
osasuna['league_name'] = temp1['league.name']
osasuna['league_id'] = temp1['league.id']
osasuna['fixtures.played'] = fixtures['total']
osasuna['fixtures.home'] = fixtures['home']
osasuna['fixtures.away'] = fixtures['away']
osasuna['goals'] = goals['total']
osasuna['goals_home'] = goals['home']
osasuna['goals_away'] = goals['away']
osasuna['most_goals_scored'] = b_goals_scored['total']
osasuna['most_goals_conceded'] = b_goals_conceded['total']
osasuna['clean_sheets'] = temp1['clean_sheet.total']
osasuna['penalties_scored'] = pens_scored['total']
osasuna['penalties_missed'] = pens_missed['total']
osasuna['yellow_cards'] = y_cards_final['total']
osasuna['red_cards'] = r_cards_final['total']






####### RAYO VALLECANO ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"728"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
rayo_vallecano = pd.DataFrame()

rayo_vallecano['team_name'] = temp1['team.name']
rayo_vallecano['team_id'] = temp1['team.id']
rayo_vallecano['league_name'] = temp1['league.name']
rayo_vallecano['league_id'] = temp1['league.id']
rayo_vallecano['fixtures.played'] = fixtures['total']
rayo_vallecano['fixtures.home'] = fixtures['home']
rayo_vallecano['fixtures.away'] = fixtures['away']
rayo_vallecano['goals'] = goals['total']
rayo_vallecano['goals_home'] = goals['home']
rayo_vallecano['goals_away'] = goals['away']
rayo_vallecano['most_goals_scored'] = b_goals_scored['total']
rayo_vallecano['most_goals_conceded'] = b_goals_conceded['total']
rayo_vallecano['clean_sheets'] = temp1['clean_sheet.total']
rayo_vallecano['penalties_scored'] = pens_scored['total']
rayo_vallecano['penalties_missed'] = pens_missed['total']
rayo_vallecano['yellow_cards'] = y_cards_final['total']
rayo_vallecano['red_cards'] = r_cards_final['total']






####### REAL BETIS ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"543"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
real_betis = pd.DataFrame()

real_betis['team_name'] = temp1['team.name']
real_betis['team_id'] = temp1['team.id']
real_betis['league_name'] = temp1['league.name']
real_betis['league_id'] = temp1['league.id']
real_betis['fixtures.played'] = fixtures['total']
real_betis['fixtures.home'] = fixtures['home']
real_betis['fixtures.away'] = fixtures['away']
real_betis['goals'] = goals['total']
real_betis['goals_home'] = goals['home']
real_betis['goals_away'] = goals['away']
real_betis['most_goals_scored'] = b_goals_scored['total']
real_betis['most_goals_conceded'] = b_goals_conceded['total']
real_betis['clean_sheets'] = temp1['clean_sheet.total']
real_betis['penalties_scored'] = pens_scored['total']
real_betis['penalties_missed'] = pens_missed['total']
real_betis['yellow_cards'] = y_cards_final['total']
real_betis['red_cards'] = r_cards_final['total']






####### REAL BETIS ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"543"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
real_betis = pd.DataFrame()

real_betis['team_name'] = temp1['team.name']
real_betis['team_id'] = temp1['team.id']
real_betis['league_name'] = temp1['league.name']
real_betis['league_id'] = temp1['league.id']
real_betis['fixtures.played'] = fixtures['total']
real_betis['fixtures.home'] = fixtures['home']
real_betis['fixtures.away'] = fixtures['away']
real_betis['goals'] = goals['total']
real_betis['goals_home'] = goals['home']
real_betis['goals_away'] = goals['away']
real_betis['most_goals_scored'] = b_goals_scored['total']
real_betis['most_goals_conceded'] = b_goals_conceded['total']
real_betis['clean_sheets'] = temp1['clean_sheet.total']
real_betis['penalties_scored'] = pens_scored['total']
real_betis['penalties_missed'] = pens_missed['total']
real_betis['yellow_cards'] = y_cards_final['total']
real_betis['red_cards'] = r_cards_final['total']






####### REAL MADRID ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"541"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
real_madrid = pd.DataFrame()

real_madrid['team_name'] = temp1['team.name']
real_madrid['team_id'] = temp1['team.id']
real_madrid['league_name'] = temp1['league.name']
real_madrid['league_id'] = temp1['league.id']
real_madrid['fixtures.played'] = fixtures['total']
real_madrid['fixtures.home'] = fixtures['home']
real_madrid['fixtures.away'] = fixtures['away']
real_madrid['goals'] = goals['total']
real_madrid['goals_home'] = goals['home']
real_madrid['goals_away'] = goals['away']
real_madrid['most_goals_scored'] = b_goals_scored['total']
real_madrid['most_goals_conceded'] = b_goals_conceded['total']
real_madrid['clean_sheets'] = temp1['clean_sheet.total']
real_madrid['penalties_scored'] = pens_scored['total']
real_madrid['penalties_missed'] = pens_missed['total']
real_madrid['yellow_cards'] = y_cards_final['total']
real_madrid['red_cards'] = r_cards_final['total']






####### REAL SOCIEDAD ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"548"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
real_sociedad = pd.DataFrame()

real_sociedad['team_name'] = temp1['team.name']
real_sociedad['team_id'] = temp1['team.id']
real_sociedad['league_name'] = temp1['league.name']
real_sociedad['league_id'] = temp1['league.id']
real_sociedad['fixtures.played'] = fixtures['total']
real_sociedad['fixtures.home'] = fixtures['home']
real_sociedad['fixtures.away'] = fixtures['away']
real_sociedad['goals'] = goals['total']
real_sociedad['goals_home'] = goals['home']
real_sociedad['goals_away'] = goals['away']
real_sociedad['most_goals_scored'] = b_goals_scored['total']
real_sociedad['most_goals_conceded'] = b_goals_conceded['total']
real_sociedad['clean_sheets'] = temp1['clean_sheet.total']
real_sociedad['penalties_scored'] = pens_scored['total']
real_sociedad['penalties_missed'] = pens_missed['total']
real_sociedad['yellow_cards'] = y_cards_final['total']
real_sociedad['red_cards'] = r_cards_final['total']






####### SEVILLA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"536"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
sevilla = pd.DataFrame()

sevilla['team_name'] = temp1['team.name']
sevilla['team_id'] = temp1['team.id']
sevilla['league_name'] = temp1['league.name']
sevilla['league_id'] = temp1['league.id']
sevilla['fixtures.played'] = fixtures['total']
sevilla['fixtures.home'] = fixtures['home']
sevilla['fixtures.away'] = fixtures['away']
sevilla['goals'] = goals['total']
sevilla['goals_home'] = goals['home']
sevilla['goals_away'] = goals['away']
sevilla['most_goals_scored'] = b_goals_scored['total']
sevilla['most_goals_conceded'] = b_goals_conceded['total']
sevilla['clean_sheets'] = temp1['clean_sheet.total']
sevilla['penalties_scored'] = pens_scored['total']
sevilla['penalties_missed'] = pens_missed['total']
sevilla['yellow_cards'] = y_cards_final['total']
sevilla['red_cards'] = r_cards_final['total']






####### VALENCIA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"532"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
valencia = pd.DataFrame()

valencia['team_name'] = temp1['team.name']
valencia['team_id'] = temp1['team.id']
valencia['league_name'] = temp1['league.name']
valencia['league_id'] = temp1['league.id']
valencia['fixtures.played'] = fixtures['total']
valencia['fixtures.home'] = fixtures['home']
valencia['fixtures.away'] = fixtures['away']
valencia['goals'] = goals['total']
valencia['goals_home'] = goals['home']
valencia['goals_away'] = goals['away']
valencia['most_goals_scored'] = b_goals_scored['total']
valencia['most_goals_conceded'] = b_goals_conceded['total']
valencia['clean_sheets'] = temp1['clean_sheet.total']
valencia['penalties_scored'] = pens_scored['total']
valencia['penalties_missed'] = pens_missed['total']
valencia['yellow_cards'] = y_cards_final['total']
valencia['red_cards'] = r_cards_final['total']






####### VILLAREAL ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"140","season":"2021","team":"533"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
villareal = pd.DataFrame()

villareal['team_name'] = temp1['team.name']
villareal['team_id'] = temp1['team.id']
villareal['league_name'] = temp1['league.name']
villareal['league_id'] = temp1['league.id']
villareal['fixtures.played'] = fixtures['total']
villareal['fixtures.home'] = fixtures['home']
villareal['fixtures.away'] = fixtures['away']
villareal['goals'] = goals['total']
villareal['goals_home'] = goals['home']
villareal['goals_away'] = goals['away']
villareal['most_goals_scored'] = b_goals_scored['total']
villareal['most_goals_conceded'] = b_goals_conceded['total']
villareal['clean_sheets'] = temp1['clean_sheet.total']
villareal['penalties_scored'] = pens_scored['total']
villareal['penalties_missed'] = pens_missed['total']
villareal['yellow_cards'] = y_cards_final['total']
villareal['red_cards'] = r_cards_final['total']




############################################################################################################################################################################################

# Append all the TEAMS in this league to ONE data frame

la_liga = pd.concat([alaves,
					athletic_club,
					athletico_madrid,
					barcelona,
					cadiz,
					celta_vigo,
					elche,
					espanyol,
					getafe,
					granada,
					levante,
					mallorca,
					osasuna,
					rayo_vallecano,
					real_betis,
					real_madrid,
					real_sociedad,
					sevilla,
					valencia,
					villareal
					], ignore_index=True)



# Data frames to list
#prem_league = [arsenal.columns.values.tolist()] 
#arsenal_list =  arsenal.values.tolist()
#aston_villa_list = aston_villa.values.tolist()
#spurs_list = spurs.values.tolist()
#wolves_list = wolves.values.tolist()
#prem_league.append(arsenal_list)





####################################### 4. SERIE A ##############################################



# Get the list of teams in Italy's top flight

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/teams"
querystring = {"league":"135","season":"2021"}

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# Pass the json response to a variable 
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
df_t = pd.DataFrame(temp)


# Serie A Teams
serie_a_teams = df_t['team'].apply(pd.Series)
serie_a_teams = serie_a_teams.sort_values(by='name')
print(serie_a_teams.to_string(index=False))   # to hide row index

# Serie A clubs' venues
serie_a_venues = df_t['venue'].apply(pd.Series)



####### AC MILAN ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"489"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
ac_milan = pd.DataFrame()

ac_milan['team_name'] = temp1['team.name']
ac_milan['team_id'] = temp1['team.id']
ac_milan['league_name'] = 'Bundesliga'
ac_milan['league_id'] = temp1['league.id']
ac_milan['fixtures.played'] = fixtures['total']
ac_milan['fixtures.home'] = fixtures['home']
ac_milan['fixtures.away'] = fixtures['away']
ac_milan['goals'] = goals['total']
ac_milan['goals_home'] = goals['home']
ac_milan['goals_away'] = goals['away']
ac_milan['most_goals_scored'] = b_goals_scored['total']
ac_milan['most_goals_conceded'] = b_goals_conceded['total']
ac_milan['clean_sheets'] = temp1['clean_sheet.total']
ac_milan['penalties_scored'] = pens_scored['total']
ac_milan['penalties_missed'] = pens_missed['total']
ac_milan['yellow_cards'] = y_cards_final['total']
ac_milan['red_cards'] = r_cards_final['total']






####### AS ROMA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"497"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
roma = pd.DataFrame()

roma['team_name'] = temp1['team.name']
roma['team_id'] = temp1['team.id']
roma['league_name'] = 'Bundesliga'
roma['league_id'] = temp1['league.id']
roma['fixtures.played'] = fixtures['total']
roma['fixtures.home'] = fixtures['home']
roma['fixtures.away'] = fixtures['away']
roma['goals'] = goals['total']
roma['goals_home'] = goals['home']
roma['goals_away'] = goals['away']
roma['most_goals_scored'] = b_goals_scored['total']
roma['most_goals_conceded'] = b_goals_conceded['total']
roma['clean_sheets'] = temp1['clean_sheet.total']
roma['penalties_scored'] = pens_scored['total']
roma['penalties_missed'] = pens_missed['total']
roma['yellow_cards'] = y_cards_final['total']
roma['red_cards'] = r_cards_final['total']







####### ATALANTA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"499"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
atalanta = pd.DataFrame()

atalanta['team_name'] = temp1['team.name']
atalanta['team_id'] = temp1['team.id']
atalanta['league_name'] = 'Bundesliga'
atalanta['league_id'] = temp1['league.id']
atalanta['fixtures.played'] = fixtures['total']
atalanta['fixtures.home'] = fixtures['home']
atalanta['fixtures.away'] = fixtures['away']
atalanta['goals'] = goals['total']
atalanta['goals_home'] = goals['home']
atalanta['goals_away'] = goals['away']
atalanta['most_goals_scored'] = b_goals_scored['total']
atalanta['most_goals_conceded'] = b_goals_conceded['total']
atalanta['clean_sheets'] = temp1['clean_sheet.total']
atalanta['penalties_scored'] = pens_scored['total']
atalanta['penalties_missed'] = pens_missed['total']
atalanta['yellow_cards'] = y_cards_final['total']
atalanta['red_cards'] = r_cards_final['total']






####### BOLOGNA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"500"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
bologna = pd.DataFrame()

bologna['team_name'] = temp1['team.name']
bologna['team_id'] = temp1['team.id']
bologna['league_name'] = 'Bundesliga'
bologna['league_id'] = temp1['league.id']
bologna['fixtures.played'] = fixtures['total']
bologna['fixtures.home'] = fixtures['home']
bologna['fixtures.away'] = fixtures['away']
bologna['goals'] = goals['total']
bologna['goals_home'] = goals['home']
bologna['goals_away'] = goals['away']
bologna['most_goals_scored'] = b_goals_scored['total']
bologna['most_goals_conceded'] = b_goals_conceded['total']
bologna['clean_sheets'] = temp1['clean_sheet.total']
bologna['penalties_scored'] = pens_scored['total']
bologna['penalties_missed'] = pens_missed['total']
bologna['yellow_cards'] = y_cards_final['total']
bologna['red_cards'] = r_cards_final['total']






####### CAGLIARI ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"490"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
cagliari = pd.DataFrame()

cagliari['team_name'] = temp1['team.name']
cagliari['team_id'] = temp1['team.id']
cagliari['league_name'] = 'Bundesliga'
cagliari['league_id'] = temp1['league.id']
cagliari['fixtures.played'] = fixtures['total']
cagliari['fixtures.home'] = fixtures['home']
cagliari['fixtures.away'] = fixtures['away']
cagliari['goals'] = goals['total']
cagliari['goals_home'] = goals['home']
cagliari['goals_away'] = goals['away']
cagliari['most_goals_scored'] = b_goals_scored['total']
cagliari['most_goals_conceded'] = b_goals_conceded['total']
cagliari['clean_sheets'] = temp1['clean_sheet.total']
cagliari['penalties_scored'] = pens_scored['total']
cagliari['penalties_missed'] = pens_missed['total']
cagliari['yellow_cards'] = y_cards_final['total']
cagliari['red_cards'] = r_cards_final['total']






####### EMPOLI ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"511"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
empoli = pd.DataFrame()

empoli['team_name'] = temp1['team.name']
empoli['team_id'] = temp1['team.id']
empoli['league_name'] = 'Bundesliga'
empoli['league_id'] = temp1['league.id']
empoli['fixtures.played'] = fixtures['total']
empoli['fixtures.home'] = fixtures['home']
empoli['fixtures.away'] = fixtures['away']
empoli['goals'] = goals['total']
empoli['goals_home'] = goals['home']
empoli['goals_away'] = goals['away']
empoli['most_goals_scored'] = b_goals_scored['total']
empoli['most_goals_conceded'] = b_goals_conceded['total']
empoli['clean_sheets'] = temp1['clean_sheet.total']
empoli['penalties_scored'] = pens_scored['total']
empoli['penalties_missed'] = pens_missed['total']
empoli['yellow_cards'] = y_cards_final['total']
empoli['red_cards'] = r_cards_final['total']






####### FIORENTINA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"502"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
fiorentina = pd.DataFrame()

fiorentina['team_name'] = temp1['team.name']
fiorentina['team_id'] = temp1['team.id']
fiorentina['league_name'] = 'Bundesliga'
fiorentina['league_id'] = temp1['league.id']
fiorentina['fixtures.played'] = fixtures['total']
fiorentina['fixtures.home'] = fixtures['home']
fiorentina['fixtures.away'] = fixtures['away']
fiorentina['goals'] = goals['total']
fiorentina['goals_home'] = goals['home']
fiorentina['goals_away'] = goals['away']
fiorentina['most_goals_scored'] = b_goals_scored['total']
fiorentina['most_goals_conceded'] = b_goals_conceded['total']
fiorentina['clean_sheets'] = temp1['clean_sheet.total']
fiorentina['penalties_scored'] = pens_scored['total']
fiorentina['penalties_missed'] = pens_missed['total']
fiorentina['yellow_cards'] = y_cards_final['total']
fiorentina['red_cards'] = r_cards_final['total']






####### GENOA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"495"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
genoa = pd.DataFrame()

genoa['team_name'] = temp1['team.name']
genoa['team_id'] = temp1['team.id']
genoa['league_name'] = 'Bundesliga'
genoa['league_id'] = temp1['league.id']
genoa['fixtures.played'] = fixtures['total']
genoa['fixtures.home'] = fixtures['home']
genoa['fixtures.away'] = fixtures['away']
genoa['goals'] = goals['total']
genoa['goals_home'] = goals['home']
genoa['goals_away'] = goals['away']
genoa['most_goals_scored'] = b_goals_scored['total']
genoa['most_goals_conceded'] = b_goals_conceded['total']
genoa['clean_sheets'] = temp1['clean_sheet.total']
genoa['penalties_scored'] = pens_scored['total']
genoa['penalties_missed'] = pens_missed['total']
genoa['yellow_cards'] = y_cards_final['total']
genoa['red_cards'] = r_cards_final['total']






####### INTER MILAN ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"505"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
inter_milan = pd.DataFrame()

inter_milan['team_name'] = temp1['team.name']
inter_milan['team_id'] = temp1['team.id']
inter_milan['league_name'] = 'Bundesliga'
inter_milan['league_id'] = temp1['league.id']
inter_milan['fixtures.played'] = fixtures['total']
inter_milan['fixtures.home'] = fixtures['home']
inter_milan['fixtures.away'] = fixtures['away']
inter_milan['goals'] = goals['total']
inter_milan['goals_home'] = goals['home']
inter_milan['goals_away'] = goals['away']
inter_milan['most_goals_scored'] = b_goals_scored['total']
inter_milan['most_goals_conceded'] = b_goals_conceded['total']
inter_milan['clean_sheets'] = temp1['clean_sheet.total']
inter_milan['penalties_scored'] = pens_scored['total']
inter_milan['penalties_missed'] = pens_missed['total']
inter_milan['yellow_cards'] = y_cards_final['total']
inter_milan['red_cards'] = r_cards_final['total']






####### JUVENTUS ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"496"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
juventus = pd.DataFrame()

juventus['team_name'] = temp1['team.name']
juventus['team_id'] = temp1['team.id']
juventus['league_name'] = 'Bundesliga'
juventus['league_id'] = temp1['league.id']
juventus['fixtures.played'] = fixtures['total']
juventus['fixtures.home'] = fixtures['home']
juventus['fixtures.away'] = fixtures['away']
juventus['goals'] = goals['total']
juventus['goals_home'] = goals['home']
juventus['goals_away'] = goals['away']
juventus['most_goals_scored'] = b_goals_scored['total']
juventus['most_goals_conceded'] = b_goals_conceded['total']
juventus['clean_sheets'] = temp1['clean_sheet.total']
juventus['penalties_scored'] = pens_scored['total']
juventus['penalties_missed'] = pens_missed['total']
juventus['yellow_cards'] = y_cards_final['total']
juventus['red_cards'] = r_cards_final['total']





####### LAZIO ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"487"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
lazio = pd.DataFrame()

lazio['team_name'] = temp1['team.name']
lazio['team_id'] = temp1['team.id']
lazio['league_name'] = 'Bundesliga'
lazio['league_id'] = temp1['league.id']
lazio['fixtures.played'] = fixtures['total']
lazio['fixtures.home'] = fixtures['home']
lazio['fixtures.away'] = fixtures['away']
lazio['goals'] = goals['total']
lazio['goals_home'] = goals['home']
lazio['goals_away'] = goals['away']
lazio['most_goals_scored'] = b_goals_scored['total']
lazio['most_goals_conceded'] = b_goals_conceded['total']
lazio['clean_sheets'] = temp1['clean_sheet.total']
lazio['penalties_scored'] = pens_scored['total']
lazio['penalties_missed'] = pens_missed['total']
lazio['yellow_cards'] = y_cards_final['total']
lazio['red_cards'] = r_cards_final['total']






####### NAPOLI ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"492"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
napoli = pd.DataFrame()

napoli['team_name'] = temp1['team.name']
napoli['team_id'] = temp1['team.id']
napoli['league_name'] = 'Bundesliga'
napoli['league_id'] = temp1['league.id']
napoli['fixtures.played'] = fixtures['total']
napoli['fixtures.home'] = fixtures['home']
napoli['fixtures.away'] = fixtures['away']
napoli['goals'] = goals['total']
napoli['goals_home'] = goals['home']
napoli['goals_away'] = goals['away']
napoli['most_goals_scored'] = b_goals_scored['total']
napoli['most_goals_conceded'] = b_goals_conceded['total']
napoli['clean_sheets'] = temp1['clean_sheet.total']
napoli['penalties_scored'] = pens_scored['total']
napoli['penalties_missed'] = pens_missed['total']
napoli['yellow_cards'] = y_cards_final['total']
napoli['red_cards'] = r_cards_final['total']






####### SALERNITANA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"514"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
salernitana = pd.DataFrame()

salernitana['team_name'] = temp1['team.name']
salernitana['team_id'] = temp1['team.id']
salernitana['league_name'] = 'Bundesliga'
salernitana['league_id'] = temp1['league.id']
salernitana['fixtures.played'] = fixtures['total']
salernitana['fixtures.home'] = fixtures['home']
salernitana['fixtures.away'] = fixtures['away']
salernitana['goals'] = goals['total']
salernitana['goals_home'] = goals['home']
salernitana['goals_away'] = goals['away']
salernitana['most_goals_scored'] = b_goals_scored['total']
salernitana['most_goals_conceded'] = b_goals_conceded['total']
salernitana['clean_sheets'] = temp1['clean_sheet.total']
salernitana['penalties_scored'] = pens_scored['total']
salernitana['penalties_missed'] = pens_missed['total']
salernitana['yellow_cards'] = y_cards_final['total']
salernitana['red_cards'] = r_cards_final['total']






####### SAMPDORIA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"498"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
sampdoria = pd.DataFrame()

sampdoria['team_name'] = temp1['team.name']
sampdoria['team_id'] = temp1['team.id']
sampdoria['league_name'] = 'Bundesliga'
sampdoria['league_id'] = temp1['league.id']
sampdoria['fixtures.played'] = fixtures['total']
sampdoria['fixtures.home'] = fixtures['home']
sampdoria['fixtures.away'] = fixtures['away']
sampdoria['goals'] = goals['total']
sampdoria['goals_home'] = goals['home']
sampdoria['goals_away'] = goals['away']
sampdoria['most_goals_scored'] = b_goals_scored['total']
sampdoria['most_goals_conceded'] = b_goals_conceded['total']
sampdoria['clean_sheets'] = temp1['clean_sheet.total']
sampdoria['penalties_scored'] = pens_scored['total']
sampdoria['penalties_missed'] = pens_missed['total']
sampdoria['yellow_cards'] = y_cards_final['total']
sampdoria['red_cards'] = r_cards_final['total']




####### SASSUOLO ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"488"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
sassuolo = pd.DataFrame()

sassuolo['team_name'] = temp1['team.name']
sassuolo['team_id'] = temp1['team.id']
sassuolo['league_name'] = 'Bundesliga'
sassuolo['league_id'] = temp1['league.id']
sassuolo['fixtures.played'] = fixtures['total']
sassuolo['fixtures.home'] = fixtures['home']
sassuolo['fixtures.away'] = fixtures['away']
sassuolo['goals'] = goals['total']
sassuolo['goals_home'] = goals['home']
sassuolo['goals_away'] = goals['away']
sassuolo['most_goals_scored'] = b_goals_scored['total']
sassuolo['most_goals_conceded'] = b_goals_conceded['total']
sassuolo['clean_sheets'] = temp1['clean_sheet.total']
sassuolo['penalties_scored'] = pens_scored['total']
sassuolo['penalties_missed'] = pens_missed['total']
sassuolo['yellow_cards'] = y_cards_final['total']
sassuolo['red_cards'] = r_cards_final['total']



####### SPEZIA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"515"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
spezia = pd.DataFrame()

spezia['team_name'] = temp1['team.name']
spezia['team_id'] = temp1['team.id']
spezia['league_name'] = 'Bundesliga'
spezia['league_id'] = temp1['league.id']
spezia['fixtures.played'] = fixtures['total']
spezia['fixtures.home'] = fixtures['home']
spezia['fixtures.away'] = fixtures['away']
spezia['goals'] = goals['total']
spezia['goals_home'] = goals['home']
spezia['goals_away'] = goals['away']
spezia['most_goals_scored'] = b_goals_scored['total']
spezia['most_goals_conceded'] = b_goals_conceded['total']
spezia['clean_sheets'] = temp1['clean_sheet.total']
spezia['penalties_scored'] = pens_scored['total']
spezia['penalties_missed'] = pens_missed['total']
spezia['yellow_cards'] = y_cards_final['total']
spezia['red_cards'] = r_cards_final['total']







####### TORINO ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"503"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
torino = pd.DataFrame()

torino['team_name'] = temp1['team.name']
torino['team_id'] = temp1['team.id']
torino['league_name'] = 'Bundesliga'
torino['league_id'] = temp1['league.id']
torino['fixtures.played'] = fixtures['total']
torino['fixtures.home'] = fixtures['home']
torino['fixtures.away'] = fixtures['away']
torino['goals'] = goals['total']
torino['goals_home'] = goals['home']
torino['goals_away'] = goals['away']
torino['most_goals_scored'] = b_goals_scored['total']
torino['most_goals_conceded'] = b_goals_conceded['total']
torino['clean_sheets'] = temp1['clean_sheet.total']
torino['penalties_scored'] = pens_scored['total']
torino['penalties_missed'] = pens_missed['total']
torino['yellow_cards'] = y_cards_final['total']
torino['red_cards'] = r_cards_final['total']






####### UDINESE ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"494"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
udinese = pd.DataFrame()

udinese['team_name'] = temp1['team.name']
udinese['team_id'] = temp1['team.id']
udinese['league_name'] = 'Bundesliga'
udinese['league_id'] = temp1['league.id']
udinese['fixtures.played'] = fixtures['total']
udinese['fixtures.home'] = fixtures['home']
udinese['fixtures.away'] = fixtures['away']
udinese['goals'] = goals['total']
udinese['goals_home'] = goals['home']
udinese['goals_away'] = goals['away']
udinese['most_goals_scored'] = b_goals_scored['total']
udinese['most_goals_conceded'] = b_goals_conceded['total']
udinese['clean_sheets'] = temp1['clean_sheet.total']
udinese['penalties_scored'] = pens_scored['total']
udinese['penalties_missed'] = pens_missed['total']
udinese['yellow_cards'] = y_cards_final['total']
udinese['red_cards'] = r_cards_final['total']






####### VENEZIA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"517"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
venezia = pd.DataFrame()

venezia['team_name'] = temp1['team.name']
venezia['team_id'] = temp1['team.id']
venezia['league_name'] = 'Bundesliga'
venezia['league_id'] = temp1['league.id']
venezia['fixtures.played'] = fixtures['total']
venezia['fixtures.home'] = fixtures['home']
venezia['fixtures.away'] = fixtures['away']
venezia['goals'] = goals['total']
venezia['goals_home'] = goals['home']
venezia['goals_away'] = goals['away']
venezia['most_goals_scored'] = b_goals_scored['total']
venezia['most_goals_conceded'] = b_goals_conceded['total']
venezia['clean_sheets'] = temp1['clean_sheet.total']
venezia['penalties_scored'] = pens_scored['total']
venezia['penalties_missed'] = pens_missed['total']
venezia['yellow_cards'] = y_cards_final['total']
venezia['red_cards'] = r_cards_final['total']






####### VERONA ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"135","season":"2021","team":"504"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
verona = pd.DataFrame()

verona['team_name'] = temp1['team.name']
verona['team_id'] = temp1['team.id']
verona['league_name'] = 'Bundesliga'
verona['league_id'] = temp1['league.id']
verona['fixtures.played'] = fixtures['total']
verona['fixtures.home'] = fixtures['home']
verona['fixtures.away'] = fixtures['away']
verona['goals'] = goals['total']
verona['goals_home'] = goals['home']
verona['goals_away'] = goals['away']
verona['most_goals_scored'] = b_goals_scored['total']
verona['most_goals_conceded'] = b_goals_conceded['total']
verona['clean_sheets'] = temp1['clean_sheet.total']
verona['penalties_scored'] = pens_scored['total']
verona['penalties_missed'] = pens_missed['total']
verona['yellow_cards'] = y_cards_final['total']
verona['red_cards'] = r_cards_final['total']




############################################################################################################################################################################################

# Append all the TEAMS in this league to ONE data frame

serie_a = pd.concat([ac_milan,
					roma,
					atalanta,
					bologna,
					cagliari,
					empoli,
					fiorentina,
					genoa,
					inter_milan,
					juventus,
					lazio,
					napoli,
					salernitana,
					sampdoria,
					sassuolo,
					spezia,
					torino,
					udinese,
					venezia,
					verona
					], ignore_index=True)








					
					
					
					

####################################### 5. LIGUE 1 ##############################################



# Get the list of teams in France's top flight

API_HOST = "api-football-v1.p.rapidapi.com"
API_KEY = "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"

url = "https://api-football-v1.p.rapidapi.com/v3/teams"
querystring = {"league":"61","season":"2021"}

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# Pass the json response to a variable 
t = response.json()
temp = t['response']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
df_t = pd.DataFrame(temp)


# Ligue 1 teams
ligue_1_teams = df_t['team'].apply(pd.Series)
ligue_1_teams = ligue_1_teams.sort_values(by='name')
print(ligue_1_teams.to_string(index=False))   # to hide row index

# Ligue 1 clubs' venues
ligue_1_venues = df_t['venue'].apply(pd.Series)






####### ANGERS ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"77"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
angers = pd.DataFrame()

angers['team_name'] = temp1['team.name']
angers['team_id'] = temp1['team.id']
angers['league_name'] = temp1['league.name']
angers['league_id'] = temp1['league.id']
angers['fixtures.played'] = fixtures['total']
angers['fixtures.home'] = fixtures['home']
angers['fixtures.away'] = fixtures['away']
angers['goals'] = goals['total']
angers['goals_home'] = goals['home']
angers['goals_away'] = goals['away']
angers['most_goals_scored'] = b_goals_scored['total']
angers['most_goals_conceded'] = b_goals_conceded['total']
angers['clean_sheets'] = temp1['clean_sheet.total']
angers['penalties_scored'] = pens_scored['total']
angers['penalties_missed'] = pens_missed['total']
angers['yellow_cards'] = y_cards_final['total']
angers['red_cards'] = r_cards_final['total']







####### BORDEAUX ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"78"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
bordeaux = pd.DataFrame()

bordeaux['team_name'] = temp1['team.name']
bordeaux['team_id'] = temp1['team.id']
bordeaux['league_name'] = temp1['league.name']
bordeaux['league_id'] = temp1['league.id']
bordeaux['fixtures.played'] = fixtures['total']
bordeaux['fixtures.home'] = fixtures['home']
bordeaux['fixtures.away'] = fixtures['away']
bordeaux['goals'] = goals['total']
bordeaux['goals_home'] = goals['home']
bordeaux['goals_away'] = goals['away']
bordeaux['most_goals_scored'] = b_goals_scored['total']
bordeaux['most_goals_conceded'] = b_goals_conceded['total']
bordeaux['clean_sheets'] = temp1['clean_sheet.total']
bordeaux['penalties_scored'] = pens_scored['total']
bordeaux['penalties_missed'] = pens_missed['total']
bordeaux['yellow_cards'] = y_cards_final['total']
bordeaux['red_cards'] = r_cards_final['total']







####### CLERMONT FOOT ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"99"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
clermont_foot = pd.DataFrame()

clermont_foot['team_name'] = temp1['team.name']
clermont_foot['team_id'] = temp1['team.id']
clermont_foot['league_name'] = temp1['league.name']
clermont_foot['league_id'] = temp1['league.id']
clermont_foot['fixtures.played'] = fixtures['total']
clermont_foot['fixtures.home'] = fixtures['home']
clermont_foot['fixtures.away'] = fixtures['away']
clermont_foot['goals'] = goals['total']
clermont_foot['goals_home'] = goals['home']
clermont_foot['goals_away'] = goals['away']
clermont_foot['most_goals_scored'] = b_goals_scored['total']
clermont_foot['most_goals_conceded'] = b_goals_conceded['total']
clermont_foot['clean_sheets'] = temp1['clean_sheet.total']
clermont_foot['penalties_scored'] = pens_scored['total']
clermont_foot['penalties_missed'] = pens_missed['total']
clermont_foot['yellow_cards'] = y_cards_final['total']
clermont_foot['red_cards'] = r_cards_final['total']






####### ESTAC TROYES ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"110"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
estac_troyes = pd.DataFrame()

estac_troyes['team_name'] = temp1['team.name']
estac_troyes['team_id'] = temp1['team.id']
estac_troyes['league_name'] = temp1['league.name']
estac_troyes['league_id'] = temp1['league.id']
estac_troyes['fixtures.played'] = fixtures['total']
estac_troyes['fixtures.home'] = fixtures['home']
estac_troyes['fixtures.away'] = fixtures['away']
estac_troyes['goals'] = goals['total']
estac_troyes['goals_home'] = goals['home']
estac_troyes['goals_away'] = goals['away']
estac_troyes['most_goals_scored'] = b_goals_scored['total']
estac_troyes['most_goals_conceded'] = b_goals_conceded['total']
estac_troyes['clean_sheets'] = temp1['clean_sheet.total']
estac_troyes['penalties_scored'] = pens_scored['total']
estac_troyes['penalties_missed'] = pens_missed['total']
estac_troyes['yellow_cards'] = y_cards_final['total']
estac_troyes['red_cards'] = r_cards_final['total']






####### LENS ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"116"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
lens = pd.DataFrame()

lens['team_name'] = temp1['team.name']
lens['team_id'] = temp1['team.id']
lens['league_name'] = temp1['league.name']
lens['league_id'] = temp1['league.id']
lens['fixtures.played'] = fixtures['total']
lens['fixtures.home'] = fixtures['home']
lens['fixtures.away'] = fixtures['away']
lens['goals'] = goals['total']
lens['goals_home'] = goals['home']
lens['goals_away'] = goals['away']
lens['most_goals_scored'] = b_goals_scored['total']
lens['most_goals_conceded'] = b_goals_conceded['total']
lens['clean_sheets'] = temp1['clean_sheet.total']
lens['penalties_scored'] = pens_scored['total']
lens['penalties_missed'] = pens_missed['total']
lens['yellow_cards'] = y_cards_final['total']
lens['red_cards'] = r_cards_final['total']






####### LILLE ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"79"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
lille = pd.DataFrame()

lille['team_name'] = temp1['team.name']
lille['team_id'] = temp1['team.id']
lille['league_name'] = temp1['league.name']
lille['league_id'] = temp1['league.id']
lille['fixtures.played'] = fixtures['total']
lille['fixtures.home'] = fixtures['home']
lille['fixtures.away'] = fixtures['away']
lille['goals'] = goals['total']
lille['goals_home'] = goals['home']
lille['goals_away'] = goals['away']
lille['most_goals_scored'] = b_goals_scored['total']
lille['most_goals_conceded'] = b_goals_conceded['total']
lille['clean_sheets'] = temp1['clean_sheet.total']
lille['penalties_scored'] = pens_scored['total']
lille['penalties_missed'] = pens_missed['total']
lille['yellow_cards'] = y_cards_final['total']
lille['red_cards'] = r_cards_final['total']






####### LORIENT ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"97"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
lorient = pd.DataFrame()

lorient['team_name'] = temp1['team.name']
lorient['team_id'] = temp1['team.id']
lorient['league_name'] = temp1['league.name']
lorient['league_id'] = temp1['league.id']
lorient['fixtures.played'] = fixtures['total']
lorient['fixtures.home'] = fixtures['home']
lorient['fixtures.away'] = fixtures['away']
lorient['goals'] = goals['total']
lorient['goals_home'] = goals['home']
lorient['goals_away'] = goals['away']
lorient['most_goals_scored'] = b_goals_scored['total']
lorient['most_goals_conceded'] = b_goals_conceded['total']
lorient['clean_sheets'] = temp1['clean_sheet.total']
lorient['penalties_scored'] = pens_scored['total']
lorient['penalties_missed'] = pens_missed['total']
lorient['yellow_cards'] = y_cards_final['total']
lorient['red_cards'] = r_cards_final['total']






####### LYON ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"80"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
lyon = pd.DataFrame()

lyon['team_name'] = temp1['team.name']
lyon['team_id'] = temp1['team.id']
lyon['league_name'] = temp1['league.name']
lyon['league_id'] = temp1['league.id']
lyon['fixtures.played'] = fixtures['total']
lyon['fixtures.home'] = fixtures['home']
lyon['fixtures.away'] = fixtures['away']
lyon['goals'] = goals['total']
lyon['goals_home'] = goals['home']
lyon['goals_away'] = goals['away']
lyon['most_goals_scored'] = b_goals_scored['total']
lyon['most_goals_conceded'] = b_goals_conceded['total']
lyon['clean_sheets'] = temp1['clean_sheet.total']
lyon['penalties_scored'] = pens_scored['total']
lyon['penalties_missed'] = pens_missed['total']
lyon['yellow_cards'] = y_cards_final['total']
lyon['red_cards'] = r_cards_final['total']






####### MARSEILLE ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"81"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
marseille = pd.DataFrame()

marseille['team_name'] = temp1['team.name']
marseille['team_id'] = temp1['team.id']
marseille['league_name'] = temp1['league.name']
marseille['league_id'] = temp1['league.id']
marseille['fixtures.played'] = fixtures['total']
marseille['fixtures.home'] = fixtures['home']
marseille['fixtures.away'] = fixtures['away']
marseille['goals'] = goals['total']
marseille['goals_home'] = goals['home']
marseille['goals_away'] = goals['away']
marseille['most_goals_scored'] = b_goals_scored['total']
marseille['most_goals_conceded'] = b_goals_conceded['total']
marseille['clean_sheets'] = temp1['clean_sheet.total']
marseille['penalties_scored'] = pens_scored['total']
marseille['penalties_missed'] = pens_missed['total']
marseille['yellow_cards'] = y_cards_final['total']
marseille['red_cards'] = r_cards_final['total']






####### METZ ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"112"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
metz = pd.DataFrame()

metz['team_name'] = temp1['team.name']
metz['team_id'] = temp1['team.id']
metz['league_name'] = temp1['league.name']
metz['league_id'] = temp1['league.id']
metz['fixtures.played'] = fixtures['total']
metz['fixtures.home'] = fixtures['home']
metz['fixtures.away'] = fixtures['away']
metz['goals'] = goals['total']
metz['goals_home'] = goals['home']
metz['goals_away'] = goals['away']
metz['most_goals_scored'] = b_goals_scored['total']
metz['most_goals_conceded'] = b_goals_conceded['total']
metz['clean_sheets'] = temp1['clean_sheet.total']
metz['penalties_scored'] = pens_scored['total']
metz['penalties_missed'] = pens_missed['total']
metz['yellow_cards'] = y_cards_final['total']
metz['red_cards'] = r_cards_final['total']






####### MONACO ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"91"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
monaco = pd.DataFrame()

monaco['team_name'] = temp1['team.name']
monaco['team_id'] = temp1['team.id']
monaco['league_name'] = temp1['league.name']
monaco['league_id'] = temp1['league.id']
monaco['fixtures.played'] = fixtures['total']
monaco['fixtures.home'] = fixtures['home']
monaco['fixtures.away'] = fixtures['away']
monaco['goals'] = goals['total']
monaco['goals_home'] = goals['home']
monaco['goals_away'] = goals['away']
monaco['most_goals_scored'] = b_goals_scored['total']
monaco['most_goals_conceded'] = b_goals_conceded['total']
monaco['clean_sheets'] = temp1['clean_sheet.total']
monaco['penalties_scored'] = pens_scored['total']
monaco['penalties_missed'] = pens_missed['total']
monaco['yellow_cards'] = y_cards_final['total']
monaco['red_cards'] = r_cards_final['total']






####### MONTPELLIER ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"82"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
montpellier = pd.DataFrame()

montpellier['team_name'] = temp1['team.name']
montpellier['team_id'] = temp1['team.id']
montpellier['league_name'] = temp1['league.name']
montpellier['league_id'] = temp1['league.id']
montpellier['fixtures.played'] = fixtures['total']
montpellier['fixtures.home'] = fixtures['home']
montpellier['fixtures.away'] = fixtures['away']
montpellier['goals'] = goals['total']
montpellier['goals_home'] = goals['home']
montpellier['goals_away'] = goals['away']
montpellier['most_goals_scored'] = b_goals_scored['total']
montpellier['most_goals_conceded'] = b_goals_conceded['total']
montpellier['clean_sheets'] = temp1['clean_sheet.total']
montpellier['penalties_scored'] = pens_scored['total']
montpellier['penalties_missed'] = pens_missed['total']
montpellier['yellow_cards'] = y_cards_final['total']
montpellier['red_cards'] = r_cards_final['total']






####### NANTES ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"83"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
nantes = pd.DataFrame()

nantes['team_name'] = temp1['team.name']
nantes['team_id'] = temp1['team.id']
nantes['league_name'] = temp1['league.name']
nantes['league_id'] = temp1['league.id']
nantes['fixtures.played'] = fixtures['total']
nantes['fixtures.home'] = fixtures['home']
nantes['fixtures.away'] = fixtures['away']
nantes['goals'] = goals['total']
nantes['goals_home'] = goals['home']
nantes['goals_away'] = goals['away']
nantes['most_goals_scored'] = b_goals_scored['total']
nantes['most_goals_conceded'] = b_goals_conceded['total']
nantes['clean_sheets'] = temp1['clean_sheet.total']
nantes['penalties_scored'] = pens_scored['total']
nantes['penalties_missed'] = pens_missed['total']
nantes['yellow_cards'] = y_cards_final['total']
nantes['red_cards'] = r_cards_final['total']






####### NICE ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"84"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
nice = pd.DataFrame()

nice['team_name'] = temp1['team.name']
nice['team_id'] = temp1['team.id']
nice['league_name'] = temp1['league.name']
nice['league_id'] = temp1['league.id']
nice['fixtures.played'] = fixtures['total']
nice['fixtures.home'] = fixtures['home']
nice['fixtures.away'] = fixtures['away']
nice['goals'] = goals['total']
nice['goals_home'] = goals['home']
nice['goals_away'] = goals['away']
nice['most_goals_scored'] = b_goals_scored['total']
nice['most_goals_conceded'] = b_goals_conceded['total']
nice['clean_sheets'] = temp1['clean_sheet.total']
nice['penalties_scored'] = pens_scored['total']
nice['penalties_missed'] = pens_missed['total']
nice['yellow_cards'] = y_cards_final['total']
nice['red_cards'] = r_cards_final['total']






####### PARIS SAINT GERMAIN ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"85"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
psg = pd.DataFrame()

psg['team_name'] = temp1['team.name']
psg['team_id'] = temp1['team.id']
psg['league_name'] = temp1['league.name']
psg['league_id'] = temp1['league.id']
psg['fixtures.played'] = fixtures['total']
psg['fixtures.home'] = fixtures['home']
psg['fixtures.away'] = fixtures['away']
psg['goals'] = goals['total']
psg['goals_home'] = goals['home']
psg['goals_away'] = goals['away']
psg['most_goals_scored'] = b_goals_scored['total']
psg['most_goals_conceded'] = b_goals_conceded['total']
psg['clean_sheets'] = temp1['clean_sheet.total']
psg['penalties_scored'] = pens_scored['total']
psg['penalties_missed'] = pens_missed['total']
psg['yellow_cards'] = y_cards_final['total']
psg['red_cards'] = r_cards_final['total']






####### REIMS ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"93"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
reims = pd.DataFrame()

reims['team_name'] = temp1['team.name']
reims['team_id'] = temp1['team.id']
reims['league_name'] = temp1['league.name']
reims['league_id'] = temp1['league.id']
reims['fixtures.played'] = fixtures['total']
reims['fixtures.home'] = fixtures['home']
reims['fixtures.away'] = fixtures['away']
reims['goals'] = goals['total']
reims['goals_home'] = goals['home']
reims['goals_away'] = goals['away']
reims['most_goals_scored'] = b_goals_scored['total']
reims['most_goals_conceded'] = b_goals_conceded['total']
reims['clean_sheets'] = temp1['clean_sheet.total']
reims['penalties_scored'] = pens_scored['total']
reims['penalties_missed'] = pens_missed['total']
reims['yellow_cards'] = y_cards_final['total']
reims['red_cards'] = r_cards_final['total']






####### RENNES ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"94"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
rennes = pd.DataFrame()

rennes['team_name'] = temp1['team.name']
rennes['team_id'] = temp1['team.id']
rennes['league_name'] = temp1['league.name']
rennes['league_id'] = temp1['league.id']
rennes['fixtures.played'] = fixtures['total']
rennes['fixtures.home'] = fixtures['home']
rennes['fixtures.away'] = fixtures['away']
rennes['goals'] = goals['total']
rennes['goals_home'] = goals['home']
rennes['goals_away'] = goals['away']
rennes['most_goals_scored'] = b_goals_scored['total']
rennes['most_goals_conceded'] = b_goals_conceded['total']
rennes['clean_sheets'] = temp1['clean_sheet.total']
rennes['penalties_scored'] = pens_scored['total']
rennes['penalties_missed'] = pens_missed['total']
rennes['yellow_cards'] = y_cards_final['total']
rennes['red_cards'] = r_cards_final['total']






####### SAINT ETIENNE ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"1063"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
saint_etienne = pd.DataFrame()

saint_etienne['team_name'] = temp1['team.name']
saint_etienne['team_id'] = temp1['team.id']
saint_etienne['league_name'] = temp1['league.name']
saint_etienne['league_id'] = temp1['league.id']
saint_etienne['fixtures.played'] = fixtures['total']
saint_etienne['fixtures.home'] = fixtures['home']
saint_etienne['fixtures.away'] = fixtures['away']
saint_etienne['goals'] = goals['total']
saint_etienne['goals_home'] = goals['home']
saint_etienne['goals_away'] = goals['away']
saint_etienne['most_goals_scored'] = b_goals_scored['total']
saint_etienne['most_goals_conceded'] = b_goals_conceded['total']
saint_etienne['clean_sheets'] = temp1['clean_sheet.total']
saint_etienne['penalties_scored'] = pens_scored['total']
saint_etienne['penalties_missed'] = pens_missed['total']
saint_etienne['yellow_cards'] = y_cards_final['total']
saint_etienne['red_cards'] = r_cards_final['total']






####### STADE BRESTOIS 29 ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"106"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
stade_brestois = pd.DataFrame()

stade_brestois['team_name'] = temp1['team.name']
stade_brestois['team_id'] = temp1['team.id']
stade_brestois['league_name'] = temp1['league.name']
stade_brestois['league_id'] = temp1['league.id']
stade_brestois['fixtures.played'] = fixtures['total']
stade_brestois['fixtures.home'] = fixtures['home']
stade_brestois['fixtures.away'] = fixtures['away']
stade_brestois['goals'] = goals['total']
stade_brestois['goals_home'] = goals['home']
stade_brestois['goals_away'] = goals['away']
stade_brestois['most_goals_scored'] = b_goals_scored['total']
stade_brestois['most_goals_conceded'] = b_goals_conceded['total']
stade_brestois['clean_sheets'] = temp1['clean_sheet.total']
stade_brestois['penalties_scored'] = pens_scored['total']
stade_brestois['penalties_missed'] = pens_missed['total']
stade_brestois['yellow_cards'] = y_cards_final['total']
stade_brestois['red_cards'] = r_cards_final['total']






####### STRASBOURG ######


url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

querystring = {"league":"61","season":"2021","team":"95"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

# Get the data of this team in JSON format from RapidAPI via REST API call
response = requests.request("GET", url, headers=headers, params=querystring)
content = response.json()

# Pass JSON content into another variable to untangle nested JSON
temp = content['response']
temp1 = pd.json_normalize(temp, max_level=1) 


# temp1.columns   ---- In case you want the source data columns


# Extract the general team stats from the normalized dataframe



## 1. Goals
g = temp1['goals.for'].apply(pd.Series)
g1 = g['total'].apply(pd.Series)


# Goals in every 15 min segment of the game
g_min = g['minute'].apply(pd.Series)


##### Goals between 0-15 mins
g_min1 = g_min['0-15'].apply(pd.Series)
g_min1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 16-30 mins
g_min2 = g_min['16-30'].apply(pd.Series)
g_min2.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 31-45 mins
g_min3 = g_min['31-45'].apply(pd.Series)
g_min3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 46-60 mins
g_min4 = g_min['46-60'].apply(pd.Series)
g_min4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 61-75 mins
g_min5 = g_min['61-75'].apply(pd.Series)
g_min5.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 76-90 mins
g_min6 = g_min['76-90'].apply(pd.Series)
g_min6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### Goals between 91-105 mins
g_min7 = g_min['91-105'].apply(pd.Series)
g_min7.fillna(0, inplace= True)  # Replace "None" with '0' integer value


##### Goals between 106-120 mins
g_min8 = g_min['106-120'].apply(pd.Series)
g_min8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total goals scored
g_min_final = g_min
g_min_final['total'] = g_min1['total'] + g_min1['total'] + g_min2['total'] + g_min3['total'] + g_min4['total'] + g_min5['total'] + g_min6['total'] + g_min7['total'] + g_min8['total']


goals = g1



## 2. Fixtures
fixtures = temp1['fixtures.played'].apply(pd.Series)



## 3. Cards

"""Define your card variables (yellow & red) """


### 3.1. Yellow Cards
cards = temp1['cards.yellow'].apply(pd.Series)

##### YC between 0-15 mins
y_cards1 = cards['0-15'].apply(pd.Series)
y_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
y_cards2 = cards['16-30'].apply(pd.Series)
y_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
y_cards3 = cards['31-45'].apply(pd.Series)
y_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
y_cards4 = cards['46-60'].apply(pd.Series)
y_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
y_cards5 = cards['61-75'].apply(pd.Series)
y_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
y_cards6 = cards['76-90'].apply(pd.Series)
y_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
y_cards7 = cards['91-105'].apply(pd.Series)
y_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
y_cards8 = cards['106-120'].apply(pd.Series)
y_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value


## Total yellow cards
y_cards_final = cards
y_cards_final['total'] = y_cards1['total'] + y_cards2['total'] + y_cards3['total'] + y_cards4['total'] + y_cards5['total'] + y_cards6['total'] + y_cards7['total'] + y_cards8['total']



### 3.2. Red Cards

cards2 = temp1['cards.red'].apply(pd.Series)

##### YC between 0-15 mins
r_cards1 = cards2['0-15'].apply(pd.Series)
r_cards1.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 16-30 mins
r_cards2 = cards2['16-30'].apply(pd.Series)
r_cards2.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 31-45 mins
r_cards3 = cards2['31-45'].apply(pd.Series)
r_cards3.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 46-60 mins
r_cards4 = cards2['46-60'].apply(pd.Series)
r_cards4.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 61-75 mins
r_cards5 = cards2['61-75'].apply(pd.Series)
r_cards5.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 76-90 mins
r_cards6 = cards2['76-90'].apply(pd.Series)
r_cards6.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 91-105 mins
r_cards7 = cards2['91-105'].apply(pd.Series)
r_cards7.fillna(0, inplace= True)  # Replace "None" with '0' integer value

##### YC between 106-120 mins
r_cards8 = cards2['106-120'].apply(pd.Series)
r_cards8.fillna(0, inplace= True)  # Replace "None" with '0' integer value

## Total red cards
r_cards_final = cards
r_cards_final['total'] = r_cards1['total'] + r_cards2['total'] + r_cards3['total'] + r_cards4['total'] + r_cards5['total'] + r_cards6['total'] + r_cards7['total'] + r_cards8['total']




## 4. Formation (requires further fixing, multi-indexing required maybe?)
#l_ups = temp1['lineups'].apply(pd.Series)

### Rename column from '0' to 'data'
#l_ups.columns = ['data']

### Continue the unnesting process
#l_ups1 = l_ups['data'].apply(pd.Series)





## 5. Penalties
pens_scored = temp1['penalty.scored'].apply(pd.Series)  
pens_missed = temp1['penalty.missed'].apply(pd.Series)


## 6. Clean Sheets
cs_home = temp1['clean_sheet.home'].apply(pd.Series)
cs_away = temp1['clean_sheet.away'].apply(pd.Series)
cs_total = temp1['clean_sheet.total'].apply(pd.Series)


## 7. Biggest Wins/Loses
b_wins = temp1['biggest.wins'].apply(pd.Series)
b_loses = temp1['biggest.loses'].apply(pd.Series)




## 8. Most Goals Scored/Conceded in a Game

"""Define your goal variables"""

b_goals = temp1['biggest.goals'].apply(pd.Series)
b_goals

#### 8.1. Most goals scored 
b_goals_scored = b_goals['for'].apply(pd.Series)
b_goals_scored['total'] = b_goals_scored['home'] + b_goals_scored['away']

#### 8.2. Most goals conceded
b_goals_conceded = b_goals['against'].apply(pd.Series)
b_goals_conceded['total'] = b_goals_conceded['home'] + b_goals_conceded['away']



# Create the final data frame for team stats
strasbourg = pd.DataFrame()

strasbourg['team_name'] = temp1['team.name']
strasbourg['team_id'] = temp1['team.id']
strasbourg['league_name'] = temp1['league.name']
strasbourg['league_id'] = temp1['league.id']
strasbourg['fixtures.played'] = fixtures['total']
strasbourg['fixtures.home'] = fixtures['home']
strasbourg['fixtures.away'] = fixtures['away']
strasbourg['goals'] = goals['total']
strasbourg['goals_home'] = goals['home']
strasbourg['goals_away'] = goals['away']
strasbourg['most_goals_scored'] = b_goals_scored['total']
strasbourg['most_goals_conceded'] = b_goals_conceded['total']
strasbourg['clean_sheets'] = temp1['clean_sheet.total']
strasbourg['penalties_scored'] = pens_scored['total']
strasbourg['penalties_missed'] = pens_missed['total']
strasbourg['yellow_cards'] = y_cards_final['total']
strasbourg['red_cards'] = r_cards_final['total']





############################################################################################################################################################################################
# This STEP merges all 5 leagues into ONE data frame  
# (SIDE NOTE: Deploy this method with Europe's top goal scorers, assists, passes and clean sheets also) 
#
# Premier League = 20  
# Bundesliga =     18
# La Liga =        20
# Ligue 1 =        20
# Serie A  =       20
 # ----------------------
# Grand Total =    98
############################################################################################################################################################################################

# Append all the TEAMS in this league to ONE data frame

ligue_1 = pd.concat([angers,
					bordeaux,
					clermont_foot,
					estac_troyes,
					lens,
					lille,
					lorient,
					lyon,
					marseille,
					metz,
					monaco,
					montpellier,
					nantes,
					nice,
					psg,
					reims,
					rennes,
					saint_etienne,
					stade_brestois,
					strasbourg
					], ignore_index=True)



# Data frames to list
#prem_league = [arsenal.columns.values.tolist()] 
#arsenal_list =  arsenal.values.tolist()
#aston_villa_list = aston_villa.values.tolist()
#spurs_list = spurs.values.tolist()
#wolves_list = wolves.values.tolist()
#prem_league.append(arsenal_list)



# Append all 98 TEAMS to ONE data frame
leagues = pd.concat([prem_league, 
						bundesliga, 
						la_liga, 
						serie_a,	
						ligue_1
						], ignore_index = True)


						
						


#############################################################################################################################################################################################################
# SAVE LEAGUE TABLES INTO CSV FILES 

"""

1. Change working directory using the 'os' library
2. Save data frame outputs as CSV files 
3. Revert directory to original path


"""



prem_league.to_csv('D:/Projects/Python/Football/Teams/Premier League/outputs/2021-2022/prem_league.csv', index = False)
bundesliga.to_csv('D:/Projects/Python/Football/Teams/Bundesliga/outputs/2021-2022/bundesliga.csv', index = False)
la_liga.to_csv('D:/Projects/Python/Football/Teams/La Liga/outputs/2021-2022/la_liga.csv', index = False)
serie_a.to_csv('D:/Projects/Python/Football/Teams/Serie A/outputs/2021-2022/serie_a.csv', index = False)
ligue_1.to_csv('D:/Projects/Python/Football/Teams/Ligue 1/outputs/2021-2022/ligue_1.csv', index = False)





# Write data from each team to CSV

# # PREMIER LEAGUE
# 
# arsenal.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# aston_villa.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# brentford.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# burnley.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# brighton.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# chelsea.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# crystal_palace.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# everton.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# leeds.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# leicester.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# liverpool.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# man_city.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# man_utd.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# newcastle.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# norwich.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# southampton.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# spurs.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# watford.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# west_ham.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# wolves
# 
# # BUNDESLIGA
# hoffenheim.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# bielefeld.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# leverkusen.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# bayern_munich.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# dortmund.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# monchengladbach.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# frankfurt.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# augsburg.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# koln.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# mainz.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# hertha_berlin.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# leipzig.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# freiburg.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# greuther_furth.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# union_berlin.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# stuttgart.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# vfl_bochum.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# wolfsburg.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# 
# 
# # LA LIGA
# alaves.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# athletic_club.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# athletico_madrid.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# barcelona.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# cadiz.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# celta_vigo.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# elche.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# espanyol.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# getafe.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# granada.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# levante.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# mallorca.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# osasuna.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# rayo_vallecano.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# real_betis.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# real_madrid.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# real_sociedad.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# sevilla.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# valencia.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# villareal.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# 
# 
# 
# 
# 
# 
# # SERIE A
# ac_milan.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# roma.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# atalanta.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# bologna.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# cagliari.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# empoli.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# fiorentina.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# genoa.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# inter_milan.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# juventus.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# lazio.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# napoli.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# salernitana.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# sampdoria.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# sassuolo.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# spezia.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# torino.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# udinese.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# venezia.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# verona.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# 
# 
# 
# 
# # LIGUE 1
# angers.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# bordeaux.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# clermont_foot.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# estac_troyes.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# lens.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# lille.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# lorient.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# lyon.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# marseille.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# metz.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# monaco.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# montpellier.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# nantes.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# nice.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# psg.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# reims.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# rennes.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# saint_etienne.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# stade_brestois.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
# strasbourg.to_csv(‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’, index = False)
 

# ‘D:\Projects\Python\Football\Teams\Serie A\outputs\2021-2022\test.csv’


