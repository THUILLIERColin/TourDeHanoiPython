import heapq
from tkinter import *

from cube import Cube
from robot import Robot
from etat import Etat
from utilities import *

if __name__ == "__main__":
    
    # Créer une instance de robot
    robot = Robot(True)

    # Demander combien de cubes
    nb_cubes = int(input("Combien de cubes? "))

    # Créer les cubes et demander pour chaque cube si il est sur la table 
    # ou sur un autre cube et si il est libre
    # Créer une liste de cubes qui contient les cubes créés
    cubes_initial = []
    for i in range(nb_cubes):
        print("Cube", chr(ord("A") + i), "est-il sur la table? (o/n)")
        surtable = input() == "o"
        if not surtable:
            print("Sur quel cube est-il?")
            sur = input()
        else:
            sur = None
        print ("Est-il libre? (o/n)")
        libre = input() == "o"
        cubes_initial.append(Cube(chr(ord("A") + i),libre, sur, surtable))
    
    # Creation de l'état initial
    # On l'utilise maintenant car l'attribut cube.sur est une chaine de caractère
    try:
        print("\nCreation de l'état initial")
        etat_initial = Etat.genererEtat(cubes_initial, robot.brasvide)
    except Exception as e:
        print(e)
    
    # Pour chaque cube, si il est sur un autre cube, trouver ce cube et
    # mettre le pointeur sur ce cube
    cubes_initial = put_cube_on_cube(cubes_initial)

    # Demander l'état final des cubes
    cubes_final = cubes_initial.copy()
    print("\n\nQuel est l'état final des cubes?")
    for cube in cubes_final:
        print("Cube", cube.name , "est-il sur la table? (o/n)")
        surtable = input() == "o"
        if not surtable:
            print("Sur quel cube est-il?")
            sur = input()
        else:
            sur = None
        print ("Est-il libre? (o/n)")
        libre = input() == "o"
        cube.libre = libre
        cube.surtable = surtable
        cube.sur = sur
    
    # Creation de l'état final
    # On l'utilise maintenant car l'attribut cube.sur est une chaine de caractère
    try:
        print("\nCreation de l'état final")
        etat_final = Etat.genererEtat(cubes_final, True)
    except Exception as e:
        print(e)

    # Afficher l'état des cubes
    for cube in cubes_final:
        print(cube)

    print("\n\n")

    
    