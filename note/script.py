#from js import document
from statistics import mean
import js
from js import document
from time import sleep

opt_matieres = Element('matieres')
opt_notes = Element('notes')

opt_moyenne = Element('moyenne')

notes = {"Redaction":mean([12]),
        "TSQ"       :mean([17.5]),
        "Dictee"    :mean([14]),
        "Anglais"   :mean([17]),
        "Espagnole" :mean([13,12]),
        "SVT"       :mean([18.25]),
        "Maths"     :mean([16]),
        "PC"        :mean([12.5,18]),
        "EC"        :mean([19]),
        "HG"        :mean([15]),
        "Eco-Fam"   :mean([18]),
        "EPS"       :mean([16,17,9]),
}

list_notes = []


for matiere in notes:
    note = notes.get(matiere)

    list_notes.append(note)

    opt_matieres.write(matiere,note)


for n in list_notes:
    opt_notes.write(n,note)

total = sum(list_notes)

pts_t = 20*len(list_notes)

m = mean(list_notes) # la moyenne
m = round(m,2) # arrondir la moyenne a 2 chiffres apres la virgule

prc = (total * 100) / pts_t # la pourcentages de points

def calcule(*args, **kwargs):
    opt_moyenne.write(m)



