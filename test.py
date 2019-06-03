#!/usr/bin/env python3
"""
name: test.py
description: tests for FileSearch Class
author: Eric Mattison
date: 2019-06-03
"""
import unittest
from main import FileSearch

class TestFileSearch(unittest.TestCase):
    def setUp(self):
        self.fs = FileSearch()

    def test_boring_search(self):
        self.fs.dir_path = "./sample/"
        self.fs.search_pattern = "ir"
        self.fs.options.update({'ignore_case': True})
        self.assertEqual(self.fs.boring_search(), [2, 2])
        self.fs.options.update({'ignore_case': False})
        self.assertEqual(self.fs.boring_search(), [1, 3])
        self.fs.search_pattern = "r"
        self.assertEqual(self.fs.boring_search(), [3, 1])
        self.fs.search_pattern = "BongoBoy"
        self.assertEqual(self.fs.boring_search(), [0, 4])

if __name__ == "__main__":
    unittest.main()