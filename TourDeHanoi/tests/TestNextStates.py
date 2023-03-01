
from etat import Etat
from cube import Cube
from robot import Robot


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

    # On applique la methode put_cube_on_cube
    cubes = put_cube_on_cube(cubes_initial)

    # On cree l'etat final
    cubes_final = []
    cubes_final.append(Cube("A", False, None, True))
    cubes_final.append(Cube("B", True, "C", False))
    cubes_final.append(Cube("C", False, "A", False))

    # Creer l'etat final
    etat_final = Etat(cubes_final, robot)
    # On applique la methode put_cube_on_cube
    cubes = put_cube_on_cube(cubes_final)

    # Afficher l'état des cubes (deja dans la fonction nextSatates)
    for cube in cubes_initial:
        print(cube)

    #test de la fonction NextStates pour l'etat initial

        # Tester la méthode nextStates
    node_initial = Node(None, etat_initial)

    next_states = node_initial.nextStates(node_initial)

    # Afficher l'état des cubes (deja dans la fonction nextSatates)
    print(next_states)



