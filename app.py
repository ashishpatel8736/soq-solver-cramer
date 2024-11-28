import streamlit as st  # type: ignore
import numpy as np  # type: ignore
from fractions import Fraction  # Import fractions module

# Function to compute determinant manually with Fractions
def compute_determinant(matrix):
    """Recursively compute determinant using Fractions for exact arithmetic."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        # Determinant of a 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive expansion along the first row
    determinant = Fraction(0)
    for col in range(n):
        sub_matrix = [
            [matrix[row][c] for c in range(n) if c != col]
            for row in range(1, n)
        ]
        determinant += (
            (-1) ** col * matrix[0][col] * compute_determinant(sub_matrix)
        )
    return determinant

# Solve system of equations using Cramer's Rule with fractional output
def cramer_rule_fractions(coeff_matrix, const_matrix):
    try:
        # Convert input matrix and constants to Fractions
        A = [[Fraction(num).limit_denominator() for num in row] for row in coeff_matrix]
        B = [Fraction(num).limit_denominator() for num in const_matrix]

        det_A = compute_determinant(A)

        if det_A == 0:
            return "The system is unsolvable (determinant is zero)."

        solutions = []
        n = len(A)
        for i in range(n):
            Ai = [row.copy() for row in A]
            for row_idx in range(n):
                Ai[row_idx][i] = B[row_idx]  # Replace the i-th column with the constants vector
            det_Ai = compute_determinant(Ai)
            fraction_solution = Fraction(det_Ai, det_A).limit_denominator()  # Fractional form
            solutions.append(fraction_solution)

        return solutions

    except Exception as e:
        return str(e)

# Helper function to format fractions for LaTeX
def format_fraction(num):
    """Convert Fraction object to LaTeX format."""
    if isinstance(num, Fraction):
        if num.denominator == 1:  # If the fraction is actually an integer
            return str(num.numerator)
        else:
            return f"\\frac{{{num.numerator}}}{{{num.denominator}}}"
    return str(num)

# App title and description
st.title("📊 System of Equations Solver using Cramer's Rule (Fractional Outputs)")
st.markdown("""
This app helps you solve systems of linear equations using **Cramer's Rule**.  
You can enter the coefficients in a square matrix and constants in a column vector. The app will display the matrix and equations, and solve the system for you.
""")

# Step 1: Input the number of variables
num_vars = st.slider("Select the number of variables:", min_value=2, max_value=10, value=3, step=1)

# Generate variable names dynamically (e.g., x, y, z, ...)
variable_names = ["x", "y", "z", "w", "v", "u", "p", "q", "r", "s"][:num_vars]

# Step 2: Input the coefficient matrix
st.subheader("Coefficient Matrix (A)")
st.markdown("Enter the coefficients of the equations in the matrix below:")

coeff_matrix = np.zeros((num_vars, num_vars))  # Initialize a square matrix

# Create a square grid for the coefficient matrix input
matrix_container = st.container()
with matrix_container:
    for i in range(num_vars):
        cols = st.columns(num_vars)
        for j in range(num_vars):
            coeff_matrix[i, j] = cols[j].number_input(f"A[{i+1}][{j+1}]", value=0.0, step=1.0, format="%.2f", key=f"coeff_{i}_{j}")

# Step 3: Input the constant vector
st.subheader("Constant Vector (B)")
st.markdown("Enter the constants on the right-hand side of the equations:")

const_vector = np.zeros(num_vars)  # Initialize a constant vector
cols = st.columns(num_vars)

# Create an input row for the constants
for i in range(num_vars):
    const_vector[i] = cols[i].number_input(f"B[{i+1}]", value=0.0, step=1.0, format="%.2f", key=f"const_{i}")

# Step 4: Display matrices and AX = B
st.subheader("System Representation: \(AX = B\)")
latex_matrix_a = "\\begin{bmatrix}" + " \\\\ ".join(
    [" & ".join(map(str, row)) for row in coeff_matrix]
) + "\\end{bmatrix}"

latex_vector_x = "\\begin{bmatrix}" + " \\\\ ".join(variable_names) + "\\end{bmatrix}"

latex_vector_b = "\\begin{bmatrix}" + " \\\\ ".join(map(str, const_vector)) + "\\end{bmatrix}"

st.latex(f"{latex_matrix_a} \\cdot {latex_vector_x} = {latex_vector_b}")

# Step 5: Solve the system using Cramer's Rule with fractional outputs
if st.button("🔍 Solve"):
    # Validate the inputs
    if len(coeff_matrix) != num_vars or any(len(row) != num_vars for row in coeff_matrix) or len(const_vector) != num_vars:
        st.error("❌ Error: Please ensure the input matrix and vector have the correct dimensions.")
    else:
        # Call the Cramer's Rule function
        solution = cramer_rule_fractions(coeff_matrix.tolist(), const_vector.tolist())
        
        if isinstance(solution, str):  # Error message
            st.error(solution)
        else:  # Display solution
            st.success("✅ Solution Found!")
            st.markdown("The solutions for the variables are:")
            for i, val in enumerate(solution):
                st.latex(f"{variable_names[i]} = {format_fraction(val)}")

# Footer
# Displaying main message
st.markdown("<h1 style='text-align: center;'>Developed with ❤️ using Streamlit</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Supports systems up to 10 variables</h3>", unsafe_allow_html=True)

# Adding a separator
st.markdown("---")

# Footer with developer and technology stack
st.markdown("""
<div style='text-align: center;'>
    <p><strong>Developed by <a href='https://github.com/ashishpatel8736' target='_blank'>Ashish Patel</a></strong></p>
    <p>Powered by <strong>Streamlit</strong></p>
</div>
""", unsafe_allow_html=True)

