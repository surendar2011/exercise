class Solution:
    def reverse_digit(self, N):
        # Convert N to a string, reverse it, and remove leading zeroes
        reversed_str = str(N)[::-1].lstrip('0')
        
        # Convert the reversed string back to an integer
        reversed_num = int(reversed_str)
        
        return reversed_num

if __name__ == '__main__':
    # Prompt the user to input the value of N
    N = int(input("Enter a number: "))
    
    # Create an instance of the Solution class
    ob = Solution()
    
    # Call the reverse_digit method to reverse the digits of N and print the result
    print(ob.reverse_digit(N))
