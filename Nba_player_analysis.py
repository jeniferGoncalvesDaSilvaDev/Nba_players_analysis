import numpy as np
import pandas as pd
from scipy.stats import linregress, f_oneway
players={
    "players": [
        {
            "name": "LeBron James",
            "team": "Los Angeles Lakers",
            "position": "Small Forward",
            "points": 25000,
            "xp": 1500,
            "rebounds": 7000,
            "assists": 7000,
            "fgm": 9000,
            "fga": 15000,
            "ftm": 5000,
            "fta": 7000,
            "3pm": 2000,
            "3pa": 4000,
            "steals": 2000,
            "blocks": 1000,
            "games_played": 1300
        },
        {
            "name": "Stephen Curry",
            "team": "Golden State Warriors",
            "position": "Point Guard",
            "points": 23000,
            "xp": 1400,
            "rebounds": 5000,
            "assists": 6000,
            "fgm": 8000,
            "fga": 13000,
            "ftm": 4000,
            "fta": 5000,
            "3pm": 3000,
            "3pa": 5000,
            "steals": 1500,
            "blocks": 500,
            "games_played": 1200
        },
        {
            "name": "Giannis Antetokounmpo",
            "team": "Milwaukee Bucks",
            "position": "Power Forward",
            "points": 20000,
            "xp": 1200,
            "rebounds": 8000,
            "assists": 3000,
            "fgm": 7000,
            "fga": 11000,
            "ftm": 3000,
            "fta": 4000,
            "3pm": 1000,
            "3pa": 2000,
            "steals": 1200,
            "blocks": 1500,
            "games_played": 1000
        },
        {
            "name": "Kevin Durant",
            "team": "Phoenix Suns",
            "position": "Small Forward",
            "points": 22000,
            "xp": 1300,
            "rebounds": 6000,
            "assists": 4000,
            "fgm": 8500,
            "fga": 14000,
            "ftm": 3500,
            "fta": 5000,
            "3pm": 1500,
            "3pa": 3000,
            "steals": 1000,
            "blocks": 800,
            "games_played": 1100
        },
        {
            "name": "Joel Embiid",
            "team": "Philadelphia 76ers",
            "position": "Center",
            "points": 18000,
            "xp": 1100,
            "rebounds": 7500,
            "assists": 2000,
            "fgm": 6000,
            "fga": 10000,
            "ftm": 2000,
            "fta": 3000,
            "3pm": 500,
            "3pa": 1000,
            "steals": 800,
            "blocks": 2000,
            "games_played": 900
        }
    ]
}



# Extraindo dados do JSON para um dataframe
data = {
    "name": ["LeBron James", "Stephen Curry", "Giannis Antetokounmpo", "Kevin Durant", "Joel Embiid"],
    "team": ["Los Angeles Lakers", "Golden State Warriors", "Milwaukee Bucks", "Phoenix Suns", "Philadelphia 76ers"],
    "position": ["Small Forward", "Point Guard", "Power Forward", "Small Forward", "Center"],
    "points": [25000, 23000, 20000, 22000, 18000],
    "xp": [1500, 1400, 1200, 1300, 1100],
    "rebounds": [7000, 5000, 8000, 6000, 7500],
    "assists": [7000, 6000, 3000, 4000, 2000],
    "fgm": [9000, 8000, 7000, 8500, 6000],
    "fga": [15000, 13000, 11000, 14000, 10000],
    "ftm": [5000, 4000, 3000, 3500, 2000],
    "fta": [7000, 5000, 4000, 5000, 3000],
    "3pm": [2000, 3000, 1000, 1500, 500],
    "3pa": [4000, 5000, 2000, 3000, 1000],
    "steals": [2000, 1500, 1200, 1000, 800],
    "blocks": [1000, 500, 1500, 800, 2000],
    "games_played": [1300, 1200, 1000, 1100, 900]
}

# Convertendo para DataFrame
df = pd.DataFrame(data)
#print(df)


#print(array_points)


# Desempenho geral dos jogadores:

#Quais jogadores têm o maior número de pontos acumulados na carreira? Como isso se correlaciona com outros indicadores, como assistências ou rebotes?
#O que diferencia os jogadores com maior experiência (XP) dos menos experientes em termos de pontos, rebotes e assistências?
#print(df.columns)
#pegar os jogadores e pontos

jogador_pontos = df[['name','points']]
array_jogador_pontos = np.array(jogador_pontos)
#print(jogador_pontos)
#print(array_jogador_pontos)
#sortear os pontos com lambda 

sorted_points = sorted(array_jogador_pontos, key=lambda x: x[1], reverse=True) 
#print(sorted_points)
array_sorted = np.array(sorted_points)
#print(array_sorted)
df_points = pd.DataFrame(array_sorted)
#print(df_points)
#pegar assistência e rebotes 
assistencia_rebotes = df[['assists', 'rebounds']]
print(assistencia_rebotes)
rebotes = assistencia_rebotes["rebounds"].tolist() 
#print(rebotes)
assistencia = assistencia_rebotes["assists"].tolist()
#print(assistencia)
sorted_assistencia_rebotes_1 = sorted(rebotes, key=lambda x: x, reverse=True) 
#print(sorted_assistencia_rebotes_1)
sorted_assistencia_rebotes_2 = sorted(assistencia, key=lambda x: x, reverse=True) 
#print(sorted_assistencia_rebotes_2)
array_assitencia = np.array(sorted_assistencia_rebotes_1)
array_rebotes = np.array(sorted_assistencia_rebotes_2)
print(array_assitencia)
print(array_rebotes)
df_rebotes = pd.DataFrame(array_rebotes)
#print(df_rebotes)
df_assistencia = pd.DataFrame(array_assitencia)
df_points =df_points.merge(df_assistencia,left_index=True, right_index=True)
df_points=df_points.merge(df_rebotes,left_index=True, right_index=True) 
print(df_points.columns)
#print(df_points)
df_points['name'] = df_points['0_x']

df_points.drop(columns=['0_x'],inplace=True)

#print(df_points['name'])
df_points['points'] = df_points[1]
df_points.drop(columns=[1],inplace=True)
df_points['assists'] = df_points['0_y']
df_points.drop(columns=['0_y'],inplace=True)
df_points['rebots'] = df_points[0]
df_points.drop(columns=[0],inplace=True)
print(df_points)

#p_value, r_value, intercept, slope, std_err
x_rebotes = df_points['rebots'].tolist()
y_points = df_points['points'].tolist()
x_assistencia = df_points['assists'].tolist() 
intercept, slope, r_value, p_value, std_err = linregress(x_rebotes, y_points)


# Print the results
#print("correlação entre pontos e rebotes")
#print("Intercept:", intercept)
#print("Slope:", slope)
#print("R-value:", r_value)
#print("P-value:", p_value)
#print("Standard Error:", std_err)
#teste anova 
f_statistic, p_value = f_oneway(x_rebotes, y_points)
#f_statistic = f_statistic[0]
#print("teste anova",f_statistic)

intercept2, slope2, p_value2, r_value2, std_err2 = linregress(x_assistencia, y_points)


# Print the results
#print("correlação entre pontos e assistencia")
#print("Intercept:", intercept2)
#print("Slope:", slope2)
#print("R-value:", r_value2)
#print("P-value:", p_value2)
#print("Standard Error:", std_err2)
#teste anova 
#f_statistic2, p_value2 = f_oneway(x_assistencia, y_points)
#f_statistic = f_statistic[0]
#print("teste anova",f_statistic2)
#ha uma correlação maior entre pontos e rebotes do que pontos e assistencia

#Eficiência de arremessos:

#Quais jogadores têm a melhor eficiência de arremesso (Field Goal Percentage - FGM/FGA)? Isso afeta diretamente o número de pontos por jogo?
#Quem é o jogador com melhor aproveitamento de três pontos (3PM/3PA)?
fgm_players = df[['name','fgm']].values.tolist() 
#print(fgm_players)

sorted_fgm = sorted(fgm_players, key=lambda x: x[1], reverse=True) 
#print(sorted_fgm)
array_fgm_players = np.array(sorted_fgm)
#print(array_fgm_players)
df_fgm = pd.DataFrame(array_fgm_players)
df_points = df_points.merge(df_fgm, left_index=True, right_index=True)
df_points.drop(columns= [0],inplace=True)

df_points['fgm'] = df_points[1]
df_points.drop(columns= [1],inplace=True)

x_fgm = df_points['fgm'].tolist() 
#convert to integer
x_fgm =[int(i) for i in x_fgm]

intercept3, slope3, r_value3, p_value3, std_err3 = linregress(x_fgm, y_points)
f_statistic3 = f_oneway(x_fgm, y_points)
# Print the results
print("correlação entre pontos e eficiência de arremeso-fgm")
#print("Intercept:", intercept3)
#print("Slope:", slope3)
#print("R-value:", r_value3)
print("P-value:", p_value3) 
#print("Standard Error:", std_err3)
print("teste anova",f_statistic3[0])
print('nao ha interferência direta entre fgm e pontos')
df_player_3pm = df[['name', '3pm']].values.tolist()
#print(df_player_3pm)
sorted_3pm = sorted(df_player_3pm, key=lambda x: x[1], reverse=True) 
array_3pm_players = np.array(sorted_3pm)
#print(array_3pm_players)

df_points['fg_percent'] = df['fgm'] / df['fga']
fg_percent = df_points['fg_percent'].tolist()
print(fg_percent)

intercept4, slope4, r_value4, p_value4, std_err4 = linregress(fg_percent, y_points)
f_statistic4 = f_oneway(fg_percent, y_points)
# Print the results
print("correlação entre pontos e eficiência de arremeso-fgm")
#print("Intercept:", intercept3)
#print("Slope:", slope3)
#print("R-value:", r_value3)
print("P-value:", p_value4) 
#print("Standard Error:", std_err3)
print("teste anova",f_statistic4[0])




