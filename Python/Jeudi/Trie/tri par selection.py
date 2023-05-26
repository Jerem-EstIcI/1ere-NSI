def tri(t):
    """
    tri par selection, en place
    >>>tab=[76,14,50,35,22,29,56,44]
    >>>tri(tab)
    >>>tab 
    [14,22,29,35,44,50,56,76]
    """
    for i in range(len(t)):
        j=rangminimum(t,i)
        t[i],t[j]=t[j],t[i]
        