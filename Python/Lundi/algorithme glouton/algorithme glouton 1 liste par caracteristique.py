def sac(poids):
    lo=['or','tv','ordi','portable'] #liste objets
    lv=[10000,4000,3000,3000] #liste valeurs
    lm=[1,8,6,1] #liste masse
    charge=[]
    vsac=0 #valeur dans le sac
    msac=0 #masse dans le sac
    i=0
    
    for i in range(0,4):
        if msac+lm[i]<=poids:
            vsac = vsac + lv[i]
            msac = msac + lm[i]                
            charge.append(lo[i])
    print('objets',charge,'valeur',vsac,'€','masse',msac,'kg')
sac(13)