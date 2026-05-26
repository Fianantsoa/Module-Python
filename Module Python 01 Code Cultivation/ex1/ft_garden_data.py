#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    p1.show()
    p2 = Plant("Sunflower", 80, 45)
    p2.show()
    p3 = Plant("Cactus", 15, 120)
    p3.show()
