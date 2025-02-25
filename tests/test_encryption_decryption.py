import myencryption.encryption as enc
import unittest

encoder_str = enc.encoder_str


class TestEncryption(unittest.TestCase):

    def testTextEncoding(self):
        message = "HALLO123_"
        result = enc.textEncoding(message, encoder_str)
        expected = [
            17,
            10,
            21,
            21,
            24,
            1,
            2,
            3,
            40,
        ]
        self.assertListEqual(result, expected)

    def testCreateKeys(self):
        encoded_message = [
            17,
            10,
            21,
            21,
            24,
            1,
            2,
            3,
            40,
        ]

        result = enc.createKeys(encoded_message)

        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], list)
        self.assertIsInstance(result[1], list)
        self.assertEqual(len(result[0]), 9)
        self.assertEqual(len(result[1]), 9)

    def testDecryptmessage(self):
        key1 = [13, 4, 15, 10, 8, 0, 2, 3, 14]
        key2 = [4, 6, 6, 11, 16, 1, 0, 0, 26]
        expected = "HALLO123_"
        result = enc.decryptMessage(encoder_str, key1, key2)
        self.assertEqual(expected, result)
