# This code snipped must be run from a python file to visualize Bloch sphere in an interactive 3D manner
import numpy as np
from qutip import Bloch, Qobj
import matplotlib.pyplot as plt

# Function to normalize the state
def normalize_state(alpha, beta):
    norm = np.sqrt(np.abs(alpha)**2 + np.abs(beta)**2)
    return alpha / norm, beta / norm

# Function to visualize the qubit on the Bloch sphere using Matplotlib
def plot_bloch_sphere(alpha, beta):
    # Normalize the coefficients
    alpha, beta = normalize_state(alpha, beta)

    # Create a Qobj representing the quantum state
    state = Qobj([[alpha], [beta]])

    # Initialize the Bloch sphere
    b = Bloch()

    # Add the quantum state to the Bloch sphere
    b.add_states(state)


    # Render the Bloch sphere
    b.show()

    # Ensure the window remains open
    plt.show()

# Example values for alpha and beta
alpha = 1/np.sqrt(2)  # Example alpha
beta = -1/np.sqrt(2) * (complex(1/np.sqrt(2),1/np.sqrt(2)))  # Example beta

# Plot the Bloch sphere with the given state
plot_bloch_sphere(alpha, beta)
