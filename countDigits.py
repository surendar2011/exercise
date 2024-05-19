#Count digits in a number(Solving above last digit prob wil make this easy for you)

class Solution:
    def evenlyDivides(self, N):
        n = str(N)  # Convert N to a string
        count = 0   # Initialize the count to 0
        
        for i in n:  # Loop through each digit in the string
            digit = int(i)  # Convert the character to an integer
            
            if digit == 0:
                continue  # Skip if the digit is 0
            elif N % digit == 0:
                count += 1  # Increment the count if N is divisible by the digit
        
        return count

if __name__ == "__main__":
    solution = Solution()
    N = int(input("Enter a number: "))
    print(solution.evenlyDivides(N))  # Output the result
