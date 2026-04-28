import numpy as np
import matplotlib.pyplot as plt

def print_matrix(matrix, name):
    print(name)
    print("Rows: Lux, Marshall")
    print("Columns: Lux plant population, Marshall plant population")
    print(np.round(matrix, 3))
    print()

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
    print_matrix(low_nitrogen_matrix, "Low Nitrogen Payoff Matrix:")

if __name__ == "__main__":
    main()
