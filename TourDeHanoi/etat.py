from robot import Robot
from cube import Cube
from erreur import Erreur
from utilities import *

class Etat:
    
    # Constructeur de la classe Etat.
    def __init__(self, cubes, robot):
        """Constructeur de la classe Etat.

        Parameters:
            cubes (list): la liste des cubes
            robot (Robot): le robot

        Raises:
            Erreur.LISTE_CUBES_INEXISTANTE: si la liste des cubes n'existe pas
        """
        self.libre = []
        self.sur = []
        self.surtable = []
        self.cubes = cubes

        if cubes is None:
            raise Erreur.LISTE_CUBES_INEXISTANTE
        for cube in cubes:
            if cube.libre:
                self.libre.append(cube.name)
            if isinstance(cube.sur, Cube):
                self.sur.append((cube.name, cube.sur.name))
            elif cube.sur is not None:
                self.sur.append((cube.name, cube.sur))
            if cube.surtable:
                self.surtable.append(cube.name)
        self.robot = Robot.copy(robot)

    # Méthode qui retourne l'état du cube sous forme de chaîne de caractères.
    def __str__(self):
        return "libre = " + str(self.libre) + ", sur = " + str(self.sur) + ", surtable = " + str(self.surtable) + ", robot = " + str(self.robot)
    
    # Méthode qui retourne l'état du cube sous forme de chaîne de caractères.
    def __repr__(self):
        return self.__str__()
    
    # Méthode qui retourne l'état du cube sous forme de chaîne de caractères.
    def __eq__(self, other):
        return self.libre == other.libre and self.sur == other.sur and self.surtable == other.surtable and self.robot == other.robot

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

    #creation etat
    @property
    def etat(self):
        return self.etat



