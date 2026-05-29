#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    else:
        return (temp_int)


def test_temperature() -> None:
    values_test: list[str] = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")
    for value_test in values_test:
        print(f"Input data is '{value_test}'")
        try:
            temp = input_temperature(value_test)
        except ValueError as e:
            print("Caught input_temperature error: ", end="")
            print(f"{e}\n")
        else:
            print(f"Temperature is now {temp}°C\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
