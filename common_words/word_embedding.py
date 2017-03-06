import numpy as np

class WordEmbedding:
    def __init__(self, vector_file):
        self.entries = dict()
        with open(vector_file, 'r') as f:
            for line in f:
                entry = line.split()
                word = entry[0]
                vector = np.array([float(index) for index in entry[1:]])
                self.entries[word] = vector

    def __len__(self):
        return len(self.entries)

    def vocabulary(self):
        return self.entries.keys()

    def cosine_similarity(self, word1, word2):
        if word1 in self.entries and word2 in self.entries:
            vector1 = self.entries[word1]
            vector2 = self.entries[word2]
            norm1 = np.linalg.norm(vector1)
            norm2 = np.linalg.norm(vector2)
            dot_product = np.dot(vector1, vector2)
            return dot_product / (norm1 * norm2)
        else:
            raise KeyError('one of the requested words, {} or {}, \
                    is not in the embedding'.format(word1, word2))

