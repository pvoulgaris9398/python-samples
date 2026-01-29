from cvxopt import matrix, solvers

"""
Notes:
One-dimensional matrix is otherwise known as a vector (an array)
Two-dimensional matrix is a rectangular two-dimensional grid of numbers
N-dimensional matrix (where N > 2) is otherwise known as a Tensor

Scalar  ==> Rank 0 (zero) ==> single number
Vector  ==> Rank 1        ==> 1-dimensional array
Matrix  ==> Rank 2        ==> 2-dimensional array or table
Tensor  ==> Rank 3        ==> n-dimensional "array"

"""

"""
Cost Function
(Linear Cost Vector)

2 * x1 + (1) * x2

"""
c = matrix([2.0, 1.0])

"""
Constraints
(Coefficients in parenthesis)
(Linear Inequality Constraint Matrix)

(-1) * x1 + (+1) * x2 <= [1]
(+1) * x1 + (+1) * x2 >= 2 ===> (-1) * x1 + (-1) * x2 <= [-2] (make less than or equal to)
(0)  * x1 + (+1) * x2 >= 0 ===> (0)  * x1 + (-1) * x2 <= [0]  (same as above)
(+1) * x1 + (-2) * x2 <= [4]

"""  # noqa
G = matrix([[-1.0, -1.0, 0.0, 1.0], [1.0, -1.0, -1.0, -2.0]])

"""
Linear Inequality Constraint Vector
"""
h = matrix([1.0, -2.0, 0.0, 4.0])

solution = solvers.lp(c, G, h)

if solution["status"] == "optimal":
    print("Optimal Solution found:")
    print(f"x1: {solution['x'][0]:.2e}")
    print(f"x2: {solution['x'][1]:.2e}")
    print(f"Minimum Cost: {solution['primal objective']:.2e}")
else:
    print(f"Solution Status: {solution['status']}")
