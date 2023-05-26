def minimum(t):
    """ la fonction renvoie le minimum du tableau t 
    >>>minimum([12,25,-5,15]) 
    -5
    """ 
    m=t[0] 
    for k in range(1,len(t)): 
        if t[k]<m: 
            m=t[k] 
    return m