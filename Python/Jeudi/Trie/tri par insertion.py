def tri_insertion(t): 
    """ 
    cette fonction tri e en place le tableau t 
    >>>t = [5, 3, 8, 2, 1]
    >>>tri_insertion(t)
    >>>print(t)
    [1, 2, 3, 5, 8]
    """ 
    tri_insertion(t)
    for i in range(1,len(t)): 
        j,e=i,t[i] 
        while j>0 and t[j-1]>e: 
            t[j],j=t[j-1],j-1 
        t[j]=e