import requests
import datetime

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip()

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def get_updated_at():
    r = requests.get(url="https://yungesau.net/collections/tees-more.json")
    data = r.json()
    return datetime.datetime.fromisoformat(data['collection']['updated_at'])

prev_time = datetime.datetime.fromisoformat(read_file('./updated_at.txt'))
updated_at = get_updated_at()

write_file('./updated_at.txt', updated_at.isoformat())

if prev_time < updated_at:
    print('updated. generating screenshot...')
    exec('shot-scraper multi shots.yml')
else:
    print('not updated')