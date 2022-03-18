from core.controller import Controller
from core.model import GameModel
from core.view import View

if __name__ == "__main__":
    model = GameModel()
    view = View()
    controller = Controller(
        model=model,
        view=view
    )

    controller.start()
