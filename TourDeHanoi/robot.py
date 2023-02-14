from cube import Cube
from erreur import Erreur

class Robot: 
    #
    # 1. Ajout d'un constructeur qui prend prends en paramètre le booléen brasvide
    #
    def __init__(self, brasvide):
        self.brasvide = brasvide
        self.possedeCube = None

    #
    # 2. Ajout d'une méthode __str__ qui retourne une chaîne de caractères qui décrit l'état du robot.
    #
    def __str__(self):
        return "Robot: brasvide = " + str(self.brasvide) + ", possedeCube = " + str(self.possedeCube)
    
    #
    # 3. Ajout des méthodes get/set pour l'attribut brasvide et pour l'attribut possedeCube.
    #
    @property
    def brasvide(self):
        return self._brasvide
    
    @brasvide.setter
    def brasvide(self, value):
        self._brasvide = value

    @property
    def possedeCube(self):
        return self._possedeCube
    
    @possedeCube.setter
    def possedeCube(self, value):
        self._possedeCube = value
    
    # Actions disponibles

    # Tenir un cube (le robot doit être libre)
    @classmethod
    def TENIR(cls, cube):
        # Pour prendre le cube, il faut que le cube soit libre et que le bras du robot soit vide
        if cube is None:
            raise Erreur.CUBE_INEXISTANT
        else:
            if cls.brasvide == False:
                raise Erreur.BRAS_NON_VIDE
            elif cube.libre == False:
                raise Erreur.CUBE_NON_LIBRE
            else:
                cls.brasvide = False
                cls.possedeCube = cube
                if cube.surtable == True:
                    cube.surtable = False
                else:
                    cube.sur.libre = True
                    cube.sur = None
        return None

    # Poser un cube (le robot doit tenir un cube), il peut le poser sur la table ou sur un autre cube
    @classmethod
    def POSER(cls, cubeX, cubeY):
        # Pour poser le cube, il faut que le cubeX soit dans le bras du robot
        if cubeX is None:
            raise Erreur.CUBE_INEXISTANT
        else:
            if cls.brasvide == True:
                raise Erreur.BRAS_VIDE
            elif cubeX != cls.possedeCube:
                raise Erreur.CUBE_BRAS_DIFFERENT
            else:
                # Pour le poser sur la table, il faut que le cubeX soit dans le bras du robot et que le 
                # cubeY soit égal à None
                if cubeY is None:
                    cubeX.surtable = True
                    cls.brasvide = True
                    cls.possedeCube = None
                # Pour le poser sur un cube, il faut que le cubeX soit dans le bras du robot et que le
                # cubeY soit libre
                elif cubeY.libre == True:
                    cubeX.sur = cubeY
                    cubeY.libre = False
                    cls.brasvide = True
                    cls.possedeCube = None
                else:
                    raise Erreur.CUBE_NON_LIBRE
        return None