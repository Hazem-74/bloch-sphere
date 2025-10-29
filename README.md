# Bloch Sphere Project

This repository contains Python scripts for visualizing and interacting with quantum states on the Bloch sphere. The Bloch sphere is a powerful geometrical representation of the pure state space of a two-level quantum mechanical system (qubit). These scripts leverage the `qutip` library for rendering the Bloch sphere and `matplotlib` for creating interactive user interfaces, allowing for dynamic exploration of qubit states.

## Table of Contents

*   [Project Overview](#project-overview)
*   [Files](#files)
    *   [Bloch_Sphere.py](#bloch_spherepy)
    *   [Bloch_Sphere_simple.py](#bloch_sphere_simplepy)
    *   [Bloch_sphere_1.py](#bloch_sphere_1py)
*   [Requirements](#requirements)
*   [Installation](#installation)
*   [How to Run](#how-to-run)
*   [Contributing](#contributing)
*   [License](#license)

## Project Overview

The "Bloch Sphere" project aims to provide intuitive tools to understand how a qubit's state, defined by its complex superposition coefficients ($\alpha, \beta$) or its spherical coordinates ($\theta, \phi$), maps to a unique point on the Bloch sphere. The interactive scripts facilitate hands-on learning by allowing users to manipulate these parameters and observe the state change in real-time.

## Files

### `Bloch_Sphere.py`

*   **Purpose**: This script provides an advanced, fully interactive environment for visualizing and manipulating single-qubit states on the Bloch sphere. Users can dynamically adjust the qubit's parameters and instantly see the corresponding state on the sphere.
*   **Methods & Logic**:
    *   **State Normalization**: Ensures that the input complex coefficients $(\alpha, \beta)$ defining the qubit state ($|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$) are always normalized, maintaining a valid quantum state.
    *   **Angle Conversion**: Functions (`calculate_angles`) convert between the complex coefficients $(\alpha, \beta)$ and the Bloch sphere's polar ($\theta$) and azimuthal ($\phi$) angles.
    *   **Interactive UI**: Employs `matplotlib.widgets` (Sliders and RadioButtons) to offer two distinct interaction modes:
        *   **Alpha/Beta Mode**: Sliders control the real and imaginary parts of both $\alpha$ and $\beta$.
        *   **Theta/Phi Mode**: Sliders control the polar angle $\theta$ (0-180°) and azimuthal angle $\phi$ (0-360°).
    *   **Visualization**: Uses `qutip.Bloch` to render a 3D Bloch sphere, updating the qubit's position in real-time based on slider input. The calculated $\theta$ and $\phi$ values are annotated on the plot.

### `Bloch_Sphere_simple.py`

*   **Purpose**: This is a minimalist script designed for a quick and non-interactive visualization of a single, predefined qubit state on the Bloch sphere. It's suitable for demonstrating a specific quantum state without user input.
*   **Methods & Logic**:
    *   **State Definition**: Takes example complex coefficients for $\alpha$ and $\beta$.
    *   **Normalization**: Normalizes these initial complex coefficients.
    *   **Visualization**: Initializes a `qutip.Bloch` sphere and directly adds the calculated quantum state to it, then displays the resulting 3D plot. The script focuses solely on rendering a static representation of the qubit.

### `Bloch_sphere_1.py`

*   **Purpose**: This script offers an alternative interactive method for visualizing and controlling qubit states on the Bloch sphere, distinct from `Bloch_Sphere.py` in its user interface approach.
*   **Methods & Logic**:
    *   **Normalization & Angle Conversion**: Similar to `Bloch_Sphere.py`, it handles state normalization and calculation of Bloch sphere angles.
    *   **Interactive UI**: Integrates `matplotlib.widgets` (Sliders and TextBoxes) for user interaction:
        *   **Sliders**: Control the *real parts* of $\alpha$ and $\beta$. Note that this script does not provide direct slider control over the imaginary components of $\alpha$ and $\beta$.
        *   **Text Boxes**: Allow users to input specific numeric values for $\theta$ and $\phi$ (in degrees). Submitting values in these text boxes updates the Bloch sphere position.
    *   **Visualization**: Employs `qutip.Bloch` for rendering the 3D sphere, dynamically adjusting the qubit's displayed position based on changes from either the sliders or text box inputs. $\theta$ and $\phi$ values are also shown as text annotations on the plot.

## Requirements

To run these Python scripts, you will need the following libraries installed:

*   `Python 3.x`
*   `numpy`
*   `qutip`
*   `matplotlib`

## Installation

Follow these steps to set up the project on your local machine:

1.  **Clone the Repository**:
    Navigate to your desired directory in the terminal and clone Hazem-74's repository:
    ```bash
    git clone https://github.com/Hazem-74/Hazem-s-Bible.git
    ```

2.  **Navigate to the Project Directory**:
    Change your current directory to the 'Bloch Sphere' project folder:
    ```bash
    cd Hazem-s-Bible/Bloch\ Sphere
    ```
    *(Note: The `\` is used to escape the space in "Bloch Sphere" for command-line compatibility.)*

3.  **Install Dependencies**:
    It is highly recommended to create and activate a virtual environment before installing dependencies to avoid conflicts with your system's Python packages:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install numpy qutip matplotlib
    ```

## How to Run

Once you have installed the requirements and navigated to the `Bloch Sphere` directory, you can run each script as follows:

*   **To run `Bloch_Sphere.py` (Advanced Interactive Tool)**:
    ```bash
    python Bloch_Sphere.py
    ```
    This will open an interactive Matplotlib window featuring the Bloch sphere, sliders for parameter adjustment, and radio buttons to switch between input modes.

*   **To run `Bloch_Sphere_simple.py` (Basic Static Visualization)**:
    ```bash
    python Bloch_Sphere_simple.py
    ```
    This will display a static Matplotlib window showing the Bloch sphere with a predefined qubit state. The window will close once you close it manually.

*   **To run `Bloch_sphere_1.py` (Alternative Interactive Tool)**:
    ```bash
    python Bloch_sphere_1.py
    ```
    This will open an interactive Matplotlib window with the Bloch sphere, sliders for $\alpha$ and $\beta$ real parts, and text boxes for entering $\theta$ and $\phi$ values.

## Contributing

Contributions, bug reports, and feature requests are welcome! Please feel free to open an issue or submit a pull request on the GitHub repository.

## License

This project is open-source. Please refer to the repository's license for specific terms.
