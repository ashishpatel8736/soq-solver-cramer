
# **📊 System of Equations Solver using Cramer's Rule**

Welcome to the **System of Equations Solver**! This app, built with [Streamlit](https://streamlit.io/), allows you to solve systems of linear equations using **Cramer's Rule**. You can input your equations in matrix form, visualize them dynamically, and get a step-by-step solution.

---

## 🚀 Features

- **Matrix Representation**:
  - Input your system of equations as a **coefficient matrix (A)** and a **constant vector (B)**.
  - Dynamically display the system in the form \(AX = B\), where:
    - \(A\): Coefficient matrix
    - \(X\): Variables (\(x, y, z, \dots\))
    - \(B\): Constants vector
  - Beautiful LaTeX-rendered matrices and equations.

- **Equation Visualization**:
  - Automatically generates equations from your matrix inputs.
  - Displays them with proper formatting in an easy-to-read form.

- **Dynamic Input Handling**:
  - Supports **integer and float values**:
    - Integers are displayed without decimals (e.g., \(5\)).
    - Floats are displayed with two decimal places (e.g., \(5.20\)).

- **Scalable**:
  - Solve systems with **2 to 10 variables**.
  - Easily adapt to any problem size.

- **Real-time Solutions**
    - Get solutions for \(x, y, z, \dots\) instantly after clicking **"Solve"**.
  - Handles errors gracefully if the system is unsolvable, such as when the determinant of the coefficient matrix is zero.


---

## 🛠️ How It Works

The app solves a system of linear equations using **Cramer's Rule**, a method in linear algebra that calculates solutions by finding determinants of matrices.

The system of equations is represented as:
\[
AX = B
\]

Where:
- \(A\) is the coefficient matrix.
- \(X\) is the variable vector (e.g., \(x, y, z, \dots\)).
- \(B\) is the constant vector.

Using **Cramer's Rule**:
<!-- \[
x_i = rac{	ext{det}(A_i)}{	ext{det}(A)}, \quad i = 1, 2, \dots, n
\] -->
![Cramer's Rule](https://latex.codecogs.com/svg.latex?x_i%20%3D%20%5Cfrac%7B%5Ctext%7Bdet%7D%28A_i%29%7D%7B%5Ctext%7Bdet%7D%28A%29%7D%2C%20i%20%3D%201%2C%202%2C%20%5Cdots%2C%20n)

Here:
- \(	ext{det}(A)\): Determinant of the coefficient matrix.
- \(	ext{det}(A_i)\): Determinant of the matrix \(A\) with the \(i^{th}\) column replaced by the constants vector \(B\).

---

## 🖥️ Screenshots

### 1. Input System of Equations
Input the coefficient matrix (\(A\)) and constants vector (\(B\)) using a simple interface:

![Input Matrix](equation_ss.png)

---

### 2. Visualize \(AX = B\)
View your system of equations in matrix form:

![AX = B Display](ax_b_ss.png)

---

### 3. Solution
Get the solution for \(x, y, z, \dots\) in real-time:

![Solution](solu_ss.png)

---

## 🧑‍💻 Usage

### Prerequisites
- Python 3.7 or higher
- Streamlit library installed

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ashish/soq-solver-cramer.git
   cd system-of-equations-solver
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser at [http://localhost:8501](http://localhost:8501).

---

## 📚 Example Usage

### Example 1: Integer Inputs
System:
\[
2x + y - z = 3
\]
\[
x + y + z = 1
\]
\[
x - 2y - 3z = 4
\]

Input:
\[
A = egin{bmatrix}
2 & 1 & -1 \
1 & 1 & 1 \
1 & -2 & -3
\end{bmatrix}, \quad
B = egin{bmatrix}
3 \
1 \
4
\end{bmatrix}
\]

Solution:
\[
x = 2, \quad y = -1, \quad z = 0
\]

### Example 2: Float Inputs
System:
\[
2.5x + 1.2y - 1.1z = 3.3
\]
\[
x + y + z = 1
\]
\[
x - 2.2y - 3.3z = 4.1
\]

Input:
\[
A = egin{bmatrix}
2.5 & 1.2 & -1.1 \
1.0 & 1.0 & 1.0 \
1.0 & -2.2 & -3.3
\end{bmatrix}, \quad
B = egin{bmatrix}
3.3 \
1.0 \
4.1
\end{bmatrix}
\]

Solution:
\[
x = 2.00, \quad y = -1.00, \quad z = 0.00
\]

---

## 📂 Project Structure

```plaintext

├── README.md                           
├── app.py                  
├── solve_cramers_rule.py   
├── requirements.txt        
├── ax_b_ss.png              
├── LICENSE             
├── equation_ss.png               
├── solu_ss.png
├── icons8-github-50.png                           
```

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or want to improve the app, feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author  
**Ashish Patel**  
[![GitHub](icons8-github-50.png)](https://github.com/ashishpatel8736) | [![LinkedIn](https://img.icons8.com/ios-filled/50/0077b5/linkedin.png)](https://www.linkedin.com/in/ashishpatel8736)

---

## 🌟 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for an interactive interface.
- Inspired by the elegance of **Cramer's Rule** in linear algebra.

---

Enjoy solving your systems of equations effortlessly! 🎉
