from unittest import TestCase
import task2


class TestTask2(TestCase):

    def test_sort(self):

        self.assertEqual(task2.sort(4256, 2147), (6542, 1247))
        self.assertEqual(task2.sort(784623, 361476), (876432, 134667))
        self.assertEqual(task2.sort(1, -26), (1, -62))

    def test_get_difference(self):

        self.assertEqual(task2.get_difference(401278136, 350120145), 776308655)
        self.assertEqual(task2.get_difference(871024, 369780), 567421)
        self.assertEqual(task2.get_difference(1, -1234), 4322)
