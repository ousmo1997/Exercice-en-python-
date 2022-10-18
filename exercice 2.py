class Pet:
    def __init__(self,name,animaltype,age):
        self.name=name
        self.animaltype=animaltype
        self.age=age
    def affichage(self):
        print("Le nom de l'animal est:",self.name)
        print("L'animal est de type:",self.animaltype)
        print("Son age est:",self.age)
nom=input("Donner le nom de l'animal :")
type=input("Donner le type de l'animal :")
age=int(input("Donner l'age de l'animal : "))
p=Pet(nom,type,age)
p.affichage()
