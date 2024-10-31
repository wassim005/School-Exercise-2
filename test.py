from abonne import Abonne
from salle import Salle
import sys, subprocess

a1=Abonne(nom="Babakhali",prenom="Ouassim",taille=180,poids=61,prix=2500)
a2=Abonne(nom="Babakhali",prenom="Saad",taille=180,poids=65,prix=2500)
a3=Abonne(nom="Babakhali",prenom="Oussama",taille=183,poids=63,prix=2500)

s1 = Salle("City Club", "Centre Ville")

s1.ajouter(a1)
s1.ajouter(a2)
s1.ajouter(a3)


def ajouter():
    clear()
    nom = input("le nom: ")
    prenom = input("le prenom: ")
    taille = input("la taille: ")
    poids = input("le poids: ")
    prix = input("le prix: ")
    a=Abonne(nom,prenom,taille,poids,prix)
    s1.ajouter(a)
    
    
def rechercher():
    clear()
    code = int(input("Enter le code de l'abonnee: "))
    s1.rechercher(code)
                
    
def listAbonne():
    clear()
    s1.listAbonne()
    
    
def prixTotal():
    clear()
    s1.prixTotal()
    
    
def quitter(self):
    print("Merci")    

def  erreur():
    print("choix incorrect!!!")
def clear():
    subprocess.run('cls', shell=True)
    
d = {
    1: ajouter,
    2: rechercher,
    3: listAbonne,
    4: prixTotal,
    5: quitter
}

choix = 1

while choix != 5:
    print("""

                ================
                Gestion Abonnees
                ================
                
            1- Ajouter un abonnee
        
            2- Rechercher un abonnee
        
            3- Liste des abonnees
        
            4- Prix total des abonnees
        
            5- Quitter l'application
        
          """)
    choix = int(input("Entrer votre choix: "))
    d.get(choix, erreur)()
    input("press enter to continue......")
    clear()    
