import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution('test_input.txt')

    def test_solution(self):
        # Arrange
        expected = 1206

        # Act
        actual = self.solution.countFenceCostTotalP2()

        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
