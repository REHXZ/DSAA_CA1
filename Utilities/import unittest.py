import unittest
from utility import Utility

class TestUtility(unittest.TestCase):
    def test_check_file_type_valid_files(self):
        self.assertFalse(Utility.CheckFileType("file1.txt", "file2.txt"))

    def test_check_file_type_invalid_files(self):
        self.assertTrue(Utility.CheckFileType("file1.txt", "file3.txt"))

    def test_check_file_type_missing_file(self):
        self.assertTrue(Utility.CheckFileType("file1.txt", "file4.txt"))

if __name__ == '__main__':
    unittest.main()