
# Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
# le nombre de mots (sans caractère spéciaux) qui s’y trouvent.

# from ast import pattern
import re 
import re

fichier = open("data.txt","r")
txt = fichier.read()
pattern = '[a-zA-Z]+'
matches = re.findall(pattern, txt)

print(len(matches))