from datasets import load_dataset
from transformers import DefaultDataCollator, TFDeiTModel#TFAutoModelForImageClassification, TFResNetForImageClassification
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np


def convert_to_tf_tensor(image):
    np_image = np.array(image)
    tf_image = tf.convert_to_tensor(np_image)
    tf_image = data_augmentation(tf_image)
    tf_image = tf.transpose(tf_image)
    return tf_image

def preprocess_data(batch):
    batch["pixel_values"] = [convert_to_tf_tensor(image.convert("RGB")) for image in batch["image"]]
    return batch

batch_size = 16
num_epochs = 3
test_split = 0.2
data_collator = DefaultDataCollator(return_tensors="tf")
model_name = "bert-base-uncased"

ds = load_dataset("mnist", split="train[:500]")
ds = ds.train_test_split(test_size=test_split)

id2label, label2id = {}, {}
for i in range(10):
    id2label[str(i)] = str(i)
    label2id[str(i)] = str(i)

data_augmentation = keras.Sequential(
    [
        layers.RandomCrop(28, 28),
        layers.Rescaling(scale=1.0/255)
    ]
)

ds["train"].set_transform(preprocess_data)
ds["test"].set_transform(preprocess_data)

train_dataset = ds["train"].to_tf_dataset(
    columns="pixel_values", label_cols="label", batch_size=batch_size, collate_fn=data_collator
)
test_dataset = ds["test"].to_tf_dataset(
    columns="pixel_values", label_cols="label", batch_size=batch_size, collate_fn=data_collator
)

loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model = TFDeiTModel.from_pretrained(model_name, id2label=id2label, label2id=label2id)
model.compile(optimizer="adam", loss=loss, metrics=['accuracy'])
hist = model.fit(train_dataset, epochs=num_epochs)
model.save("digit_rec")

score = model.evaluate(test_dataset)
print(hist.history)
print("Accuracy: {}%".format(round(score[1]*100, 2)))
print("Loss: {}%".format(round(score[0]*100, 2)))

print(train_dataset[0])