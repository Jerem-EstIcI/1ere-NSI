def minimum(t):
    """
    la fonction renvoie le minimum du tableau t et son indice 
    >>>minimum([12,25,-5,15]) 
    (-5,2) 
    """ 
    indice=0 
    for k in range(1,len(t)):
        if t[k]<t[indice]: 
            indice=k 
    return t[indice],indice