# Math-in-AI

This repository contains implementation examples and code supporting the blog posts in my "Mathematics for AI" series.

## Overview

The purpose of this repository is to provide hands-on, practical implementations of mathematical concepts essential for understanding AI and machine learning algorithms.

## Course Topics and Progress

| Week | Topic | Subtopics | Blog Post | Code Examples | Status |
|------|-------|-----------|-----------|---------------|--------|
| 1 | **Linear Algebra** | Vectors, matrices, matrix-vector products | [Part 1](https://dineshkumars.dev/blog/2025/05/01/linear-algebra-part-1/) | [matrix.py](linear-algebra/matrix.py), [matrix-step-by-step.py](linear-algebra/matrix-step-by-step.py) | ✅ |
| 1 | **Linear Algebra** | Rank, null space, solution of equations | [Part 1](https://dineshkumars.dev/blog/2025/05/01/linear-algebra-part-1/) | [matrix.py](linear-algebra/matrix.py), [matrix-step-by-step.py](linear-algebra/matrix-step-by-step.py) | ✅ |
| 1 | **Linear Algebra** | Pseudo-inverse | - | - | ⬜️ |
| 1 | **Linear Algebra** | Distance, projections | - | - | ⬜️ |
| 1 | **Linear Algebra** | Eigenvalue decomposition | - | - | ⬜️ |
| 2 | **Statistics** | Descriptive statistics | - | - | ⬜️ |
| 2 | **Statistics** | Probability concepts | - | - | ⬜️ |
| 2 | **Statistics** | Probability distributions | - | - | ⬜️ |
| 2 | **Statistics** | Mean, variance, covariance | - | - | ⬜️ |
| 2 | **Statistics** | Normal distributions | - | - | ⬜️ |
| 2 | **Statistics** | Hypothesis testing | - | - | ⬜️ |
| 2 | **Statistics** | Confidence intervals | - | - | ⬜️ |
| 3 | **Optimization** | Multivariate optimization | - | - | ⬜️ |
| 3 | **Optimization** | Gradient descent | - | - | ⬜️ |
| 4 | **Linear Regression** | Simple linear regression | - | - | ⬜️ |
| 4 | **Linear Regression** | Regression assumptions | - | - | ⬜️ |
| 4 | **Linear Regression** | Multivariate regression | - | - | ⬜️ |
| 4 | **Linear Regression** | Model assessment | - | - | ⬜️ |
| 4 | **Linear Regression** | Variable importance | - | - | ⬜️ |
| 5 | **Classification** | Cross validation | - | - | ⬜️ |
| 5 | **Classification** | Logistic regression | - | - | ⬜️ |
| 6 | **Classification & Clustering** | k-Nearest Neighbors | - | - | ⬜️ |
| 6 | **Classification & Clustering** | k-means clustering | - | - | ⬜️ |

## Linear Algebra for Data Science

The `linear-algebra` directory contains implementations related to the blog post [Getting a Grip on Linear Algebra for Data Science](https://dineshkumars.dev/blog/2025/05/01/linear-algebra-part-1/) where I explain:

- How matrices are used to organize and represent data
- Understanding matrix rank to determine truly independent features
- Finding relationships between variables using null space and nullity
- Practical applications of linear algebra in machine learning

### Implementations

- `matrix.py`: Implementation using NumPy's built-in functions
- `matrix-step-by-step.py`: Implementation from scratch for better understanding of the concepts
- Detailed explanations in the corresponding `readme.md`

## Getting Started

1. Clone this repository
2. Set up the environment:
   - On macOS/Linux: Run `./setup.sh`
   - On Windows: Run `setup.bat`
3. Navigate to specific directories for examples related to each blog post

## Dependencies

- Python 3.x
- NumPy

## License

All code is available for educational purposes to help learners understand the mathematical foundations of AI.