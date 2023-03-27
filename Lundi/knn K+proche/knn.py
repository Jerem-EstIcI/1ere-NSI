import csv
def lis_csv(fichier,delimiteur=","):
	'''
	lis un fichier csv sépararé par un delimiteur (,  par défaut)
	entrée : nom du fichier, optionnel : delimiteur
	sortie : un tableau de dictionnaire contenant les champs comme clés
	'''	
	table=[]
	#ouverture du fichier csv en lecture (r=read)
	with open(fichier,'r',encoding='utf-8') as fichierCsv:
		contenu = csv.DictReader(fichierCsv, delimiter=delimiteur)
		#les enregistrements correspondent aux lignes de contenu
		for ligne in contenu:
				#ajout de chaque ligne à la table
				table.append(dict(ligne))
		return table

def d(A,B):
    '''
    Fonction qui calcule la distance 
    entre les 2 points A et B les points sont représentés
    par des tuples(x,y)
    '''
    x1=A[0]
    y1=A[1]
    x2=B[0]
    y2=B[1]
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def knn(maison,k):
    '''
    prendre les coordonnées d'une maison et
    renvoie les k maison de table les plus proches
    '''
    donnees=lis_csv("familles.csv",';')
    
    for ligne in donnees:
        pt=eval(ligne['coordonnées_maison'])
        distance=d(maison,pt)
        ligne['distance']=distance
    #print(donnees)    
    dtrie=sorted(donnees,key=lambda ligne:ligne['distance'])
    #print(dtrie)
    place={}
    choix=0
    for valeur in dtrie[0:k]:
        try:
	        # si la clé n'existe pas la ligne suivante crée une exception (erreur) 
	        place[valeur["numéro_école"]]+=1
	        # sinon la ligne de code ajoute bien 1 à la valeur du dico de clé "clé" 
        except: 
	        # cette ligne est exécutée seulement en cas d'erreur
            place[valeur["numéro_école"]]=1
    #print(place)
    vmax = max(place.values())
    for endroit, v in place.items():
        '''
        Retourne l'index correspondant le plus grand dans
        le dictionnaire et renvoie le nom de la valeur
        (choix de l'école)
        '''
        if v == vmax:
            choix = endroit
            break
    print(choix)
knn((5,3),5)

