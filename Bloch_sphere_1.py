import numpy as np
from qutip import Bloch, Qobj
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

# Section 1: Function definitions

def normalize_state(alpha, beta):
    """
    Normalize the quantum state coefficients alpha and beta.

    Parameters:
    alpha (complex): Coefficient of the |0state.
    beta (complex): Coefficient of the |1state.

    Returns:
    alpha (complex): Normalized coefficient of the |0state.
    beta (complex): Normalized coefficient of the |1state.
    """
    norm = np.sqrt(np.abs(alpha) ** 2 + np.abs(beta) ** 2)
    return alpha / norm, beta / norm


def calculate_angles(alpha, beta):
    """
    Calculate the polar and azimuthal angles from the quantum state coefficients.

    Parameters:
    alpha (complex): Coefficient of the |0state.
    beta (complex): Coefficient of the |1state.

    Returns:
    theta (float): Polar angle θ in radians.
    phi (float): Azimuthal angle φ in radians.
    """
    theta = 2 * np.arccos(np.abs(alpha))  # Polar angle θ
    phi = np.angle(beta) - np.angle(alpha)  # Azimuthal angle φ
    return theta, phi


def plot_bloch_sphere(alpha, beta, ax_bloch, theta=None, phi=None):
    """
    Visualize the qubit on the Bloch sphere using Matplotlib.

    Parameters:
    alpha (complex): Coefficient of the |0state.
    beta (complex): Coefficient of the |1state.
    ax_bloch (Axes3D): Axes for the Bloch sphere visualization.
    theta (float): Polar angle θ in radians (optional).
    phi (float): Azimuthal angle φ in radians (optional).
    """
    # Normalize the coefficients
    alpha, beta = normalize_state(alpha, beta)

    # Create a Qobj representing the quantum state
    state = Qobj([[alpha], [beta]])

    # Initialize the Bloch sphere
    b = Bloch(fig=plt.gcf(), axes=ax_bloch)
    b.clear()  # Clear previous states
    b.add_states(state)

    # Calculate angles if not provided
    if theta is None or phi is None:
        theta, phi = calculate_angles(alpha, beta)

    # Display theta and phi on the plot
    print(f"Polar angle (θ): {np.degrees(theta):.2f}°")
    print(f"Azimuthal angle (φ): {np.degrees(phi):.2f}°")

    # Annotate the plot with θ and φ
    ax_bloch.text2D(0.05, 0.95, f"θ = {np.degrees(theta):.2f}°", transform=ax_bloch.transAxes, fontsize=12, color='blue')
    ax_bloch.text2D(0.05, 0.90, f"φ = {np.degrees(phi):.2f}°", transform=ax_bloch.transAxes, fontsize=12, color='blue')

    # Render the Bloch sphere
    b.render()


# Section 2: GUI setup

fig = plt.figure(figsize=(8, 8))  # Increased figure size
ax_bloch = fig.add_subplot(111, projection='3d')

# Initialize alpha and beta sliders
ax_alpha = plt.axes([0.1, 0.05, 0.3, 0.03])
ax_beta = plt.axes([0.6, 0.05, 0.3, 0.03])

s_alpha = Slider(ax_alpha, 'Alpha', -1, 1, valinit=1)
s_beta = Slider(ax_beta, 'Beta', -1, 1, valinit=0)

# Initialize theta and phi text boxes
ax_theta = plt.axes([0.1, 0.01, 0.3, 0.03])
ax_phi = plt.axes([0.6, 0.01, 0.3, 0.03])

t_theta = TextBox(ax_theta, 'Theta (°): ', initial='')
t_phi = TextBox(ax_phi, 'Phi (°): ', initial='')


# Update function for sliders
def update(val):
    alpha = s_alpha.val
    beta = s_beta.val
    plot_bloch_sphere(alpha, beta, ax_bloch)


# Update function for text boxes
def update_manual(val):
    theta = np.radians(float(t_theta.text) if t_theta.text else 0)
    phi = np.radians(float(t_phi.text) if t_phi.text else 0)
    alpha = np.cos(theta / 2)
    beta = np.exp(1j * phi) * np.sin(theta / 2)
    plot_bloch_sphere(alpha, beta, ax_bloch, theta, phi)


# Register update functions
s_alpha.on_changed(update)
s_beta.on_changed(update)
t_theta.on_submit(update_manual)
t_phi.on_submit(update_manual)

# Initialize the plot
update(0)

plt.show()
