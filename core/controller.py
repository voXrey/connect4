from core.players_controller import PlayersController

class Controller:
    def __init__(self, model, view):
        self.model = model
        view.controller = self
        self.view = view
        self.players_controller = PlayersController(
            self,
            self.model.player1,
            self.model.player2
        )

        self.initTab()
    
    def initTab(self) -> None:
        """
        Set game's tab
        """
        self.model.tab = [[0 for col in range(self.model.columns_count)] for line in range(self.model.lines_count)]
    
    def getTab(self) -> list[list[int]]:
        """
        Get game's tab

        Returns:
            list[list[int]]: game's tab
        """
        return self.model.tab

    def getLinesCount(self) -> int:
        """
        Get game's lines count

        Returns:
            int: lines count
        """
        return self.model.lines_count

    def getColumnsCount(self) -> int:
        """
        Get game's columns count

        Returns:
            int: columns count
        """
        return self.model.columns_count

    def isFilledColumn(self, column:int, tab:list[list[int]]=None) -> bool:
        """
        Check if a column is filled

        Args:
            column (int): index of column to check
            tab (list[list[int]]): tab, default `None` = current game's tab

        Returns:
            bool: `True` if column is filled, `False` if not
        """
        if tab is None: tab = self.getTab()
        return tab[0][column] != 0

    def isFilledTab(self) -> bool:
        """
        Check if tab is filled

        Returns:
            bool: `True` if tab is filled, `False` if not
        """
        # For each column
        for col in range(len(self.model.tab[0])):
            # Check if column is filled, if not return False
            if not self.isFilledColumn(col): return False
        # If all columns are filled return True
        return True
    
    def columnLowestLine(self, column:int, tab:list[list[int]]=None) -> int:
        """
        Get lowest column's line 

        Args:
            column (int): index of column to get lowest line
            tab (list[list[int]]): tab, default `None` = current game's tab

        Returns:
            int: line's index or `-1` if column is filled
        """
        if tab is None: tab = self.getTab()
        # For each line of column...
        for line in range(self.model.lines_count-1, -1, -1):
            # ...check if place is available
            if tab[line][column] == 0: return line
        # If column is filled
        return -1

    def play(self, player:int, column:int) -> None:
        """
        Place token in a column
        (we suppose that column was checked before and is not filled)

        Args:
            player (int): player who plays (`1` or `-1`)
            column (int): index of column where place token
        """
        # Get lowest line available in column
        line = self.columnLowestLine(column)
        # Place token in tab
        self.model.tab[line][column] = player

    def printTab(self) -> None:
        """
        Ask to view to print tab in consol
        """
        self.view.printTab(self.model.tab)

    def align_h(self, case) -> list[list[tuple[int]]]:
        """
        Get list of horizontal alignments

        Args:
            case (tuple[int]): (line, col) coordinates of played case
        
        Returns:
            list[list[tuple[int]]] : list of horizontal alignments
        """
        line, col = case
        align = [] # var to stock horizontal alignments

        # Check 4 gaps which can be valid alignments
        for gap in range(4):
            coord = [col-gap+i for i in range(4)]
            # Add alignement if no case (with gap) is out of tab
            valid = True
            for elem in coord:
                if elem < 0 or elem > self.model.columns_count-1:
                    valid = False
            if valid:
                align.append([self.model.tab[line][col] for col in coord])

        # Return alignments
        return align

    def align_v(self, case) -> list[list[tuple[int]]]:
        """
        Get list of vertical alignments

        Args:
            case (tuple[int]): (line, col) coordinates of played case
        
        Returns:
            list[list[tuple[int]]] : list of vertical alignments 
        """
        line, col = case
        align = [] # var to stock vertical alignments

        # Check 4 gaps which can be valid alignments
        for dec in range(4):
            coord = [line-dec+i for i in range(4)]
            # Add alignement if no case (with gap) is out of tab
            test = True
            for elem in coord:
                if elem < 0 or elem > self.model.lines_count-1:
                    test = False
            if test:
                align.append([self.model.tab[line][col] for line in coord])
        
        # Return alignments
        return align

    def align_rd(self, case) -> list[list[tuple[int]]]:
        """
        Get list of rising diagonal alignments

        Args:
            case (tuple[int]): (line, col) coordinates of played case
        
        Returns:
            list[list[tuple[int]]] : list of rising diagonal alignments 
        """
        line, col = case
        align = [] # var to stock alignments

        # Check 4 gaps which can be valid alignments
        for dec in range(4):
            coord_line = [line-dec-i for i in range(4)]
            coord_col = [col-dec+i for i in range(4)]

            # Add alignement if no case (with gap) is out of tab
            test = True

            for elem in coord_line:
                if elem < 0 or elem > self.model.lines_count-1:
                    test = False

            for elem in coord_col:
                if elem < 0 or elem > self.model.columns_count-1:
                    test = False
            if test:
                align.append([self.model.tab[line][col] for line,col in zip(coord_line, coord_col)])

        # Return alignments
        return align

    def align_dd(self, case) -> list[list[tuple[int]]]:
        """
        Get list of downward diagonal alignments

        Args:
            case (tuple[int]): (line, col) coordinates of played case
        
        Returns:
            list[list[tuple[int]]] : list of downward diagonal alignments 
        """
        line, col = case
        align = [] # var to stock vertical alignments

        # Check 4 gaps which can be valid alignments
        for dec in range(4):
            coord_line = [line-dec+i for i in range(4)]
            coord_col = [col-dec+i for i in range(4)]

            # Add alignement if no case (with gap) is out of tab
            test = True

            for elem in coord_line:
                if elem < 0 or elem > self.model.lines_count-1:
                    test = False

            for elem in coord_col:
                if elem < 0 or elem > self.model.columns_count-1:
                    test = False
            if test:
                align.append([self.model.tab[line][col] for line,col in zip(coord_line, coord_col)])

        # Return alignments
        return align

    def travelAligns(self, aligns) -> bool:
        """
        Travel a list of aligns and check if there is an alignement of 4 sames tokens

        Args:
            aligns (list[list[tuple]]): liste des alignments
        
        Returns:
            bool: `True` if have an correct alignement, else, `False`
        """
        for align in aligns:
            if sum(align) == 4 or sum(align) == -4:
                return True
        return False

    def victory(self) -> bool:
        """
        Check if there is a victory

        Returns:
            bool: `True` if have a victory, else, `False`
        """
        for line in range(self.model.lines_count):
            for col in range(self.model.columns_count):
                aligns = (
                    self.align_h((line, col))
                    + self.align_v((line, col))
                    + self.align_dd((line, col))
                    + self.align_rd((line, col))
                )
                travel_result = self.travelAligns(aligns)
                if travel_result:
                    return True
        return False

    def getAvailableColumns(self) -> list[int]:
        """
        Get all avaible columns in game's tab

        Returns:
            list[int]: list of available columns index
        """
        available_cols = []
        for col in range(self.model.columns_count):
            if not self.isFilledColumn(col):
                available_cols.append(col)
        return available_cols

    def printMessage(self, message:str) -> None:
        """
        Print a message

        Args:
            message (str): message to print
        """
        self.view.printMessage(message)

    def ask(self, message:str) -> str:
        """
        Ask something

        Args:
            message (str): a message to send

        Returns:
            str: input
        """
        return self.view.ask(message)

    def getPlayer(self, player_number:int) -> any:
        """
        Return a player

        Args:
            player_number (int): number of player asked

        Returns:
            any: Player asked
        """
        if player_number == 1:
            return self.model.player1
        elif player_number == 2:
            return self.model.player2

    def start(self) -> None:
        """
        Main loop of program
        """
        def check(player_number) -> bool:
            """
            Check if game must be terminated and act in consequence

            Returns:
                bool: `True` if yes, `False` if not
            """
            # Check if game's tab is filled
            isFilledTab = self.isFilledTab()
            if isFilledTab:
                self.view.printMessage("Game is finished because game's tab is filled!")
                return True
            
            # Check if there is a victory
            victory = self.victory()
            if victory:
                self.view.printMessage(f"Congratulations {self.getPlayer(player_number).name}! You win game!")
                return True
            
            # Game musn't be terminated
            return False

        while True:
            player_number = (self.model.counter % 2) + 1
            self.players_controller.managePlay(player_number)
            if check(player_number):
                # Display game's tab
                self.printTab()
                break
            self.model.counter += 1
