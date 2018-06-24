import requests
from bs4 import BeautifulSoup
import csv
from multiprocessing import Pool


# function for pool method
def make_all(url):
    write_csv(get_data(get_html(url)))


# write coin data to the csv file if price > 1000$
def write_csv(data):
    try:
        with open('coins.csv', 'a') as file:
            writer = csv.writer(file)
            if int(float(data['price'].split(' ')[0])) > 1000:
                writer.writerow((data['name'],
                                 data['price']))
                print(data['price'])
            else:
                pass
    except ValueError:
        pass


# gets html of the link
def get_html(url):
    return requests.get(url).text


# collecting all links for each coin
def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find('table', id='currencies-all').findAll('td', class_='currency-name')
    links = []
    root_url = 'https://coinmarketcap.com'
    for row in rows:
        link = row.find('a', class_='currency-name-container link-secondary').get('href')
        links.append(root_url + link)
    return links


# collects name and price of each currancy
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        currency_name = soup.find('h1', {'class': 'details-panel-name'}).text.strip().replace('\n', ' ')
    except:
        currency_name = ''
    try:
        currency_price = soup.find('span', id='quote_price').text.strip().replace('\n', ' ').replace(',', '')
    except:
        currency_price = ''

    data = {
        'name': currency_name,
        'price': currency_price
    }
    return data


def main():
    url = 'https://coinmarketcap.com/all/views/all/'
    html = get_html(url)
    all_links = get_links(html)
    with Pool(40) as p:  # 40 proccesses at the same time
        p.map(make_all, all_links)


main()
