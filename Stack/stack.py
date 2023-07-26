import sys


class Stack:

    STACK_CAPACITY = 10_000

    def __init__(self) -> None:

        # Initializes an empty list to store the elements of the stack.
        self.__items = []


    def __len__(self) -> int:

        # Returns the number of elements in the stack.
        return len(self.__items)


    def is_empty(self) -> bool:

        # Checks if the stack is empty and returns True if it is, otherwise False.
        return len(self) == 0


    def is_full(self) -> bool:

        # Checks if the stack is full (reached its capacity) and returns True if it is, otherwise False.
        return len(self) == self.STACK_CAPACITY


    def push(self, item : int) -> None:

        # Adds the given item to the top of the stack.
        # Raises a TypeError if the item is not an integer.
        # Raises an OverflowError if the stack is already full.

        if type(item) != int:
            raise TypeError('The item must be an integer')

        if not self.is_full():
            self.__items.append(item)
        else:
            raise OverflowError('Stack Overflow Error')


    def pop(self) -> int:

        if self.is_empty():
            raise IndexError('The Stack is empty')
        # Removes and returns the item from the top of the stack.
        return self.__items.pop()


    def top(self) -> int:

        if self.is_empty():
            raise IndexError('The Stack is empty')
        # Returns the item at the top of the stack without removing it.
        return self.__items[-1]


    def __repr__(self) -> str:

        # Returns a string representation of the Stack object for debugging purposes.
        return f'{self.__class__.__name__}()'


    def __str__(self) -> str:

        # Returns a string representation of the Stack object, showing its contents.
        items = f'{self.__items}'

        # somthing like : Stack(2, 3, 4, 8) will be return because [1:-1] returns just values without prantheses.
        return f'{self.__class__.__name__}({items[1:-1]})'


if __name__ == '__main__':
    print(sys.version_info)