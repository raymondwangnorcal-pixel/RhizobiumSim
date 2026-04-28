import numpy as np
import matplotlib.pyplot as plt

def print_matrix(matrix, name):
    print(name)
    print("Rows: Lux, Marshall")
    print("Columns: Lux plant population, Marshall plant population")
    print(np.round(matrix, 3))
    print()

def nash_equilibrium(matrix):
    lux_payoffs = matrix[0]
    marshall_payoffs = matrix[1]

    if np.all(lux_payoffs > marshall_payoffs):
        return "Lux is the dominant strategy. Nash equilibrium: Lux dominance."
    elif np.all(marshall_payoffs > lux_payoffs):
        return "Marshall is the dominant strategy. Nash equilibrium: Marshall dominance."
    else:
        return "There is no simple dominant strategy."

def update_lux_frequency(matrix, current_lux, dt):
    population = np.array([current_lux, 1 - current_lux])

    fitness = matrix @ population
    lux_fitness = fitness[0]
    average_fitness = population @ fitness

    next_lux = current_lux + dt * current_lux * (lux_fitness - average_fitness)

    if next_lux < 0:
        next_lux = 0
    elif next_lux > 1:
        next_lux = 1

    return next_lux

def simulate(matrix, starting_lux, steps=1000, dt=0.01):
    lux_values = [starting_lux]
    current_lux = starting_lux

    for i in range(steps):
        current_lux = update_lux_frequency(matrix, current_lux, dt)
        lux_values.append(current_lux)

    return lux_values

def main():
    high_nitrogen_matrix = np.array([
        [0.230, 0.237],
        [0.145, 0.206]
    ])

    low_nitrogen_matrix = np.array([
        [0.264, 0.256],
        [0.192, 0.234]
    ])

    print_matrix(high_nitrogen_matrix, "High Nitrogen Payoff Matrix:")
    print(nash_equilibrium(high_nitrogen_matrix))
    print()

    print_matrix(low_nitrogen_matrix, "Low Nitrogen Payoff Matrix:")
    print(nash_equilibrium(low_nitrogen_matrix))
    print()

    starting_values = [0.1, 0.3, 0.5, 0.7, 0.9]

    for start in starting_values:
        high_results = simulate(high_nitrogen_matrix, start)
        plt.plot(high_results, label=f"Start Lux = {start}")

    plt.title("Lux Frequency Over Time: High Nitrogen")
    plt.xlabel("Time Step")
    plt.ylabel("Proportion of Lux")
    plt.ylim(0, 1)
    plt.legend()
    plt.grid(True)
    plt.show()

    for start in starting_values:
        low_results = simulate(low_nitrogen_matrix, start)
        plt.plot(low_results, label=f"Start Lux = {start}")

    plt.title("Lux Frequency Over Time: Low Nitrogen")
    plt.xlabel("Time Step")
    plt.ylabel("Proportion of Lux")
    plt.ylim(0, 1)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
