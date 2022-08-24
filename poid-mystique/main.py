import js

l1 = 'ا'
l2 = 'ب'
l3 = 'ج'
l4 = 'د'
l5 = 'ه'
l6 = 'و'
l7 = 'ز'
l8 = 'ح'
l9 = 'ط'
l10 = 'ي'
l11 = 'ك'
l12 = 'ل'
l13 = 'م'
l14 = 'ن'
l15 = 'ص'
l16 = 'ع'
l17 = 'ف'
l18 = 'ض'
l19 = 'ق'
l20 = 'ر'
l21 = 'س'
l22 = 'ت'
l23 = 'ث'
l24 = 'خ'
l25 = 'ذ'
l26 = 'ظ'
l27 = 'غ'
l28 = 'ش'

l29 = 'ة'
l30 = 'ء'
l31 = ' '


sum_dict = {l1 : 1, l2 : 2, l3 : 3, l4 : 4,  
            l5 : 5, l6 : 6, l7 : 7, l8 : 8,
            l9 : 9, l10 : 10, l11 : 20, l12 : 30,
            l13 : 40, l14 : 50, l15 : 60, l16 : 70,
            l17 : 80, l18 : 90, l19 : 100, l20 : 200,
            l21 : 300, l22 : 400, l23 : 500, l24 : 600, 
            l25 : 700, l26 : 800, l27 : 900, l28 : 1000,
            l29 : 5, l30:1, l31:0} 
def pm(*args, **kwargs):  
    entry = Element('search').value
    opt = Element('output')
    opt2 = Element('valeur-num')

    if entry == '':
        js.alert('Le champ est vide')
        quit()
    else:
        pass

    try:
        res = sum(sum_dict[ele] for ele in entry) 
        opt.write(f"Sa valeur numerique est de: ")
        opt2.write(f"{str(res)}")
    except:
        js.alert('Erreur de saisie')
    

