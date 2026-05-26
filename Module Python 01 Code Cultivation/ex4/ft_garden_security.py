#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name: str = name
        self._height: float = 0
        self._age = 0
        self._initialized = False
        self.set_height(height)
        self.set_age(age)
        self._initialized = True
        self.evolution: float = self._height / self._age
        print("Plant created: ", end="")
        self.show()

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = new_height
        if self._initialized:
            print(f"Height updated: {self._height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = new_age
        if self._initialized:
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def age(self) -> None:
        self._age += 1

    def grow(self) -> None:
        self._height = round(self.evolution * self._age, 1)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print()
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-25)
    plant.set_age(-30)
    print()
    print(f"Current state: {plant.name}: {plant.get_height()}cm,", end="")
    print(f" {plant.get_age()} days old")
