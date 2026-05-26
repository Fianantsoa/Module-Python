
def ft_water_reminder() -> None:
    last_waterning: int = int(input("Days since last watering: "))
    if last_waterning > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
