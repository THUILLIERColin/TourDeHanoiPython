from cube import Cube
from erreur import Erreur

class Robot: 
    #
    # 1. Ajout d'un constructeur qui prend prends en paramètre le booléen brasvide
    #
    def __init__(self, brasvide, possedeCube=None):
        self.brasvide = brasvide
        self.possedeCube = possedeCube


    #
    # 2. Ajout d'une méthode __str__ qui retourne une chaîne de caractères qui décrit l'état du robot.
    #
    def __str__(self):
        return "Robot: [ brasvide = " + str(self.brasvide) + ", possedeCube = " + str(self.possedeCube) + " ]"

    #
    #
    #
    def __eq__(self, other):
        return self.brasvide == other.brasvide and self.possedeCube == other.possedeCube

    #
    # 3. Ajout d'une méthode __copy__ qui retourne une copie du robot.
    #
    def copy(self):
        return Robot(self.brasvide, self.possedeCube)

    #
    # 4. Ajout des méthodes get/set pour l'attribut brasvide et pour l'attribut possedeCube.
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
    def TENIR(cls, robot, cube):
        # Pour prendre le cube, il faut que le cube soit libre et que le bras du robot soit vide
        if cube is None:
            raise Erreur.CUBE_INEXISTANT
        else:
            if not robot.brasvide:
                raise Erreur.BRAS_NON_VIDE
            elif not cube.libre:
                raise Erreur.CUBE_NON_LIBRE
            else:
                robot.brasvide = False # Le bras n'est plus vide
                cube.libre = False # Le cube n'est plus libre
                if cube.surtable:
                    cube.surtable = False # Le cube n'est plus sur la table
                else:
                    cube.sur.libre = True # Le cube n'est plus sur un autre cube
                    cube.sur = None # Le cube n'est plus sur un autre cube
                robot.possedeCube = cube # Le robot possède le cube
        return None

    # Poser un cube (le robot doit tenir un cube), il peut le poser sur la table ou sur un autre cube
    @classmethod
    def POSER(cls, robot, cubeX, cubeY=None):
        # Pour poser le cube, il faut que le cubeX soit dans le bras du robot
        if cubeX is None:
            raise Erreur.CUBE_INEXISTANT
        if robot.brasvide:
            raise Erreur.BRAS_VIDE
        if cubeX != robot.possedeCube:
            raise Erreur.CUBE_BRAS_DIFFERENT
        if isinstance(cubeY, Cube) and not cubeY.libre:
            raise Erreur.CUBE_NON_LIBRE

        # Pour le poser sur la table, il faut que le cubeX soit dans le bras du robot et que le
        # cubeY soit égal à None
        if cubeY is None:
            cubeX.surtable = True
            cubeX.libre = True
            robot.brasvide = True
            robot.possedeCube = None

        # Pour le poser sur un cube, il faut que le cubeX soit dans le bras du robot et que le
        # cubeY soit libre
        elif cubeY.libre:
            if cubeX == cubeY:
                raise Erreur.CUBE_BRAS_IDENTIQUE
            cubeX.sur = cubeY # Le cubeX est sur le cubeY
            cubeY.libre = False # Le cubeY n'est plus libre
            cubeX.libre = True # Le cubeX n'est plus libre
            robot.brasvide = True # Le bras est vide
            robot.possedeCube = None
        return None

    #
    @classmethod
    def annuleTenir(cls, robot):
        robot.brasvide = True # Le bras est vide
        robot.possedeCube = None # Le robot ne possède plus de cube
        return None

    #
    @classmethod
    def annulePoser(cls, robot, cubeX, cubeY=None):#cubeX est le cube posé, cubeY est le cube sur lequel il est posé
        #cubeX.libre = False
        #cubeX.surtable = False
        #cubeX.sur = None

        robot.brasvide = False # Le bras n'est plus vide
        robot.possedeCube = cubeX # Le robot possède le cube
        if cubeY is not None:
            cubeY.libre = True # Le cube n'est plus sur un autre cube

        return None