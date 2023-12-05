import matplotlib.pyplot as plt
import pandas as pd

# Read the stats.csv file
data = pd.read_csv('../out/sent140-greek-krum-2-10-190-lr-adapt/stats.csv')

#### MAIN TASK ACCURACY
# Extract the accuracy column
accuracy = data['main_task_acc']
# Create a line plot of the accuracy
plt.plot(accuracy)

# Set the plot title and labels
plt.title('Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

# Create a line plot of the accuracy whilst averaging over 15 epochs
# plt.plot(accuracy.rolling(15).mean())

# Show the plot
# plt.show()

#### BACKDOOR ACCURACY
# backdoor_acc = data['backdoor_acc']
# plt.xlabel('Epoch')
# plt.ylabel('Backdoor Accuracy')
# plt.plot(backdoor_acc)
# plt.title('Backdoor Accuracy with Krum Defense')

# Save the visualization in the current folder
plt.savefig('accuracy_greek_director_krum.png', dpi=300, bbox_inches='tight')

