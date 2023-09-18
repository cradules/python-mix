import random

def generate_combination():
    return random.sample(range(1, 50), 6)

def simulate_lottery(num_plays, target_combination):
    for _ in range(num_plays):
        played_combination = generate_combination()
        if played_combination == target_combination:
            return True
    return False

def calculate_tickets_for_probability(target_combination, target_probability):
    num_plays = 0
    wins = 0
    while wins / num_plays < target_probability:
        num_plays += 1
        if simulate_lottery(1, target_combination):
            wins += 1
    return num_plays

target_combination = generate_combination()  # Choose a target combination
target_probability = 0.5  # 50% chance of winning

num_tickets = calculate_tickets_for_probability(target_combination, target_probability)
print(f"To have a {target_probability*100}% chance of winning at least once, you need to buy approximately {num_tickets} tickets.")
