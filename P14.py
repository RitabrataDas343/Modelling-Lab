import random

def play_round(p_A, p_B):
    choices_A = ["Rock", "Paper", "Scissors"]
    choices_B = ["Rock", "Paper", "Scissors"]
    
    choice_A = random.choices(choices_A, weights=p_A)[0]
    choice_B = random.choices(choices_B, weights=p_B)[0]
    
    if (choice_A == "Rock" and choice_B == "Scissors") or \
       (choice_A == "Paper" and choice_B == "Rock") or \
       (choice_A == "Scissors" and choice_B == "Paper"):
        return 1
    elif choice_A == choice_B:
        return 0
    else:
        return -1

def calculate_expected_utilities(p_A, p_B, num_rounds=10000):
    total_utility_A = 0
    total_utility_B = 0
    
    for _ in range(num_rounds):
        utility = play_round(p_A, p_B)
        total_utility_A += utility
        total_utility_B -= utility  # Symmetric game
    
    expected_utility_A = total_utility_A / num_rounds
    expected_utility_B = total_utility_B / num_rounds
    
    return expected_utility_A, expected_utility_B

def print_payoff_matrix(payoff_matrix):
    for i in range(len(payoff_matrix)):
        for j in range(len(payoff_matrix[i])):
            print(payoff_matrix[i][j], end="    ")
        print()

payoff_matrix=[[(-1,-1),(1,0),(0,1)],[(0,1),(-1,-1),(1,0)],[(1,0),(0,1),(-1,-1)]]
print("Name: Ritabrata Das\nRoll Number: 20CS8002\n")
print('-'*40)
print("The payoff matrix:")
print_payoff_matrix(payoff_matrix)
print('-'*40)

# Initial mixed strategies for players A and B
p_A = [0.4, 0.3, 0.3]  # Initial probabilities for Rock, Paper, and Scissors
p_B = [0.3, 0.4, 0.3]  # Initial probabilities for Rock, Paper, and Scissors

expected_utility_A, expected_utility_B = calculate_expected_utilities(p_A, p_B)
print("\nAfter 10000 rounds: ")

print("Expected Utility for Player A:", expected_utility_A)
print("Expected Utility for Player B:", expected_utility_B)