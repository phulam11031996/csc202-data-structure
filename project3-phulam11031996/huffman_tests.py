import unittest
import subprocess

# NOTE: Do not import anything else from huffman.  If you do, your tests
# will crash when I test them.  You shouldn't need to test your helper
# functions directly, just via testing the required functions.
from huffman import (
    HuffmanNode, count_frequencies, build_huffman_tree, create_codes,
    create_header, huffman_encode, parse_header, huffman_decode)


class TestList(unittest.TestCase):
    # ########################## PROJECT 3A BEGINS ########################## #
    # frequencies()
    def test_count_frequencies_01(self):
        frequencies = count_frequencies("text_files/file2.txt")
        expected = [0, 2, 4, 8, 16, 0, 2, 0]

        self.assertEqual(frequencies[96:104], expected)

        frequencies_empty = count_frequencies("text_files/empty_file.txt")
        self.assertEqual(frequencies_empty, [0] * 256)

    # __lt__()
    def test_node_lt_01(self):
        node1 = HuffmanNode(97, 10)
        node2 = HuffmanNode(65, 20)
        node3 = HuffmanNode(65, 10)
        node4 = HuffmanNode(97, 10)

        self.assertLess(node1, node2)
        self.assertGreater(node2, node1)
        self.assertLess(node3, node4)
        self.assertGreater(node4, node3)

    # __eq__()
    def test_eq_01(self):
        node1 = HuffmanNode(97, 10)
        node2 = HuffmanNode(65, 20)
        node3 = HuffmanNode(65, 20)

        self.assertEqual(node2, node3)
        self.assertNotEqual(node1, node2)

    # build_huffman_tree()
    def test_build_huffman_tree_01(self):
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10
        fre_zero = [0] * 256
        self.assertEqual(build_huffman_tree(fre_zero), None)  # empty edge case

        huffman_tree = build_huffman_tree(frequencies)

        # NOTE: This also requires a working __eq__ for your HuffmanNode
        self.assertEqual(
            huffman_tree,
            HuffmanNode(97, 15, HuffmanNode(97, 5), HuffmanNode(98, 10))
        )

        frequencies_aaa = [0] * 256  # aaa edge case
        frequencies_aaa[97] = 3
        huffman_tree_aaa = build_huffman_tree(frequencies_aaa)
        self.assertEqual(huffman_tree_aaa, HuffmanNode(97, 3))

    # create_codes()
    def test_create_codes_01(self):
        huffman_tree = HuffmanNode(
            97, 15,
            HuffmanNode(97, 5),
            HuffmanNode(98, 10)
        )

        codes = create_codes(huffman_tree)
        self.assertEqual(codes[ord('a')], '0')
        self.assertEqual(codes[ord('b')], '1')

        huffman_tree_aaa = HuffmanNode(97, 3)  # aaa edge case
        codes_aaa = create_codes(huffman_tree_aaa)
        self.assertEqual(codes_aaa[97], '')

        self.assertEqual(create_codes(None), [''] * 256)  # empty edge case

    # create_header()
    def test_create_header_01(self):
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10
        self.assertEqual(create_header(frequencies), "97 5 98 10")

        frequencies_aaa = [0] * 256  # aaa edge case
        frequencies_aaa[97] = 3
        self.assertEqual(create_header(frequencies_aaa), '97 3')

        frequencies_empty = [0] * 256  # empty edge case
        self.assertEqual(create_header(frequencies_empty), '')

    # huffman_encode() for file1.txt
    def test_huffman_encode_01(self):
        huffman_encode("text_files/file1.txt", "text_files/file1_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/file1_out.txt',
             'text_files/file1_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    # huffman_encode() for file2.txt
    def test_huffman_encode_02(self):
        huffman_encode("text_files/file2.txt", "text_files/file2_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/file2_out.txt',
             'text_files/file2_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    # huffman_encode() for multiline
    def test_huffman_encode_03(self):
        huffman_encode(
            "text_files/multiline.txt",
            "text_files/multiline_out.txt"
            )

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/multiline_out.txt',
             'text_files/multiline_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    # huffman_encode() for declaration.txt
    def test_huffman_encode_04(self):
        huffman_encode(
            "text_files/declaration.txt",
            "text_files/declaration_out.txt"
            )

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/declaration_out.txt',
             'text_files/declaration_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    # huffman_encode() for empty_file.txt
    def test_huffman_encode_05(self):
        huffman_encode(
            "text_files/empty_file.txt",
            "text_files/empty_file_out.txt"
            )

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/empty_file_out.txt',
             'text_files/empty_file_out.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    # ########################## PROJECT 3B BEGINS ########################## #
    # parse_header()
    def test_parse_header_01(self):
        header = "97 2 98 4 99 8 100 16 102 2\n"

        frequencies = parse_header(header)
        expected = [0, 2, 4, 8, 16, 0, 2, 0]

        self.assertEqual(frequencies[96:104], expected)

    # file1
    def test_huffman_decode_file1(self):
        huffman_decode(
            "text_files/file1_soln.txt",
            "text_files/file1_decoded.txt"
            )

        with open("text_files/file1_decoded.txt") as student_out, \
             open("text_files/file1.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    # file2
    def test_huffman_decode_file2(self):
        huffman_decode(
            "text_files/file2_soln.txt",
            "text_files/file2_decoded.txt"
            )

        with open("text_files/file2_decoded.txt") as student_out, \
             open("text_files/file2.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    # multiline
    def test_huffman_decode_multiline(self):
        huffman_decode(
            "text_files/multiline_soln.txt",
            "text_files/multiline_decoded.txt"
            )

        with open("text_files/multiline_decoded.txt") as student_out, \
             open("text_files/multiline.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    # empty
    def test_huffman_decode_empty_file(self):
        huffman_decode(
            "text_files/empty_file_out.txt",
            "text_files/empty_file_decoded.txt"
            )

        with open("text_files/empty_file_decoded.txt") as student_out, \
             open("text_files/empty_file.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    # declaration
    def test_huffman_decode_declaration(self):
        huffman_decode(
            "text_files/declaration_soln.txt",
            "text_files/declaration_decoded.txt"
            )

        with open("text_files/declaration_decoded.txt") as student_out, \
             open("text_files/declaration.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())


if __name__ == '__main__':
    unittest.main()
