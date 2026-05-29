#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    values_test: list[str] = ["25", "abc"]
    print("=== Garden Temperature ===\n")
    for value_test in values_test:
        print(f"Input data is '{value_test}'")
        try:
            temp = input_temperature(value_test)
        except ValueError as e:
            print("Caught input_temperature error: ", end="")
            print(f"{e}")
        else:
            print(f"Temperature is now {temp}°C\n")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
