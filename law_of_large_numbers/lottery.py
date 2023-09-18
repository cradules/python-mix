import random


# Generate a unique combination of 6 numbers between 1 and 49
def generate_combination():
    return random.sample(range(1, 50), 6)


# Simulate playing the lottery with a given number of plays and target combinations
def simulate_lottery(num_plays, target_combinations):
    # Convert target combinations to a set for faster membership checking
    winning_combinations = set(target_combinations)
    num_wins = 0

    # Perform the lottery simulation
    for _ in range(num_plays):
        played_combination = generate_combination()
        # Check if any number in the played combination matches a winning number
        if any(num in winning_combinations for num in played_combination):
            num_wins += 1

    # Calculate the probability of winning
    probability_of_win = num_wins / num_plays
    return probability_of_win


# List of target combinations you want to simulate winning
target_combinations = [[4, 5, 6], [10, 20, 30], [15, 25, 35]]  # Replace with your desired target combinations

# Number of plays to simulate
num_plays = 1000000  # You can adjust the number of plays

total_probability = 0

# Simulate and calculate probabilities for each target combination
for combination in target_combinations:
    probability = simulate_lottery(num_plays, combination)
    total_probability += probability
    print(f"Probability of winning {combination}: {probability:.4f}")

# Calculate the average probability across all target combinations
average_probability = total_probability / len(target_combinations)
print(f"\nAverage Probability: {average_probability:.4f}")
