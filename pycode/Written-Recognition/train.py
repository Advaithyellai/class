import tensorflow as tf
# Note: tensorflow version greater than 2.10.1 is incompatible with windows

EPOCHS = 3

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Rescaling(1./255, input_shape=(28, 28, 1)))
model.add(tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'))
model.add(tf.keras.layers.MaxPooling2D())
model.add(tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'))
model.add(tf.keras.layers.MaxPooling2D())
model.add(tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'))
model.add(tf.keras.layers.MaxPooling2D())
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation="softmax"))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
hist = model.fit(x_train, y_train, epochs = EPOCHS, validation_split=0.2)

score = model.evaluate(x_test, y_test)
print(hist.history)
print("Accuracy: {:.2%}".format(score[1]))
print("Loss: {:.2%}".format(score[0]))

model.save("digit_rec")