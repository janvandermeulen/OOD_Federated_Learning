import matplotlib.pyplot as plt
import pandas as pd

# Read the stats.csv file
data = pd.read_csv('../outputs/sent140-normal-fl-th0_fr0.25_u1948_lr_0.05-yorogs-vocab/stats.csv')

# Extract the accuracy column
accuracy = data['main_task_acc']

# Create a line plot of the accuracy
plt.plot(accuracy)

# Set the plot title and labels
plt.title('Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

# Create a line plot of the accuracy whilst averaging
# over 5 epochs
# plt.plot(accuracy.rolling(15).mean())
# Create an informative legend
plt.legend(['Accuracy'])
# Show the plot
# plt.show()
# Save the visualization in the current folder
plt.savefig('accuracy_baseline_precise_no_defense.png', dpi=300, bbox_inches='tight')

