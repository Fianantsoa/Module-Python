#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name: str | None = None) -> None:
        if name is None:
            message = "Unknown plant error"
        else:
            message = f"The {name} plant is wilting!"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self) -> None:
        message = "Not enough water in the tank!"
        super().__init__(message)


def test_plantError(name: str, temp: float) -> None:
    print("Testing PlantError...")
    try:
        if temp < 0 or temp > 40:
            raise PlantError(name)
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_waterError(water_level: float) -> None:
    print("Testing WaterError...")
    try:
        if water_level < 3 or water_level > 6:
            raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_garden_errors() -> None:
    print("Testing catching all garden errors...")

    errors = [
        ("tomato", "plant"),
        ("tank", "water")
    ]

    for name, error_type in errors:
        try:
            if error_type == "plant":
                raise PlantError(name)
            elif error_type == "water":
                raise WaterError()
        except GardenError as e:
            print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    name: str = "tomato"
    temperature = 50
    water_level = 2
    test_plantError(name, temperature)
    print()
    test_waterError(water_level)
    print()
    test_garden_errors()

    print("\nAll custom error types work correctly!")
