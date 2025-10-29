import numpy as np
from qutip import Bloch, Qobj
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons


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


def plot_bloch_sphere(alpha, beta, ax_bloch):
    """
    Visualize the qubit on the Bloch sphere using Matplotlib.

    Parameters:
    alpha (complex): Coefficient of the |0state.
    beta (complex): Coefficient of the |1state.
    ax_bloch (Axes3D): Axes for the Bloch sphere visualization.
    """
    # Normalize the coefficients
    alpha, beta = normalize_state(alpha, beta)

    # Create a Qobj representing the quantum state
    state = Qobj([[alpha], [beta]])

    # Initialize the Bloch sphere
    b = Bloch(fig=fig, axes=ax_bloch)
    b.clear()  # Clear previous states
    b.add_states(state)

    # Calculate angles
    theta, phi = calculate_angles(alpha, beta)

    # Display theta and phi on the plot
    print(f"Polar angle (θ): {np.degrees(theta):.2f}°")
    print(f"Azimuthal angle (φ): {np.degrees(phi):.2f}°")

    # Annotate the plot with θ and φ
    ax_bloch.annotate(f"θ = {np.degrees(theta):.2f}°",
                      xy=(0, 0), xytext=(1.5, 1.5),
                      textcoords='axes fraction',
                      fontsize=12, color='blue')

    ax_bloch.annotate(f"φ = {np.degrees(phi):.2f}°",
                      xy=(0, 0), xytext=(1.5, 1.0),
                      textcoords='axes fraction',
                      fontsize=12, color='blue')

    # Render the Bloch sphere
    b.render()


def update_alpha_beta(val):
    """
    Update the Bloch sphere in Mode 1 (alpha, beta).

    Parameters:
    val (float): Slider value.
    """
    real_alpha = slider_real_alpha.val
    imag_alpha = slider_imag_alpha.val
    real_beta = slider_real_beta.val
    imag_beta = slider_imag_beta.val

    # Update alpha and beta with slider values
    alpha = complex(real_alpha, imag_alpha)
    beta = complex(real_beta, imag_beta)

    # Update Bloch sphere
    plot_bloch_sphere(alpha, beta, ax_bloch)


def update_theta_phi(val):
    """
    Update the Bloch sphere in Mode 2 (theta, phi).

    Parameters:
    val (float): Slider value.
    """
    theta = np.radians(slider_theta.val)
    phi = np.radians(slider_phi.val)

    # Calculate alpha and beta from theta and phi
    alpha = np.cos(theta / 2)
    beta = np.sin(theta / 2) * np.exp(1j * phi)

    # Update Bloch sphere
    plot_bloch_sphere(alpha, beta, ax_bloch)


def toggle_mode(label):
    """
    Toggle between the two modes (alpha/beta and theta/phi).

    Parameters:
    label (str): Radio button label.
    """
    if label == 'Alpha/Beta':
        # Hide theta/phi sliders and show alpha/beta sliders
        slider_real_alpha.ax.set_visible(True)
        slider_imag_alpha.ax.set_visible(True)
        slider_real_beta.ax.set_visible(True)
        slider_imag_beta.ax.set_visible(True)
        slider_theta.ax.set_visible(False)
        slider_phi.ax.set_visible(False)
        update_alpha_beta(None)
    elif label == 'Theta/Phi':
        # Hide alpha/beta sliders and show theta/phi sliders
        slider_real_alpha.ax.set_visible(False)
        slider_imag_alpha.ax.set_visible(False)
        slider_real_beta.ax.set_visible(False)
        slider_imag_beta.ax.set_visible(False)
        slider_theta.ax.set_visible(True)
        slider_phi.ax.set_visible(True)
        update_theta_phi(None)
    plt.draw()


# Section 2: Initial setup

# Example initial values for alpha, beta, theta, and phi
alpha = 1 / np.sqrt(2)  # Initial alpha
beta = complex(-1 / 2, -1 / 2)  # Initial beta
theta = 90  # Initial theta in degrees
phi = 45  # Initial phi in degrees

# Create a figure with subplots for sliders and Bloch sphere
fig = plt.figure(figsize=(10, 8))  # Increase figure size to make Bloch sphere larger
plt.subplots_adjust(left=0.25, bottom=0.35)

# Add Bloch sphere axes
ax_bloch = fig.add_subplot(111, projection='3d', aspect='auto')
ax_bloch.set_box_aspect([1, 1, 1])  # Make the Bloch sphere visualization larger

# Plot the initial state
plot_bloch_sphere(alpha, beta, ax_bloch)

# Section 3: Slider setup

# Define slider axes for real and imaginary parts of alpha and beta
ax_real_alpha = plt.axes([0.25, 0.25, 0.4, 0.02], facecolor='lightgoldenrodyellow')
ax_imag_alpha = plt.axes([0.25, 0.20, 0.4, 0.02], facecolor='lightgoldenrodyellow')
ax_real_beta = plt.axes([0.25, 0.15, 0.4, 0.02], facecolor='lightgoldenrodyellow')
ax_imag_beta = plt.axes([0.25, 0.10, 0.4, 0.02], facecolor='lightgoldenrodyellow')

# Define slider axes for theta and phi
ax_theta = plt.axes([0.25, 0.25, 0.4, 0.02], facecolor='lightgreen')
ax_phi = plt.axes([0.25, 0.20, 0.4, 0.02], facecolor='lightgreen')

# Create sliders for real and imaginary parts of alpha and beta
slider_real_alpha = Slider(ax_real_alpha, 'Real(α)', -1.0, 1.0, valinit=np.real(alpha))
slider_imag_alpha = Slider(ax_imag_alpha, 'Imag(α)', -1.0, 1.0, valinit=np.imag(alpha))
slider_real_beta = Slider(ax_real_beta, 'Real(β)', -1.0, 1.0, valinit=np.real(beta))
slider_imag_beta = Slider(ax_imag_beta, 'Imag(β)', -1.0, 1.0, valinit=np.imag(beta))

# Create sliders for theta and phi
slider_theta = Slider(ax_theta, 'θ (Theta)', 0, 180, valinit=theta)
slider_phi = Slider(ax_phi, 'φ (Phi)', 0, 360, valinit=phi)

# Hide theta/phi sliders initially
slider_theta.ax.set_visible(False)
slider_phi.ax.set_visible(False)

# Update Bloch sphere when slider values change
slider_real_alpha.on_changed(update_alpha_beta)
slider_imag_alpha.on_changed(update_alpha_beta)
slider_real_beta.on_changed(update_alpha_beta)
slider_imag_beta.on_changed(update_alpha_beta)

slider_theta.on_changed(update_theta_phi)
slider_phi.on_changed(update_theta_phi)

# Section 4: Radio button setup

# Add radio buttons to toggle between alpha/beta and theta/phi modes
ax_mode = plt.axes([0.025, 0.5, 0.1, 0.1], facecolor='lightgray')
radio = RadioButtons(ax_mode, ('Alpha/Beta', 'Theta/Phi'), activecolor='blue')

# Connect the radio button to the mode toggle function
radio.on_clicked(toggle_mode)

# Show the plot
plt.show()