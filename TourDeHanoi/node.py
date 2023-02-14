from cube import Cube
from robot import Robot
from erreur import Erreur

class Node:
    #
    # 1. Ajout d'un constructeur qui prend prends en paramètre le robot et la liste des cubes
    #
    #       Ici g est le coût du chemin depuis la racine jusqu'à ce noeud
    #       h est l'estimation du coût du chemin le plus court depuis ce noeud jusqu'à la fin
    #       f est la somme de g et h

    def __init__(self, parent=None, position=None):
        """Constructeur de la classe Node
        
        Parameters:
            parent (Node): le noeud parent
            position (Etat): l'état du noeud
        """
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
    
    #
    # 2. Ajout d'une méthode __str__ qui retourne une chaîne de caractères qui décrit l'état de l'arbre.
    #
    def __str__(self):
        return "Arbre: robot = " + str(self.robot) + ", cubes = " + str(self.cubes) 
    
    #
    # 3. Ajout d'une méthode __repr__ qui retourne une chaîne de caractères qui décrit l'état de l'arbre.
    #
    def __repr__(self):
        return str(self)
    
    #
    # 4. Ajout d'une méthode __eq__ qui compare deux arbres en fonction de leur robot et de leur liste de cubes.
    #
    def __eq__(self, other):
        return self.position == other.position
    
    @classmethod
    def a_star(cls, cubes, start, end):
        """On génère l'arbre en utilisant l'algorithme A*

        Parameters:
        cubes (list): la liste des cubes
        start (Etat): l'état initial
        end (Etat): l'état final

        Returns:
        list: le chemin le plus court

        """
        # Création des noeuds de départ et d'arrivée
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialisation des listes ouverte et fermée
        open_list = []
        closed_list = []

        # Ajout du noeud de départ à la liste ouverte
        open_list.append(start_node)

        # Boucle tant que la liste ouverte n'est pas vide
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # On enlève le noeud courant de la liste ouverte et on l'ajoute à la liste fermée
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Si on a trouvé le noeud final alors on retourne le chemin
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] # Revoie le chemin dans le bon ordre

            # On génère les enfants
            children = []
            
            # On récupère les cubes qui sont sur la table
            for cube in cubes:
                try:
                    Robot.TENIR(cube)
                except Erreur:
                    continue
                else:
                    children.append(Node(current_node, ))

            for cube in cubes:
                try:
                    Robot.POSER(cube)
                except Erreur:
                    continue
                else:
                    children.append(Node(current_node, ))
                

            # On parcourt les enfants
            for child in children:

                # Si le noeud est dans la liste fermée, on passe au suivant
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Création des valeurs g, h et f
                child.g = current_node.g + 1
                child.h = 4 - child
                child.f = child.g + child.h

                # Si le noeud est dans la liste ouverte, on compare les valeurs g
                # Si la valeur g du noeud courant est plus grande, on passe au suivant
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)