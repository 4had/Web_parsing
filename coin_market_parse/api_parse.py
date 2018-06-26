import requests
import csv

csv_header = ['name', 'symbol', 'rank']
start = 1
first_circle = True
while True:
    try:
        url = 'https://api.coinmarketcap.com/v2/ticker'
        params = {'sort': 'rank', 'start': start, 'structure': 'array'}
        response = requests.get(url, params=params)
        json_data = response.json()['data']

        with open('api_coins_parse.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)

            if first_circle:
                writer.writerow(csv_header)
                first_circle = False
            for data in json_data:
                writer.writerow([data['name'],
                                 data['symbol'],
                                 data['rank']])
        start += 100
        print(start)
    except TypeError:
        print('Done')
        break
