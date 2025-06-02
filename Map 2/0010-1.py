import numpy as np

def demonstrate_numpy_operations():
    
    print("Basic NumPy Array Operations\n")
    
    # Create arrays
    print("1. Creating Arrays:")
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([6, 7, 8, 9, 10])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    print(f"Array 1 shape: {arr1.shape}")
    print(f"Array 1 data type: {arr1.dtype}")
    
    # Basic arithmetic operations
    print("\n2. Arithmetic Operations:")
    print(f"Addition: {arr1} + {arr2} = {arr1 + arr2}")
    print(f"Subtraction: {arr2} - {arr1} = {arr2 - arr1}")
    print(f"Multiplication: {arr1} * {arr2} = {arr1 * arr2}")
    print(f"Division: {arr2} / {arr1} = {arr2 / arr1}")
    
    # Array reshaping
    print("\n3. Array Reshaping:")
    matrix = np.arange(12).reshape(3, 4)
    print(f"Original array: {np.arange(12)}")
    print(f"Reshaped to 3x4 matrix:\n{matrix}")
    
    # Statistical operations
    print("\n4. Statistical Operations:")
    data = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    print(f"Data: {data}")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard deviation: {np.std(data):.2f}")
    print(f"Min value: {np.min(data)}")
    print(f"Max value: {np.max(data)}")
    print(f"Sum: {np.sum(data)}")
    
    # Array indexing and slicing
    print("\n5. Array Indexing and Slicing:")
    arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print(f"Original array: {arr}")
    print(f"First element: {arr[0]}")
    print(f"Last element: {arr[-1]}")
    print(f"Elements 2-5: {arr[2:6]}")
    print(f"Every 2nd element: {arr[::2]}")
    
    # Boolean indexing
    print("\n6. Boolean Indexing:")
    print(f"Elements greater than 50: {arr[arr > 50]}")
    print(f"Elements divisible by 3: {arr[arr % 3 == 0]}")
    
    # 2D array operations
    print("\n7. 2D Array Operations:")
    matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
    matrix_b = np.array([[7, 8, 9], [10, 11, 12]])
    
    print(f"Matrix A:\n{matrix_a}")
    print(f"Matrix B:\n{matrix_b}")
    print(f"Matrix addition:\n{matrix_a + matrix_b}")
    print(f"Matrix transpose of A:\n{matrix_a.T}")
    
    # Creating special arrays
    print("\n8. Special Arrays:")
    zeros = np.zeros((2, 3))
    ones = np.ones((2, 3))
    identity = np.eye(3)
    
    print(f"Zeros array (2x3):\n{zeros}")
    print(f"Ones array (2x3):\n{ones}")
    print(f"Identity matrix (3x3):\n{identity}")
# Numpy implementaation
def interactive_numpy_playground():
    
    while True:
        print("\nChoose an operation:")
        print("1. Create and manipulate 1D array")
        print("2. Create and manipulate 2D array")
        print("3. Perform statistical analysis")
        print("4. Array reshaping demonstration")
        print("5. Back to main menu")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            try:
                size = int(input("Enter array size: "))
                arr = np.random.randint(1, 100, size)
                print(f"Generated array: {arr}")
                print(f"Sum: {np.sum(arr)}")
                print(f"Mean: {np.mean(arr):.2f}")
                print(f"Max: {np.max(arr)}")
                print(f"Min: {np.min(arr)}")
            except ValueError:
                print("Please enter a valid number!")
                
        elif choice == '2':
            try:
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                matrix = np.random.randint(1, 50, (rows, cols))
                print(f"Generated {rows}x{cols} matrix:\n{matrix}")
                print(f"Matrix shape: {matrix.shape}")
                print(f"Matrix sum: {np.sum(matrix)}")
            except ValueError:
                print("Please enter valid numbers!")
                
        elif choice == '3':
            data = np.random.normal(50, 15, 20)  # Normal distribution
            print(f"Sample data (20 values): {data.round(2)}")
            print(f"Mean: {np.mean(data):.2f}")
            print(f"Standard deviation: {np.std(data):.2f}")
            print(f"Min: {np.min(data):.2f}")
            print(f"Max: {np.max(data):.2f}")
            
        elif choice == '4':
            original = np.arange(1, 25)  # 1 to 24
            print(f"Original array: {original}")
            
            reshaped_2d = original.reshape(4, 6)
            print(f"Reshaped to 4x6:\n{reshaped_2d}")
            
            reshaped_3d = original.reshape(2, 3, 4)
            print(f"Reshaped to 2x3x4:\n{reshaped_3d}")
            
        elif choice == '5':
            break
            
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    
    try:
        while True:
            print("\nNumPy Operations Menu")
            print("1. Run basic NumPy demonstration")
            print("2. Interactive NumPy playground")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '1':
                demonstrate_numpy_operations()
                
            elif choice == '2':
                interactive_numpy_playground()
                
            elif choice == '3':
                print("Thank you for using")
                break
                
            else:
                print("Invalid choice")
                
    except ImportError:
        print("Error: NumPy is not installed!")
        print("Please install NumPy using: pip install numpy")