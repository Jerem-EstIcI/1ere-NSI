def dicho(e,t):
    """
    >>> dicho(29,[14,22,29,35,44,50,56,76])
    True
    >>> dicho(61,[14,22,29,35,44,50,56,76])
    False
    """
    i=0
    j=len(t)-1
    while i<=j:
        m=(i+j)//2
        if t[m]==e:
            return True
        elif e<t[m]:
            j=m-1
        else:
            i=m+1
    return False

print(dicho(29,[14,22,29,35,44,50,56,76]))
print(dicho(61,[14,22,29,35,44,50,56,76]))