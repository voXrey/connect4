
class View:
    controller = None
    
    def __init__(self):
        pass

    def printTab(self, tab:list[list[int]]) -> None:
        """
        Print game's tab to console

        Args:
            tab (list[list[int]]): game's tab to print
        """
        # Count lines and cols
        cols_count = len(tab[0])

        # Create var to stock what to print
        to_print = ""

        # Add col numbers
        numbers = []
        for col in range(cols_count): numbers.append(str(col+1))
        to_print += f" {' '.join(numbers)} "

        # Add lines
        for line in tab:
            to_join = []
            for col in line:
                if col == 1: to_join.append(self.controller.getPlayer(1).symbol)
                elif col == -1: to_join.append(self.controller.getPlayer(2).symbol)
                else: to_join.append(" ")

            line_string = '|'.join(to_join)
            to_print += f"\n|{line_string}|"
        
        # Print final tab to console
        print(to_print)
    
    def ask(self, message:str) -> str:
        """
        Ask something with console 

        Args:
            message (str): a message to send

        Returns:
            str: console input
        """
        return input(message)

    def printMessage(self, message:str) -> None:
        """
        Print a message in console

        Args:
            message (str): message to print
        """
        print(message)
    