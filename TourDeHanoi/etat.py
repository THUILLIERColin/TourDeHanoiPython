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

        # On crée une liste de cubes avec les cubes sur lesquels ils sont
        self.libre = []
        self.sur = []
        self.surtable = []
        self.cubes = cubes
        self.robot = Robot.copy(robot)

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

    #hash sert a la comparaison de deux etats
    @property
    def __hash__(self):
        return hash((self.libre, self.sur, self.surtable, self.robot))

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
    def h1(cls, etatActuel, etatFinal):
        """Méthode heuristique h1

        Parameters:
            etatActuel (Etat): l'état actuel
            etatFinal (Etat): l'état final

        Returns:
            int: la différence entre l'état final et l'état actuel
        """
        # on intialise les sets de l etat actuel et de l etat final
        setLibre = set(etatActuel.libre)
        setSur = set(etatActuel.sur)
        setSurtable = set(etatActuel.surtable)

        setLibreFinal = set(etatFinal.libre)
        setSurFinal = set(etatFinal.sur)
        setSurtableFinal = set(etatFinal.surtable)

        # on calcule la difference entre les sets de l etat actuel et de l etat final
        differenceLibre = setLibreFinal.difference(setLibre)
        differenceSur = setSurFinal.difference(setSur)
        differenceSurtable = setSurtableFinal.difference(setSurtable)

        # on retourne la somme des longueurs des differences
        return len(differenceLibre) + len(differenceSur) + len(differenceSurtable)

    @classmethod
    def h2(self, etatActuel, etatFinal):
        """Méthode heuristique h2

        Parameters:
            etatActuel (Etat): l'état actuel
            etatFinal (Etat): l'état final

        Returns:
            int: h
        """
        # on intialise h a 0
        h = 0

        setLibre = set(etatActuel.libre)
        setLibreFinal = set(etatFinal.libre)
        differenceLibre = setLibreFinal.difference(setLibre)

        #si tous les cubes sont a leur position finale Libre, on incremente pas h sinon on incremente h
        if len(differenceLibre)==0:
            h+=0
        else:
            h+=1

        setSur = set(etatActuel.sur)
        setSurFinal = set(etatFinal.sur)
        differenceSur = setSurFinal.difference(setSur)

        #si tous les cubes sont a leur position finale Sur, on incremente pas h sinon on incremente h
        if len(differenceSur)==0:
            h+=0
        else:
            h+=1

        setSurtable = set(etatActuel.surtable)
        setSurtableFinal = set(etatFinal.surtable)
        differenceSurtable = setSurtableFinal.difference(setSurtable)

        #si tous les cubes sont a leur position finale Surtable, on incremente pas h sinon on incremente h
        if len(differenceSurtable)==0:
            h+=0
        else:
            h+=1

        #return h qui soit egal a 0 si tous les cubes sont a leur position finale soit egal a 1 ou 2 ou 3
        return h




