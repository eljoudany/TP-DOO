import json
class professeur :

    def __init__(self,n,p,t,s,a,e,d,ei, sal=0.0):
        self.nom=n
        self.prenom=p
        self.tel=t
        self.specialite=s
        self.salaire=sal
        self.anciennete=0
        self.etat_familial=e
        self.dateNaissance=d
        self.adresse=a
        self.email=ei

    def calculsalairetotal(self):
        return  self.salaire + (self.anciennete//5 ) * 2000
    
    def todict(self):
        dictprof = {
            "nom": self.nom,
            "prenom": self.prenom,
            "tel": self.tel,
            "specialite": self.specialite,
            "salaire": self.salaire,
            "anciennete": self.anciennete,
            "etat_familial": self.etat_familial,
            "dateNaissance": self.dateNaissance,
            "adresse": self.adresse,
            "email": self.email
        }
        return dictprof
    
    @staticmethod
    def fromdict(self,dict):
        p=professeur(dict["nom"],dict["prenom"],dict["salaire"])
        p.tel=dict["tel"]
        p.specialite=dict["specialite"]
        p.anciennete=dict["anciennete"]
        p.etat_familial=dict["etat_familial"]
        p.dateNaissance=dict["dateNaissance"]
        p.adresse=dict["adresse"]
        p.email=dict["email"]

               
    def enregistrer(self):
        with open(f"prof{self.nom}_{self.prenom}.json" , "w" ) as f:
            json.dump(self.todict(), f , indent=4)