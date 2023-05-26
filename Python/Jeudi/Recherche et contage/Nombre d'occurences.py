def occurrences(e,t): 
    """ 
    cette fonction compte les occurrences de e dans t 
    >>>occurrences(0,[1,0,1,1,0]) 
    2 
    >>>occurrences(1,[1,0,1,1,0]) 
    3 
    """ 
    nb=0 
    for v in t: 
        if v==e: 
            nb=nb+1 
    return nb