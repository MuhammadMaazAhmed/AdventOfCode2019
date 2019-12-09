def calculate_fuel(mass):
    fuel = (int(mass)//3) - 2
    return (fuel)

def cumulative_fuel(filename):
    required_fuel=0
    with open(filename) as f:
        for module in f:
            required_fuel+= calculate_fuel(module)
    return (required_fuel)
    