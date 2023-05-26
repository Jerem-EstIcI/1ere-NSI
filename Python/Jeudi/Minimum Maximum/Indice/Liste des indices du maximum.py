def indices_max(t): 
    """ 
    la fonction renvoie les indices où le maximum 
    du tableau t est atteint 
    >>>indices_max([12,25,-5,15,25,17]) 
    [1,4] 
    """ 
    m=t[0] 
    liste=[] 
    for k in range(1,len(t)): 
        if t[k]==m: 
            liste.append(k) 
        if t[k]>m: 
            m,liste=t[k],[k] 
    return liste
