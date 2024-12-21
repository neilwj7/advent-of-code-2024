import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution('test_input.txt', 11, 7)

    def test_solution(self):
        # Arrange
        expected = 12

        # Act
        actual = self.solution.solveP2()

        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
