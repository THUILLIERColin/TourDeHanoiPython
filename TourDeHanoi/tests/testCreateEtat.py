from cube import Cube
from robot import Robot
from etat import Etat
from utilities import *


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

    # Afficher l'état des cubes
    for cube in cubes_initial:
        print(cube)

    # Initialisation de l'état initial
    try:
        etat_initial = Etat(cubes_initial, robot)
        print("\nEtat initial : " + str(etat_initial))
    except Exception as e:
        print(e)

    put_cube_on_cube(cubes_initial)
    print("\n")


    # Afficher l'état des cubes finaux
    for cube in cubes_final:
        print(cube)

    # Initialisation de l'état final
    try:
        etat_final = Etat(cubes_final, robot)
        print("\nEtat final : " + str(etat_final))
    except Exception as e:
        print(e)

    # Test d'un enchainement d'actions possibles
    cubes = cubes_initial.copy()

    # Tenir le cube C
    Robot.TENIR(Robot, find_cube_by_name(cubes, "C"))
    print("\nLe robot tient le cube : " + str(robot.possedeCube) + "\n")

    for cube in cubes:
        print(cube)

    print("Etat après tenir C : " + str(Etat(cubes, robot)))

    # Poser le cube C sur la table
    Robot.POSER(Robot, find_cube_by_name(cubes, "C"), None)
    print("\nLe robot a posé le cube " + str(find_cube_by_name(cubes, "C")) + " sur la table")
    print("Le robot est libre\n")

    for cube in cubes:
        print(cube)

    print("Etat après poser C : " + str(Etat(cubes, robot)))



