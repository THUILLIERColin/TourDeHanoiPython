from utilities import *
from etat import Etat
from cube import Cube
from robot import Robot
from etat import Etat
from utilities import *
from node import *

if __name__ == "__main__":
    # Créer une instance de robot
    robot = Robot(True)

    # Créer les cubes et on les ajoute à la liste de cubes
    cubes_initial = []
    cubes_initial.append(Cube("A", True, None, True))
    cubes_initial.append(Cube("B", True, None, True))
    cubes_initial.append(Cube("C", True, None, True))


    # Creer l'etat initial
    etat_initial = Etat(cubes_initial, robot)

    # On cree l'etat final
    cubes_final = []
    cubes_final.append(Cube("A", False, None, True))
    cubes_final.append(Cube("B", True, "C", False))
    cubes_final.append(Cube("C", False, "A", False))

    # Creer l'etat final
    etat_final = Etat(cubes_final, robot)

    #test de la fonction NextStates dans node.py
