import random


# Simulating Coin Tosses and the Law of Large Numbers
# ---------------------------------------------------
# This program simulates coin tosses and demonstrates the Law of Large Numbers.
# The Law of Large Numbers states that as the number of trials (in this case, coin tosses) increases,
# the observed relative frequency of an event (such as getting heads or tails) approaches its true probability.
# In this simulation, we'll toss a fair coin and observe how the proportions of heads and tails converge towards 50%.
# Keep in mind that due to randomness, the proportions won't always be exactly 50%, but they should get closer to it
# as we increase the number of tosses.

def simulate_coin_tosses(num_tosses):
    # Initialize counters for heads and tails
    heads_count = 0
    tails_count = 0

    # Simulate coin tosses
    for _ in range(num_tosses):
        # Generate a random number between 0 and 1
        if random.random() < 0.5:
            heads_count += 1  # If the random number is less than 0.5, count it as a heads
        else:
            tails_count += 1  # Otherwise, count it as a tails

    # Calculate proportions of heads and tails
    proportion_heads = heads_count / num_tosses
    proportion_tails = tails_count / num_tosses

    return proportion_heads, proportion_tails


# Number of tosses to simulate
num_tosses = 1000

# Simulate coin tosses and calculate proportions
proportion_heads, proportion_tails = simulate_coin_tosses(num_tosses)

# Print the results
print(f"Number of tosses: {num_tosses}")
print(f"Proportion of heads: {proportion_heads}")
print(f"Proportion of tails: {proportion_tails}")
