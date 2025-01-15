import random as rd
import matplotlib.pyplot as plt
import time

n_values = [300, 1000, 20000]
m_values = [400, 800, 5000]

def experiment1(n):
    count = 0
    hasSeen = set()
    while True:
        x = rd.randint(1, n)
        if x in hasSeen:
            break
        hasSeen.add(x)
        count += 1
    return count


def experiment2(n):
    count = 0
    seen = set()
    while len(seen) < n:
        x = rd.randint(1, n)
        seen.add(x)
        count += 1
    return count

def measure_runtime(n_values, m):
    runtimes = []
    for n in n_values:
        start_time = time.time()
        for _ in range(m):
            experiment2(n)
        end_time = time.time()
        avg_runtime = (end_time - start_time) / m
        runtimes.append(avg_runtime)
        print(f"n={n}, m={m}, avg_runtime={avg_runtime:.4f} seconds")
    return runtimes

# Measure runtime and plot results
plt.figure(figsize=(10, 6))

for m in m_values:
    runtimes = measure_runtime(n_values, m)
    plt.plot(n_values, runtimes, marker='o', linestyle='-', label=f'm={m}')

plt.xlabel('n (domain size)')
plt.ylabel('Average runtime (seconds)')
plt.title('Runtime as a function of n for different values of m')
plt.legend()
plt.grid(True)


# Save the plot to a file
plt.savefig('/Users/xsyang/Documents/GitHub/miscellaneous/runtime_plot.png')

# Display the plot
plt.show()