from CONFIGS import *
import turtle


class Chateau:
    def __init__(self):
        self.matrice = self.lire_matrice(fichier_plan)
        self.pas = self.calculer_pas(self.matrice)
        self.map = turtle.Turtle()
        self.map.speed(0)
        self.map.ht()
        self.afficher_plan(self.matrice)

    @staticmethod
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

    def calculer_pas(self, matrice):
        """
        Calcule la dimension à donner aux cases et renvoie la plus petite valeur
        :param matrice:
        :return dimension:
        """
        largeur_plan = abs(ZONE_PLAN_MINI[0] - ZONE_PLAN_MAXI[0])
        hauteur_plan = abs(ZONE_PLAN_MINI[0] - ZONE_PLAN_MAXI[1])
        nb_ligne = len(matrice)
        nb_colonne = len(matrice[0])
        if (largeur_plan // nb_colonne) >= (hauteur_plan // nb_ligne):
            dimension = hauteur_plan // nb_ligne
        else:
            dimension = largeur_plan // nb_colonne
        return dimension

    def tracer_carre(self, dimension):
        """
        Trace un carré dont la dimensions est passée en paramètre
        :param dimension:
        :return:
        """
        for _ in range(4):
            self.map.forward(dimension)
            self.map.right(90)

    def tracer_case(self, case, couleur):
        """
        Tracer un carré d’une certaine couleur et taille à un certain endroit
        :param self:
        :param case:
        :param couleur:
        :param pas:
        :return:
        """
        self.map.up()
        self.map.goto(case)
        self.map.down()
        self.map.fillcolor(couleur)
        self.map.begin_fill()
        self.tracer_carre(self.pas)
        self.map.end_fill()

    def coordonnees(self, case):
        """
        Calcule les coordonnées en pixels du coin inférieur gauche d’une case passée en paramètre
        :param case:
        :param pas:
        :return coordX, coordY:
        """
        coordX = -240 + (self.pas * case[1])
        coordY = 200 - (self.pas * case[0])
        return coordX, coordY

    def afficher_plan(self, matrice):
        for i in range(len(matrice)):
            for y in range(len(matrice[i])):
                if matrice[i][y] == '0':
                    self.tracer_case(self.coordonnees((i, y)), COULEUR_CASES)
                elif matrice[i][y] == '1':
                    self.tracer_case(self.coordonnees((i, y)), COULEUR_MUR)
                elif matrice[i][y] == '2':
                    self.tracer_case(self.coordonnees((i, y)), COULEUR_OBJECTIF)
                elif matrice[i][y] == '3':
                    self.tracer_case(self.coordonnees((i, y)), COULEUR_PORTE)
                elif matrice[i][y] == '4':
                    self.tracer_case(self.coordonnees((i, y)), COULEUR_OBJET)
