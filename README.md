# Bloch Sphere Project

This repository contains Python scripts for visualizing and interacting with quantum states on the Bloch sphere. The Bloch sphere is a powerful geometrical representation of the pure state space of a two-level quantum mechanical system (qubit). These scripts leverage the `qutip` library for rendering the Bloch sphere and `matplotlib` for creating interactive user interfaces, allowing for dynamic exploration of qubit states.


## Project Overview

The "Bloch Sphere" project aims to provide intuitive tools to understand how a qubit's state, defined by its complex superposition coefficients ($\alpha, \beta$) or its spherical coordinates ($\theta, \phi$), maps to a unique point on the Bloch sphere. The interactive scripts facilitate hands-on learning by allowing users to manipulate these parameters and observe the state change in real-time.

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
