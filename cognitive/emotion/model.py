from keras.models import Sequential
from keras.layers import MaxPooling1D, Conv1D, Flatten, Dropout, Dense
from keras.layers.embeddings import Embedding


def build_model(words, vec_len, review_len):
    model = Sequential()
    model.add(Embedding(words, vec_len, input_length=review_len))
    model.add(Dropout(0.25))
    model.add(Conv1D(32, 3, padding="same"))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Conv1D(16, 3, padding="same"))
    model.add(Flatten())
    model.add(Dropout(0.25))
    model.add(Dense(100, activation="sigmoid"))
    model.add(Dropout(0.25))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.summary()
    return model
