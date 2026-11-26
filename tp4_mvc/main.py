import pygame
from model.game_board import GameBoard
from model.alt_game_model import CatchGameModel
from view.game_view import GameView
from controller.game_controller import GameController

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    
    model = GameBoard(width=800, height=600)
    

    view = GameView(model, theme_path="assets/theme_default")
    controller = GameController(model, view)
    controller.run()