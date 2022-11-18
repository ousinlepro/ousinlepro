import statistics
import math

def calcule_moyenne(notes:list,matiere:list):
    t = 20 * len(notes)
    moyenne = statistics.mean(notes) # la moyenne
    print(f'{matiere} : {moyenne}')

notes_hg = [15,19,17]
#calcule_moyenne(notes_hg,'histo-Geo')

matiere = input('[!] Discipline: ')
notes = input('Veuillez saisir les notes en les separant par "/" \n[!] notes:')
notes = notes.split('/')
notes = [float(x) for x in notes]
calcule_moyenne(notes,matiere)


#print(moyenne)