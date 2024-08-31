""" Imports """
from collections.abc import Iterable, Iterator # pylint: disable=unused-import

class ListHandler(Iterator):
    """ Clase que maneja las colecciones de todo el programa """
    def __init__(self, collection: list):
        self.__collection = collection
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__collection):
            raise StopIteration

        result = self.__collection[self.__index]
        self.__index += 1
        return result

    def __getitem__(self, index):
        return self.__collection[index]

    def append(self, item):
        """ Método que permite agregar elementos a la lista que se está manejando """
        self.__collection.append(item)

    def check_if_elements_inside_list_are_equal(self) -> bool:
        """ Método que verifica si los elementos dentro de una lista son iguales """
        element = self.__collection[0]

        for item in self.__collection:
            if element != item:
                return False

        return True

    def get_list(self):
        """ Retorna la lista """
        return self.__collection
