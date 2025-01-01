import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution('test_input.txt')

    def test_solution(self):
        # Arrange
        expected = ['co', 'de', 'ka', 'ta']

        # Act
        actual = self.solution.solveP2()

        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
