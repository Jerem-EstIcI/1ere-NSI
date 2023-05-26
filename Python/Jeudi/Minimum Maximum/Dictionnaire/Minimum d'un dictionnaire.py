def mindico(d): 
    """ 
    la fonction renvoie le minimum du dictionnaire 
    >>>mindico({'Alfred':12,'Chloé':30,'Joe':6}) 
    6 
    """ 
    m= float('inf') 
    for v in d.values(): 
        if v<m: 
            m=v 
    return m