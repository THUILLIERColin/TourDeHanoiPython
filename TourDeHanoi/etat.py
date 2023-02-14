from robot import Robot
from cube import Cube
from erreur import Erreur

class Etat:
    
    # Constructeur de la classe Etat.
    def __init__(self):
        """Constructeur de la classe Etat.

        Parameters:
            libre (list): liste des cubes libres
            sur (list): liste pair des cubes sur lesquels un cube est posé
            surtable (list): liste des cubes sur la table
            brasvide (bool): True si le bras du robot est vide, False sinon
        """
        self.libre = []
        self.sur = []
        self.surtable = []
        self.brasvide = True

    # Méthode qui retourne l'état du cube sous forme de chaîne de caractères.
    def __str__(self):
        return "libre = " + str(self.libre) + ", sur = " + str(self.sur) + ", surtable = " + str(self.surtable) + ", brasvide = " + str(self.brasvide)
    
    # Méthode qui retourne l'état du cube sous forme de chaîne de caractères.
    def __repr__(self):
        return self.__str__()
    
    # Méthode qui retourne l'état du cube sous forme de chaîne de caractères.
    def __eq__(self, other):
        return self.libre == other.libre and self.sur == other.sur and self.surtable == other.surtable and self.brasvide == other.brasvide

    # Ajout des méthodes get/set pour l'attribut libre, sur, surtable et brasvide.
    @property
    def libre(self):
        return self._libre

    @libre.setter
    def libre(self, value):
        self._libre = value

    @property
    def sur(self):
        return self._sur

    @sur.setter
    def sur(self, value):
        self._sur = value

    @property
    def surtable(self):
        return self._surtable

    @surtable.setter
    def surtable(self, value):
        self._surtable = value

    # Méthode qui retourne l'état du cube sous forme de chaîne de caractères.
    @classmethod      
    def genererEtat(cls, cubes, brasvide):
        """Génère l'état du jeu après avoir appliqué l'action.
        
        Parameters:
            cubes (list): la liste des cubes
            brasvide (bool): True si le bras du robot est vide, False sinon
        
        Returns:
            Etat: l'état final
        """
        if cubes is None:
            raise Erreur.LISTE_CUBES_INEXISTANTE
        etat = Etat()
        for cube in cubes:
            if cube.libre:
                etat.libre.append(cube.name)
            if isinstance(cube.sur, Cube):
                etat.sur.append((cube.name, cube.sur.name))
            elif cube.sur is not None:
                etat.sur.append((cube.name, cube.sur))
            if cube.surtable:
                etat.surtable.append(cube.name)
        etat.brasvide = brasvide
        return etat

    # Methode heuristique h1
    @classmethod
    def h1(self, etatActuel, etatFinal):
        """Méthode heuristique h1

        Parameters:
            etatActuel (Etat): l'état actuel
            etatFinal (Etat): l'état final

        Returns:
            int: la différence entre l'état final et l'état actuel
        """
        setLibre = set(etatActuel.libre)
        setSur = set(etatActuel.sur)
        setSurtable = set(etatActuel.surtable)

        setLibreFinal = set(etatFinal.libre)
        setSurFinal = set(etatFinal.sur)
        setSurtableFinal = set(etatFinal.surtable)

        differenceLibre = setLibreFinal.difference(setLibre)
        differenceSur = setSurFinal.difference(setSur)
        differenceSurtable = setSurtableFinal.difference(setSurtable)

        return len(differenceLibre) + len(differenceSur) + len(differenceSurtable)