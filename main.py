from CONFIGS import *
from Chateau import Chateau
from Personnage import Personnage
import turtle

chateau = Chateau()
petit_prince = Personnage(chateau)

turtle.listen()  # Déclenche l’écoute du clavier
turtle.onkeypress(petit_prince.deplacer_gauche, "Left")  # Associe à la touche Left une fonction appelée deplacer_gauche
turtle.onkeypress(petit_prince.deplacer_droite, "Right")
turtle.onkeypress(petit_prince.deplacer_haut, "Up")
turtle.onkeypress(petit_prince.deplacer_bas, "Down")
turtle.mainloop()  # Place le programme en position d’attente d’une action du joueur
