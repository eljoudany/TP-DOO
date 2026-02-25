from file1 import professeur 
import json

with open("professeur.json", mode="r", encoding="utf8") as file :
    lista=json.load(file)
listprof=[]

for dictp in lista : 
    listprof.append(professeur.fromdict(dictp))

print("nombre de profs :", len(lista))
print(f"le professeur 61 est :  {listprof[61].nom} habite a {listprof[61]}.adress")
print(f"le professeur 90 est :  {listprof[90].nom} habite a {listprof[90]}.adress")