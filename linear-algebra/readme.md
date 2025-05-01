# Matrix Operations and Null Space Exploration

This project demonstrates matrix operations and linear algebra concepts implemented both with NumPy and from scratch to help build intuition.

## What is a Null Space?

The null space (or kernel) of a matrix A is the set of all vectors x such that Ax = 0. In other words, it's the set of all solutions to the homogeneous system of linear equations represented by the matrix.

The null space reveals important information about linear dependencies between variables in a dataset:
- If the null space contains non-zero vectors, there are linear relationships between columns
- The dimension of the null space (nullity) tells us how many independent relationships exist
- Each basis vector in the null space represents a specific relationship

## Implementation Comparison

The repository contains two implementations:
1. `matrix.py`: Uses NumPy's built-in linear algebra functions
2. `matrix-step-by-step.py`: Implements the same operations manually for better understanding

### Example: Finding the Null Space

For the matrix:
```
A = [
    [1, 2, 5],
    [2, 4, 6],
    [3, 6, 7]
]
```

We found that:
- The matrix has rank 2
- The nullity is 1 (meaning there's one linear relationship)
- The null space has one basis vector

### Why the Results Look Different

The null space vectors from the two implementations look different but represent the same relationship:

| Implementation | Null Space Vector |
|----------------|-------------------|
| NumPy (SVD)    | `[-8.94427191e-01, 4.47213595e-01, -1.02948341e-16]` |
| From scratch   | `[-2.0, 1, 0]` |

The differences are due to:

1. **Scaling**:
   - NumPy normalizes vectors to unit length (magnitude = 1)
   - Our implementation uses simpler scaling where the free variable is set to 1

2. **Mathematical equivalence**:
   - If we calculate the ratio in NumPy's vector: `-0.894/0.447 ≈ -2`
   - Our vector has ratio: `-2/1 = -2`
   - Both describe the same relationship: `Var2 = 2 × Var1`

3. **Numerical precision**:
   - NumPy has a tiny non-zero value for Var3 (`-1.02948341e-16`) due to floating-point arithmetic
   - Our implementation has exactly 0 for Var3

## Interpretation

In our example matrix, we discovered that `Var2 = 2 × Var1`, which matches what we can see in the original data. This is useful for:

- Discovering hidden patterns in data
- Dimensionality reduction
- Feature engineering
- Understanding multicollinearity in regression

## Getting Started

1. Set up the environment using `setup.sh` (macOS/Linux) or `setup.bat` (Windows)
2. Run the implementations:
   ```
   python3 linear-algebra/matrix.py
   python3 linear-algebra/matrix-step-by-step.py
   ```