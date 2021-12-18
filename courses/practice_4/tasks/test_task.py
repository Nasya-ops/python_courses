import unittest
from practice_4.tasks.sorting_task import dict_to_result, purchase_settings, result


class TestHello(unittest.TestCase):

    def test_result(self):
        self.assertEqual(dict_to_result(purchase_settings), result)


if __name__ == '__main__':
    unittest.main()



