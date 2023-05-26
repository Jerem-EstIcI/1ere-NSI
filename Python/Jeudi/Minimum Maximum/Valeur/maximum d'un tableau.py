def maximum(t):
    """ la fonction renvoie le maximum du tableau t 
    >>>maximum([12,25,-5,15]) 
    25 
    """ 
    m=t[0] 
    for k in range(1,len(t)): 
        if t[k]>m: 
            m=t[k] 
    return m