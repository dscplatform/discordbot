from keras.preprocessing import sequence
from keras.models import load_model
from data import encode_sentence
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Parameters
version = 3
review_len = 128

# Model
model = load_model(("export/mdl_v%d.h5")%(version))

def encode_batch(arr):
    result = []
    for sentence in arr:
        result.append(encode_sentence(sentence))
    return sequence.pad_sequences(result, maxlen=review_len)

def predict_batch(arr):
    batch = encode_batch(arr)
    result = model.predict(batch, batch_size=len(batch), verbose=0)
    return result

print(predict_batch([
"good",
"this was the best thing ever",
"bad",
"such a horrible judgement",
"nice"
]))
