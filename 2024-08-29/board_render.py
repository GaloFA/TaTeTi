# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from os import system
from board import Board

class BoardRender(list):
    """ Clase que representa al tablero de juego,
    guarda su estado y sus dimensiones. """

    def __init__(self, board: Board):
        self.__board = board

    def draw_reference_board(self):
        """ Tablero que se utiliza para dar una referencia del número
        de las posiciones de cada casillero en el tablero """
        reference_board = ""

        for row in range(self.__board.dimensions):
            for col in range(self.__board.dimensions):
                position = row * self.__board.dimensions + col # Representa la posición de cada casillero en el tablero
                reference_board += f"{position}   " # Agrega cada posición a un string y la formatea para que tenga formato de tablero
            reference_board += "\n"

        return reference_board # Retorna el tablero de referencia

    def draw_board(self):
        """ Método que se encarga de dibujar el tablero """
        final_board = ""
        iterator = iter(self.__board.board_list)

        for _ in range(0, self.__board.dimensions ** 2, self.__board.dimensions):
            for _ in range(self.__board.dimensions):
                final_board += f"{next(iterator)}   " # Genera el tablero en su estado actual
            final_board += "\n" # Agrega nuevas lineas para poner el formato de tablero correcto

        return final_board # Retorna el tablero en formato correcto

    def print_board(self):
        """ Método para imprimir el estado actual del tablero """
        system("cls")
        print("\n")
        print(self.draw_reference_board())
        print(self.draw_board())
