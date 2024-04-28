import numpy as np
import math

# Function to generate binary values
def generate_binary_values(num_values):
    binary_values = []
    for i in range(1, num_values + 1):  # Start from 1 instead of 0
        binary_values.append(bin(i)[2:])  # Convert integer to binary string and remove '0b' prefix
    return binary_values

# Function to create qubit matrices and qubit dictionary
def qubit_matrix(binary_values, num_qs):
    matrix = []
    qubit_dict = {}
    for idx, binary_str in enumerate(binary_values):
        binary_list = list(map(int, binary_str.zfill(num_qs)))  # Pad with zeros to match num_qs
        matrix.append(binary_list)
        qubit_dict[f'T{idx + 1}'] = binary_str.zfill(num_qs)  # Add qubit name to dictionary
    return np.array(matrix), qubit_dict

# Function to initialize qubit matrices based on the qubit dictionary
def create_qubit_matrices(qubit_dict, num_qs):
    qubit_matrices = {}
    for key, value in qubit_dict.items():
        matrix = np.zeros((2 ** num_qs, 1), dtype=int)
        index = int(value, 2)  # Convert binary string to integer
        matrix[index][0] = 1  # Set the corresponding element to 1
        qubit_matrices[key] = matrix  # Add qubit matrix to dictionary
    return qubit_matrices

# Function to compute the density matrix from a ket vector
def compute_density_matrix(ket_vector):
    return np.outer(ket_vector, np.conj(ket_vector).T)

# Function to check if the stack is empty
def check_empty(stack):
    return np.array_equal(stack, np.array([[1]]))  # Check if the stack is equal to the identity matrix

# Function to push a qubit density matrix into the stack
def push_operation(stack, qubit_density_matrix):
    composite_system = np.kron(stack, qubit_density_matrix)  # Kronecker product
    return composite_system

# Function to retrieve the top element (last pushed qubit) from the stack
def get_top(stack, qubit_matrices):
    if check_empty(stack):
        print("Stack is empty. There are no elements.")
    else:
        last_qubit = list(qubit_matrices.keys())[-1]  # Get the name of the last pushed qubit
        last_qubit_density_matrix = stack[-1]  # Retrieve the top element from the stack
        print(f"Top Element ({last_qubit})")
        

# Function to calculate and print the size of the stack
def get_size(stack, qubit_matrices):
    if check_empty(stack):
        print("Size of the stack: 0")
    else:
        n = len(qubit_matrices)  # Number of unique stack symbols (number of rows in the qubit)
        m = math.ceil(math.log2(n))  # Ceiling of log n to the base 2
        d = 2 ** m  # Dimension of density matrix of each qubit
        k = stack.shape[0]  # Number of rows and columns of the stack matrix
        size = math.log(k, d)  # Log k to the base d
        print(f"Size of the stack: {size}")

# Function to pop the top element from the stack
def pop_operation(stack, qubit_matrices, initialized):
    if not initialized:
        print("Error: Stack is not initialized. Please push elements into the stack first.")
        return stack, initialized
    elif check_empty(stack):
        print("Error: Stack underflow. There are no elements to pop.")
        return stack, initialized
    else:
        last_qubit = list(qubit_matrices.keys())[-1]  # Get the name of the last pushed qubit
        density_matrix_to_remove = qubit_matrices[last_qubit]  # Get the density matrix to remove
        stack_dimension = stack.shape[0]  # Number of rows in the stack matrix
        top_dimension = density_matrix_to_remove.shape[0]  # Dimension of the top element
        if stack_dimension % top_dimension != 0:
            print("Error: Incompatible dimensions for popping.")
            return stack, initialized
        else:
            rows_to_keep = stack_dimension // top_dimension  # Calculate the number of rows to keep
            # Perform partial trace to remove the top element
            updated_stack = np.trace(np.reshape(stack, (rows_to_keep, top_dimension, rows_to_keep, top_dimension)), axis1=1, axis2=3)
            print("Top element popped from the stack.")
            print("Updated Composite System:")
            print(updated_stack)
            return updated_stack, initialized

# Flag to track if the stack has been initialized
initialized = False

# Prompt the user to enter a number
while True:
    user_input = input("Enter a number greater than 0: ")
    try:
        number = int(user_input)
        if number > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Now you can use the 'number' variable for further operations
print("Enter the number of states required:", number)
num_qs = 2

# Generate binary values and create qubit matrices
binary_values = generate_binary_values(number)
qubit_matrix, qubit_dict = qubit_matrix(binary_values, num_qs)
qubit_matrices = create_qubit_matrices(qubit_dict, num_qs)

# Print qubit matrices and density matrices
print("Qubit Matrices:")
for key, matrix in qubit_matrices.items():
    print(f"{key}:")
    print(matrix)
    density_matrix = compute_density_matrix(matrix)
    qubit_matrices[key] = density_matrix  # Replace ket vectors with density matrices
    print(f"Density Matrix for {key}:")  # Print density matrices with qubit names
    print(density_matrix)
    print()

# Define the identity matrix for the empty stack
stack = np.array([[1]])

# Set the initialized flag to True after initializing the stack
initialized = True

# Perform stack operations based on user input
while True:
    operations = input("[1] Check if the stack is empty [2] Push a qubit into the stack [3] Get the top qubit [4] Get the size of the stack [5] Pop the top element [6] Exit\nEnter your choice: ")
    match operations:
        case "1":
            if check_empty(stack):
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        case "2":
            qubit_to_insert = input("Enter the quantum state you want to insert: ")
            if qubit_to_insert in qubit_matrices:
                qubit_density_matrix = qubit_matrices[qubit_to_insert]
                stack = push_operation(stack, qubit_density_matrix)
                print("Qubit density matrix inserted into the stack.")
                print("Updated Composite System:")
                print(stack)
            else:
                print("Invalid quantum state name. Please enter a valid qubit.")
        case "3":
            get_top(stack, qubit_matrices)
        case "4":
            get_size(stack, qubit_matrices)
        case "5":
            stack, initialized = pop_operation(stack, qubit_matrices, initialized)
        case "6":
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please enter a valid option.")
