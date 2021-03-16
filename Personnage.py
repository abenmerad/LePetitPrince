from CONFIGS import *
import turtle


class Personnage:
    def __init__(self, chateau):
        self.position = POSITION_DEPART
        self.chateau = chateau
        self.personnage = turtle.Turtle()
        self.personnage.speed(0)
        self.personnage.ht()
        self.spawn_personnage(self.position)

    def coordonnees_personnage(self, case, pas):
        coordX = -240 + (pas * case[1]) + (pas / 2)
        coordY = 200 - (pas * case[0]) - (pas / 2)
        return coordX, coordY

    def spawn_personnage(self, coordonnees):
        self.personnage.clear()
        self.personnage.up()
        self.personnage.goto(self.coordonnees_personnage(coordonnees, self.chateau.pas))
        self.personnage.dot(self.chateau.pas * RATIO_PERSONNAGE, COULEUR_PERSONNAGE)

    def deplacer(self, mouvement):
        prochainePosition = (self.position[0] + mouvement[0], self.position[1] + mouvement[1])
        if self.chateau.matrice[prochainePosition[0]][prochainePosition[1]] == '0':
            self.position = prochainePosition
            self.spawn_personnage(self.position)

    def deplacer_gauche(self):
        turtle.onkeypress(None, "Left")  # Désactive la touche Left
        self.deplacer((0, -1))
        turtle.onkeypress(self.deplacer_gauche, "Left")  # Réactivation de la touche

    def deplacer_droite(self):
        turtle.onkeypress(None, "Right")  # Désactive la touche Left
        self.deplacer((0, 1))
        turtle.onkeypress(self.deplacer_droite, "Right")  # Réactivation de la touche

    def deplacer_haut(self):
        turtle.onkeypress(None, "Up")  # Désactive la touche Left
        self.deplacer((-1, 0))
        turtle.onkeypress(self.deplacer_haut, "Up")  # Réactivation de la touche

    def deplacer_bas(self):
        turtle.onkeypress(None, "Down")  # Désactive la touche Left
        self.deplacer((1, 0))
        turtle.onkeypress(self.deplacer_bas, "Down")  # Réactivation de la touche