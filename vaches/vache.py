

from .exceptions import InvalidVacheException

class Vache:
    AGE_MAX = 25
    POIDS_MAX = 1200.0
    PANSE_MAX = 200.0
    RENDEMENT_RUMINATION = 0.25
    AGE_NAISSANCE = 0
    POIDS_NAISSANCE = 50.0

    def __init__(self, petit_nom):
        if not petit_nom or not petit_nom.strip():
            raise InvalidVacheException("petit_nom ne peut pas être vide")

        self.petit_nom = petit_nom
        self._poids = float(self.POIDS_NAISSANCE)
        self.age = self.AGE_NAISSANCE
        self.panse = 0.0

    @property
    def poids(self):
        return self._poids

    @poids.setter
    def poids(self, value):
        if value < 0:
             raise InvalidVacheException("le poids doit être positif")
        if value > self.POIDS_MAX:
             raise InvalidVacheException(f"le poids doit être <= {self.POIDS_MAX}")
        self._poids = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (0 <= value <= self.AGE_MAX):
            raise InvalidVacheException(f"l'âge doit être compris entre 0 et {self.AGE_MAX}")
        self._age = value

    def brouter(self, quantite, nourriture=None):
        if quantite <= 0:
            raise InvalidVacheException("la quantité doit être positive")
        if nourriture is not None:
             raise InvalidVacheException("Une vache standard ne peut pas manger de nourriture spécialisée")
        
        if self.panse + quantite > self.PANSE_MAX:
             raise InvalidVacheException("Panse pleine")
        
        self.panse += quantite

    def ruminate(self):
        return self.ruminer()

    def ruminer(self):
        if self.panse <= 0:
            raise InvalidVacheException("Panse vide")
        
        panse_avant = self.panse
        
        gain = self.RENDEMENT_RUMINATION * panse_avant
        self.poids += gain
        
        lait = self._calculer_lait(panse_avant)
        self._stocker_lait(lait)
        
        self.panse = 0.0
        
        self._post_rumination()
        
        return lait

    def vieillir(self):
        if self.age >= self.AGE_MAX:
            raise InvalidVacheException("Age maximum atteint")
        self.age += 1

    # Hooks
    def _calculer_lait(self, panse_avant):
        return 0.0

    def _stocker_lait(self, lait):
        pass

    def _post_rumination(self):
        pass

    def __str__(self):
        return f"Vache {self.petit_nom} (Age: {self.age}, Poids: {self.poids}, Panse: {self.panse})"
