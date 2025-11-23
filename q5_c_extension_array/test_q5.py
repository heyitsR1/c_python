import sys
import os

sys.path.append(os.getcwd())

try:
    import array_manager
    print("Module imported successfully.")
except ImportError as e:
    print(f"Failed to import module: {e}")
    sys.exit(1)

def test_array_manager():
    print("Initializing array of size 10...")
    array_manager.init(10)
    
    print("Setting index 0 to 100...")
    array_manager.set(0, 100)
    
    print("Setting index 5 to 55...")
    array_manager.set(5, 55)
    
    val0 = array_manager.get(0)
    print(f"Index 0: {val0}")
    assert val0 == 100, f"Expected 100, got {val0}"
    
    val5 = array_manager.get(5)
    print(f"Index 5: {val5}")
    assert val5 == 55, f"Expected 55, got {val5}"
    
    val9 = array_manager.get(9)
    print(f"Index 9: {val9}")
    assert val9 == 0, f"Expected 0 (default), got {val9}"
    
    print("Testing out of bounds...")
    try:
        array_manager.get(10)
    except IndexError:
        print("Caught expected IndexError for out of bounds access.")
    except Exception as e:
        print(f"Caught unexpected exception: {e}")
        
    print("Freeing array...")
    array_manager.free()
    
    print("Testing access after free...")
    try:
        array_manager.get(0)
    except RuntimeError:
        print("Caught expected RuntimeError for uninitialized access.")
    except Exception as e:
        print(f"Caught unexpected exception: {e}")

    print("All tests passed!")

if __name__ == "__main__":
    test_array_manager()
