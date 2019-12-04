with open('input_day1') as f:
    masses = [int(line) for line in f]

# Part 1
print(sum((mass // 3) - 2 for mass in masses))


# Part 2
def part2_fuel_required(mass):
    fuel = 0
    while True:
        mass = fuel_used = (mass // 3) - 2
        if fuel_used <= 0:
            return fuel
        mass = fuel_used
        fuel += fuel_used


print(sum(part2_fuel_required(mass) for mass in masses))
