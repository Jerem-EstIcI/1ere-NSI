objets=[
    ['or','1','10000'],
    ['TV','8','4000'],
    ['orinateur','6','3000'],
    ['portable','1','3000']
]
    
def sac(masse,objets):
    valeur=0
    dispo=masse
    charge=[]
    for objet in objets:
        if objet[1]<=dispo:
            charge.append(objet[0])
            valeur=valeur+objet[2]
            dispo=dispo-objet[1]
    return charge,valeur
print(sac(13,objets))