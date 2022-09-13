import requests
import json

def get_products():
    r = requests.get(url="https://yungesau.net/products.json")
    data = r.json()
    return data

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip()

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

prev_products = read_file('./products.json')
products = json.dumps(get_products(), indent=4)

if products != prev_products:
    print('updated. saving product list...')
    write_file('./products.json', products)
else:
    print('not updated')