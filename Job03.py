

"""Créez un script job03.py qui dans un premier temps va afficher la phrase “Bonjour, quel
âge as tu ? ”
L’utilisateur devra ensuite entrer son âge.
Déclarez une variable “âge”, qui prendra la valeur saisie par l’utilisateur.
A l’aide d’une fonction system, affichez “Tu es mineur” si l’âge est inférieur à 18, et “Tu
es majeur” si l’âge est supérieur ou égal à 18."""""

age = int(input("Salut, quel age as tu ?"))
if age < 18:
    print("tu es mineur")
else:
    print("tu es majeur")
