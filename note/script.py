#from js import document
from statistics import mean

notes = {"Eco-Fam"  :mean([18]),
        "Redaction" :mean([12]),
        "Anglais"   :mean([17]),
        "TSQ"       :mean([17.5]),
        "Espagnole" :mean([13]),
        "Dictee"    :mean([14]),
        "SVT"       :mean([18.25]),
        "Maths"     :mean([16]),
        "PC"        :mean([12.5]),
        "EC"        :mean([19]),
        "EPS"       :mean([16]),
        "HG"        :mean([16]),
}

list_notes = []


for matiere in notes:
    note = notes.get(matiere)
    #note = map(lambda n: float(n), note)

    #note = float(mean(note))

    list_notes.append(note)

    print(matiere,note)


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