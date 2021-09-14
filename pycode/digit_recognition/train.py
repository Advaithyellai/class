from tensorflow.keras.utils import to_categorical
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
import numpy as np
from sklearn.metrics import classification_report
from datetime import datetime

(x_train, y_train), (x_test, y_test) = mnist.load_data()

NUMBER_OF_EPOCHS = 3

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

model = Sequential()

print("Successfully created a new model.")
print("Now Training the model\n")

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(64, (3, 3), activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(81, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(10, activation='sigmoid'))

print("Starting the training process. This might take a few minutes\n")
start_time = datetime.now()

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])
hist = model.fit(x_train, y_train, epochs=NUMBER_OF_EPOCHS, validation_data=(x_test, y_test))

end_time = datetime.now()
diff = end_time-start_time

print("\nDone with the training process")
print("Time taken to train: {} minutes, {} seconds".format(diff.seconds//60, diff.seconds%60))
print("Accuracy of model: {}%".format(round(hist.history['accuracy'][0]*100, 2)))

model.save("digit_rec_model")

print("\nModel successfully saved")