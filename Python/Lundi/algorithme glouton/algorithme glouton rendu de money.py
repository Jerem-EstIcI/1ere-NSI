def rendre(arendre):
    lp=[200,100,50,20,10,5,2,1]
    rendu=[]
    index=0
    while arendre>0:    
        if lp[index]<=arendre:
            rendu.append(lp[index])
            arendre=arendre-lp[index]
        else:
            index=index+1

    return rendu
    
print(rendre(853))