#!/usr/bin/env python3

def garden_operations(operation_number):
    """
    Triggers a specific exception based on the operation number.
    Operation 0: ValueError
    Operation 1: ZeroDivisionError
    Operation 2: FileNotFoundError
    Operation 3: TypeError
    """
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "string" + 5


def test_error_types():
    """
    Tests each individual operation to catch errors separately,
    and then demonstrates how to catch multiple errors with one try block.
    """
    print("=== Garden Error Types Demo ===")

    # Test individual errors (Operations 0 to 3)
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    # Test successful operation (Operation 4)
    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully")
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print(f"Caught an unexpected error: {e}")
	
    try:
        garden_operations(1)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        # This confirms we can group different exceptions into a tuple
        pass

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
