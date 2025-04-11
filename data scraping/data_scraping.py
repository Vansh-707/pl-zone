##importing all required libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests 
import time

all_teams = [] ## list to store all teams

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

url = 'https://fbref.com/en/comps/9/Premier-League-Stats'
soup = get_html(url)

table = soup.find_all('table', class_ = 'stats_table')[0] ##only want the first table, therefore the first index

links = table.find_all('a') ## finding all links in the table 
links = [l.get("href") for l in links] ##parsing through links
links = [l for l in links if '/squads/' in l] ##filtering through links to only get squads

team_urls = [f"https://fbref.com{l}" for l in links] ## formatting back to links

print(team_urls)

for team_url in team_urls: 
    team_name = team_url.split("/")[-1].replace("-Stats", "") ##isolating the names of the teams
    print(team_name)

    soup = get_html(team_url)
    stats = soup.find_all('table', class_ = "stats_table")[0] ##again, only want the first table

    if stats and stats.columns: stats.columns = stats.columns.droplevel() ##formatting the stats

    # Assuming 'team_data' is a BeautifulSoup Tag
    # Convert it into a DataFrame

    team_data = pd.read_html(str(stats))[0]
    team_data.columns = [x[1] for x in team_data.columns] # convert the multi index to single index columns
    team_data["Team"]= team_name
    all_teams.append(team_data) ## appending the data
    time.sleep(5) ## making sure we don't get blocked from scraping by delaying each loop by 5 seconds

stat_df = pd.concat(all_teams) ## concatenating all of the stats
print(stat_df.columns)

stat_df = stat_df[['Player','Nation','Pos','Age','MP','Starts','Min','Gls','Ast','PK','CrdY','CrdR','xG','xAG', 'Team']]
stat_df = stat_df.drop(stat_df[stat_df['Player'] == 'Squad Total'].index)
stat_df = stat_df.drop(stat_df[stat_df['Player'] == 'Opponent Total'].index)

stat_df['Age'] = [float(str(x).split("-")[0]) for x in stat_df['Age']]
stat_df.fillna(0.0, inplace= True)
stat_df = stat_df.loc[:,~stat_df.columns.duplicated()]

stat_df.to_csv("data/stats.csv")

df = pd.read_csv("data/stats.csv", index_col = 0)
df = df.loc[:,~df.columns.duplicated()]
print(df)