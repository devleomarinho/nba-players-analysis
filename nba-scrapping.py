#%%
import requests
import time
import pandas as pd
pd.set_option('display.max_columns', None)
#%%
url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2003-04&SeasonType=Playoffs&StatCategory=PTS'
response = requests.get(url=url).json()
#%%
table_headers = response['resultSet']['headers']
table_headers
#%%
df_cols = ['SEASON'] + table_headers
df = pd.DataFrame(columns=df_cols)

seasons = ['2003-04', '2004-05','2005-06','2006-07','2007-08', '2008-09','2009-10','2010-11','2011-12','2012-13',
           '2013-14', '2014-15','2015-16','2016-17','2017-18', '2018-19','2019-20','2020-21','2021-22','2022-23','2023-24']

for s in seasons:
    api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season='+s+'&SeasonType=Playoffs&StatCategory=PTS'
    r = requests.get(url=api_url).json()
    temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
    temp_df2 = pd.DataFrame({'SEASON': [s for i in range(len(temp_df1))]})
    temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)
    df = pd.concat([df, temp_df3], axis=0)
    print(f'Raspagem dos stats da temporada {s} finalizada...')
    print('... esperando 10s para continuar')
    time.sleep(10)

print('Scrapping concluído!')
#%%
df.to_csv('nba_players_stats_20years.csv')
#%%
df['PLAYER']

