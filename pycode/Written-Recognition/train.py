import tensorflow as tf
# Note: tensorflow version greater than 2.10.1 is incompatible with windows

EPOCHS = 3

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1).reshape(x_train.shape[0], 28, 28, 1)
x_test = tf.keras.utils.normalize(x_test, axis=1).reshape(x_test.shape[0], 28, 28, 1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(28, 28, 1)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Dropout(0.1))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs = EPOCHS)

score = model.evaluate(x_test, y_test)
print("Accuracy: {}%".format(round(score[1]*100, 2)))
print("Loss: {}%".format(round(score[0]*100, 2)))

model.save("digit_rec")