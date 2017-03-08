import unittest
from common_words.word_embedding import WordEmbedding


class WordEmbeddingTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.embedding = WordEmbedding('data/text9.vec')

    def test_length(self):
        self.assertEqual(218316, len(self.embedding))

    def test_vocabulary(self):
        self.assertEqual(218316, len(self.embedding.vocabulary()))
        for word in self.embedding.vocabulary():
            self.assertTrue(word is not None)

    def test_find_word_vector(self):
        self.assertIsNot(None, self.embedding.find_vector('hello'))
        self.assertIs(None, self.embedding.find_vector('supercalifragic'))

    def test_cosine_similarity(self):
        vector1 = self.embedding.find_vector('hello')
        vector2 = self.embedding.find_vector('world')
        self.assertAlmostEqual(1.0, self.embedding.cosine_similarity(vector1, vector1), 2)
        different_similarity = self.embedding.cosine_similarity(vector1, vector2)
        self.assertTrue(different_similarity > 0.0 and different_similarity < 1.0)

    def test_word_similarity(self):
        self.assertAlmostEqual(1.0, self.embedding.word_similarity('hello', 'hello'), 2)
        different_similarity = self.embedding.word_similarity('hello', 'world')
        self.assertTrue(different_similarity > 0.0 and different_similarity < 1.0)

    def test_find_k_nearest_neighbors(self):
        knn = self.embedding.find_k_nearest_neighbors('meth', 10)
        self.assertEqual(10, len(knn))
        for word, score in knn:
            self.assertNotEqual('meth', word)
            self.assertTrue(score > 0.8)
