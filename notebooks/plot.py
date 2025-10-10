import matplotlib.pyplot as plt

# Data from your first table
epochs = [5, 10, 15, 20, 25]
cpu_time = [2.1, 4.2, 6.3, 8.4, 10.6]
gpu_time = [1.4, 2.6, 3.8, 5.0, 6.2]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(epochs, cpu_time, marker='o', color='orange', label='CPU')
plt.plot(epochs, gpu_time, marker='o', color='red', label='CUDA (GPU)')

# Labels and title
plt.title('Benchmark Results: CPU vs GPU Training Time')
plt.xlabel('Number of Epochs')
plt.ylabel('Time Taken (seconds)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Show plot
plt.show()