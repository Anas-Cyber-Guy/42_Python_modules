#!/usr/bin/env python3

def input_temperature(temp_str):
    """
    Converts input string to an integer.
    Handles the case when conversion fails.
    """
    try:
        return int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid temperature number.")
        return None


def test_temperature():
    """
    Performs specific required tests on input_temperature()
    """
    print("=== Testing Smart Agriculture Data Validation ===")

    print("\nTesting valid input:")
    res1 = input_temperature("25")
    if res1 is not None:
        print(f"Successfully processed temperature: {res1}")

    print("\nTesting invalid input:")
    input_temperature("abc")


if __name__ == "__main__":
    test_temperature()
