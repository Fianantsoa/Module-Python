#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name: str = name
        self.height: float = height
        self.age_day: int = age
        self.evolution: float = height / age
        print("Created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_day} days old")

    def age(self) -> None:
        self.age_day += 1

    def grow(self) -> None:
        self.height = round(self.evolution * self.age_day, 1)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants: list[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
