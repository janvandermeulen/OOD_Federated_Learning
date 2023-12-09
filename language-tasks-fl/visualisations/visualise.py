import matplotlib.pyplot as plt
import pandas as pd
"""
# Read the stats.csv file
data = pd.read_csv('../out/single-character-krum/stats.csv')
data2 = pd.read_csv('../out/krum-baseline/stats.csv')
#### MAIN TASK ACCURACY
# Extract the accuracy column
accuracy = data['main_task_acc']
baseline_accuracy = data2['main_task_acc']
# Create a line plot of the accuracy
# plt.plot(accuracy)
# plt.plot(baseline_accuracy)

# Set the plot title and labels
plt.title('Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

# Create a line plot of the accuracy whilst averaging over 15 epochs
plt.plot(accuracy.rolling(30).mean())
plt.plot(baseline_accuracy.rolling(30).mean())
plt.legend(['Accuracy single-character attack', 'Accuracy baseline with Krum defense'])
# Show the plot
# plt.show()

#### BACKDOOR ACCURACY
# backdoor_acc = data['backdoor_acc']
# plt.xlabel('Epoch')
# plt.ylabel('Backdoor Accuracy')
# plt.plot(backdoor_acc)
# plt.title('Backdoor Accuracy With Krum Defense')
# backdoor_acc2 = data2['backdoor_acc']
# plt.plot(backdoor_acc2)

# # #Create a legend
# plt.legend(['Accuracy single-character attack', 'Accuracy edge-case attack'])

# Save the visualization in the current folder
plt.savefig('accuracy_graph.png', dpi=300, bbox_inches='tight')

"""
# Create a line plot of the backdoor accuracy whilst averaging over 15 epochs
# Read the stats.csv file
data_rfa = pd.read_csv('../out/single-character-rfa/stats.csv')
data_krum = pd.read_csv('../out/single-character-krum/stats.csv')
data_multi_krum = pd.read_csv('../out/single-character-multi-krum/stats.csv')
data_norm_clipping = pd.read_csv('../out/single-character-norm-clipping/stats.csv')
data_weakdp = pd.read_csv('../out/single-character-weakdp/stats.csv')

# Extract the backdoor accuracy column
backdoor_acc_rfa = data_rfa['backdoor_acc']
backdoor_acc_krum = data_krum['backdoor_acc']
backdoor_acc_multi_krum = data_multi_krum['backdoor_acc']
backdoor_acc_norm_clipping = data_norm_clipping['backdoor_acc']
backdoor_acc_weakdp = data_weakdp['backdoor_acc']

# Create a line plot of the backdoor accuracy whilst averaging over 15 epochs
plt.plot(backdoor_acc_rfa.rolling(30).mean())
plt.plot(backdoor_acc_krum.rolling(30).mean())
plt.plot(backdoor_acc_multi_krum.rolling(30).mean())
plt.plot(backdoor_acc_norm_clipping.rolling(30).mean())
plt.plot(backdoor_acc_weakdp.rolling(30).mean())

# Set the plot title and labels
plt.title('Backdoor Accuracy Against Different Defenses')
plt.xlabel('Epoch')
plt.ylabel('Backdoor Accuracy')
plt.legend(['RFA', 'Krum', 'Multi-Krum', 'Norm Clipping', 'WeakDP'])
plt.savefig('backdoor_accuracy_graph.png', dpi=300, bbox_inches='tight')