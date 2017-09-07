import pandas as pd
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.preprocessing.text import text_to_word_sequence

word_dict = imdb.get_word_index()

def encode_sentence(text):
    result = []
    arr = text_to_word_sequence(text, lower=True, split=" ")
    for word in arr:
        w = encode_word(word)
        if w is not None:
            result.append(w)
    return result


def encode_word(word):
    if word not in word_dict:
        return None
    return word_dict[word]


def build_dataset(max_len):
    df = pd.read_csv("data/twitter.csv", delimiter=",", names=["y", "X"], usecols=[1,3], header=None, nrows=6000)
    Xts = df["X"].values
    arr = []
    for text in Xts:
        arr.append(encode_sentence(text))
    X = sequence.pad_sequences(arr, maxlen=max_len)
    y = df["y"].values
    return (X, y)
