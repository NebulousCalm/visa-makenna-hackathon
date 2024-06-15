import string
import random
import requests


def create_random_string(amount: int):
    return ''.join(random.choice(string.ascii_letters) for character in range(amount))


def get_site_impact(url: str):
    website_url = f'https://api.websitecarbon.com/site?url={url}'
    req = requests.get(website_url)
    resp = req.json()
    results = {
        'url': resp.get('url'),
        'green': resp.get('green'),
        'cleanerThan': resp.get('cleanerThan'),
        'rating': resp.get('rating'),
        'carbon-grams': str(resp.get('statistics', {}).get('co2', {}).get('grid', {}).get('grams')),
        'full_resp': resp
    }
    return results
