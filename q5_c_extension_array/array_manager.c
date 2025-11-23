#include <Python.h>
#include <stdlib.h>

// Global pointer to the array
static int *int_array = NULL;
static int array_size = 0;

// Initialize the array
static PyObject *method_init(PyObject *self, PyObject *args) {
  int size;
  if (!PyArg_ParseTuple(args, "i", &size)) {
    return NULL;
  }

  if (int_array != NULL) {
    free(int_array);
  }

  int_array = (int *)malloc(size * sizeof(int));
  if (int_array == NULL) {
    return PyErr_NoMemory();
  }

  array_size = size;

  // Initialize with zeros
  for (int i = 0; i < size; i++) {
    int_array[i] = 0;
  }

  Py_RETURN_NONE;
}

// Set a value in the array
static PyObject *method_set(PyObject *self, PyObject *args) {
  int index, value;
  if (!PyArg_ParseTuple(args, "ii", &index, &value)) {
    return NULL;
  }

  if (int_array == NULL) {
    PyErr_SetString(PyExc_RuntimeError, "Array not initialized");
    return NULL;
  }

  if (index < 0 || index >= array_size) {
    PyErr_SetString(PyExc_IndexError, "Index out of bounds");
    return NULL;
  }

  int_array[index] = value;
  Py_RETURN_NONE;
}

// Get a value from the array
static PyObject *method_get(PyObject *self, PyObject *args) {
  int index;
  if (!PyArg_ParseTuple(args, "i", &index)) {
    return NULL;
  }

  if (int_array == NULL) {
    PyErr_SetString(PyExc_RuntimeError, "Array not initialized");
    return NULL;
  }

  if (index < 0 || index >= array_size) {
    PyErr_SetString(PyExc_IndexError, "Index out of bounds");
    return NULL;
  }

  return PyLong_FromLong(int_array[index]);
}

// Free the array
static PyObject *method_free(PyObject *self, PyObject *args) {
  if (int_array != NULL) {
    free(int_array);
    int_array = NULL;
    array_size = 0;
  }
  Py_RETURN_NONE;
}

static PyMethodDef ArrayMethods[] = {
    {"init", method_init, METH_VARARGS, "Initialize the array with a size."},
    {"set", method_set, METH_VARARGS, "Set a value at an index."},
    {"get", method_get, METH_VARARGS, "Get a value at an index."},
    {"free", method_free, METH_VARARGS, "Free the array memory."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef arraymodule = {
    PyModuleDef_HEAD_INIT, "array_manager",
    "A module to manage a simple integer array.", -1, ArrayMethods};

PyMODINIT_FUNC PyInit_array_manager(void) {
  return PyModule_Create(&arraymodule);
}
