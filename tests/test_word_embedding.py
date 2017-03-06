import unittest
from common_words.word_embedding import WordEmbedding

class WordEmbeddingTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.embedding = WordEmbedding('data/text9.vec')

    def test_length(self):
        self.assertEqual(218317, len(self.embedding))

    def test_vocabulary(self):
        self.assertEqual(218317, len(self.embedding.vocabulary()))
        for word in self.embedding.vocabulary():
            self.assertTrue(word is not None)

    def test_cosine_similarity(self):
        self.assertAlmostEqual(1.0, self.embedding.cosine_similarity('hello', 'hello'), 2)
        different_similarity = self.embedding.cosine_similarity('hello', 'world')
        self.assertTrue(different_similarity > 0.0 and different_similarity < 1.0)

