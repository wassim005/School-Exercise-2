from datetime import datetime

class Abonne:
    c = 0
    def __init__(self,nom,prenom,taille,poids,prix):
        self.__nom = nom 
        self.__prenom = prenom 
        Abonne.c += 1 
        self.__code = Abonne.c
        self.__taille = taille 
        self.__poids = poids
        self.__prix = prix
        self.__dateAbonnement = datetime.now()
        
        
    def __str__(self):
        return f"Prenom: {self.__prenom}  Nom: {self.__nom} Code: {self.__code}"
        
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,value):
        if len(value) >= 3:
             self.__nom = value
         
        
        
    @property
    def prenom(self):
        return self.__prenom
    
    @prenom.setter
    def prenom(self,value):
        if len(value) >= 3:
             self.__prenom = value
             
             
    @property
    def code(self):
        return self.__code
    
    
    @property
    def taille(self):
        return self.__taille
    

    @property
    def poids(self):
        return self.__poids
             
    
    @property
    def prix(self):
        return self.__prix  
    @prix.setter
    def prix(self,value):
        if value >= 2000 and value <= 3000:
             self.__prix = value
          
    
     
    @property
    def dateAbonnement(self):
        return self.__dateAbonnement    
        
    def afficher(self):
        return f"Prenom: {self.__prenom}\nNom: {self.__nom}\nCode: {self.__code}\nTaille: {self.__taille}cm\nPoids: {self.__poids}Kg\nPrix: {self.__prix}DH\nDate d'abonnement: {self.__dateAbonnement}"
    

        