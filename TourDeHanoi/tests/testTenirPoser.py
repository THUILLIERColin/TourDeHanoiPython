from robot import Robot
from cube import Cube
from utilities import *


if __name__ == "__main__":
      
    # Créer une instance de robot
    robot = Robot(True)

    # Créer les cubes et on les ajoute à la liste de cubes
    cubes = []
    cubes.append(Cube("A", False, None, True))
    cubes.append(Cube("B", True, None, True))
    cubes.append(Cube("C", True, cubes[0], False))

    # Afficher l'état des cubes
    for cube in cubes:
        print(cube)

    # Test d'un enchainement d'actions possibles

    # Tenir le cube C

    Robot.TENIR(robot,find_cube_by_name(cubes, "C"))
    print("\nLe robot tient le cube : " + str(robot.possedeCube) + "\n")

    for cube in cubes:
        print(cube)

    # Tenir le cube A
    print("\n")

    try:
        Robot.TENIR(robot, find_cube_by_name(cubes, "A"))
    except Exception as e:
        print(e.value)
        print("\n")
        
    # Poser le cube C sur la table

    Robot.POSER(robot, find_cube_by_name(cubes, "C"), None)
    print("Le robot a posé le cube : " + str(find_cube_by_name(cubes, "C")) + " sur la table")
    print("Le robot est libre\n")

    for cube in cubes:
        print(cube)

    # Tenir le cube A

    print("\n")
    Robot.TENIR(robot, find_cube_by_name(cubes, "A"))
    print("Le robot tient le cube : " + str(robot.possedeCube) + "\n")

    for cube in cubes:
        print(cube)

    # Poser le cube A sur le cube B

    Robot.POSER(robot, find_cube_by_name(cubes, "A"), find_cube_by_name(cubes, "B"))
    print("\nLe robot a posé le cube : " + str(find_cube_by_name(cubes, "A")) + " sur le cube : " + str(find_cube_by_name(cubes, "B")) + "\n")

    for cube in cubes:
        print(cube)

    # Tenir le cube B

    print("\n")

    try:
        Robot.TENIR(robot,find_cube_by_name(cubes, "B"))
    except Exception as e:
        print(e.value)
        print("\n")

    for cube in cubes:
        print(cube)
