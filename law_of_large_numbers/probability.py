import random
import time

def generate_combination():
    return random.sample(range(1, 50), 6)

def simulate_lottery(num_plays, target_combination):
    wins = 0
    for _ in range(num_plays):
        played_combination = target_combination  # Use the same target combination for each simulation
        if played_combination == target_combination:
            wins += 1
    return wins / num_plays

def calculate_probability(target_combination, num_plays, seed=None):
    random.seed(seed)  # Set the random seed
    probability = simulate_lottery(num_plays, target_combination)
    return probability

target_combination = generate_combination()  # Choose a target combination

# Calculate the probabilities for different numbers of plays with the current time as seed
plays_list = [1000, 10000, 100000, 1000000]
for num_plays in plays_list:
    seed = int(time.time())  # Set the seed to the current time in seconds
    probability = calculate_probability(target_combination, num_plays, seed)
    print(f"Probability of winning {target_combination} in {num_plays} plays: {probability:.6f}")
