# 0x0C-python-almost_a_circle

This repository contains the code for the "Almost a Circle" project, which is part of the larger Python curriculum. The project focuses on object-oriented programming (OOP) concepts and covers various topics related to classes, inheritance, serialization, and unit testing.

## Project Structure

The project is organized into several modules and files:

- `models/` directory: Contains the implementation of classes used in the project.
- `tests/` directory: Contains unit tests for the project.
- `README.md`: Provides an overview and instructions for the project.
- Other supporting files: These include the `base.py` module, which serves as the foundation for other classes, and `__init__.py` files to mark directories as Python packages.

## Functionality

The main goal of the project is to create a base class named `Base` and derived classes `Rectangle` and `Square`, which represent geometric shapes. The classes have attributes and methods for managing their properties, performing calculations, and applying serialization.

Key functionality of the project includes:

- Creating instances of `Rectangle` and `Square` with specified dimensions.
- Calculating the area and perimeter of shapes.
- Implementing serialization and deserialization of objects using JSON.
- Saving and loading objects to and from files.
- Performing unit tests to ensure the functionality and correctness of the implemented classes and methods.

## Getting Started

To run the project and execute the unit tests, follow these steps:

1. Clone the repository:

   ````bash
    git clone https://github.com/your-username/0x0C-python-almost_a_circle.git
   ```

2. Navigate to the project directory:

   ````bash
    cd 0x0C-python-almost_a_circle
   ```

3. Run the unit tests:

   ````bash
    python3 -m unittest discover tests
   ```
   ````bash

  python3 -m unittest tests/test_models/test_base.py
  ```
