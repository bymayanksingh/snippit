import unittest
from text_processor import generate_blobs

class TestTextProcessor(unittest.TestCase):

    def test_generate_blobs_single_blob(self):
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        expected_blobs = ["Lorem ipsum dolor sit amet consectetur adipiscing elit"]
        actual_blobs = generate_blobs(text)
        self.assertEqual(actual_blobs, expected_blobs)

    def test_generate_blobs_word_limit(self):
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id gravida ipsum."
        expected_blobs = ["Lorem ipsum dolor sit amet consectetur adipiscing elit", "Donec id gravida ipsum"]
        word_limit = 8
        actual_blobs = generate_blobs(text, word_limit=word_limit)
        self.assertEqual(actual_blobs, expected_blobs)


if __name__ == "__main__":
    unittest.main()