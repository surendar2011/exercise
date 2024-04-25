class Solution:
    def countDividingDigits(self, N):
        # Convert the number N to a string to iterate through its digits
        N_str = str(N)
        
        # Initialize a counter to keep track of the number of dividing digits
        count = 0
        
        # Iterate through each digit in N_str
        for digit in N_str:
            # Convert the digit back to an integer
            digit = int(digit)
            # Check if digit evenly divides N (leaves a remainder 0 when divided)
            if digit != 0 and N % digit == 0:
                # If it does, increment the counter
                count += 1
        
        # Return the count of dividing digits
        return count

if __name__ == '__main__':
    # Prompt the user to input the value of N
    N = int(input("Enter a number: "))
    
    # Create an instance of the Solution class
    ob = Solution()
    
    # Call the countDividingDigits method to calculate and print the count of dividing digits
    print(ob.countDividingDigits(N))
