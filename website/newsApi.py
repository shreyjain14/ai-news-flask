import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

URL = f'https://newsdata.io/api/1/news?apikey={NEWS_API_KEY}&language=en'


def read_next_page():
    with open('website/next_page.txt') as f:
        page = f.readline()
    return page


def write_next_page(new_val):
    with open('website/next_page.txt', 'w') as f:
        lines = f.write(new_val)


def get_india_news():

    try:
        page = read_next_page()
        if page:
            response = requests.get(f'{URL}&country=in&page={page}').json()
        else:
            response = requests.get(f'{URL}&country=in').json()

        write_next_page(response['nextPage'])

        res = []

        if response['status'] == 'success':
            for result in response['results']:
                res.append([result['content'], result['article_id']])

        return res

    except KeyError:
        print('request limit')
        return []


if __name__ == '__main__':
    print(get_india_news()[0][0])
