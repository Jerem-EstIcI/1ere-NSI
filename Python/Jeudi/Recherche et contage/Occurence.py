def occurrence(e,t): 
    """ 
    cette fonction booléenne renvoie True si e est dans t 
    >>>occurrence(22,[76,14,50,35]) 
    False 
    >>>occurrence(14,[76,14,50,35]) 
    True 
    """ 
    for v in t: 
        if v==e: 
            return True 
    return False