#Reverse a number(Try thinking how you can use above logic in solving this)

class Solution:
    def reverse_digit(self, n):
        # Convert the number to a string
        n_str = str(n)
        
        # Reverse the string
        reversed_str = n_str[::-1]
        
        # Convert the reversed string back to an integer
        reversed_int = int(reversed_str)
        
        # Return the reversed integer
        return reversed_int

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    n = int(input("Enter a number: "))
    print(solution.reverse_digit(n))
