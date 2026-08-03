# 📊 Functional Treat: Data Analyzer and Transformer Program

A menu-driven, feature-rich Python application designed to analyze, transform, and process 1D and 2D numerical array datasets. This project demonstrates core Python programming concepts including functional programming, recursive logic, global state management, variable-length arguments (`*args`, `**kwargs`), and array formatting.

---

## 🚀 Features

- **Dynamic Data Input:** Accepts user inputs dynamically to build 1D numeric datasets.
- **Statistical Analysis:** Calculates essential statistics like Minimum, Maximum, Total Sum, and Average using built-in Python functions.
- **Global Summary Tracking:** Uses the `global` keyword to maintain a persistent summary state across execution turns.
- **Recursive Factorial Calculation:** Demonstrates recursion by calculating the factorial of non-negative integers.
- **Lambda & Filter Processing:** Efficiently filters data elements based on custom user-defined threshold values.
- **Flexible Data Sorting:** Provides options for sorting data in both Ascending and Descending order (demonstrating in-place `.sort()` and non-destructive `sorted()` functions).
- **Multiple Return Values & Keyword Arguments:** Returns tuples of summary metrics and utilizes `**kwargs` for clean tabular console output.
- **2D Grid Formatter:** Provides a visual tab-formatted display structure for matrix/2D representation.

---

## 🛠️ Python Concepts Covered

| Concept | Description in Project |
| :--- | :--- |
| **Built-in Functions** | `len()`, `min()`, `max()`, `sum()`, `map()`, `filter()` |
| **User-Defined Functions (UDF)** | Modular function design across processing tasks |
| **Variable Arguments** | Demonstrates `*args` and `**kwargs` handling |
| **Recursion** | `calculate_factorial()` function |
| **Lambda Functions** | Inline condition-based data filtering |
| **Global Keyword** | Modifying `global_summary` state from internal scopes |
| **Docstrings (`__doc__`)** | Clear function documentation dynamically fetched in execution |
| **Multiple Return Values** | Tuple unpacking (`min_val, max_val, sum_val, avg_val`) |

---

## 📂 Project Structure

```text
.
├── main.py          # Complete application logic with interactive CLI menu
└── README.md        # Project documentation

==================================================
Welcome to the Data Analyzer and Transformer Program
==================================================
Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
0. Exit Program
==================================================
