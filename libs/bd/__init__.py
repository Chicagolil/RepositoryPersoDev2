class BandeDessinee :
    def __init__(self,prix,  nomBD, qteVendue = 0):
        self.__prix = prix
        self.qteVendue = qteVendue
        self.nomBD = nomBD
        self.total= float(self.__prix) * float(self.qteVendue)

    def __str__(self):

        return f"La BD {self.nomBD} a été vendue  {self.qteVendue}  fois au prix de {self.__prix}€ ==> {self.total:.2f} € "


    @property
    def prix(self):
        return self.__prix

    def ajouterVentes(self,numLivre):
        self.qteVendue += numLivre

