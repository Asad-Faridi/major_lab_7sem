import numpy as np

# AND gate inputs and outputs
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

# Initialize random weights and bias
weights = np.random.rand(2) * 0.1
bias = np.random.rand(1)[0] * 0.1

# Activation function
def step_function(z):
    return 1 if z >= 0 else 0

# Learning parameters
learning_rate = 0.1
epochs = 20

# Training the perceptron
for epoch in range(epochs):
    for x, y_true in zip(X_and, y_and):

        # Calculate weighted sum
        z = np.dot(x, weights) + bias

        # Predict output
        prediction = step_function(z)

        # Calculate error
        error = y_true - prediction

        # Update weights and bias
        weights = weights + learning_rate * error * x
        bias = bias + learning_rate * error

# Test the perceptron
print("AND Gate Predictions:")

for x in X_and:
    z = np.dot(x, weights) + bias
    prediction = step_function(z)
    print(f"Input: {x}, Predicted Output: {prediction}")

print("\nFinal Weights:", weights)
print("Final Bias:", bias)