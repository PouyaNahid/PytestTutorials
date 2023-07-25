class Stack:

    CAPACITY = 10

    def __init__(self) -> None:

        self.__items = []


    def __len__(self) -> int:

        return len(self.__items)