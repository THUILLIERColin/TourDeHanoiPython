# Description: Utility functions for the TP1 project

# Imports
from cube import Cube
from erreur import Erreur
from robot import Robot


# La fonction return le cube dont le nom est name
def find_cube_by_name(cubes, name):
        """ Cherche un cube dans une liste de cubes à partir de son nom

        Parameters:
                cubes (list): liste de cubes
                name (str): nom du cube à trouver

        Returns:
                cube (Cube): le cube dont le nom est name
        """
        return next((cube for cube in cubes if cube.name == name), None)

# put_cube_on_cube prend une liste de cubes et pour chaque cube, 
# si le cube a un cube sur lui, on le remplace par l'instance du cube correspondant
def put_cube_on_cube(cubes):
        """ Creation de la liste de cubes avec les cubes sur lesquels ils sont

        Parameters:
                cubes (list): liste de cubes

        Returns:
                cubes (list): liste de cubes avec les cubes sur lesquels ils sont
        """
        for cube in cubes:
                if isinstance(cube.sur, Cube):
                        # Si le cube à deja le cube sur lequel il est, on passe au cube suivant
                        continue
                elif    cube.sur is not None:
                        tmp = cube.sur
                        cube.sur = find_cube_by_name(cubes, tmp)
        return cubes
