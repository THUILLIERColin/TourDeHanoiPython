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
        print("\nEtat initial : ")
        etat_initial = Etat.genererEtat(cubes_initial, robot.brasvide)
    except Exception as e:
        print(e)

    put_cube_on_cube(cubes_initial)
    print("\n")


    # Afficher l'état des cubes finaux
    for cube in cubes_final:
        print(cube)

    # Initialisation de l'état final
    try:
        print("\nEtat final : ")
        etat_final = Etat.genererEtat(cubes_final, robot.brasvide)
    except Exception as e:
        print(e)

    # Test d'un enchainement d'actions possibles
    cubes = cubes_initial.copy()

    # Tenir le cube C
    Robot.TENIR(find_cube_by_name(cubes, "C"))
    print("\nLe robot tient le cube \t")
    print(robot.possedeCube)
    print("\n")

    for cube in cubes:
        print(cube)

    print("Etat après tenir C : ")
    Etat.genererEtat(cubes, robot.brasvide)

    # Poser le cube C sur la table
    Robot.POSER(find_cube_by_name(cubes, "C"), None)
    print("\nLe robot a posé le cube \t")
    print(find_cube_by_name(cubes, "C")), print("sur la table")
    print("Le robot est libre\n")

    for cube in cubes:
        print(cube)

    print("Etat après poser C : "), Etat.genererEtat(cubes, robot.brasvide)
