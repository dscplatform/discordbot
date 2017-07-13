import numpy as np
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.callbacks import EarlyStopping
from model import build_model
from data import build_dataset
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Parameters
version = 3
words = 10000
review_len = 128
vec_len = 300
patience = 5
batch_size = 1
epochs = 30

# Load data
X, y = build_dataset(review_len)

# Build model
model = build_model(words, vec_len, review_len)

# Early stopping
early_stopping_monitor = EarlyStopping(patience=patience, monitor="loss", mode="auto")

# Fit model
model.fit(X, y, epochs=epochs, callbacks=[early_stopping_monitor], batch_size=batch_size, verbose=1, validation_split=0.25)

# Export
model.save(("export/mdl_v%d.h5")%(version))
print("Model successfully exported!")
