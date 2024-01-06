import random

def run_simulation(payoff_matrix):
    player_a_payoff = 0
    player_b_payoff = 0
    total_rounds = 10

    for round_num in range(total_rounds):
        player_a_choice = random.choice(['C', 'D'])
        player_b_choice = random.choice(['C', 'D'])

        if (player_a_choice == 'C' and player_b_choice == 'C'):
            player_a_payoff += payoff_matrix[0][0]
            player_b_payoff -= payoff_matrix[0][0]
        elif (player_a_choice == 'C' and player_b_choice == 'D'):
            player_a_payoff += payoff_matrix[0][1]
            player_b_payoff -= payoff_matrix[0][1]
        elif (player_a_choice == 'D' and player_b_choice == 'C'):
            player_a_payoff += payoff_matrix[1][0]
            player_b_payoff -= payoff_matrix[1][0]
        elif (player_a_choice == 'D' and player_b_choice == 'D'):
            player_a_payoff += payoff_matrix[1][1]
            player_b_payoff -= payoff_matrix[1][1]

        print(f"Round {round_num + 1} - Player A: {player_a_choice}, Player B: {player_b_choice}")
        print(f"Payoffs - Player A: {player_a_payoff}, Player B: {player_b_payoff}\n")

    average_payoff_a = player_a_payoff / total_rounds
    average_payoff_b = player_b_payoff / total_rounds
    print(f"Average Payoff for Player A: {average_payoff_a}")
    print(f"Average Payoff for Player B: {average_payoff_b}")

    if average_payoff_a > average_payoff_b:
        print("Player A has a higher average payoff, so cooperating may be a better strategy.")
    elif average_payoff_a < average_payoff_b:
        print("Player B has a higher average payoff, so defecting may be a better strategy.")
    else:
        print("Both players have the same average payoff, indicating a balanced strategy.")

print("Name: Ritabrata Das\nRoll Number: 20CS8002\n")

payoff_matrix = list()
rem = list()
a, b = input("If A and B both cooperates, the payoff will be: ").split()
rem.append(int(a)-int(b))
a, b = input("If A cooperates but B defects, the payoff will be: ").split()
rem.append(int(a)-int(b))
payoff_matrix.append(rem)

rem = list()
a, b = input("If B cooperates but A defects, the payoff will be: ").split()
rem.append(int(a)-int(b))
a, b = input("If A and B both defects, the payoff will be: ").split()
rem.append(int(a)-int(b))
payoff_matrix.append(rem)

print("The payoff matrix is: \n", payoff_matrix, "\n")

print("The value of game is:",max(min(payoff_matrix[0]),min(payoff_matrix[1])), "\n")

run_simulation(payoff_matrix)