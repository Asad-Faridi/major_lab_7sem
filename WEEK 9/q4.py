import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# 1. Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 2. Normalize data
X_train = X_train / 255.0
X_test = X_test / 255.0

# Use a smaller dataset for faster comparison
X_train = X_train[:10000]
y_train = y_train[:10000]
X_test = X_test[:2000]
y_test = y_test[:2000]

# 3. Define activation functions
activations = ['sigmoid', 'tanh', 'relu']

results = {}

# 4. Train model with each activation function
for activation in activations:

    print("\nTraining with activation:", activation)

    model = Sequential([
        Flatten(input_shape=(28, 28)),
        Dense(128, activation=activation),
        Dense(64, activation=activation),
        Dense(10, activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    history = model.fit(
        X_train, y_train,
        epochs=5,
        batch_size=32,
        validation_split=0.1,
        verbose=1
    )

    # Evaluate model
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

    results[activation] = {
        'accuracy': accuracy,
        'loss': loss,
        'history': history
    }

    print("Test Accuracy:", accuracy)
    print("Test Loss:", loss)

# 5. Compare accuracy
print("\nActivation Function Comparison")

for activation in activations:
    print(
        activation,
        "Accuracy:", results[activation]['accuracy'],
        "Loss:", results[activation]['loss']
    )

# 6. Plot training accuracy
for activation in activations:
    plt.plot(
        results[activation]['history'].history['accuracy'],
        label=activation
    )

plt.title("Training Accuracy Comparison")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# 7. Plot training loss
for activation in activations:
    plt.plot(
        results[activation]['history'].history['loss'],
        label=activation
    )

plt.title("Training Loss Comparison")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()