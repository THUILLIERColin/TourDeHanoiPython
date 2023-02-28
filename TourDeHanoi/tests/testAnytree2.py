from anytree import AnyNode, RenderTree, DoubleStyle

from etat import Etat
from utilities import *
from node import Node

if __name__ == "__main__":
    # Créer une instance de robot
    robot = Robot(True)

    # Créer les cubes et on les ajoute à la liste de cubes
    cubes_initial = []
    cubes_initial.append(Cube("A", False, None, True))
    cubes_initial.append(Cube("B", True, "A", False))


    # Creer l'etat initial
    etat_initial = Etat(cubes_initial, robot)

    # On applique la methode put_cube_on_cube
    cubes = put_cube_on_cube(cubes_initial)

    # On cree l'etat final
    cubes_final = []
    cubes_final.append(Cube("A", True, "B", False))
    cubes_final.append(Cube("B", False, None, True))

    # Creer l'etat final
    etat_final = Etat(cubes_final, robot)

    # Créer le noeud initial
    start = Node(None, etat_initial)

    for pre, fill, node in RenderTree(start, style=DoubleStyle()):
        print("%s%s" % (pre, node.etat))

    #start:nom du nœud de départ
    #print(RenderTree(start, style=DoubleStyle()).by_attr("name"))