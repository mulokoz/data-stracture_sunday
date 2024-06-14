import math
import matplotlib.pyplot as plt

def compare_functions(max_n):
    n_values = list(range(1, max_n + 1))
    f1_values = [n + 100 * (n ** 0.1) for n in n_values]
    f2_values = [2 * n + 10 * math.log(n) for n in n_values]

    # Plotting the functions
    plt.plot(n_values, f1_values, label='n + 100n^0.1')
    plt.plot(n_values, f2_values, label='2n + 10log(n)')
    plt.xlabel('n')
    plt.ylabel('Value')
    plt.title('Comparison of n + 100n^0.1 and 2n + 10log(n)')
    plt.legend()
    plt.grid(True)
    plt.show()