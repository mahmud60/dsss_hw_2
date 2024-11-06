import unittest
from math_quiz import generate_random_integer, get_random_operator, generate_problem_and_answer


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Test if random operator returns one of the '+', '-', '*'
        for _ in range(10):  # Run multiple times to verify randomness
            operator = get_random_operator()
            self.assertIn(operator, ['+', '-', '*'])

    def test_generate_problem_and_answer(self):
        # test cases for different operators
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (6, 4, '*', '6 * 4', 24)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            if expected_problem == 'Invalid':
                with self.assertRaises(ValueError):
                    generate_problem_and_answer(num1, num2, operator)
            else:
                problem, answer = generate_problem_and_answer(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
