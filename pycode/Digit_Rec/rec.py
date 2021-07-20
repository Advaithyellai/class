from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

EPOCHS = 3
MODELS = ["cnn", "nn"]
MODEL = "cnn"
INPUT_SHAPE = x_train.shape[1]

model = Sequential()

if MODEL == "nn":
    
    model.add(Dense(32, input_shape=(INPUT_SHAPE,), activation='relu'))
    model.add(Dropout(0.2))

    model.add(Dense(16, activation='relu'))
    model.add(Dropout(0.2))

    model.add(Dense(8, activation='relu'))
    model.add(Dropout(0.2))

    model.add(Dense(units=1, activation="sigmoid"))

else:
    
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
    
    model.add(Conv2D(64, (3, 3), activation='relu'))
    
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    # model.add(Flatten())

    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))

    model.add(Dense(10, activation='softmax'))

model.compile(optimizer='Adadelta', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs= EPOCHS)

print(history.history['accuracy'])

print(model.evaluate(x_test, y_test))