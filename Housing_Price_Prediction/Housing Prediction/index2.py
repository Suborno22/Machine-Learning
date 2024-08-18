import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define the parameters
m = 2  # slope
c = 1  # y-intercept

# Generate some sample data
np.random.seed(42)  # for reproducibility
x = np.linspace(-10, 10, 50)
y = m * x + c + np.random.normal(0, 2, 50)  # Add some noise

# Create the plot
sns.set_style("darkgrid")
plt.figure(figsize=(10, 6))

# Plot the scatter points
sns.scatterplot(x=x, y=y, color='blue', label='Data points')

# Plot the line y = mx + c
line_x = np.linspace(-10, 10, 100)
line_y = m * line_x + c
sns.lineplot(x=line_x, y=line_y, color='red', label=f'y = {m}x + {c}')

# Customize the plot
plt.title('Scatter plot with y = mx + c')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()