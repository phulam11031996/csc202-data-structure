import unittest

from perm_lex import perm_gen_lex


class Tests(unittest.TestCase):
    def test_perm_gen_lex_empty(self):
        self.assertEqual(perm_gen_lex(''), [''])

    def test_perm_gen_length_1(self):
        self.assertEqual(perm_gen_lex('a'), ['a'])

    # TODO: add more tests
    def test_perm_gen_lex1(self):
        self.assertEqual(perm_gen_lex('abcd'), [
                'abcd', 'abdc', 'acbd', 'acdb',
                'adbc', 'adcb', 'bacd', 'badc',
                'bcad', 'bcda', 'bdac', 'bdca',
                'cabd', 'cadb', 'cbad', 'cbda',
                'cdab', 'cdba', 'dabc', 'dacb',
                'dbac', 'dbca', 'dcab', 'dcba'
                ]
        )


if __name__ == '__main__':
    unittest.main()
