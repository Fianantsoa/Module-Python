#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name: str = name
        self._height: float = 0
        self._age = 0
        self.initialized = False
        self.set_height(height)
        self.set_age(age)
        self.initialized = True
        self.evolution: float = self._height / self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = new_height
        if self.initialized:
            print(f"Height updated: {self._height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = new_age
        if self.initialized:
            print(f"Age updated: {self._age} day")

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


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str):
        print("=== Flower")
        super().__init__(name, height, age)
        self.color = color
        self.show()
        print(f" {self.name} has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

    def bloom(self) -> None:
        print(f" {self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 t_diameter: float):
        print("=== Tree")
        super().__init__(name, height, age)
        self.trunk_diameter = t_diameter
        self.show()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str):
        print("=== Vegetable")
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        self.evolution = 1.566
        self.show()

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def grow(self) -> None:
        super().grow()

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    flower_o = Flower("Rose", 15.0, 10, "red")
    print(f"[asking the {flower_o.name.lower()} to bloom]")
    flower_o.show()
    flower_o.bloom()
    print()

    tree_o = Tree("Oak", 200.0, 365, 5.0)
    print(f"[asking the {tree_o.name.lower()} to produce shade]")
    tree_o.produce_shade()
    print()

    vegetable_o = Vegetable("Tomato", 5.0, 10, "April")
    print(f"[make {vegetable_o.name.lower()} grow and age for 20 days]")
    for i in range(20):
        vegetable_o.age()
        vegetable_o.grow()
    vegetable_o.show()
    print()
