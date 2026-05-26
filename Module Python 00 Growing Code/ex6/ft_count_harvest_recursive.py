
def ft_count_harvest_recursive() -> None:
    def helper(day: int) -> None:
        if day > 0:
            helper(day - 1)
            print("Day ", day)
    count_harvest = int(input("Days until harvest: "))
    helper(count_harvest)
    print("Harvest time!")
