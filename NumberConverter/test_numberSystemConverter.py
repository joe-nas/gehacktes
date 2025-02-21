import unittest
import recursiveNumberSystemConverter as nsc


hexLookUpDict = nsc.hexLookUpDict


class TestRecursiveFromBaseToDecimalConversion(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_recursiveFromBaseToDecimalConversion(self):

        self.assertEqual(nsc.recursiveFromBaseToDecimalConversion("110011", 2, 0), 51)
        self.assertEqual(nsc.recursiveFromBaseToDecimalConversion("ZA7", 36, 0), 45727)

    def test_recursiveFromDecimalToBase(self):

        self.assertEqual(nsc.recursiveFromDecimalToBase(212, 2, []), 11010100)
        self.assertEqual(nsc.recursiveFromDecimalToBase(255, 2, []), 11111111)

    def test_combinedRecursiveConversion(self):
        self.assertEqual(nsc.combinedRecursiveConversion())
