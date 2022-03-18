import random

class PlayersController:
    """Class to manage players (humans, random, bot)"""
    def __init__(self, controller, player1, player2):
        self.controller = controller
        self.players = {
            1: player1,
            2: player2
        } 

    def managePlay(self, player_number:int) -> int:
        """
        Manage how to play and return column where player played

        Args:
            player_number (int): number of player who plays
        """
        player = self.players[player_number] # define player
        tab:list[list[int]] = self.controller.getTab() # get game's tab
        available_columns:list[int] = self.controller.getAvailableColumns() # get index of all available columns

        if player.type == "random":
            column = random.choice(available_columns)
            self.controller.play(player.tab_number, column)

        elif player.type == "human":
            # Display game's tab
            self.controller.printTab()
            # Ask to player where play
            while True:
                player_input = self.controller.ask(f"{player.name}, where do you want to play ? ")
                # try to convert input as integer
                try:
                    column = int(player_input)-1 # use column index (with -1)

                    # if column is not filled...
                    if column in available_columns:
                        # ... play
                        self.controller.play(player.tab_number, column)
                        break
                    else:
                        # column is filled so print message
                        self.controller.printMessage("This column is filled! Retry please... ")

                except:
                    # player's input is not an integer
                    self.controller.printMessage("This is not a column number! Retry please... ")


                    