from statistics import mean
from art import text2art
import csv
import re
from urllib.request import urlopen
import requests

# dev

with open('notes-db.csv',encoding='utf-8') as f:
    file_content = list(csv.reader(f))

list_notes = []

print()
for line in file_content: 

    note = line[1:]
    if '.' in note:
        note = map(lambda n: float(n), note)

    else:
        note = map(lambda n: float(n), note)
        #note = int(note)
    note = mean(note)
    list_notes.append(note)

    print(line[0],note)
    

total = sum(list_notes)

pts_t = 20*len(list_notes)

m = mean(list_notes) # la moyenne
#m = round(m,2) # arrondir la moyenne a 2 chiffres apres la virgule

prc = (total * 100) / pts_t # la pourcentages de points

print()
print(f'[+] moyenne: {m}')
print(f'[+] meilleure note: {max(list_notes)}')
print(f'[+] plus petite note: {min(list_notes)}')
print(f'[+] {total} / {pts_t} points')
print(f'[+] {round(prc)}% ')
print()

with open('moyenne.txt', 'w') as f:
    f.write(f"""Moyenne: {m} \n
    Meilleure note {max(list_notes)} \n
    plus petite note: {min(list_notes)} \n
    {round(total)} / {pts_t} points \n
    {round(prc)}% 
    """)

