import ctypes
import os
import sys

# Load the shared library
lib_path = os.path.join(os.getcwd(), 'libstringutils.so')
try:
    lib = ctypes.CDLL(lib_path)
except OSError as e:
    print(f"Failed to load library: {e}")
    sys.exit(1)

# Define the function signature
# char* reverse_string(char* str)
lib.reverse_string.argtypes = [ctypes.c_char_p]
lib.reverse_string.restype = ctypes.c_char_p

def test_reverse_string():
    original = "Hello, World!"
    # We need to create a mutable buffer because Python strings are immutable
    # and the C function modifies the string in place.
    # create_string_buffer creates a mutable char array.
    input_str = ctypes.create_string_buffer(original.encode('utf-8'))
    
    print(f"Original: {input_str.value.decode('utf-8')}")
    
    result_ptr = lib.reverse_string(input_str)
    
    # result_ptr points to the same buffer as input_str
    result = ctypes.c_char_p(result_ptr).value.decode('utf-8')
    
    print(f"Reversed: {result}")
    
    expected = original[::-1]
    assert result == expected, f"Expected {expected}, got {result}"
    print("Test passed!")

if __name__ == "__main__":
    test_reverse_string()
