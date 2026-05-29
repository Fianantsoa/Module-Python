#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name: str | None = None):
        if name is None:
            message = "Unknown plant error"
        else:
            message = f"Invalid plant name to water: '{name}'"
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(plant_name)
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    print("Opening watering system")
    plants_valid: list[str] = ["Tomato", "Lettuce", "Carrots"]
    try:
        for plant in plants_valid:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    plants_invalid: list[str] = ["Tomato", "lettuce", "Carrots"]
    try:
        for plant in plants_invalid:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    test_watering_system()
    print("Cleanup always happens, even with errors!")
