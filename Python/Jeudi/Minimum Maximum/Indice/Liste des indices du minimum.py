def indices_min(t): 
    """ 
    la fonction renvoie les indices où le minimum 
    du tableau t est atteint 
    >>>indices_min([12,25,-5,15,25,17]) 
    [1,4] 
    """ 
    m=t[0] 
    liste=[] 
    for k in range(1,len(t)): 
        if t[k]==m: 
            liste.append(k) 
        if t[k]<m: 
            m,liste=t[k],[k] 
    return liste
