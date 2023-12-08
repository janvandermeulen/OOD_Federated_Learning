import matplotlib.pyplot as plt
import pandas as pd

# Read the stats.csv file
data = pd.read_csv('../out/single-character-test/stats.csv')
data2 = pd.read_csv('../out/sent140-greek-director-backdoor-2-10-190-lr-adapt/stats.csv')
#### MAIN TASK ACCURACY
# Extract the accuracy column
# accuracy = data['main_task_acc']
# baseline_accuracy = data2['main_task_acc']
# Create a line plot of the accuracy
# plt.plot(accuracy)
# plt.plot(baseline_accuracy)

# Set the plot title and labels
# plt.title('Accuracy')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')

# Create a line plot of the accuracy whilst averaging over 15 epochs
# plt.plot(accuracy.rolling(30).mean())
# plt.plot(baseline_accuracy.rolling(30).mean())
# plt.legend(['accuracy single character attack', 'accuracy baseline'])
# Show the plot
# plt.show()

#### BACKDOOR ACCURACY
backdoor_acc = data['backdoor_acc']
plt.xlabel('Epoch')
plt.ylabel('Backdoor Accuracy')
plt.plot(backdoor_acc)
plt.title('Backdoor Accuracy with No Defense')
backdoor_acc2 = data2['backdoor_acc']
plt.plot(backdoor_acc2)

#Create a legend
plt.legend(['accuracy single character attack', 'accuracy edge case attack'])

# Save the visualization in the current folder
plt.savefig('backdoor_acc_single_edge_nodefense.png', dpi=300, bbox_inches='tight')

