# Créer un programme job11.py qui parcourt le contenu du fichier “domains.xml” et qui
# compte le nombre de noms de domaine.

from xml.dom import minidom

doc = minidom.parse('domains.xml')
elements = doc.getElementsByTagName("column")
newList = []

for element in elements:
    if element.getAttribute("name") == "domain":
        newList.append(element.childNodes[0].data)
        
print(len(newList))