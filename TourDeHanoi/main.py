import heapq
from tkinter import *

from node import Node
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

    # Pour chaque cube, si il est sur un autre cube, trouver ce cube et
    # mettre le pointeur sur ce cube
    cubes_initial = put_cube_on_cube(cubes_initial)

    # Creer l'etat initial
    etat_initial = Etat(cubes_initial, robot)

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
    cubes_final = put_cube_on_cube(cubes_final)
    etat_final = Etat(cubes_final, Robot(True))

    paths, all_nodes = Node.a_star(etat_initial, etat_final)

    # Affichage de l'arbre à l'aide de tkinter
    window = Tk()
    canvas = Canvas(window, width=800, height=600)
    canvas.pack()

    node_coords = {}  # Dictionnaire qui stocke les coordonnées de chaque noeud
    node_size = 20
    x_spacing = 50
    y_spacing = 100

    # Placement des noeuds sur le canvas
    for i, node in enumerate(all_nodes):

        nodeOfPath = False

        x = node_size + (i % 10) * x_spacing
        y = node_size + (i // 10) * y_spacing
        node_coords[node] = (x, y)
        for path in paths:
            if node.etat == path:
                nodeOfPath = True

        canvas.create_oval(x - node_size, y - node_size, x + node_size, y + node_size, fill="red" if nodeOfPath else "white")
        canvas.create_text(x, y, text=node.etat)

    # Placement des arcs entre les noeuds
    for node in all_nodes:
        for child in node.children:
            canvas.create_line(node_coords[node][0], node_coords[node][1], node_coords[child][0], node_coords[child][1])

    window.mainloop()

    
    