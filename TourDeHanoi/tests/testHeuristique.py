from cube import Cube
from robot import Robot
from etat import Etat
from utilities import *
from node import Node


if __name__ == "__main__":
    # Créer une instance de robot
    robot = Robot(True)

    # Créer les cubes et on les ajoute à la liste de cubes
    cubes_initial = []
    cubes_initial.append(Cube("A", False, None, True))
    cubes_initial.append(Cube("B", True, None, True))
    cubes_initial.append(Cube("C", True, 'A', False))

    cubes_final = []
    cubes_final.append(Cube("A", True, 'B', False))
    cubes_final.append(Cube("B", False, 'C', False))
    cubes_final.append(Cube("C", False, None, True))

    # Initialisation de l'état initial
    try:
        etat_initial = Etat.genererEtat(cubes_initial, robot.brasvide)
        print("\nEtat initial : " + str(etat_initial))
    except Exception as e:
        print(e)

    put_cube_on_cube(cubes_initial)
    print("\n")

    # Initialisation de l'état final
    try:
        etat_final = Etat.genererEtat(cubes_final, robot.brasvide)
        print("\nEtat final : " + str(etat_final))
    except Exception as e:
        print(e)

    # Premier test de l'heuristique h1
    print("\nÉtat initial : " + str(etat_initial))
    print("État final : " + str(etat_final) + "\n")
    print("Heuristique h1 : " + str(Etat.h1(etat_initial, etat_final)) + "\n")

    # Deuxième test de l'heuristique h1
    cubes = (Cube("A", True, None, True), Cube("B", False, None, True), Cube("C", True, "B", False))
    etat_test = Etat.genererEtat(cubes, robot.brasvide)
    print("État test2 : " + str(etat_test))
    print("État final : " + str(etat_final) + "\n")
    print("Heuristique h1 : " + str(Etat.h1(etat_test, etat_final)) + "\n")

    # Troisième test de l'heuristique h1
    cubes = (Cube("A", False, None, False), Cube("B", True, "C", False), Cube("C", False, None, True))
    etat_test = Etat.genererEtat(cubes, robot.brasvide)
    print("État test3 : " + str(etat_test))
    print("État final : " + str(etat_final) + "\n")
    print("Heuristique h1 : " + str(Etat.h1(etat_test, etat_final)))

    # Quatrième test de l'heuristique h1
    print("\nÉtat test4 : " + str(etat_initial))
    print("État final : " + str(etat_final) + "\n")
    print("Heuristique h1 : " + str(Etat.h1(etat_final, etat_final)) + "\n")
