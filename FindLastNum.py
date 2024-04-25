class Solution:
    def getLastDigit(self, a, b):
        # Convert string inputs to integers
        a = int(a)  # Convert the first input (a) to an integer
        b = int(b)  # Convert the second input (b) to an integer
        
        # Calculate a^b (a raised to the power of b)
        result = a ** b
        
        # Extract the last digit of the result
        last_digit = result % 10  # Get the remainder when dividing the result by 10
        
        return last_digit  # Return the last digit of the result

if __name__ == '__main__':
    # Prompt the user to input the number of test cases
    t = int(input("Enter the number of test cases: "))  # t is the number of test cases
    
    # Loop through each test case
    for _ in range(t):
        # Prompt the user to input values of a and b for the current test case
        a, b = input("Enter values of a and b: ").split()  # a and b are the base and exponent
        
        # Create an instance of the Solution class
        ob = Solution()
        
        # Call the getLastDigit method to calculate and print the last digit of a^b
        print(ob.getLastDigit(a, b))
