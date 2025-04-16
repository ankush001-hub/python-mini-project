import numpy as np

def get_matrix(order, name):
    print(f"\nEnter elements of {name} matrix (row by row):")
    matrix = []
    for i in range(order[0]):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        while len(row) != order[1]:
            print(f"Please enter exactly {order[1]} values.")
            row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

def main():
    print(" MATRIX CALCULATOR ")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Transpose\n5. Inverse\n6. Determinant\n7. Exit")

    while True:
        choice = input("\nChoose an operation (1-7): ")

        if choice == '1' or choice == '2':
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            A = get_matrix((r, c), "first")
            B = get_matrix((r, c), "second")

            if choice == '1':
                print("Result:\n", A + B)
            else:
                print("Result:\n", A - B)

        elif choice == '3':
            r1 = int(input("Enter rows of first matrix: "))
            c1 = int(input("Enter columns of first matrix: "))
            A = get_matrix((r1, c1), "first")

            r2 = int(input("Enter rows of second matrix: "))
            c2 = int(input("Enter columns of second matrix: "))
            B = get_matrix((r2, c2), "second")

            if c1 != r2:
                print("Matrix multiplication not possible (columns of A ≠ rows of B)")
            else:
                print("Result:\n", A @ B)

        elif choice == '4':
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            A = get_matrix((r, c), "the")
            print("Transpose:\n", A.T)

        elif choice == '5':
            n = int(input("Enter size of square matrix (n x n): "))
            A = get_matrix((n, n), "the")
            try:
                inv = np.linalg.inv(A)
                print("Inverse:\n", inv)
            except np.linalg.LinAlgError:
                print(" Matrix is singular and cannot be inverted.")

        elif choice == '6':
            n = int(input("Enter size of square matrix (n x n): "))
            A = get_matrix((n, n), "the")
            det = np.linalg.det(A)
            print("Determinant:", det)

        elif choice == '7':
            print(" Exiting Matrix Calculator.")
            break
        else:
            print(" Invalid choice. Please select from 1 to 7.")

if __name__ == "__main__":
    main()