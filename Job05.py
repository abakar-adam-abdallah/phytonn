"""Créez un script job05.py
L’utilisateur devra entrer deux valeurs en input.
A l’aide d’une boucle for et d’une fonction system, affichez uniquement les nombres se
trouvant entre l’input 1 et l’input 2. Le programme doit toujours partir de l’input 1 et
aller jusqu’à l’input 2.
Si les deux sont égaux, le programme devra écrire “Valeurs égales”."""

aba = int(input("Valeur 1 : "))
fer = int(input("Valeur 2 : "))

for aba in range(aba+1,fer):
    print(aba)

for fer in reversed(range(fer+1,aba)):
    print(fer)
if aba == fer:
    print("Valeur égales") 
