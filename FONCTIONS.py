from CONFIGS import *
import turtle

def lire_matrice(fichier):
    """
    Recoit en argument le nom d’un fichier texte contenant le plan à tracer.
    Ouvre ce fichier et renvoit en sortie une matrice dont chaque élément sera une ligne horizontale de cases du plan.
    :param fichier:
    :return matrice:
    """
    matrice = []
    for ligne in open(fichier, encoding="utf-8"):
        matrice.append(ligne.strip().split(" "))
    return matrice

def calculer_pas(matrice):
    """
    Calcule la dimension à donner aux cases et renvoie la plus petite valeur
    :param matrice:
    :return dimension:
    """
    largeur_plan = abs(ZONE_PLAN_MINI[0] - ZONE_PLAN_MAXI[0])
    hauteur_plan = abs(ZONE_PLAN_MINI[0] - ZONE_PLAN_MAXI[1])
    nb_ligne = len(matrice)
    nb_colonne = len(matrice[0])
    if((largeur_plan / nb_colonne) >= (hauteur_plan / nb_ligne)):
        dimension = hauteur_plan // nb_ligne
    else:
        dimension = largeur_plan // nb_colonne
    return dimension

def coordonnees(case, pas):
    """
    Calcule les coordonnées en pixels du coin inférieur gauche d’une case passée en paramètre
    :param case:
    :param pas:
    :return coordX, coordY:
    """
    coordX = -240 + (pas * case[1])
    coordY = 200 - (pas * case[0])
    return coordX, coordY

def tracer_carre(dimension):
    """
    Trace un carré dont la dimensions est passée en paramètre
    :param dimension:
    :return:
    """
    for i in range(4):
        turtle.forward(dimension)
        turtle.left(90)

def tracer_case(case, couleur, pas):
    """
    Tracer un carré d’une certaine couleur et taille à un certain endroit
    :param case:
    :param couleur:
    :param pas:
    :return:
    """
    turtle.up()
    turtle.goto(case)
    turtle.down()
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    tracer_carre(pas)
    turtle.end_fill()

def afficher_plan(matrice):
    pas = calculer_pas(matrice)
    for i in range(len(matrice)):
        for y in range(len(matrice[i])):
            if matrice[i][y] == '0':
                tracer_case(coordonnees((i, y), pas), COULEUR_CASES, pas)
            elif matrice[i][y] == '1':
                tracer_case(coordonnees((i, y), pas), COULEUR_MUR, pas)
            elif matrice[i][y] == '2':
                tracer_case(coordonnees((i, y), pas), COULEUR_OBJECTIF, pas)
            elif matrice[i][y] == '3':
                tracer_case(coordonnees((i, y), pas), COULEUR_PORTE, pas)
            elif matrice[i][y] == '4':
                tracer_case(coordonnees((i, y), pas), COULEUR_OBJET, pas)


