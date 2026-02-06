from .vache import Vache
from .exceptions import InvalidVacheException

class VacheALait(Vache):
    RENDEMENT_LAIT = 1.1
    PRODUCTION_LAIT_MAX = 80.0

    def __init__(self, petitNom):
        super().__init__(petit_nom=petitNom)
        self.lait_disponible = 0.0
        self.lait_total_produit = 0.0
        self.lait_total_traite = 0.0

    def _calculer_lait(self, panse_avant):
        return self.RENDEMENT_LAIT * panse_avant

    def _stocker_lait(self, lait):
        if self.lait_disponible + lait > self.PRODUCTION_LAIT_MAX:
            raise InvalidVacheException("Production de lait maximale atteinte")
        
        self.lait_disponible += lait
        self.lait_total_produit += lait

    def traire(self, litres):
        if litres <= 0:
            raise InvalidVacheException("les litres doivent être positifs")
        if litres > self.lait_disponible + 1e-9: 
             raise InvalidVacheException("Pas assez de lait")
        
        if litres > self.lait_disponible:
            litres = self.lait_disponible

        self.lait_disponible -= litres
        self.lait_total_traite += litres
        return litres
    
    def __str__(self):
        return super().__str__() + f", Lait disponible : {self.lait_disponible} L, Lait total trait : {self.lait_total_traite} L"
