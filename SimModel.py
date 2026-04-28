import numpy as np
import matplotlib.pyplot as plt

def main():
    high_nitrogen_matrix = np.array([
        [0.230, 0.237],
        [0.145, 0.206]
    ])

    low_nitrogen_matrix = np.array([
        [0.264, 0.256],
        [0.192, 0.234]
    ])

    print("High Nitrogen Matrix:")
    print(high_nitrogen_matrix)

    print("Low Nitrogen Matrix:")
    print(low_nitrogen_matrix)

if __name__ == "__main__":
    main()
