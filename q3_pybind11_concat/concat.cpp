#include <pybind11/pybind11.h>
#include <string>

namespace py = pybind11;

std::string concatenate(const std::string &s1, const std::string &s2) {
  return s1 + s2;
}

PYBIND11_MODULE(concat_module, m) {
  m.doc() = "pybind11 example plugin"; // optional module docstring
  m.def("concatenate", &concatenate,
        "A function that concatenates two strings");
}
