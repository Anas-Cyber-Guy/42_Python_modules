#!/usr/bin/env python3

class PlantError(Exception):
    """Custom exception for problems with plants."""
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name):
    """
    Tries to water a plant. Succeeds if the name is capitalized.
    Raises a PlantError if it is not capitalized.
    """
    if plant_name == str.capitalize(plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system():
    """
    Simulates watering tests. Uses a try-except-finally architecture to
    ensure the irrigation hardware layer closes safely under all conditions.
    """
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
    print("Cleanup always happens, even with errors!")
