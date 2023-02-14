from enum import Enum

class Erreur(Exception, Enum):
    CUBE_NON_LIBRE = "Erreur: Le cube n'est pas libre"
    CUBE_NON_SURTABLE = "Erreur: Le cube n'est pas sur la table"
    CUBE_BRAS_DIFFERENT = "Erreur: Le cube n'est pas dans le bras du robot"
    CUBE_INEXISTANT = "Erreur: Le cube n'existe pas"
    BRAS_NON_VIDE = "Erreur: Le bras du robot n'est pas vide"
    BRAS_VIDE = "Erreur: Le bras du robot est vide"
    ROBOT_INEXISTANT = "Erreur: Le robot n'existe pas"
    ETAT_INEXISTANT = "Erreur: L'état n'existe pas"
    LISTE_CUBES_INEXISTANTE = "Erreur: La liste de cubes n'existe pas"
    CUBE_DEJA_SUR = "Erreur: Le cube du dessous est déjà initialisé"