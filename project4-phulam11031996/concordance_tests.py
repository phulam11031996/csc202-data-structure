import unittest

from concordance import (
    build_stop_words_table, build_concordance_table,
    djbx33a, write_concordance_table
    )


class Tests(unittest.TestCase):
    def test_file1(self) -> None:
        stop_words = build_stop_words_table("text_files/stop_words.txt")
        concordance_table = build_concordance_table(
            "text_files/file1.txt", stop_words)
        write_concordance_table("text_files/file1_con.txt", concordance_table)

        with open('text_files/file1_con.txt') as student_out, \
             open('text_files/file1_sol.txt') as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_file2(self) -> None:
        stop_words = build_stop_words_table("text_files/stop_words.txt")
        concordance_table = build_concordance_table(
            "text_files/file2.txt", stop_words)
        write_concordance_table("text_files/file2_con.txt", concordance_table)

        with open('text_files/file2_con.txt') as student_out, \
             open('text_files/file2_sol.txt') as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_declaration(self) -> None:
        stop_words = build_stop_words_table("text_files/stop_words.txt")
        concordance_table = build_concordance_table(
            "text_files/declaration.txt", stop_words)
        write_concordance_table(
            "text_files/declaration_con.txt", concordance_table)

        with open('text_files/declaration_con.txt') as student_out, \
             open('text_files/declaration_sol.txt') as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    # djbx33a
    def test_djbx33a(self) -> None:
        self.assertEqual(djbx33a('a'), 177670)


if __name__ == '__main__':
    unittest.main()
