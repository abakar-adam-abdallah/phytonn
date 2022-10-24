
"""Créer un programme job19.py. Le programme devra contenir une seule fonction qui
prend en paramètres un nombre de paramètres indéfini (uniquement des nombres).
La fonction devra :
- Remplir une liste myList contenant tous ces paramètres.
- Trier par ordre croissant la liste à l’aide de la fonction sort (Donc sans la fonction
sort)
- Afficher la liste dans un terminal"""""



def  myFunction( *params ):
    
    
     myList = []

     for param in params:
        if isinstance(param,(int)):
            myList.append(param)
        else:
            print("Attention un des paramètre n'est pas numerique")

     permutation = True
     passage = 0 



     while permutation == True:
    
        permutation = False 
        passage = passage + 1
        
        
        for en_cours in range(0, len(myList) - passage):
            if myList[en_cours] > myList[en_cours + 1]:
                permutation = True
                # on change les deux elements
                myList[en_cours], myList[en_cours + 1] = \
                myList[en_cours + 1],myList[en_cours]
     print (myList)

myFunction(3,6,89,78,66,45,2)

