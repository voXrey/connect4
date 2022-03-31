import copy
import itertools

class BotMinMax:
    def __init__(self, controller, level=1, player=-1):
        self.controller = controller
        self.level = level
        self.player = player

    def caseValue(self, case:tuple[int]) -> int:
        """
        Calculate the value of a case

        Args:
            case (tuple[int]): case targeted

        Returns:
            int: value of the case
        """
        aligns = (
            self.controller.align_h(case) +
            self.controller.align_v(case) +
            self.controller.align_rd(case) +
            self.controller.align_dd(case)
        )
        val = 0
        for align in aligns:
            if -self.player not in align:
                val += sum(align)
        return -val

    def gridValue(self, tab:list[list[int]]):
        """
        Calculate the value of a grid
        
        Args:
            tab (list[list[int]]): the grid

        Returns:
            int: grid's value
        """
        val = 0
        lines_count = self.controller.getLinesCount()
        columns_count = self.controller.getLinesCount()

        for line in range(lines_count):
            for col in range(columns_count):
                val += self.caseValue((line, col))
        return val

    def wherePlay(self) -> int:
        """
        Determine where to play

        Returns:
            int: column where play
        """
        a = itertools.product(
            [i for i in range(self.controller.getColumnsCount())],
            repeat=2*self.level
        )
        grids = []
        for elem in a:
            tab = copy.deepcopy(self.controller.getTab())
            player = self.player
            test = True
            for col in elem:
                if not self.controller.isFilledColumn(col, tab): # check if column is not filled in this tab
                    line = self.controller.columnLowestLine(col, tab)
                    tab[line][col] = player
                else:
                    test = False
                    break
                player = -player

            if not test: continue
            grids.append((elem, self.gridValue(tab)))

        grids.sort(key=lambda x: x[1])
        best_grid = grids.pop()
        col = best_grid[0][0]
        
        return col

    
