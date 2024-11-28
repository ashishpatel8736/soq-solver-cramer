import streamlit as st # type: ignore
import numpy as np # type: ignore
from solve_cramers_rule import solve_cramers_rule  # Assuming the function is defined separately

# Helper function to format numbers for LaTeX
def format_number(num):
    """Format numbers for LaTeX output: integers without decimal, floats with decimals."""
    if num == int(num):  # If the number is an integer
        return str(int(num))
    else:  # If the number is a float
        return f"{num:.2f}"

# App title and description
st.title("📊 System of Equations Solver using Cramer's Rule")
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
    [" & ".join(map(format_number, row)) for row in coeff_matrix]
) + "\\end{bmatrix}"

latex_vector_x = "\\begin{bmatrix}" + " \\\\ ".join(variable_names) + "\\end{bmatrix}"

latex_vector_b = "\\begin{bmatrix}" + " \\\\ ".join(map(format_number, const_vector)) + "\\end{bmatrix}"

st.latex(f"{latex_matrix_a} \\cdot {latex_vector_x} = {latex_vector_b}")

# Step 5: Display equations
st.subheader("Equations:")
st.markdown("The system of equations is:")
equations = []
for i in range(num_vars):
    equation = " + ".join([f"{format_number(coeff_matrix[i, j])}{variable_names[j]}" for j in range(num_vars)]) + f" = {format_number(const_vector[i])}"
    equations.append(equation)

# Render each equation in LaTeX
for eq in equations:
    st.latex(eq)

# Step 6: Solve the system using Cramer's Rule
if st.button("🔍 Solve"):
    # Validate the inputs
    if len(coeff_matrix) != num_vars or any(len(row) != num_vars for row in coeff_matrix) or len(const_vector) != num_vars:
        st.error("❌ Error: Please ensure the input matrix and vector have the correct dimensions.")
    else:
        # Call the Cramer's Rule function
        solution = solve_cramers_rule(coeff_matrix.tolist(), const_vector.tolist())
        
        if isinstance(solution, str):  # Error message
            st.error(solution)
        else:  # Display solution
            st.success("✅ Solution Found!")
            st.markdown("The solutions for the variables are:")
            for i, val in enumerate(solution):
                st.latex(f"{variable_names[i]} = {format_number(val)}")

# Footer
st.markdown("---")
# st.markdown("Developed with ❤️ using Streamlit. Supports systems up to 10 variables.")
# st.markdown("""
# ---
# **Developed by [Ashish Patel](https://github.com/ashishpatel8736)**  
# Powered by **Streamlit** and **Scikit-learn**.
# """)

# Displaying main message
st.markdown("<h1 style='text-align: center;'>Developed with ❤️ using Streamlit</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Supports systems up to 10 variables</h3>", unsafe_allow_html=True)

# Adding a separator
st.markdown("---")

# Footer with developer and technology stack
st.markdown("""
<div style='text-align: center;'>
    <p><strong>Developed by <a href='https://github.com/ashishpatel8736' target='_blank'>Ashish Patel</a></strong></p>
    <p>Powered by <strong>Streamlit</strong> and <strong>Scikit-learn</strong></p>
</div>
""", unsafe_allow_html=True)
