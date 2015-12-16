# -*- coding: utf-8 -*-
import os
import re
from enum import Enum


def read_all_in_lowercase(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text.decode("utf-8").lower().encode("utf-8")


def write_pairs_to_file(filename, pairs, nameinfile=None, rewrite=True):
    with open(filename, 'w' if rewrite else 'a') as f:
        if nameinfile:
            f.write(str(nameinfile) + os.linesep)
        for pair in pairs:
            f.write(";".join(map(str, pair)) + os.linesep)


class TypeNGram(Enum):
    UNIGRAMS = 1
    BIGRAMS = 2
    TRIGRAMS = 3

    def __str__(self):
        return self._name_


class NGrams(object):
    def __init__(self, words, type_ngram):
        self.__type = type_ngram
        self.__len_one_ngram = type_ngram.value
        self.freq_uniques = 0
        self.amount_ngrams = None
        self.__create_all_ngrams(words)

    def __create_all_ngrams(self, words):
        assert all(words), "Exist empty words"
        ngrams = {}
        amount_ngrams = 0
        index = 0
        for index in xrange(len(words) - self.__len_one_ngram):
            ngram = " ".join(words[index:index + self.__len_one_ngram])
            amount_ngrams += 1
            times = ngrams.get(ngram, 0)
            ngrams[ngram] = times + 1

        self.amount_ngrams = amount_ngrams
        self.freq_uniques = ngrams


class Text(object):
    @staticmethod
    def split_into_words(text):
        return text.split(" ")

    @staticmethod
    def strip_multiple_spaces(text):
        return re.sub('\s+', ' ', text).strip()

    @staticmethod
    def filter_text(text):
        text = unicode(text.decode("utf-8"))
        allowed_symbs_re = ur"[^абвгґдеєжзиіїйклмнопрстуфхцчшщьюя’'0123456789]"
        text = re.sub(allowed_symbs_re, " ", text)
        return text.encode('utf-8', 'ignore')
        # symbols_to_remove = string.punctuation + "\n\r\b\a"
        # table = string.maketrans(symbols_to_remove
        #    , len(symbols_to_remove) * " ")
        # return text.translate(None, "—…»«“”")

    def __init__(self, raw_text):
        super(Text, self).__init__()
        assert isinstance(raw_text, str), "Argument must be string"
        filtered_text = self.filter_text(raw_text)
        self.text = self.strip_multiple_spaces(filtered_text)
        self.words = self.split_into_words(self.text)
        self.amount_words = 0
        self.unique_words = None
        self.ngrams = {}

    def __eq__(self, other_text):
        print "call __eq__"
        return id(self) == id(other_text)

    def get_ngrams(self, type_ngram):
        assert isinstance(type_ngram, TypeNGram), "Invalid type of param"
        ngrams = self.ngrams.get(type_ngram)
        if ngrams is None:
            ngrams = NGrams(self.words, type_ngram)
            self.ngrams[type_ngram] = ngrams
        return ngrams

    def get_amount_ngrams(self, type_ngram):
        ngrams = self.get_ngrams(type_ngram)
        return ngrams.amount_ngrams

    def get_frequencies_unique_ngrams(self, type_ngram):
        ngrams = self.get_ngrams(type_ngram)
        return ngrams.freq_uniques


# from matplotlib import pyplot

# pyplot.plot([pair[1] for pair in pairs], 'ro')

# ax = pyplot.subplot()
# ax.set_yscale('log')
# ax.set_xscale('log')

# pyplot.show()
