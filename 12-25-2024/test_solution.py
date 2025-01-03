import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution('test_input.txt')

    def test_solution(self):
        # Arrange
        expected = 3

        # Act
        actual = self.solution.solveP1()

        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()