from nltk.tokenize import sent_tokenize, RegexpTokenizer
from common_words.word_embedding import WordEmbedding


class CommonWordTranslator:

    def __init__(self, common_words_file, word_embedding_file):
        self.lookup_cache = dict()
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.embedding = WordEmbedding(word_embedding_file)
        self.common_words = dict()
        with open(common_words_file, 'r') as f:
            for line in f:
                word = line.strip('\n').replace('.', '').lower()
                if word in self.embedding:
                    self.common_words[word] = self.embedding.find_vector(word)

    def translate(self, text):
        new_sentences = [self._check_sentence(sentence) for sentence in sent_tokenize(text)]
        replaced_count = sum([count for _, count, _ in new_sentences])
        processed_words = sum([count for _, _, count in new_sentences])
        translation = ' '.join([sentence for sentence, _, _ in new_sentences])
        return (translation, replaced_count, processed_words, len(new_sentences))

    def _check_sentence(self, sentence):
        last_character = sentence[-1]
        if not last_character.isalpha() and not last_character.isdigit():
            last_character = sentence[-1]
        else:
            last_character = ''
        norm_sentence = self.tokenizer.tokenize(sentence)
        new_words = [self._check_replacement(word) for word in norm_sentence]
        replaced_count = sum([replaced for _, replaced in new_words])
        new_sentence = ' '.join([word for word, _ in new_words])
        return (new_sentence + last_character, replaced_count, len(new_words))

    def _check_replacement(self, word):
        norm_word = word.lower()
        if norm_word in self.lookup_cache:
            if word[0].isupper():
                return (self.lookup_cache[norm_word].title(), 1)
            else:
                return (self.lookup_cache[norm_word], 1)
        elif norm_word in self.embedding and norm_word not in self.common_words:
            word_vector = self.embedding.find_vector(norm_word)
            nearest_neighbor = (None, 0)
            for common_word, common_vector in self.common_words.items():
                score = self.embedding.cosine_similarity(word_vector, 
                                                         common_vector)
                if score > nearest_neighbor[1]:
                    nearest_neighbor = (common_word, score)
            self.lookup_cache[norm_word] = nearest_neighbor[0]
            if word[0].isupper():
                return (nearest_neighbor[0].title(), 1)
            else:
                return (nearest_neighbor[0], 1)
        else:
            return (word, 0)
