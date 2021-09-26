# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#--------------------------------------------------------LEAGUE TABLES--------------------------------------------------------------


## Stage 1: REST API call 

import requests 
import pandas as pd
import explode



############################################# 1. PREMIER LEAGUE ##############################################

# Let's return the Premier League table in this instance


url = "-----"
querystring = {"season":"2021","league":"39"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# response.json()



## Stage 2: From JSON to Pandas 


# Read JSON response into a variable
e = response.json()['response'] #['standings']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
df_e = pd.DataFrame(e)
df_e1 = df_e['league'].apply(pd.Series)
df_e2 = df_e1['standings'].apply(pd.Series)


# The column name of this data frame was '0', which Python misinterprets as 'row values'. I had to rename my column ato data to get past this brick wall:
df_e2.columns = ['data']


# Continue splitting nested lists into different columns 
df_e3 = df_e2['data'].apply(pd.Series)



# Squeeze nested lists rows into single column
output = df_e2.explode('data').assign(Co2 = lambda x: 
                              x['data'].str.get('rank')).reset_index(drop=True)


d = output['data'].apply(pd.Series)

# Mini data frame 1
teams = d['team'].apply(pd.Series)

# Mini data frame 2
games = d['all'].apply(pd.Series)

# Mini data frame 3
goals = games['goals'].apply(pd.Series)


# Build the final data frame as your league table standings

df = pd.DataFrame()

df['Rank'] = d['rank']
df['Team'] = teams['name']
df['MP'] = games['played']
df['W'] = games['win']
df['D'] = games['draw']
df['L'] = games['lose']
df['GF'] = goals['for']
df['GA'] = goals['against']
df['GD'] = d['goalsDiff']
df['Pts'] = d['points']
df['League'] = 'Premier League'


# Show league table without index
print(df.to_string(index=False))

# Write df to Premier League table
prem_league_table = df



############################################# 2. GERMAN BUNDESLIGA ##############################################

# Let's return the Bundesliga table in this instance


url = "-----"
querystring = {"season":"2021","league":"78"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# response.json()



## Stage 2: From JSON to Pandas 


# Read JSON response into a variable
e = response.json()['response'] #['standings']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
df_e = pd.DataFrame(e)
df_e1 = df_e['league'].apply(pd.Series)
df_e2 = df_e1['standings'].apply(pd.Series)


# The column name of this data frame was '0', which Python misinterprets as 'row values'. I had to rename my column ato data to get past this brick wall:
df_e2.columns = ['data']


# Continue splitting nested lists into different columns 
df_e3 = df_e2['data'].apply(pd.Series)



# Squeeze nested lists rows into single column
output = df_e2.explode('data').assign(Co2 = lambda x: 
                              x['data'].str.get('rank')).reset_index(drop=True)


d = output['data'].apply(pd.Series)

# Mini data frame 1
teams = d['team'].apply(pd.Series)

# Mini data frame 2
games = d['all'].apply(pd.Series)

# Mini data frame 3
goals = games['goals'].apply(pd.Series)


# Build the final data frame as your league table standings

df = pd.DataFrame()


df['Rank'] = d['rank']
df['Team'] = teams['name']
df['MP'] = games['played']
df['W'] = games['win']
df['D'] = games['draw']
df['L'] = games['lose']
df['GF'] = goals['for']
df['GA'] = goals['against']
df['GD'] = d['goalsDiff']
df['Pts'] = d['points']
df['League'] = 'Bundesliga'


# Show league table without index
print(df.to_string(index=False))


# Write df to Bundesliga table
bundesliga_table = df



####################################### 3. LA LIGA ##############################################

# Let's return the La Liga table in this instance


url = "-----"
querystring = {"season":"2021","league":"140"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# response.json()



## Stage 2: From JSON to Pandas 


# Read JSON response into a variable
e = response.json()['response'] #['standings']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
df_e = pd.DataFrame(e)
df_e1 = df_e['league'].apply(pd.Series)
df_e2 = df_e1['standings'].apply(pd.Series)


# The column name of this data frame was '0', which Python misinterprets as 'row values'. I had to rename my column ato data to get past this brick wall:
df_e2.columns = ['data']


# Continue splitting nested lists into different columns 
df_e3 = df_e2['data'].apply(pd.Series)


# Squeeze nested lists rows into single column
output = df_e2.explode('data').assign(Co2 = lambda x: 
                              x['data'].str.get('rank')).reset_index(drop=True)


d = output['data'].apply(pd.Series)

# Mini data frame 1
teams = d['team'].apply(pd.Series)

# Mini data frame 2
games = d['all'].apply(pd.Series)

# Mini data frame 3
goals = games['goals'].apply(pd.Series)


# Build the final data frame as your league table standings

df = pd.DataFrame()

df['Rank'] = d['rank']
df['Team'] = teams['name']
df['MP'] = games['played']
df['W'] = games['win']
df['D'] = games['draw']
df['L'] = games['lose']
df['GF'] = goals['for']
df['GA'] = goals['against']
df['GD'] = d['goalsDiff']
df['Pts'] = d['points']
df['League'] = 'La Liga'


# Show league table without 
print(df.to_string(index=False))



# Write df to La Liga table
la_liga_table = df





####################################### 4. SERIE A ##############################################

# Let's return the Serie A table in this instance


url = "-----"
querystring = {"season":"2021","league":"135"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# response.json()



## Stage 2: From JSON to Pandas 


# Read JSON response into a variable
e = response.json()['response'] #['standings']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
df_e = pd.DataFrame(e)
df_e1 = df_e['league'].apply(pd.Series)
df_e2 = df_e1['standings'].apply(pd.Series)


# The column name of this data frame was '0', which Python misinterprets as 'row values'. I had to rename my column ato data to get past this brick wall:
df_e2.columns = ['data']


# Continue splitting nested lists into different columns 
df_e3 = df_e2['data'].apply(pd.Series)




# Squeeze nested lists rows into single column
output = df_e2.explode('data').assign(Co2 = lambda x: 
                              x['data'].str.get('rank')).reset_index(drop=True)


d = output['data'].apply(pd.Series)

# Mini data frame 1
teams = d['team'].apply(pd.Series)

# Mini data frame 2
games = d['all'].apply(pd.Series)

# Mini data frame 3
goals = games['goals'].apply(pd.Series)


# Build the final data frame as your league table standings

df = pd.DataFrame()


df['Rank'] = d['rank']
df['Team'] = teams['name']
df['MP'] = games['played']
df['W'] = games['win']
df['D'] = games['draw']
df['L'] = games['lose']
df['GF'] = goals['for']
df['GA'] = goals['against']
df['GD'] = d['goalsDiff']
df['Pts'] = d['points']
df['League'] = 'Serie A'



# Show league table without 
print(df.to_string(index=False))

# Write df to Serie A table
serie_a_table = df




####################################### 5. LIGUE 1 ##############################################

# Let's return the Ligue 1 table in this instance


url = "-----"
querystring = {"season":"2021","league":"61"}

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "5883cc35b5msh2fa28b6451a6f1cp15299cjsnea73454ab5ff"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# response.json()



## Stage 2: From JSON to Pandas 


# Read JSON response into a variable
e = response.json()['response'] #['standings']


# Read response into a Dataframe and split nested lists into different columns until you get to your desired level
df_e = pd.DataFrame(e)
df_e1 = df_e['league'].apply(pd.Series)
df_e2 = df_e1['standings'].apply(pd.Series)


# The column name of this data frame was '0', which Python misinterprets as 'row values'. I had to rename my column ato data to get past this brick wall:
df_e2.columns = ['data']


# Continue splitting nested lists into different columns 
df_e3 = df_e2['data'].apply(pd.Series)


# Squeeze nested lists rows into single column
output = df_e2.explode('data').assign(Co2 = lambda x: 
                              x['data'].str.get('rank')).reset_index(drop=True)


d = output['data'].apply(pd.Series)

# Mini data frame 1
teams = d['team'].apply(pd.Series)

# Mini data frame 2
games = d['all'].apply(pd.Series)

# Mini data frame 3
goals = games['goals'].apply(pd.Series)


# Build the final data frame as your league table standings

df = pd.DataFrame()


df['Rank'] = d['rank']
df['Team'] = teams['name']
df['MP'] = games['played']
df['W'] = games['win']
df['D'] = games['draw']
df['L'] = games['lose']
df['GF'] = goals['for']
df['GA'] = goals['against']
df['GD'] = d['goalsDiff']
df['Pts'] = d['points']
df['League'] = 'Ligue 1'



# Show league table without 
print(df.to_string(index=False))

# Write df to Ligue 1 table
ligue_1_table = df



############################################################################################################################################################################################
# This STEP merges all 5 leagues into ONE data frame  
# (SIDE NOTE: Deploy this method with Europe's top goal scorers, assists, passes and clean sheets also) 
#
# Premier League = 20  
# Bundesliga=      18
# La Liga =        20
# Ligue 1 =        20
# Serie A  =       20
 # ----------------------
# Grand Total =    98
############################################################################################################################################################################################

prem_league_table.to_csv('D:/Projects/Python/Football/Leagues/Premier League/outputs/2021-2022/prem_league_table.csv', index = False)
bundesliga_table.to_csv('D:/Projects/Python/Football/Leagues/Bundesliga/outputs/2021-2022/bundesliga_table.csv', index = False)
la_liga_table.to_csv('D:/Projects/Python/Football/Leagues/La Liga/outputs/2021-2022/la_liga_table.csv', index = False)
serie_a_table.to_csv('D:/Projects/Python/Football/Leagues/Serie A/outputs/2021-2022/serie_a_table.csv', index = False)
ligue_1_table.to_csv('D:/Projects/Python/Football/Leagues/Ligue 1/outputs/2021-2022/ligue_1_table.csv', index = False)

