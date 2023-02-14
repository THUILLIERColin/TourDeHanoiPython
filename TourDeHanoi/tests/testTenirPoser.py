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

        Robot.TENIR(find_cube_by_name(cubes, "C"))
        print("Le robot tient le cube ")
        print(robot.possedeCube)
        print("\n")

        for cube in cubes:
            print(cube)

        # Tenir le cube A

        print("\n\n")
        try :
            Robot.TENIR(find_cube_by_name(cubes, "A"))
        except Exception as e:
            print(e.value)
            print("\n")
        
        # Poser le cube C sur la table

        print("\n\n")

        Robot.POSER(find_cube_by_name(cubes, "C"), None)
        print("Le robot a posé le cube ")
        print(find_cube_by_name(cubes, "C"))
        print(" sur la table")
        print("Le robot est libre\n")

        for cube in cubes:
            print(cube)

        # Tenir le cube A

        print("\n\n")

        Robot.TENIR(find_cube_by_name(cubes, "A"))
        print("Le robot tient le cube ")
        print(robot.possedeCube)
        print("\n")

        for cube in cubes:
            print(cube)

        # Poser le cube A sur le cube B

        print("\n\n")

        Robot.POSER(find_cube_by_name(cubes, "A"), find_cube_by_name(cubes, "B"))
        print("Le robot a posé le cube ")
        print(find_cube_by_name(cubes, "A"))
        print(" sur le cube ")
        print(find_cube_by_name(cubes, "B"))
        print("\n")

        for cube in cubes:
            print(cube)
        
        # Tenir le cube B

        print("\n\n")

        try :
            Robot.TENIR(find_cube_by_name(cubes, "B"))
        except Exception as e:
            print(e.value)
            print("\n")

        for cube in cubes:
            print(cube)
