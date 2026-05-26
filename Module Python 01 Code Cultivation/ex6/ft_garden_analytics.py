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
        if self._age == 0:
            self.evolution: float = 0.0
        else:
            self.evolution = self._height / self._age
        self.stats = Plant.Stats(self)

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
            print(f"Age updated: {self._age} day")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        self.stats.set_show_calls()
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def age(self) -> None:
        self.stats.set_age_calls()
        self._age += 1

    def grow(self) -> None:
        self.stats.set_grow_calls()
        self._height = round(self.evolution * self._age, 1)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self, plant: "Plant"):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._plant = plant

        def set_grow_calls(self) -> None:
            self._grow_calls += 1

        def set_age_calls(self) -> None:
            self._age_calls += 1

        def set_show_calls(self) -> None:
            self._show_calls += 1

        def get_grow_calls(self) -> int:
            return self._grow_calls

        def get_age_calls(self) -> int:
            return self._age_calls

        def get_show_calls(self) -> int:
            return self._show_calls

        def display(self) -> None:
            print(f"[statistics for {self._plant.name}]")
            print(f"Stats: {self.get_grow_calls()} grow,", end="")
            print(f" {self.get_age_calls()} age,", end="")
            print(f" {self.get_show_calls()} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str):
        super().__init__(name, height, age)
        self.color = color
        self.show()
        print(f" {self.name} has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

    def grow(self) -> None:
        super().grow()
        self._height = self.get_height() + 8

    def bloom(self) -> None:
        print(f" {self.name} is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str):
        super().__init__(name, height, age, color)
        self.number_seeds = 0
        self.evolution = 1.57
        print(f" Seeds: {self.number_seeds}")

    def age(self) -> None:
        self.stats.set_age_calls()
        self._age += 20

    def bloom(self) -> None:
        self.number_seeds += 42
        super().bloom()
        print(f" Seeds: {self.number_seeds}")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self, plant: "Tree"):
            super().__init__(plant)
            self._produce_shade_calls = 0

        def set_produce_shade_calls(self) -> None:
            self._produce_shade_calls += 1

        def get_produce_shade_calls(self) -> int:
            return self._produce_shade_calls

        def display(self) -> None:
            super().display()
            print(f" {self.get_produce_shade_calls()} shade")

    def __init__(self, name: str, height: float, age: int,
                 t_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = t_diameter
        self.stats: Tree.Stats = Tree.Stats(self)
        self.show()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end="")
        print(f"{self._height}cm long and {self.trunk_diameter}cm wide.")
        self.stats.set_produce_shade_calls()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        self.evolution = 1.566
        self.show()

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def display_stat(plant: Plant) -> None:
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is {30} days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is {400} days more than a year? -> ", end="")
    print(f"{Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    display_stat(flower)
    print("[asking the rose to grow and bloom]")
    flower.grow()
    flower.show()
    flower.bloom()
    display_stat(flower)
    print()

    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    display_stat(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    display_stat(tree)
    print()

    print("=== Seed")
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    print("[make sunflower grow, age and bloom]")
    seed.age()
    seed.grow()
    seed.show()
    seed.bloom()
    display_stat(seed)
    print()

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_stat(anonymous)
