def maximum(t):
    """
    la fonction renvoie le maximum du tableau t 
    et son indice 
    >>>maximum([12,25,-5,15]) 
    (25,1) 
    """ 
    indice=0 
    for k in range(1,len(t)):
        if t[k]>t[indice]: 
            indice=k 
    return t[indice],indice