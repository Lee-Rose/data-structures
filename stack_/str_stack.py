
from linked_list.str_linked_list import  LinkedList


class Stack():

    def __init__(self):
        self._list = LinkedList()


    def push(self, value):
        """Inserting an element at the top of the stack"""
        self._list.insert(value, 0)


    def peek(self):
        """return the top element of the stack"""
        
        if self._list != None:
            return self._list.get(0)
        else:
            print('The stack is empty')
            exit(-1)


    def pop(self):
        """popping the top element from the stack"""
        return self._list.pop_left()


    def __len__(self):
        """returns the stack size"""
        return len(self._list)


    def __iter__(self):
        self._next_counter = 0
        return self


    def __next__(self):
        # from one element
        if self._next_counter == 0:
            self._current_element = self._list._head
        else:
            self._current_element = self._current_element.next_node

        self._next_counter += 1
        if not self._current_element:
            raise StopIteration
        return self._current_element.value

        # of two elements
        # elif:
        #     self._current_element = self._current_element.next_node


    def __repr__(self):

        values = []
        element = self._list._head

        while element:
            values.append(str(element.value))
            element = element.next_node

        return ' -> '.join(values)


if __name__ == '__main__':

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(33)
    stack.push(999)
    print(stack)
    print('Top element is ', stack.peek())
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)






