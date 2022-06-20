import unittest
# from unittest import result

from exp_eval import postfix_eval, infix_to_postfix

from array_stack import empty_stack, push, pop, peek, is_empty, size


class Tests(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval('1 2 +'), 3)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix('1 + 2'), '1 2 +')

    # TODO: add more tests!

    def test_all(self):
        infix_cases = [
            '( ( 5 - 3 ) ** 2 + ( 4 - 2 ) ** 2 ) ** ( 1 / 2 )',
            '( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )',
            '10 + 3 * 5 / ( 16 - 4 )',
            '5 * 3 ** ( 4 - 2 )',
            '( ( 1 * 2 ) + ( 3 / 4 ) )',
            '( ( 2 * ( 3 + 4 ) ) / 5 )',
            '( 3 * ( 4 + 6 / 3 ) )',
            '3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3',
            '12.0',
            '1',
            '5 // 7'
        ]
        postfix_cases = [
            '5 3 - 2 ** 4 2 - 2 ** + 1 2 / **',
            '15 7 1 1 + - / 3 * 2 1 1 + + -',
            '10 3 5 * 16 4 - / +',
            '5 3 4 2 - ** *',
            '1 2 * 3 4 / +',
            '2 3 4 + * 5 /',
            '3 4 6 3 / + *',
            '3 4 2 * 1 5 - 2 3 ** ** / +',
            '12.0',
            '1',
            '5 7 //'
        ]

        result_eval = [2.8284271, 5.0, 11.25, 45, 2.75, 2.8, 18.0, 3.00012207,
                       12.0, 1.0, 0.0]

        for idx in range(len(infix_cases)):
            get_postfix = infix_to_postfix(infix_cases[idx])
            self.assertEqual(get_postfix, postfix_cases[idx])
            self.assertAlmostEqual(postfix_eval(get_postfix), result_eval[idx])

    def test_postfix_bad_input(self):
        postfix_cases = [
            '2 a +',
            '2 +',
            '2 3 4 +',
            ''
        ]

        for idx in range(len(postfix_cases)):
            with self.assertRaises(ValueError):
                postfix_eval(postfix_cases[idx])

        with self.assertRaises(ZeroDivisionError):
            postfix_eval('1 0 /')

    def test_array_stack(self):
        test_array = empty_stack()

        with self.assertRaises(IndexError):
            peek(test_array)

        with self.assertRaises(IndexError):
            pop(test_array)

        push(test_array, 1)
        push(test_array, 2)
        push(test_array, 3)

        self.assertEqual(pop(test_array), 3)
        self.assertEqual(size(test_array), 2)
        self.assertEqual(peek(test_array), 2)
        self.assertFalse(is_empty(test_array))


if __name__ == '__main__':
    unittest.main()
