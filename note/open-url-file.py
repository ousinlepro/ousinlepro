from urllib.request import urlopen

import requests

url = "https://raw.githubusercontent.com/ousinlepro/ousinlepro.github.com/main/notes-db.csv"
page = requests.get(url)
print(page.text)

"""


f = urlopen('https://api.github.com/repos/ousinlepro/ousinlepro.github.com/contents/notes-db.csv')

for line in f:
    print(line.decode('utf-8'))

"""