from cube import Cube
from robot import Robot
from etat import Etat
from utilities import *
from node import Node


if __name__ == "__main__":
    # Créer une instance de robot
    robot = Robot(True)

    # TEST 1
    # Créer les cubes et on les ajoute à la liste de cubes
    cubes_initial1 = []
    cubes_initial1.append(Cube("A", True, "B", False))
    cubes_initial1.append(Cube("B", False, None, True))
    cubes_initial1.append(Cube("C", True, "D", False))
    cubes_initial1.append(Cube("D", False, None, True))

    # Creer l'etat initial
    etat_initial1 = Etat(cubes_initial1, robot)

    # On applique la methode put_cube_on_cube
    cubes = put_cube_on_cube(cubes_initial1)

    # TEST 2
    # Créer les cubes et on les ajoute à la liste de cubes
    cubes_initial2 = []
    cubes_initial2.append(Cube("A", True, None, True))
    cubes_initial2.append(Cube("B", True, None, True))
    cubes_initial2.append(Cube("C", True, None, True))
    cubes_initial2.append(Cube("D", True, None, True))

    # Creer l'etat initial
    etat_initial2 = Etat(cubes_initial2, robot)

    # On applique la methode put_cube_on_cube
    cubes = put_cube_on_cube(cubes_initial2)

    # TEST 3
    # Créer les cubes et on les ajoute à la liste de cubes
    cubes_initial3 = []
    cubes_initial3.append(Cube("A", False, None, True))
    cubes_initial3.append(Cube("B", False, "A", False))
    cubes_initial3.append(Cube("C", True, "B", False))
    cubes_initial3.append(Cube("D", True, None, True))

    # Creer l'etat initial
    etat_initial3 = Etat(cubes_initial3, robot)

    # On applique la methode put_cube_on_cube
    cubes = put_cube_on_cube(cubes_initial3)

    # On cree l'etat final
    cubes_final = []
    cubes_final.append(Cube("A", False, None, True))
    cubes_final.append(Cube("B", False, "A", False))
    cubes_final.append(Cube("C", True, "B", False))
    cubes_final.append(Cube("D", True, None, True))

    # Creer l'etat final
    etat_final = Etat(cubes_final, robot)

    print(" Etat final : " + str(etat_final))

    # Initialisation de l'état initial


    # Initialisation de l'état final
    try:
        etat_final = Etat.genererEtat(cubes_final, robot.brasvide)
        print("\nEtat final : " + str(etat_final))
    except Exception as e:
        print(e)


    # Premier test de l'heuristique h1
    print("\n test de l'heuristique h1 pour l'etat test1")
    print("État initial : " + str(etat_initial1))
    print("État final : " + str(etat_final) )
    print("Heuristique h1 : " + str(Etat.h1(etat_initial1, etat_final)))


    # Premier test de l'heuristique h2
    print("\n test de l'heuristique h2 pour l'etat test1")
    print("État initial : " + str(etat_initial1))
    print("État final : " + str(etat_final))
    print("Heuristique h2 : "+str(Etat.h2(etat_initial1, etat_final) ))



    # Deuxième test de l'heuristique h1

    print("\n test de l'heuristique h1 pour l'etat test2")
    print("État test2 : " + str(etat_initial2))
    print("État final : " + str(etat_final))
    print("Heuristique h1 : "+str(Etat.h1(etat_initial2, etat_final) ))


    # Deuxième test de l'heuristique h1
    print("\n test de l'heuristique h2 pour l'etat test2")
    print("État test2 : " + str(etat_initial2))
    print("État final : " + str(etat_final))
    print("Heuristique h2 : "+str(Etat.h2(etat_initial2, etat_final) ))

    # Troisième test de l'heuristique h1
    print("\n test de l'heuristique h1 pour l'etat test3")
    print("État test3 : " + str(etat_initial3))
    print("État final : " + str(etat_final))
    print("Heuristique h1:"+ str(Etat.h1(etat_initial3, etat_final) ))

    # Troisième test de l'heuristique h1
    print("\ntest de l'heuristique h2 pour l'etat test3")
    print("État test3 : " + str(etat_initial3))
    print("État final : " + str(etat_final))
    print("Heuristique h2:" + str(Etat.h2(etat_initial3, etat_final) ))




