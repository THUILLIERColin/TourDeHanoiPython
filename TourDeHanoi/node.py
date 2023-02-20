from cube import Cube
from robot import Robot
from etat import Etat
from utilities import *
from erreur import Erreur
from copy import deepcopy

class Node:
    #
    # 1. Ajout d'un constructeur qui prend prends en paramètre le robot et la liste des cubes
    #
    #       Ici g est le coût du chemin depuis la racine jusqu'à ce noeud
    #       h est l'estimation du coût du chemin le plus court depuis ce noeud jusqu'à la fin
    #       f est la somme de g et h

    def __init__(self, parent=None, etat=None):
        """Constructeur de la classe Node
        
        Parameters:
            parent (Node): le noeud parent
            etat (Etat): l'état du noeud
        """
        self.parent = parent
        self.etat = etat

        self.g = 0
        self.h = 0
        self.f = 0

    #
    # 2. Ajout d'une méthode __str__ qui retourne une chaîne de caractères qui décrit l'état de l'arbre.
    #
    def __str__(self):
        return "Node: parent = " + str(self.parent) + "\n\t\t, etat = " + str(self.etat)

    #
    # 3. Ajout d'une méthode __repr__ qui retourne une chaîne de caractères qui décrit l'état de l'arbre.
    #
    def __repr__(self):
        return str(self)

    #
    # 4. Ajout d'une méthode __eq__ qui compare deux arbres en fonction de leur robot et de leur liste de cubes.
    #
    def __eq__(self, other):
        return self.etat == other.etat

    #
    # 5. Ajout de la méthode a_star qui prend en paramètre la liste des cubes, l'état initial et l'état final.
    #    Elle retourne le chemin le plus court.
    #
    @classmethod
    def a_star(cls, start, end):
        """On génère l'arbre en utilisant l'algorithme A*

        Parameters:
            cubes (list): la liste des cubes
            start (Etat): l'état initial
            end (Etat): l'état final

        Returns:
            list: le chemin le plus court

        """
        # Création des noeuds de départ et d'arrivée
        start_node = Node(None, start)
        end_node = Node(None, end)

        robot = Robot(True)
        # Initialisation des listes ouverte et fermée
        open_list = []
        closed_list = []

        # Ajout du noeud de départ à la liste ouverte
        open_list.append(start_node)

        # Boucle tant que la liste ouverte n'est pas vide
        while len(open_list) > 0:
            print("\nJe rentre dans la list ouvert")
            # Get the current node
            current_node = open_list[0]
            current_index = 0

            # Mets le noeuf courant comme étant le noeud avec le plus petit f
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # On enlève le noeud courant de la liste ouverte et on l'ajoute à la liste fermée
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Si on a trouvé le noeud final alors on retourne le chemin
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.etat)
                    current = current.parent
                return path[::-1]  # Revoie le chemin dans le bon ordre

            # On développe le noeud courant en créant ses enfants
            # Creation des enfants grace aux actions du robot

            # On récupère les cubes qui sont sur la table
            # A partir d'un Etat on regard les état suivant possible

            print("\nNoeud courant : "+  str(current_node.etat) + "\n")

            children = cls.nextStates(current_node)

            # On parcourt les enfants
            for child in children:

                print("\nVoici mes enfants : " + str(child.etat) + " et leur cube associé : ")
                afficherCubes(child.etat.cubes)

                # Si le noeud est dans la liste fermée, on passe au suivant
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Création des valeurs g, h et f
                child.g = current_node.g + 1
                child.h = Etat.h1(current_node.etat, end_node.etat)
                child.f = child.g + child.h

                # Si le noeud est dans la liste ouverte, on compare les valeurs g
                # Si la valeur g du noeud courant est plus grande, on passe au suivant
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Ajout du noeud à la liste ouverte
                open_list.append(child)

    #
    # 6. Ajout de la méthode nextState qui prend en paramètre un état et retourne la liste des états suivants.
    #
    @classmethod
    def nextStates(cls, current_node):
        """Méthode qui retourne la liste des états suivants.

        Parameters:
            etat (Etat): l'état actuel

        Returns:
            list (de Node): la liste des états suivants
        """
        children = []
        etat = current_node.etat

        if etat.robot.brasvide:
            # ACTION DE TENIR
            # On essaye de prendre chaque cube
            for cube in etat.cubes:
                temp = deepcopy(etat.cubes)
                tempC = find_cube_by_name(temp, cube.name)
                tempRobot = deepcopy(etat.robot)
                try:
                    print("Je prend " + str(tempC))
                    tempRobot.TENIR(tempRobot, tempC)
                except Erreur as e:
                    print(e)
                    continue
                else:
                    children.append(Node(current_node, Etat(temp, tempRobot)))
                    tempRobot.annuleTenir(tempRobot)
                    etat.robot.annuleTenir(etat.robot)

            print("J'ai fini de prendre les cubes\t L'etat du robot est : " + str(etat.robot) + "\n")

        else:
            # On essaye de poser chaque cube sur la table
            for cube in etat.cubes:
                temp = deepcopy(etat.cubes)
                tempC = find_cube_by_name(temp, cube.name)
                tempRobot = etat.robot
                try:
                    print("Je pose " + tempC.name + " sur la table")
                    tempRobot.POSER(tempRobot, tempC)
                except Erreur as e:
                    print(e)
                    continue
                else:
                    print("L'etat des cubes à la pose est : ")
                    afficherCubes(temp)
                    children.append(Node(current_node, Etat(temp, tempRobot)))
                    etat.robot.annulePoser(etat.robot, cube)

            print("J'ai fini de poser les cubes sur la table\t L'etat des cubes est : ")
            afficherCubes(etat.cubes)

            # On essaye de poser chaque cube sur chaque autre cube
            for cube in etat.cubes:
                for cube2 in etat.cubes:
                    if cube.name != cube2.name:
                        temp = deepcopy(etat.cubes)
                        tempC = find_cube_by_name(temp, cube.name)
                        tempC2 = find_cube_by_name(temp, cube2.name)
                        tempRobot = etat.robot
                        try:
                            print("Je pose " + tempC.name + " sur " + tempC2.name)
                            tempRobot.POSER(tempRobot, tempC, tempC2)
                        except Erreur as e:
                            print(e)
                            continue
                        else:
                            print("L'etat des cubes à la pose est : ")
                            afficherCubes(temp)
                            children.append(Node(current_node, Etat(temp, tempRobot)))
                            etat.robot.annulePoser(etat.robot, cube, cube2)

            print("J'ai fini de poser les cubes sur les autres cubes")

        print("J'ai fini de créer les enfants\n L'etat des cubes inchangé est : ")
        afficherCubes(etat.cubes)

        return children
