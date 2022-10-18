class Personne:
    def __init__(self,nom,prenom,cin):
        self._nom=nom
        self._prenom=prenom
        self._cin=cin
    def ToString(self):
        return print(f"nom: {self._nom } prenom: {self._prenom} cin:  {self._cin}")
class Vaccine(Personne):
    def __init__(self,nom,prenom,cin,code,date):
        super().__init__(nom,prenom,cin)
        self.__code=code
        self.__date=date
    def getcode(self):
        return self.__code
    def getdate(self):
        return self.__date
    def setcode(self,code):
        self.__code=code
    def setdate(self,date):
        self.__date=date
    def ToString(self):
        return print(f"{super().ToString() }  code vaccination: {self.__code} date vaccination: {self.__date}")
class Vaccin(Personne):
    def __init__(self,nom,prenom,cin,code_vac,nom_vac,duree):
        super().__init__(nom,prenom,cin)
        self.__code_vac=code_vac
        self.__nom_vac=nom_vac
        self.__duree=duree
    def ToString(self):
        return print(f"{super().ToString()} code vaccin: {self.__code_vac} nom vaccin: {self.__nom_vac} duree vacin: {self.__duree}")
personne1 = Personne("KOUMARE","Ousmane","C2")
personne1.ToString()
vaccine1 = Vaccine("TRAORE","Mariam","H25","2","02/10/2022")
vaccine1.ToString()
vaccin = Vaccin("GASSAMA","Amadou","De20","CCYHGF2020","Covid-19","09:50 mp")
vaccin.ToString()
