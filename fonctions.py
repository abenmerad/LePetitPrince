

""" Fonctions liées à la mise en forme du chateau sur l'outil graphique python map"""





""" Fonctions liées au déplacement du joueur """


def coordonnees_personnage(case, pas):
    coordX = -240 + (pas * case[1]) + (pas / 2)
    coordY = 200 - (pas * case[0]) - (pas / 2)
    return coordX, coordY


def spawn_personnage(matrice, coordonnees):
    personnage.clear()
    personnage.up()
    personnage.goto(coordonnees_personnage(coordonnees, calculer_pas(matrice)))
    personnage.dot(calculer_pas(matrice) * RATIO_PERSONNAGE, COULEUR_PERSONNAGE)


def deplacer(mouvement):
    global matrice, position
    prochainePosition = (position[0] + mouvement[0], position[1] + mouvement[1])
    if matrice[prochainePosition[0]][prochainePosition[1]] == '0':
        position = prochainePosition
        spawn_personnage(matrice, position)

def deplacer_gauche():
    turtle.onkeypress(None, "Left")  # Désactive la touche Left
    global matrice, position
    deplacer((0, -1))
    turtle.onkeypress(deplacer_gauche, "Left")  # Réactivation de la touche

def deplacer_droite():
    turtle.onkeypress(None, "Right")  # Désactive la touche Left
    global matrice, position
    deplacer((0, 1))
    turtle.onkeypress(deplacer_droite, "Right")  # Réactivation de la touche

def deplacer_haut():
    turtle.onkeypress(None, "Up")  # Désactive la touche Left
    global matrice, position
    deplacer((-1, 0))
    turtle.onkeypress(deplacer_haut, "Up")  # Réactivation de la touche

def deplacer_bas():
    turtle.onkeypress(None, "Down")  # Désactive la touche Left
    global matrice, position
    deplacer((1, 0))
    turtle.onkeypress(deplacer_bas, "Down")  # Réactivation de la touche
