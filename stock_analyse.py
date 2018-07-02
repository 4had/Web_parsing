import requests
import pandas as pd
import matplotlib.pyplot as plt


URL = 'https://www.quandl.com/api/v3/datasets/WIKI/FB/data.json'
needed_columns = [
    'date',
    'open',
    'low',
    'high',
    'close',
]
params = {
    'api_key': '4xAGfdR3qC6LNhzkzYsn',
}


def make_request(url, params=None):
    response = requests.get(url, params=params)
    return response.json()


def make_data_frame(data):
    columns = data['dataset_data']['column_names'][0:6]
    data = [line[0:6] for line in data['dataset_data']['data']]
    data_frame = pd.DataFrame(data, columns=columns)
    data_frame['Date'] = data_frame['Date'].apply(pd.to_datetime)
    return data_frame


def make_graph(stock):
    plt.plot_date(stock['Date'], stock['High'], label='sdf', linestyle='solid', marker='None')
    plt.title('Apple high price since\n December 2017 to June 2018')
    plt.xlabel('Date', rotation=90)
    plt.ylabel('Price')
    plt.show()


def start():
    req = make_request(URL, params)
    stock = make_data_frame(req)
    make_graph(stock)


if __name__ == '__main__':
    start()
