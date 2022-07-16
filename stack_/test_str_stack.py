import unittest

from str_stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.numbers = Stack()


    def test_empty_list_and_raises_stop_iteration(self):
        """check for empty list and stop iteration"""

        iterator = iter(self.numbers)
        with self.assertRaises(StopIteration):
            next(iterator)


    def test_one_element_in_stack_and_return_element_and_stopiter(self):
        """checking a list of one element"""

        self.numbers.push(1)
        iterator = iter(self.numbers)
        self.assertEqual(1, next(iterator))
        with self.assertRaises(StopIteration):
            next(iterator)


    def test_push_element(self):
        """checks if the Stack (heap) is full. Then inserting the element
            will be lead to stack overflow"""

        self.numbers.push(12)
        self.numbers.push(43)
        self.numbers.push(88)
        self.numbers.push(90)
        
        self.assertEqual((90,88,43,12), tuple(self.numbers))
        

    def test_top_element_return_correct_value(self):
        """correctly return the last value of the stack"""

        self.numbers.push(0)
        self.numbers.push(3)
        self.numbers.push(85)

        self.assertEqual(85, self.numbers.peek())
        

    def test_empty_stack_and_raises_stop_iteration(self):
        """check for empty list and stop iteration"""

        iterator = iter(self.numbers)
        with self.assertRaises(StopIteration):
            next(iterator)


    def test_pop_element_return_correct_stack(self):
        """removing the top element of the stack
        and displaying the updated stack correctly"""

        self.numbers.push(19)
        self.numbers.push(122)
        self.numbers.push(37)

        self.assertEqual(37, self.numbers.pop())
        self.assertNotIn(37, self.numbers)

    def test_size_stack_return_correct_value(self):
        """checking the stack length and displaying the correct value"""
        
        self.numbers.push(18)
        self.numbers.push(1223)
        self.numbers.push(990)
        
        self.assertEqual(3, len(self.numbers))

