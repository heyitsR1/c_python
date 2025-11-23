import sys
import os

# Ensure the current directory is in the path so we can import the built module
# This is handled by running from the directory or installing, but for local testing:
sys.path.append(os.getcwd())

try:
    import square_module
    print("Module imported successfully.")
except ImportError as e:
    print(f"Failed to import module: {e}")
    sys.exit(1)

def test_square():
    val = 5.0
    result = square_module.square(val)
    expected = 25.0
    print(f"square({val}) = {result}")
    assert result == expected, f"Expected {expected}, got {result}"
    
    val = -3.0
    result = square_module.square(val)
    expected = 9.0
    print(f"square({val}) = {result}")
    assert result == expected, f"Expected {expected}, got {result}"

    print("All tests passed!")

if __name__ == "__main__":
    test_square()
