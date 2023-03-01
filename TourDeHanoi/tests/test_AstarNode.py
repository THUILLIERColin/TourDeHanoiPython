from etat import Etat
from utilities import *
from node import Node
import tkinter as tk

if __name__ == "__main__":
    # Créer une instance de robot
    robot = Robot(True)

    # Créer les cubes et on les ajoute à la liste de cubes
    cubes_initial = []
    cubes_initial.append(Cube("A", False, None, True))
    cubes_initial.append(Cube("B", True, None, True))
    cubes_initial.append(Cube("C", True, "A", False))

    # Creer l'etat initial
    etat_initial = Etat(cubes_initial, robot)

    # On applique la methode put_cube_on_cube
    cubes = put_cube_on_cube(cubes_initial)

    # On cree l'etat final
    cubes_final = []
    cubes_final.append(Cube("A", True, "B", False))
    cubes_final.append(Cube("B", False, "C", False))
    cubes_final.append(Cube("C", False, None, True))

    # Creer l'etat final
    etat_final = Etat(cubes_final, robot)

    print(" Etat final : " + str(etat_final))

    # On cree l'arbre A*
    paths, all_nodes = Node.a_star(etat_initial, etat_final)
    i = 0
    for path in paths:
        print("Noeud " + str(i) + " : " + str(path))
        i += 1

    # Affichage de l'arbre à l'aide de tkinter
    window = tk.Tk()
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack()

    node_coords = {}  # Dictionnaire qui stocke les coordonnées de chaque noeud
    node_size = 20
    x_spacing = 50
    y_spacing = 100

    # Placement des noeuds sur le canvas
    # Placement des noeuds sur le canvas
    for i, node in enumerate(all_nodes):
        nodeOfPath = False

        x = node_size + (i % 10) * x_spacing
        y = node_size + (i // 10) * y_spacing
        node_coords[node] = (x, y)
        for path in paths:
            if node.etat == path:
                nodeOfPath = True

        if nodeOfPath:
            canvas.create_oval(x - node_size, y - node_size, x + node_size, y + node_size, fill="red", outline="black")
        else:
            canvas.create_oval(x - node_size, y - node_size, x + node_size, y + node_size, fill="white", outline="black")
        canvas.create_text(x, y, text=str(i))

        if node.parent not in node_coords:
            # Si le parent du noeud n'a pas encore été placé sur le canvas, on l'ajoute dans le dictionnaire node_coords avec des coordonnées aléatoires
            parent_x = canvas.winfo_width() // 2
            parent_y = 20
            node_coords[node.parent] = (parent_x, parent_y)
            canvas.create_oval(parent_x - node_size, parent_y - node_size, parent_x + node_size, parent_y + node_size, fill="white", outline="black")
            canvas.create_text(parent_x, parent_y, text=str(all_nodes.index(node.parent)))

        parent_coords = node_coords[node.parent]
        canvas.create_line(x, y, parent_coords[0], parent_coords[1])
    window.mainloop()

