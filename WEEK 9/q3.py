import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# 1. Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 2. Normalize pixel values (0-255 to 0-1)
X_train = X_train / 255.0
X_test = X_test / 255.0

# 3. Convert labels into categorical format
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 4. Create Neural Network model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# 5. Compile the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 6. Train the model
model.fit(
    X_train, y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1
)

# 7. Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)

print("Test Accuracy:", accuracy)

# 8. Make predictions
predictions = model.predict(X_test)

# 9. Display predicted digit
for i in range(5):
    predicted_digit = np.argmax(predictions[i])
    actual_digit = np.argmax(y_test[i])

    print("Actual Digit:", actual_digit)
    print("Predicted Digit:", predicted_digit)

    plt.imshow(X_test[i], cmap='gray')
    plt.title(f"Predicted: {predicted_digit}")
    plt.axis('off')
    plt.show()