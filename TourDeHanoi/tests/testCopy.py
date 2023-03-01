from copy import deepcopy

import etat
from cube import Cube
from etat import Etat
from robot import Robot
from utilities import put_cube_on_cube, afficherCubes

if __name__ == "__main__":
    # Créer une instance de robot
    robot = Robot(True)
    print(id(robot))

    # Créer les cubes et on les ajoute à la liste de cubes
    cubes_initial = []
    cubes_initial.append(Cube("A", False, None, True))
    cubes_initial.append(Cube("B", True, None, True))
    cubes_initial.append(Cube("C", True, "A", False))

    # Creer l'etat initial
    etat_initial = Etat(cubes_initial, robot)

    # On applique la methode put_cube_on_cube
    cubes = put_cube_on_cube(cubes_initial)

    # On copie les cubes
    cubes2 = deepcopy(cubes)

    # On test
    robot2 = Robot.copy(robot)


    # Test de l'action tenir


    print("Avant tenir")
    print("Robot 1 : " + str(id(robot)) + " " +str(robot))
    print("Robot 2 : " + str(id(robot2)) + " " +str(robot2))
    robot.TENIR(robot, cubes_initial[1])

    print("\nAprès tenir")
    print("Robot 1 : " + str(id(robot)) + " " +str(robot))
    print("Robot 2 : " + str(id(robot2)) + " " +str(robot2))

    robot.annuleTenir(robot)
    robot2.annuleTenir(robot2)
    print("\nApres annulation de tenir")
    print("Robot 1 : " + str(id(robot)) + " " +str(robot))
    print("Robot 2 : " + str(id(robot2)) + " " +str(robot2))


    # Test de l'action poser

    print("\nAvant poser")
    print("Robot 1 : " + str(id(robot)) + " " +str(robot))
    print("Robot 2 : " + str(id(robot2)) + " " +str(robot2))

    try:
        robot2.TENIR(robot2, cubes2[2])
        robot2.POSER(robot2, cubes2[2], cubes2[1])
    except Exception as e:
        print(e)

    print("\nApres tenir et poser")
    print("Robot 1 " + str(robot))
    print("Robot 2 " + str(robot2))
    print("Etat des cubes : ")
    afficherCubes(cubes2)
