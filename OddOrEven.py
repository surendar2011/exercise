class OddEvenChecker:
    def check_odd_even(self, N):
        # Check if N is divisible by 2 to determine if it's even or odd
        if N % 2 == 0:
            return "The number is even"  # Return this message if N is even
        else:
            return "The number is odd"   # Return this message if N is odd

if __name__ == '__main__':
    # Create an object of the OddEvenChecker class
    ob = OddEvenChecker()
    
    # Prompt the user to enter a number
    N = int(input("Enter a number: "))
    
    # Call the check_odd_even method to determine if the number is odd or even
    result = ob.check_odd_even(N)
    
    # Print the result
    print(result)