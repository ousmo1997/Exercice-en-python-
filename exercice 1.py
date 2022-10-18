class table:

    # Définir les attributs par défaut :
    ref = "la référence de la table"
    matiere = "la matière de la table"
    poids = "le poids de la table"
    hauteur = "la hauteur de la table en cm"
    longueur = "la longueur de la table en cm"
    largeur = "la largeur de la table en cm"
    prix_vente = "le prix de vente"
    prix_fab = "le prix de fabrication"
    nb_stock = "le nombre de table en stock"

    # Définir le constructeur de la classe :
    def __init__(self,ref,matiere,poids,hauteur,longueur,largeur,prix_vente,prix_fab,nb_stock):
        self.ref=ref
        self.matiere=matiere
        self.poids=poids
        self.hauteur=hauteur
        self.longueur=longueur
        self.largeur=largeur
        self.prix_vente=prix_vente
        self.__prix_fab=prix_fab
        self.__nb_stock=nb_stock

 # Définir les mutateurs "getteurs" :
    def get_prix_fab(self):
            return self.__prix_fab
    def get_nb_stock(self):
            return self.__nb_stock

# Définir les mutateurs "setters" :
    def set_prix_fab(self, prix_fab):
        self.__prix_fab= prix_fab
    def set_nb_stock(self,nb_stock):
        self.__nb_stock = nb_stock


# Définir la méthode d'affichage :
    def affichage (self) :
        print("la référence de la table est :",self.ref)
        print("la matière de la table est:",self.matiere)
        print("le poids de la table est:",self.matiere)
        print("la hauteur de la table en cm est:",self.hauteur)
        print("la longueur de la table en cm est:",self.longueur)
        print("la largeur de la table en cm est:",self.largeur)
        print("le prix de vente est:",self.prix_vente)
        print("le prix de fabrication est:",self.__prix_fab)
        print("le nombre de table en stock est:",self.__nb_stock)

# methode de calcule de gain
    def gain(self):
        print("le gain est:", str((self.prix_vente * self.__nb_stock)), "Fcfa")

t=table("CT","bois_blanc","50 kg","10 cm","15 cm","5 cm",1500,"500 Fcfa",20)
t.affichage()
t.gain()