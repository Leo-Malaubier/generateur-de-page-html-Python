def Liaison(Id,Mdp): #return que True ou False pour le moment
    if Id == None:
        return None, None
    elif Id== '':
        return 'Rien', None
    elif Id== 'salut':
        return True, "SimpleUsers"
    elif Id== 'bonjour':
        return True, "SuperUtilisateur"
    elif Id!= 'salut':
        return 'Faux', None
