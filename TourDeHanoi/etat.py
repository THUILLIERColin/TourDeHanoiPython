from robot import Robot
from cube import Cube
from erreur import Erreur
from utilities import *
from node import Node

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
        self.robot = robot.copy()

    # Méthode qui retourne l'état du cube sous forme de chaîne de caractères.
    def __str__(self):
        return "libre = " + str(self.libre) + ", sur = " + str(self.sur) + ", surtable = " + str(self.surtable) + ", robot = " + str(self.robot)
    
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

    # Ajout de la méthode nextStates
    def nextStates(self, etat, current_node):
        """Méthode qui retourne la liste des états suivants.

        Parameters:
            etat (Etat): l'état actuel

        Returns:
            list: la liste des états suivants
        """
        children = []
        for cube in etat.cubes:
            temp = etat.cubes.copy()
            tempC = find_cube_by_name(temp, cube.name)
            tempRobot = etat.robot.copy()
            try:
                tempRobot.TENIR(tempC)
            except Erreur:
                continue
            else:
                children.append(Node(current_node, Etat(temp, tempRobot)))

        for cube in etat.cubes:
            temp = etat.cubes.copy()
            tempC = find_cube_by_name(temp, cube.name)
            tempRobot = etat.robot.copy()
            try:
                tempRobot.DEPOSER(tempC)
            except Erreur:
                continue
            else:
                children.append(Node(current_node, Etat(temp, tempRobot)))


