# C/C++/Python Integration Assignment

This repository contains solutions for the C/C++/Python integration assignment. Each part is located in its own directory with source code, build scripts, and test scripts.

## Project Structure

### Q1: C Extension - Square Function
- **Directory**: `q1_c_extension_square`
- **Files**: `square.c`, `setup.py`, `test_q1.py`
- **Description**: A C extension module that calculates the square of a number.
- **Usage**:
  ```bash
  cd q1_c_extension_square
  python3 setup.py build_ext --inplace
  python3 test_q1.py
  ```

### Q2: Ctypes - String Manipulation
- **Directory**: `q2_ctypes_string`
- **Files**: `string_utils.c`, `compile.sh`, `test_q2.py`
- **Description**: A shared library loaded via ctypes to reverse a string.
- **Usage**:
  ```bash
  cd q2_ctypes_string
  bash compile.sh
  python3 test_q2.py
  ```

### Q3: Pybind11 - String Concatenation
- **Directory**: `q3_pybind11_concat`
- **Files**: `concat.cpp`, `setup.py`, `test_q3.py`
- **Description**: A C++ extension using pybind11 to concatenate two strings.
- **Usage**:
  ```bash
  cd q3_pybind11_concat
  python3 setup.py build_ext --inplace
  python3 test_q3.py
  ```

### Q4: Explanation
- **Directory**: `q4_explanation`
- **Files**: `explanation.md`
- **Description**: An explanation comparing ctypes and extension modules.

### Q5: C Extension - Array Management
- **Directory**: `q5_c_extension_array`
- **Files**: `array_manager.c`, `setup.py`, `test_q5.py`
- **Description**: A C extension to manage a simple integer array (init, set, get, free).
- **Usage**:
  ```bash
  cd q5_c_extension_array
  python3 setup.py build_ext --inplace
  python3 test_q5.py
  ```