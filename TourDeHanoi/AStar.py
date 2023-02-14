from queue import PriorityQueue


class AStar:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.ouvert = PriorityQueue()
        self.ferme = set()

    def chercherChemin(self):
        """Fonction qui implémente l'algorithme A* pour trouver un chemin optimal.

        Returns:
            list: la liste des noeuds du chemin optimal, ou une liste vide si aucun chemin n'a été trouvé.
        """
        # Ajouter le noeud de départ à la liste ouverte et initialiser son coût g à 0
        self.start.g = 0
        self.ouvert.put(self.start)

        # Boucle jusqu'à ce que la liste ouverte soit vide
        while not self.ouvert.empty():
            # Récupérer le noeud avec le coût f le plus faible
            current = self.ouvert.get()

            # Ajouter le noeud courant à la liste fermée
            self.ferme.add(current)

            # Si le noeud courant est égal au noeud final, alors un chemin optimal a été trouvé
            if current == self.end:
                return self.reconstruireChemin(current)

            # Pour chaque noeud voisin
            for voisin in current.voisins():
                # Si le noeud voisin est déjà dans la liste fermée, ignorer ce noeud
                if voisin in self.ferme:
                    continue

                # Calculer le coût g du chemin depuis le noeud de départ jusqu'au noeud voisin
                nouveauG = current.g + current.distance(voisin)

                # Si le noeud voisin n'est pas dans la liste ouverte ou si le nouveau coût g est plus petit que le coût g actuel
                if (voisin not in self.ouvert.queue) or (nouveauG < voisin.g):
                    # Mettre à jour le coût g du noeud voisin
                    voisin.g = nouveauG

                    # Calculer le coût h de l'estimation du chemin le plus court depuis le noeud voisin jusqu'au noeud final
                    voisin.h = voisin.heuristique(self.end)

                    # Calculer le coût f = g + h
                    voisin.f = voisin.g + voisin.h

                    # Ajouter le noeud voisin à la liste ouverte
                    self.ouvert.put(voisin)

        # Si aucun chemin n'a été trouvé, retourner une liste vide
        return []

    def reconstruireChemin(self, noeud):
        chemin = []
        courant = noeud
        while courant is not None:
            chemin.append(courant)
            courant = courant.parent
        return chemin[::-1]

