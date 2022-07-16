import unittest

from str_linked_list import LinkedList, LinkedListNode


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.numbers = LinkedList()

    def test_empty_list_and_raises_stop_iteration(self):
        """check for empty list and stop iteration"""

        iterator = iter(self.numbers)
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_one_element_in_list_and_return_element_and_stopiter(self):
        """checking a list of one element"""

        self.numbers._head = LinkedListNode(1)
        iterator = iter(self.numbers)
        self.assertEqual(1, next(iterator))
        with self.assertRaises(StopIteration):
            next(iterator)
            
    def test_two_elements_in_list_and_return_elements_and_stopiter(self):
        """checking a list of two elements"""

        self.numbers._head = LinkedListNode(1, LinkedListNode(5))
        iterator = iter(self.numbers)
        self.assertEqual(1, next(iterator))
        self.assertEqual(5, next(iterator))
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_index_out_of_range_get_raises_index_error(self):
        """correct error handling if the index is out of range"""

        with self.assertRaises(IndexError):
            self.numbers.get(1)

    def test_valid_index_get_returns_correct_element(self):
        """checking to get the correct element by index"""

        self.numbers._head = LinkedListNode(1, LinkedListNode(3))

        self.assertEqual(3, self.numbers.get(1))


    def test_insert_by_index(self):
        """testing element insertion by index"""

        self.numbers.append(3)
        self.numbers.append(8)
        self.numbers.append(81)
        self.numbers.insert(3, 2)

        self.assertEqual(3, self.numbers.get(2))


    def test_delete_item_by_index(self):
        """testing the correct removal of an element from the list by index"""

        self.numbers.append(3)
        self.numbers.append(8)
        self.numbers.append(81)
        self.numbers.delete(0)
        self.numbers.delete(1)

        self.assertNotIn(3, self.numbers)
        self.assertNotIn(81, self.numbers)

    def test_append_element(self):
        """testing adding an element to the end of the list"""

        self.numbers.append(18)
        self.numbers.append(61)
        self.numbers.append(22)

        self.assertEqual((18, 61, 22), tuple(self.numbers))

    def test_lenght_list_returns_correct_value(self):
        """checking the length of a list and returning the correct number"""

        self.numbers.append(32)
        self.numbers.append(18)
        self.numbers.append(61)
        self.numbers.append(22)

        self.assertEqual(4, len(self.numbers))

    def test_insert_element_out_of_range(self):
        """Inserting an element at position index. If the index position is greater
        than the length of the list, the element will be added to the end of this list"""

        self.numbers.append(11)
        self.numbers.append(57)
        self.numbers.append(80)
        self.numbers.insert(9, 10)

        self.assertEqual((11, 57, 80, 9), tuple(self.numbers))



if __name__ == '__main__':
    unittest.main()