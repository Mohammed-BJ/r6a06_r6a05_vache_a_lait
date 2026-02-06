from .vache_a_lait import VacheALait
from .exceptions import InvalidVacheException
from .nourriture.TypeNourriture import TypeNourriture

class PieNoire(VacheALait):
    COEFFICIENT_NUTRITIONNEL = {
        TypeNourriture.MARGUERITE: 1.1,
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.9,
        TypeNourriture.PAILLE: 0.4,
        TypeNourriture.CEREALES: 1.3,
    }

    def __init__(self, petit_nom, nb_taches_blanches, nb_taches_noires):
        if not isinstance(nb_taches_blanches, int) or nb_taches_blanches <= 0:
             raise InvalidVacheException("nb_taches_blanches doit être un entier positif")
        if not isinstance(nb_taches_noires, int) or nb_taches_noires <= 0:
             raise InvalidVacheException("nb_taches_noires doit être un entier positif")

        super().__init__(petitNom=petit_nom)
        self.nb_taches_blanches = nb_taches_blanches
        self.nb_taches_noires = nb_taches_noires
        self._ration = {}

    @property
    def ration(self):
        return self._ration.copy()

    def brouter(self, quantite, nourriture=None):
        super().brouter(quantite)
        
        if nourriture:
            if nourriture not in self._ration:
                self._ration[nourriture] = 0.0
            self._ration[nourriture] += quantite

    def _calculer_lait(self, panse_avant):
        if not self._ration:
            return super()._calculer_lait(panse_avant)
        
        total_nutri = 0.0
        for type_n, q in self._ration.items():
            coeff = self.COEFFICIENT_NUTRITIONNEL.get(type_n, 0.0)
            total_nutri += q * coeff
            
        return self.RENDEMENT_LAIT * total_nutri

    def _post_rumination(self):
        self._ration.clear()
        super()._post_rumination()
