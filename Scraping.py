import requests
import csv
import json
import time 
import pandas as pd


games_id_api = "http://api.steampowered.com/ISteamApps/GetAppList/v0002/"

games_info_api = "http://store.steampowered.com/api/appdetails?appids="

games_id_list = []

# def get_games_id():
#     response = requests.get(games_id_api)
#     games = response.json()

#     with open('games_id.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['appid', 'name'])
#         for game in games['applist']['apps']:
#             writer.writerow([game['appid'], game['name']])
#             games_id_list.append(game['appid'])
df = pd.read_csv('games_id.csv')


games_id_list = df['appid'].tolist()

print(games_id_list)
print(len(games_id_list))




def get_games_info():
        with open('games_info.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['appid', 'name', 'type', 'required_age', 'is_free', 'detailed_description', 'about_the_game', 'short_description', 'header_image', 'developers', 'publishers', 'price', 'release_date'])

           
            for game_id in games_id_list:
                response = requests.get(games_info_api + str(game_id))
                if response.status_code == 200:
                    try:
                        game_info = response.json()
                        if str(game_id) in game_info and game_info[str(game_id)]['success']:
                            data = game_info[str(game_id)]['data']
                            writer.writerow([
                                data.get('steam_appid', ''),
                                data.get('name', ''),
                                data.get('type', ''),
                                data.get('required_age', ''),
                                data.get('is_free', ''),
                                data.get('header_image', ''),
                                ', '.join(data.get('developers', [])),
                                ', '.join(data.get('publishers', [])),
                                data.get('price_overview', {}).get('final_formatted', ''),
                                data.get('release_date', {}).get('date', '')
                            ])
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON for game ID {game_id}")
                else:
                    print(f"Failed to fetch data for game ID {game_id}, status code: {response.status_code}")
                    if response.status_code == 429:
                        print("Rate limit exceeded. Waiting for 60 seconds.")
                        time.sleep(60)  # Wait for 60 seconds before retrying





