def lexi_numbers(n):
    return sorted(range(1, n + 1), key=str)

n = 135
sorted_lexi_numbers = lexi_numbers(n)

print("Lexicographical order from 1 to", n, ":", sorted_lexi_numbers)
