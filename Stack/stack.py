class Stack:

    STACK_CAPACITY = 10

    def __init__(self) -> None:

        self.__items = []


    def __len__(self) -> int:

        return len(self.__items)


    def is_empty(self) -> bool:

        return len(self) == 0


    def is_full(self) -> bool:

        return len(self) == self.STACK_CAPACITY


    def push(self, item : int) -> None:

        if type(item) != int:
            raise TypeError('The item must be an integer')

        if not self.is_full():
            self.__items.append(item)
        else:
            raise OverflowError('Stack Overflow Error')