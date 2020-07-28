from pandas import Series


def main():
    # in inches
    hourly_rainfall_data = Series([
        0, 0.1, 0.1, 0.2, 0.2, 0.3, 0.1, 0.3, 0.1, 0.1, 0.1])


def calclate_tank_volume(previous_tank_volume: float,
                         inflow: float,
                         demand: float,
                         storage_capacity: float,
                         yield_after_spillage: bool = True) -> float:
    theta = 0 if yield_after_spillage else 1
    current_yield = calculate_yield(
        previous_tank_volume, inflow, demand, theta)
    return min([
        (previous_tank_volume + inflow - (theta * demand)) -
        (1 - theta) * current_yield,
        storage_capacity - (1 - theta) * current_yield
    ])


def calculate_yield(previous_tank_volume: float,
                    inflow: float,
                    demand: float,
                    theta: int) -> float:
    return min([demand, previous_tank_volume + (theta * inflow)])


if __name__ == '__main__':
    main()
