# python
# acquire MNIST data
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# reshape data for an MLP input
train_images = np.reshape(train_images, (-1, 784))
test_images = np.reshape(test_images, (-1, 784))

# normalize data
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# convert labels to a one-hot vector
from tensorflow.keras.utils import to_categorical

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# define network architecture
MLP = Sequential()
MLP.add(InputLayer(input_shape=(784, ))) # input layer
MLP.add(Dense(256, activation='relu')) # hidden layer 1
MLP.add(Dense(256, activation='relu')) # hidden layer 2
MLP.add(Dense(10, activation='softmax')) # output layer

# summary
MLP.summary()

# optimization
MLP.compile(loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])

# train (fit)
MLP.fit(train_images, train_labels, 
        epochs=20, batch_size=128)

# evaluate performance
test_loss, test_acc = MLP.evaluate(test_images, test_labels,
                                   batch_size=128,
                                   verbose=0)
print("Test loss:", test_loss)
print("Test accuracy:", test_acc)

# make a prediction
print("Prediction for 4")
digit = test_images[4]

digit = np.reshape(digit, (-1, 784))
digit = digit.astype('float32') / 255

MLP.predict(digit, verbose=0)
print(np.argmax(MLP.predict(digit, verbose=0)))