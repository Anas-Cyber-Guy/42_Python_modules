#!/usr/bin/env python3

def input_temperature(temp_str):
    """
    Check if temperature string is valid and within reasonable range (0-40)
    Raises a ValueError if parsing fails or if the temp is out of bounds.
    """
    try:
        num = int(temp_str)
    except ValueError as e:
        raise ValueError(e)

    if num < 0:
        raise ValueError(f"{num}°C is too cold for plants (min 0°C)")
    elif num > 40:
        raise ValueError(f"{num}°C is too hot for plants (max 40°C)")

    return num


def test_temperature():
    """
    Test temperature checking with various input values
    """
    print("=== Garden Temperature Checker ===")

    print("Input data is '25'")
    try:
        res1 = input_temperature("25")
        print(f"Temperature is now {res1}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("Input data is '100'")
    try:
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("Input data is '-50'")
    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
