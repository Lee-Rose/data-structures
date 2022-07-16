import doctest


class LinkedListNode:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self._head = None
        self.last = None


    def append(self, value):
        """Adding a value to the end of the list"""
        new_element = LinkedListNode(value)

        if not self._head:
            self._head = new_element
        else:
            element = self._head
            while element.next_node:
                element = element.next_node
            element.next_node = new_element


    def append_left(self, value):
        """Adding an element to the beginning of the list"""

        first_element = LinkedListNode(value) 
        first_element.next_node = self._head 
        self._head = first_element


    def pop_left(self):
        """Returns the value of the first element of the list and removes it"""

        cursor = self._head
        if cursor == None:
            return None
        self._head = cursor.next_node

        return cursor.value


    def insert(self, value, index):
        """Inserting an element at position index. If the index position is greater than the length of the list, the element
        will be added to the end of this list
        # >>> some = LinkedList()
        # >>> some.insert(10, 0)
        # 10, 6, 1, 0
        """

        if index == 0:
            self.append_left(value)

        elif index > (self.__len__()-1):
            self.append(value)

        else:
            item = LinkedListNode(value)
            count = 0
            previous_index = self._head

            while count < (index - 1):
                count += 1
                previous_index = previous_index.next_node
            
            item.next_node = previous_index.next_node
            previous_index.next_node = item
        

    def delete(self, index):
        """Remove element from position index"""

        if self._head == None:
            return

        item = self._head
        if index == 0:
            self._head = item.next_node

            return
        for i in range(index - 1):
            item = item.next_node
            if item is None:
                break
        if item.next_node is None:
            return
        # next_node — node to be removed.
        next_node = item.next_node.next_node
        # store a pointer to the next node to be removed
        item.next_node = next_node


    def get(self, index):
        """A function that gets the value of the element at position index"""

        cursor = self._head
        list_index = 0

        while list_index <= index and cursor is not None:
            if list_index == index:
                return cursor.value
            list_index += 1
            cursor = cursor.next_node
        if index < 0 or index >= self.__len__():
            raise IndexError('Object at this index does not exist')
        return


    def __iter__(self):
        self._next_counter = 0
        return self

    def __next__(self):

        #from one element
        if self._next_counter == 0:
            self._current_element = self._head
        else:
            self._current_element = self._current_element.next_node

        self._next_counter += 1
        if not self._current_element:
            raise StopIteration
        return self._current_element.value

        # of two elements
        # elif:
        #     self._current_element = self._current_element.next_node


    def __len__(self):
        """Return the length of a list"""

        cursor = self._head
        count = 0
        while cursor:
            count += 1
            cursor = cursor.next_node
        return count


    def __repr__(self):

        values = []
        element = self._head

        while element:
            values.append(str(element.value))
            element = element.next_node

        return ' -> '.join(values)


if __name__ == '__main__':
    numbers = LinkedList()
    numbers.append(1)
    numbers.append_left(6)
    numbers.insert(0, 2)
    print(numbers)
    numbers.delete(1)
    print(numbers)



