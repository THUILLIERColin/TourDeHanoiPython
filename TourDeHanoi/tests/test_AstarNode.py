from etat import Etat
from utilities import *
from node import Node
import tkinter as tk

if __name__ == "__main__":
    # Créer une instance de robot
    robot = Robot(True)

    # Créer les cubes et on les ajoute à la liste de cubes
    cubes_initial = []
    cubes_initial.append(Cube("A", False, None, True))
    cubes_initial.append(Cube("B", True, None, True))
    cubes_initial.append(Cube("C", True, "A", False))

    # Creer l'etat initial
    etat_initial = Etat(cubes_initial, robot)

    # On applique la methode put_cube_on_cube
    cubes = put_cube_on_cube(cubes_initial)

    # On cree l'etat final
    cubes_final = []
    cubes_final.append(Cube("A", True, "B", False))
    cubes_final.append(Cube("B", False, "C", False))
    cubes_final.append(Cube("C", False, None, True))

    # Creer l'etat final
    etat_final = Etat(cubes_final, robot)

    print(" Etat final : " + str(etat_final))

    # On cree l'arbre A*
    heuristique = Etat.h1
    paths, all_nodes = Node.a_star(etat_initial, etat_final, heuristique)
    i = 0
    for path in paths:
        print("Noeud " + str(i) + " : " + str(path))
        i += 1

