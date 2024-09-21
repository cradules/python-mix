class Solution:
    def lexi_numbers_f(self, n):
        # Generate a list of numbers from 1 to n, convert to strings, and sort lexicographically
        return sorted(range(1, n + 1), key=str)


# Sample usage
solution = Solution()
n = 30
sorted_lexi_numbers = solution.lexi_numbers(n)

print("Lexicographical order from 1 to", n, ":", sorted_lexi_numbers)
