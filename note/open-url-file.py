from urllib.request import urlopen
import csv
import requests


url = "https://raw.githubusercontent.com/ousinlepro/ousinlepro.github.com/main/notes-db.csv"


page = requests.get(url)
txt = page.text

content = list(csv.reader(str(page.text)))

for line in content:
    print(line[0])

#print(page.text)

