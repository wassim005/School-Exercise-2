from abonne import Abonne

class Salle:
    def __init__(self,nom,adresse):
        self.nom = nom
        self.adresse = adresse
        self.list = []
    
    def __str__(self):
        return f"============================\nNom: {self.nom}\nAdresse: {self.adresse}"
        
        
    def ajouter(self , abonne):
        self.list.append(abonne)
        
    def rechercher(self , code):
        exist = False
        for a in self.list:
            if a.code == code:
                exist = True
                print("============================")
                print(a.afficher())
                print("============================")
        if exist == False:
            print("L'abonne est introuvable: ")
            
    def listAbonne(self):
        print(self)
        for abonne in self.list:
            print("=============================")
            print(abonne.afficher())
            
    def prixTotal(self):
        print("Method en mode de conception")
        total = 0
        for a in self.list:
            total += a.prix
            
        print(f"le prix total est: {total} DH")
            