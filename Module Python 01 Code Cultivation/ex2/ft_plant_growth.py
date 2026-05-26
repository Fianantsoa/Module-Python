#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name: str = name
        self.height: float = height
        self.age_day: int = age
        self.evolution: float = height / age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_day} days old")

    def age(self) -> None:
        self.age_day += 1

    def grow(self) -> None:
        self.height = round(self.evolution * self.age_day, 1)


if __name__ == "__main__":
    week: int = 7
    print("=== Garden Plant Growth ===")
    p = Plant("Rose", 25.0, 30)
    p.show()
    for i in range(week):
        print(f"=== Day {i + 1} ===")
        p.age()
        p.grow()
        p.show()
    print(f"Growth this week: {round(p.evolution * week, 1)}cm")
