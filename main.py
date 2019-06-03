#!/usr/bin/env python3
"""
name: main.py
description: searches a directory for files that match a pattern
author: Eric Mattison
date: 2019-06-03
"""

import os
import glob
import argparse

class FileSearch:
    """
    Class for holding methods and properties of the file search
    """
    def __init__(self):
        self.dir_path = None
        self.search_pattern = None
        self.options = {}

    def set_args(self):
        """
        Use argparse to get the command line arguments and set the object's internal values
        :return:
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("search_dir", type=str, help="Path of the directory to search.  e.g. /home/vendetta/sample")
        parser.add_argument("search_pattern", type=str, help="Portion of the filename to be matched.  e.g. oo.py")
        parser.add_argument("--ignore-case", "-i", action="store_true", help="When set, search will match both upper"
                                                                             "and lowercase values.")
        args = parser.parse_args()
        self.dir_path = args.search_dir
        if not os.path.isdir(self.dir_path):
            #directory does not exist - error
            raise OSError(f"Error: The directory {self.dir_path} does not exist.")
        self.search_pattern = args.search_pattern
        self.options.update({'ignore_case': args.ignore_case})

    def boring_search(self):
        """
        glob does a good job of pattern matching for filenames - but it doesn't do case-insensitivity.  Otherwise, this
        would be trivial
        idea: get the full list of filenames using glob *
        if case-sensitive, use glob straight up
        otherwise, lcase the filename and use "in" (the poor man's regular expression)
        Actually, I just re-read the instructions.  Since I'm supposed to keep the code as consise as possible,
        I'm getting rid of the glob version, even though it's much more clever. (This function used to be called
        glob_search)
        :return: array of number of hits and number of misses
        """
        hits, misses = (0, 0)
        search_string = os.path.join(self.dir_path, "*")
        all_files = [ os.path.basename(filepath) for filepath in glob.glob(search_string)]
        if self.options.get('ignore_case'):
            #get just the filenames in lowercase
            all_files = [ filename.lower() for filename in all_files]
            #get the search pattern in lowercase
            self.search_pattern = self.search_pattern.lower()
        for filename in all_files:
            if self.search_pattern in filename:
                hits += 1
            else:
                misses += 1
        return [hits, misses]

if __name__ == "__main__":
    fs = FileSearch()
    fs.set_args()
    print(f"Searching {fs.dir_path} for files containing {fs.search_pattern}...")
    hits, misses = fs.boring_search()
    print(f"{hits} HIT and {misses} MISS")