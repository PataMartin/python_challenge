"""
The challenge has two stages:

1- Complete the methods of the MyQueue class using the docstrings as guides.
   The only restriction is that you can only use the list methods push and pop.
   You cannot reference list members using any sort of index nor manipulate
   the order of the elements.

2- Write unit tests for these methods on another file called test_queue.py.
   You must use the unittest module for this purpose.
"""


class MyQueue:
    """
    This class implements a custom FIFO queue of integers.
    """

    my_queue = []

    def __init__(self):
        """
        Class constructor.
        """
        pass

    def insert(self, element):
        """
        Insert a element into the queue.

        Args:
            - element(int): Element to insert into the queue.

        Returns(int): object count.
        """
        pass

    def get(self):
        """
        Get the next element of the queue.

        Args:

        Return(int): Next element of the queue.
        """
        pass

    def fetch(self):
        """
        Fetch the next element of the queue without taking it out of the queue.

        Args:

        Return(int): Next element of the queue.
        """
        pass
