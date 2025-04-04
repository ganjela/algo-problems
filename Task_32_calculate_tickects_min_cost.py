def calculate_min_cost(days, costs):
    days_set = set(days)
    cache = {}

    def calculate(day):
        if day > days[-1]:
            return 0

        if day in cache:
            return cache[day]

        if day in days_set:
            cache[day] = min(costs[0] + calculate(day + 1), costs[1] + calculate(day + 7), costs[2] + calculate(day + 30))
        else:
            cache[day] = calculate(day + 1)

        return cache[day]

    return calculate(1)