# Let's make a matrix similar to the example
# Where Var 2 is 2 times Var 1, and Var 3 is something else
# This one should have a relationship between col 1 and 2
import numpy as np

# Create the matrix
A = np.array([
    [1, 2, 5],   # Sample 1: Var1=1, Var2=2, Var3=5
    [2, 4, 6],   # Sample 2: Var1=2, Var2=4, Var3=6
    [3, 6, 7]    # Sample 3: Var1=3, Var2=6, Var3=7
])

# Number of columns
print("Number of columns:")
print(A.shape[1])

# Calculate rank of the matrix
print("Rank of the matrix:")
rank = np.linalg.matrix_rank(A)
print(rank)

# Calculate nullity
print("Nullity (Number of Relationships):")
print(A.shape[1] - rank)

# To find the null space (the relationship)
# We can use SVD decomposition
U, S, Vh = np.linalg.svd(A)
null_space = Vh[rank:].T
print("\nNull space basis vector (showing the relationship):")
print(null_space)