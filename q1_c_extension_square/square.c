#include <Python.h>

// Function to calculate square
static PyObject* method_square(PyObject* self, PyObject* args) {
    double number;
    // Parse arguments: "d" means expect a double
    if (!PyArg_ParseTuple(args, "d", &number)) {
        return NULL;
    }
    return PyFloat_FromDouble(number * number);
}

// Method definition
static PyMethodDef SquareMethods[] = {
    {"square", method_square, METH_VARARGS, "Calculate the square of a number."},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef squaremodule = {
    PyModuleDef_HEAD_INIT,
    "square_module", // Module name
    "A module that calculates the square of a number.", // Module documentation
    -1,
    SquareMethods
};

// Module initialization
PyMODINIT_FUNC PyInit_square_module(void) {
    return PyModule_Create(&squaremodule);
}
