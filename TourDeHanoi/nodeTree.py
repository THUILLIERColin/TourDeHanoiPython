from anytree import AnyNode, RenderTree, DoubleStyle
class nodeTree(AnyNode):
    #Class qui permet de créer un arbre a l aide de la librairie anytree

    def __init__(self, parent=None,chaine=None,path=None):
        self.parent = parent
        self.chaine = chaine
        self.path = path

    def __str__(self):
        return self.chaine

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.chaine == other.chaine and self.path == other.path and self.parent == other.parent

    def __hash__(self):
        return hash(self.chaine)

    def __lt__(self, other):
        return self.chaine < other.chaine

