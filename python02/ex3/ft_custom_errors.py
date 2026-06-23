#!/usr/bin/env python3

class GardenError(Exception):
    """A basic error for garden problems."""
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    """For problems with plants."""
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    """For problems with watering."""
    def __init__(self, message="Unknown watering error"):
        super().__init__(message)


def check_plant_health():
    """Simulates a plant health check and raises a PlantError."""
    raise PlantError("The tomato plant is wilting!")


def check_water_level():
    """Simulates a irrigation check and raises a WaterError."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    """
    Demonstrates catching specific custom error types and shows how
    catching a parent exception automatically catches its children.
    """
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        check_plant_health()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("Testing WaterError...")
    try:
        check_water_level()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    try:
        check_plant_health()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water_level()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()