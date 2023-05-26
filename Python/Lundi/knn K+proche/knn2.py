def knn(t,cible,k,dist): 
    nn=[] 
    for i in range(len(t)): 
        d=dist(t[i],cible) 
        if i<k: 
            nn.append((i,d)) 
            j=i 
        elif d<nn[k-1][1]: 
            j,nn[k-1]=k-1,(i,d) 
        while j>0 and nn[j][1]<nn[j-1][1]: 
            nn[j-1],nn[j]=nn[j],nn[j-1] 
            j=j-1 
    return nn
    
def euclidean_distance(a, b):
    # Calculate the Euclidean distance between two points.
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

data_points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
target_point = (6, 7)
k = 3

nearest_neighbors = knn(data_points, target_point, k, euclidean_distance)
print(nearest_neighbors)