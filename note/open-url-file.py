from urllib.request import urlopen
import csv
import requests


url = "https://raw.githubusercontent.com/ousinlepro/ousinlepro.github.com/main/note/notes-db.csv"


page = requests.get(url)
txt = page.text

content = str(page.text)

print(content)


#print(page.text)

