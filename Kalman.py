import numpy as np

# Define the system dynamics and measurement functions
def f(x, u):
    """
    State transition function.
    :param x: State vector
    :param u: Control input vector
    :return: Predicted state vector
    """
    F = np.array([[1, 1], [0, 1]])  # State transition matrix
    return F @ x + u

def h(x):
    """
    Measurement function.
    :param x: State vector
    :return: Measurement vector
    """
    H = np.array([[1, 0]])  # Measurement matrix
    return H @ x

def jacobian_F(x, u):
    """
    Jacobian of the state transition function.
    :param x: State vector
    :param u: Control input vector
    :return: Jacobian matrix of the state transition function
    """
    return np.array([[1, 1], [0, 1]])

def jacobian_H(x):
    """
    Jacobian of the measurement function.
    :param x: State vector
    :return: Jacobian matrix of the measurement function
    """
    return np.array([[1, 0]])

# Define the EKF functions
def predict(x, P, u, Q):
    """
    Prediction step of the EKF.
    :param x: State vector
    :param P: Covariance matrix
    :param u: Control input vector
    :param Q: Process noise covariance matrix
    :return: Predicted state vector and covariance matrix
    """
    x_pred = f(x, u)
    F = jacobian_F(x, u)
    P_pred = F @ P @ F.T + Q
    return x_pred, P_pred

def update(x_pred, P_pred, z, R):
    """
    Update step of the EKF.
    :param x_pred: Predicted state vector
    :param P_pred: Predicted covariance matrix
    :param z: Measurement vector
    :param R: Measurement noise covariance matrix
    :return: Updated state vector and covariance matrix
    """
    H = jacobian_H(x_pred)
    y = z - h(x_pred)  # Measurement residual
    S = H @ P_pred @ H.T + R  # Residual covariance
    K = P_pred @ H.T @ np.linalg.inv(S)  # Kalman gain
    x_upd = x_pred + K @ y
    P_upd = (np.eye(len(x_pred)) - K @ H) @ P_pred
    return x_upd, P_upd

# Example usage
# Initial state and covariance
x = np.array([0, 1])  # Initial state vector [position, velocity]
P = np.eye(2)  # Initial covariance matrix

# Process and measurement noise covariances
Q = np.array([[1, 0], [0, 1]])  # Process noise covariance
R = np.array([[1]])  # Measurement noise covariance

# Control input
u = np.array([0, 0])  # No control input

# Simulated measurement
z = np.array([1])  # Example measurement

# Perform EKF
x_pred, P_pred = predict(x, P, u, Q)
x_upd, P_upd = update(x_pred, P_pred, z, R)

print("Predicted state:", x_pred)
print("Updated state:", x_upd)