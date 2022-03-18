# connect4
A connect4 game created in python in MVC architecture and which uses machine learning. 

## Config game
In `/core/model.py` you can customize players options
* `name`: define player name
* `symbol`: define player symbol which will displayed
* `tab_number: number used in program to know which player played in a certain place
* `type`: choose how the game should treat this player (can be: **random**, **human**)

## Start game
Execute `main.py` file to start program

## MVC
I tried to use MVC architecture with:
* **Model**: `/core/model.py`, this model stocks all game's data
* **View**: `/core/view.py`, this view uses console to interact with players
* **Controller**: `/core/controller.py`, this controller use a subcontroller in `/core/players_controller.py`
