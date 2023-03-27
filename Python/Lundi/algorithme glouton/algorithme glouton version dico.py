table= [
    {'nom' : 'or','valeur' : 10000,'masse' : 1},
    {'nom' : 'TV','valeur' : 4000,'masse' : 6},
    {'nom' : 'Ordi','valeur' : 3000,'masse' : 3},
    {'nom' : 'Portable','valeur' : 3000,'masse' : 1}
]
def sac(table,msac):
    charge=[]
    vtotal=0
    for ligne in table:
        ligne['rapport']= ligne['valeur']/ ligne['masse']

    trie=sorted(table,key=lambda ligne:ligne['rapport'],reverse=True)
    for ligne in table:
        if ligne['masse']<=msac:
            charge.append(ligne['nom'])
            vtotal=vtotal+ligne['valeur']
            msac=msac-ligne['masse']
    return charge,vtotal

print(sac(table,10))
    