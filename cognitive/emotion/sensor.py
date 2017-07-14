import asyncio
import dscframework
import codecs, json
from keras.preprocessing import sequence
from keras.models import load_model
from data import encode_sentence
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Parameters
version = 4
review_len = 128

# Model
model = load_model(("export/mdl_v%d.h5")%(version))

# Client
cli = dscframework.Client("ws://localhost:8080")

def encode_batch(arr):
    result = []
    for sentence in arr:
        result.append(encode_sentence(sentence))
    return sequence.pad_sequences(result, maxlen=review_len)

def predict_batch(arr):
    batch = encode_batch(arr)
    result = model.predict(batch, batch_size=len(batch), verbose=0)
    return result

async def on_message(head, data):
    print("Got input!", flush=True)
    arr = json.loads(data.decode("utf-8"))["list"]
    batch = predict_batch(arr).tolist()
    await cli.broadcast("sentiment", head, json.dumps(batch))

async def on_update():
    pass

async def on_connect(cli):
    await cli.subscribe("message", on_message)
    await cli.register("sentiment", {"output": {}, "input": {}}, on_update)
    print("Running Sentiment Sensor", flush=True)

async def main():
    await cli.start(on_connect)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
