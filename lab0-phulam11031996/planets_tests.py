import io
import sys
import unittest
from unittest.mock import patch

import planets

# NOTE: This is what the output should look like.
PLANET_FMT = (
    'What do you weigh on Earth? \n'
    'On Mercury you would weigh {mercury_weight} pounds.\n'
    'On Jupiter you would weigh {jupiter_weight} pounds.\n'
)


class Tests(unittest.TestCase):
    def run_planets(self, weight, expected_output):
        '''Tests the behavior of the main in the planets module.

        Asserts that the main in the planets module produced the
        expected output when given the specified weight as input.

        Args:
            weight: a string containing a weight in pounds
            expected_output: a string containing what the main in
                planets should print given the specified weight
        '''
        stdin = io.StringIO(weight)
        stdout = io.StringIO()

        with patch.multiple(sys, stdin=stdin, stdout=stdout):
            planets.main()

        self.assertEqual(stdout.getvalue(), expected_output)

    # NOTE: Test functions must start with 'test'
    def test_planets_01(self):
        self.run_planets(
            '136',
            PLANET_FMT.format(mercury_weight='51.68', jupiter_weight='344.08')
        )

    def test_planets_02(self):
        self.run_planets(
            '100',
            PLANET_FMT.format(mercury_weight='38.00', jupiter_weight='253.00')
        )

    def test_planets_03(self):
        self.run_planets(
            '167.8',
            PLANET_FMT.format(mercury_weight='63.76', jupiter_weight='424.53')
        )


# NOTE: This runs the tests when you run the code (but not if you import
# this code).
if __name__ == '__main__':
    unittest.main()
