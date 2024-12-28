import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution(7, 'test_input.txt')

    def test_solution(self):
        # Arrange
        expected = 22

        # Act
        actual = self.solution.solveP1(12)

        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
