def maxdico(d): 
    """ 
    la fonction renvoie le maximum du dictionnaire 
    >>>maxdico({'Alfred':12,'Chloé':30,'Joe':6}) 
    30 
    """ 
    m=0 
    for v in d.values(): 
        if v>m: 
            m=v 
    return m