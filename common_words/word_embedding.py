import numpy as np
from heapq import heappush, heapreplace


class WordEmbedding:

    def __init__(self, vector_file, vector_length=100):
        self.entries = dict()
        with open(vector_file, 'r') as f:
            for line in f:
                entry = line.split()
                word = entry[0]
                vector = [float(index) for index in entry[1:]]
                if len(vector) == vector_length:
                    vector_array = np.array(vector)
                    self.entries[word] = vector_array

    def __len__(self):
        return len(self.entries)

    def __contains__(self, key):
        return key in self.entries

    def vocabulary(self):
        return self.entries.keys()

    def find_vector(self, word, default=None):
        return self.entries.get(word, default)

    def cosine_similarity(self, vector1, vector2):
        norm1 = np.linalg.norm(vector1)
        norm2 = np.linalg.norm(vector2)
        dot_product = np.dot(vector1, vector2)
        return dot_product / (norm1 * norm2)

    def word_similarity(self, word1, word2):
        if word1 in self.entries and word2 in self.entries:
            vector1 = self.entries[word1]
            vector2 = self.entries[word2]
            return self.cosine_similarity(vector1, vector2)
        else:
            raise KeyError('one of the requested words, {} or {}, \
                    is not in the embedding'.format(word1, word2))

    def find_k_nearest_neighbors(self, word, k=10):
        if word in self.entries:
            word_vector = self.entries[word]
            knn = []
            for other_word, other_vector in self.entries.items():
                if other_word != word:
                    score = self.cosine_similarity(word_vector, other_vector)
                    if len(knn) >= k and score > knn[0][0]:
                        heapreplace(knn, (score, other_word))
                    elif len(knn) < k:
                        heappush(knn, (score, other_word))
            return [(w, s) for s, w in knn]
        else:
            raise KeyError('{} is not in the embedding'.format(word))
