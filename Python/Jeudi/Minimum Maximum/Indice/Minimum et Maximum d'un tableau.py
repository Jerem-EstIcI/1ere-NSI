def min_et_max(t):
    """
    la fonction renvoie le minimum et le maximum du tableau t
    >>> min_et_max([12, 25, -5, 15])
    (-5, 25)
    """
    m, M = t[0], t[0]
    for k in range(1, len(t)):
        if t[k] > M:
            M = t[k]
        if t[k] < m:
            m = t[k]
    return m, M
