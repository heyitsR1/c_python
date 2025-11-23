import sys
import os

# Ensure the current directory is in the path so we can import the built module
sys.path.append(os.getcwd())

try:
    import concat_module
    print("Module imported successfully.")
except ImportError as e:
    print(f"Failed to import module: {e}")
    sys.exit(1)

def test_concat():
    s1 = "Hello, "
    s2 = "World!"
    result = concat_module.concatenate(s1, s2)
    expected = "Hello, World!"
    print(f"concatenate('{s1}', '{s2}') = '{result}'")
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("Test passed!")

if __name__ == "__main__":
    test_concat()
