import unittest
from converter import convert

class TestConvert(unittest.TestCase):
    def test_wrong_path(self):
        """
        Test if converter raise exception when the input path does not exist
        """
        with self.assertRaises(ValueError):
            convert("thisPathDoesNotExist", "tests/output.jpg")
    
    def test_not_file(self):
        """
        Test if converter raise exception if the input path is not a file
        """
        with self.assertRaises(ValueError):
            convert("tests/testC.CR2", "tests/output.jpg")
    
    def test_incorrect_extension(self):
        """
        Test if the converter raise error if input or output file doesn't have a the correct extension
        """
        with self.assertRaises(ValueError):  # Incorrect input extension
            convert("tests/testB.png", "tests/output.jpg")

        with self.assertRaises(ValueError):  # Incorrect output extension
            convert("tests/testA.CR2", "tests/output.exe")

    def test_conversion(self):
        """
        Test if the converter return the correct path after a valid conversion
        """
        out = "tests/temp/output.jpg"
        self.assertEqual(convert("tests/testA.CR2", out), out)  # Return the output path


if __name__ == "__main__":
    unittest.main()