#Find power of a number

class PowerCalculator:
    MOD = 10**9 + 7

    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def calculate_power_mod(animal):
        result = 1
        base = animal.base % PowerCalculator.MOD
        exponent = animal.exponent
        while exponent:
            if exponent % 2:
                result = (result * base) % PowerCalculator.MOD
            exponent //= 2
            base = (base * base) % PowerCalculator.MOD
        return result

if __name__ == "__main__":
    # Get input from the user
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent number: "))

    # Create an instance of the PowerCalculator class
    calculator = PowerCalculator(base, exponent)

    # Calculate and print the result
    print("Result:", PowerCalculator.calculate_power_mod(calculator))
