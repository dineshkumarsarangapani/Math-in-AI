# Matrix operations implemented from scratch (without NumPy)
# This helps to understand the mathematical concepts better

# Define the matrix using lists
A = [
    [1, 2, 5],   # Sample 1: Var1=1, Var2=2, Var3=5
    [2, 4, 6],   # Sample 2: Var1=2, Var2=4, Var3=6
    [3, 6, 7]    # Sample 3: Var1=3, Var2=6, Var3=7
]

# Print the matrix
print("Original Matrix:")
for row in A:
    print(row)

# Get matrix dimensions
rows = len(A)
cols = len(A[0])
print("\nNumber of columns:", cols)

# Helper function for row echelon form
def row_echelon_form(matrix):
    A = [row[:] for row in matrix]  # Create a copy of the matrix
    rows = len(A)
    cols = len(A[0])
    
    # Track the row and column position
    r = 0
    for c in range(cols):
        # Find pivot in column c, starting from row r
        pivot_row = None
        for i in range(r, rows):
            if abs(A[i][c]) > 1e-10:  # Non-zero element check with small tolerance
                pivot_row = i
                break
        
        if pivot_row is None:
            # No pivot in this column, move to the next column
            continue
        
        # Swap current row with pivot row
        A[r], A[pivot_row] = A[pivot_row], A[r]
        
        # Normalize the pivot row
        pivot = A[r][c]
        for j in range(c, cols):
            A[r][j] /= pivot
        
        # Eliminate other rows
        for i in range(rows):
            if i != r:
                factor = A[i][c]
                for j in range(c, cols):
                    A[i][j] -= factor * A[r][j]
        
        r += 1
        if r == rows:
            break
    
    return A

# Calculate the rank by counting non-zero rows after row reduction
def calculate_rank(matrix):
    rref = row_echelon_form(matrix)
    rank = 0
    for row in rref:
        # Check if row is non-zero
        if any(abs(val) > 1e-10 for val in row):
            rank += 1
    return rank, rref

# Calculate rank
rank, rref = calculate_rank(A)
print("\nRow Echelon Form:")
for row in rref:
    print([round(val, 10) for val in row])  # Round to avoid floating point artifacts

print("\nRank of the matrix:", rank)

# Calculate nullity
nullity = cols - rank
print("Nullity (Number of Relationships):", nullity)

# Find null space by solving the homogeneous system
def find_null_space(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create augmented matrix [A|0]
    aug = [row + [0] for row in matrix]
    
    # Row reduce the augmented matrix
    rref = row_echelon_form(aug)
    
    # Identify free variables (columns without pivots)
    pivot_cols = []
    r = 0
    for c in range(cols):
        # Check if this column has a pivot
        has_pivot = False
        for i in range(r, rows):
            if abs(rref[i][c]) > 1e-10:
                pivot_cols.append(c)
                r += 1
                has_pivot = True
                break
        if not has_pivot:
            continue
    
    free_vars = [i for i in range(cols) if i not in pivot_cols]
    
    # For each free variable, find a basis vector of the null space
    null_space = []
    for free_var in free_vars:
        # Set the free variable to 1, and solve for other variables
        solution = [0] * cols
        solution[free_var] = 1
        
        # Back-substitute to find values of pivot variables
        for i in range(rank-1, -1, -1):
            pivot_col = pivot_cols[i]
            sum_val = 0
            for j in range(pivot_col + 1, cols):
                sum_val += rref[i][j] * solution[j]
            solution[pivot_col] = -sum_val
        
        null_space.append(solution)
    
    return null_space

# Find null space basis
null_space = find_null_space(A)
print("\nNull space basis vectors (showing the relationships):")
for vector in null_space:
    print([round(val, 10) for val in vector])

# Verify that A * null_space = 0
def matrix_vector_mult(matrix, vector):
    rows = len(matrix)
    result = [0] * rows
    for i in range(rows):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result

if null_space:
    print("\nVerification - A * null space vector should give zero vector:")
    for vector in null_space:
        result = matrix_vector_mult(A, vector)
        print("A * ", [round(val, 10) for val in vector], " = ", [round(val, 10) for val in result])