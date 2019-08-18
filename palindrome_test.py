# -*- coding: utf-8 -*-
import unittest

from palindrome import PalindromeChecker

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class PalindromeTest(unittest.TestCase):
    def setUp(self):
        self.palindrome_checker = PalindromeChecker()

    #it's not good practice to unit test private methods but as a python newbie I want to be sure I understand this particular one
    def test_reverse_string(self):
        self.assertEqual(self.palindrome_checker._PalindromeChecker__reverse_string("abc"), "cba")

    def test_empty_string(self):
        self.assertFalse(self.palindrome_checker.is_palindrome(""))

    def test_single_char(self):
        self.assertTrue(self.palindrome_checker.is_palindrome("a"))

    def test_simple(self):
        self.assertTrue(self.palindrome_checker.is_palindrome("tacocat"))

    def test_numbers(self):
        self.assertTrue(self.palindrome_checker.is_palindrome("10801"))

    def test_white_space(self):
        self.assertTrue(self.palindrome_checker.is_palindrome("taco cat"))

    def test_capitals(self):
        self.assertTrue(self.palindrome_checker.is_palindrome("Taco cat"))

    def test_punctuation(self):
        self.assertTrue(self.palindrome_checker.is_palindrome("A man, a plan, a canal, Panama!"))

    def test_quotes(self):
        self.assertTrue(self.palindrome_checker.is_palindrome("No 'x' in Nixon."))

    def test_multiline(self):
        quote = """A man, 
                a plan, 
                a canal, 
                Panama!"""
        self.assertTrue(self.palindrome_checker.is_palindrome(quote))
    
    def test_emoji(self):
        self.assertTrue(self.palindrome_checker.is_palindrome("🐱 Taco cat 🐱"))

if __name__ == "__main__":
    unittest.main()
