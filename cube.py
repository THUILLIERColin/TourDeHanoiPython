
class Cube: 
    #
    # 1. Ajout d'un constructeur qui prend en paramètre le nom du cube, 
    #    et qui initialise les attributs libre, sur et surtable à en fonction 
    #    des paramètres du constructeur.
    #    ici sur est un string qui représente le cube sur lequel est posé le cube courant.
    #
    def __init__(self, name, libre, sur, surtable):
        """Constructeur de la classe Cube

        Parameters:
            name (str): nom du cube
            libre (bool): True si le cube est libre, False sinon
            sur (str): nom du cube sur lequel est posé le cube courant
            surtable (bool): True si le cube est sur la table, False sinon

        À noter que la variable sur deviendra un objet de type Cube grâce à la méthode put_cube_on_cube
        """
        self.libre = libre
        self.sur = sur
        self.surtable = surtable
        self.name = name
    
    #
    # 2. Ajout d'une méthode __eq__ qui compare deux cubes en fonction de leur nom, 
    #   leur paramètre libre, sur et surtable.
    #
    def __eq__(self, other):
        return self.name == other.name and self.libre == other.libre and self.sur == other.sur and self.surtable == other.surtable

    #
    # 3. Ajout d'une méthode __hash__ qui définit comment les objets de cette classe sont hashés,
    #    afin qu'ils puissent être utilisés comme des clés dans des structures de données
    #    telles que des dictionnaires.
    #
    @staticmethod
    def __hash__(self):
        return hash(self.name)
    
    #
    # On ajoute les méthodes get/set pour les attributs libre, sur et surtable.
    #

    @property
    def libre(self):
        return self._libre

    @libre.setter
    def libre(self, value):
        self._libre = value

    @property
    def sur(self):
        return self._sur
    
    @sur.setter
    def sur(self, value):
        self._sur = value
    
    @property
    def surtable(self):
        return self._surtable
    
    @surtable.setter
    def surtable(self, value):
        self._surtable = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    #
    # 4. Ajout d'une méthode __str__ qui retourne une chaîne de caractères représentant le cube.
    #
    def __str__(self):
        return self.name + " = [ libre = " + str(self.libre) + ", Sur = " + str(self.sur) + ", SurTable = " + str(self.surtable)+" ]"
    

