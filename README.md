Quantum Stack Operations Program

Introduction

This Python program implements quantum stack operations, including push, pop, get_top, get_size, and check_empty functions, within a composite system. It allows users to interact with a quantum stack and perform various operations related to quantum states.

Requirements

- Python 3.x
- NumPy library

Usage

1. Initialization: Upon running the program, you will be prompted to enter a number greater than 0, which determines the number of quantum states in the system.

2. Menu Options:
   - [1] Check if the stack is empty: Checks whether the quantum stack is empty.
   - [2] Push a qubit into the stack: Inserts a quantum state into the stack.
   - [3] Get the top qubit: Retrieves the top qubit from the stack without modifying the stack.
   - [4] Get the size of the stack: Calculates and prints the size of the stack.
   - [5] Pop the top element: Removes the top element from the stack using partial trace.
   - [6] Exit: Exits the program.

3. Push Operation: When choosing option [2], enter the name of the quantum state (e.g., T1, T2) to insert it into the stack.

4. Get Top Operation: Option [3] displays the top element (last pushed qubit) from the stack along with its density matrix.

5. Get Size Operation: Option [4] calculates and prints the size of the stack based on the number of qubit matrices.

6. Pop Operation: Option [5] removes the top element (last pushed qubit) from the stack using the partial trace operator.

Implementation Details

- Binary Value Generation: Generates binary values based on the specified number of values.
- Qubit Matrix Creation: Creates qubit matrices and a dictionary mapping qubit names to binary strings.
- Qubit Matrix Initialization: Initializes qubit matrices based on the qubit dictionary.
- Density Matrix Computation: Computes the density matrix from a ket vector.
- Stack Empty Check: Checks if the stack is empty by comparing it with an identity matrix.
- Push Operation: Pushes a qubit density matrix into the stack using the Kronecker product.
- Get Top Operation: Retrieves the top element (last pushed qubit) from the stack without modifying the stack itself.
- Get Size Operation: Calculates and prints the size of the stack based on the number of qubit matrices.
- Pop Operation: Pops the top element from the stack by tracing out the top qubit's density matrix.

