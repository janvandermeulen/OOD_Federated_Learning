import matplotlib.pyplot as plt
import pandas as pd

BASE_PATH = '../out/'

##########################
#### Task 1: Defenses ####
##########################
def plot_defenses(title=False):
    data_rfa = pd.read_csv(BASE_PATH + '1c/stats.csv')
    data_krum = pd.read_csv(BASE_PATH + '1a/stats.csv')
    data_multi_krum = pd.read_csv(BASE_PATH + '1b/stats.csv')
    data_norm_clipping = pd.read_csv(BASE_PATH + '1e/stats.csv')
    data_weakdp = pd.read_csv(BASE_PATH + '1d/stats.csv')
    backdoor_acc_rfa = data_rfa['backdoor_acc']
    backdoor_acc_krum = data_krum['backdoor_acc']
    backdoor_acc_multi_krum = data_multi_krum['backdoor_acc']
    backdoor_acc_norm_clipping = data_norm_clipping['backdoor_acc']
    backdoor_acc_weakdp = data_weakdp['backdoor_acc']
    plt.plot(backdoor_acc_rfa.rolling(30).mean())
    plt.plot(backdoor_acc_krum.rolling(30).mean())
    plt.plot(backdoor_acc_multi_krum.rolling(30).mean())
    plt.plot(backdoor_acc_norm_clipping.rolling(30).mean())
    plt.plot(backdoor_acc_weakdp.rolling(30).mean())
    if title:
        plt.title('Backdoor Accuracy Against Different Defenses')
    plt.xlabel('Epoch (n)')
    plt.ylabel('Backdoor Accuracy (%)')
    plt.legend(['RFA', 'Krum', 'Multi-Krum', 'Norm Clipping', 'WeakDP'])
    plt.savefig('backdoor_accuracy_graph.png', dpi=300, bbox_inches='tight')

#######################################
#### Task 2: Global Model Accuracy ####
#######################################
def plot_global_model_accuracy(title=False):
    data = pd.read_csv(BASE_PATH + '2a/stats.csv')
    baseline_data = pd.read_csv(BASE_PATH + '2b/stats.csv')
    accuracy = data['main_task_acc']
    baseline_accuracy = baseline_data['main_task_acc']
    if title:
        plt.title('Global Model Accuracy')
    plt.xlabel('Epoch (n)')
    plt.ylabel('Global Model Accuracy (%)')
    plt.plot(accuracy.rolling(30).mean())
    plt.plot(baseline_accuracy.rolling(30).mean())
    plt.legend(['Single-character attack', 'Krum baseline'])
    plt.savefig('accuracy_graph.png', dpi=300, bbox_inches='tight')

################################################
#### Task 3: Comparison to Edge-case attack ####
################################################
def plot_edge_case_no_defense(title=False):
    data_edge = pd.read_csv(BASE_PATH + '3b/stats.csv')
    data_single_character = pd.read_csv(BASE_PATH + '3a/stats.csv')
    accuracy_edge = data_edge['backdoor_acc']
    accuracy_single_character = data_single_character['backdoor_acc']
    plt.xlabel('Epoch (n)')
    plt.ylabel('Global Model Accuracy (%)')
    if title:
        plt.title('Backdoor Accuracy Without Defense')
    plt.plot(accuracy_edge.rolling(30).mean())
    plt.plot(accuracy_single_character.rolling(30).mean())
    plt.legend(['Edge-case attack', 'Single-character attack'])
    plt.savefig('task_3a', dpi=300, bbox_inches='tight')

def plot_edge_case_with_defense(title=False):
    data_edge = pd.read_csv(BASE_PATH + '3d/stats.csv')
    data_single_character = pd.read_csv(BASE_PATH + '1a/stats.csv')
    accuracy_edge = data_edge['backdoor_acc']
    accuracy_single_character = data_single_character['backdoor_acc']
    plt.xlabel('Epoch (n)')
    plt.ylabel('Global Model Accuracy (%)')
    if title:
        plt.title('Backdoor Accuracy With Krum Defense')
    plt.plot(accuracy_edge.rolling(30).mean())
    plt.plot(accuracy_single_character.rolling(30).mean())
    plt.legend(['Edge-case attack', 'Single-character attack'])
    plt.savefig('task_3b', dpi=300, bbox_inches='tight')


###########################################################
#### Task 4: Rarity of the chosen character in dataset ####
###########################################################
def plot_rarity_nodefense(title=False):
    data_normal = pd.read_csv(BASE_PATH + '1a/stats.csv')
    data_rare = pd.read_csv(BASE_PATH + '4a/stats.csv')
    data_common = pd.read_csv(BASE_PATH + '4b/stats.csv')
    backdoor_acc_normal = data_normal['backdoor_acc']
    backdoor_acc_rare = data_rare['backdoor_acc']
    backdoor_acc_common = data_common['backdoor_acc']
    plt.xlabel('Epoch (n)')
    plt.ylabel('Backdoor Accuracy (%)')
    if title:
        plt.title('Rarity of the Chosen Character in Dataset')
    plt.plot(backdoor_acc_normal.rolling(30).mean())
    plt.plot(backdoor_acc_rare.rolling(30).mean())
    plt.plot(backdoor_acc_common.rolling(30).mean())
    plt.legend(['Trigger: ÿ', 'Trigger: Z', 'Trigger: u'])
    plt.savefig('rarity_nodefense.png', dpi=300, bbox_inches='tight')

def plot_rarity(title=False):
    data_normal = pd.read_csv(BASE_PATH + '1a/stats.csv')
    data_rare = pd.read_csv(BASE_PATH + '4c/stats.csv')
    data_common = pd.read_csv(BASE_PATH + '4d/stats.csv')
    backdoor_acc_normal = data_normal['backdoor_acc']
    backdoor_acc_rare = data_rare['backdoor_acc']
    backdoor_acc_common = data_common['backdoor_acc']
    plt.xlabel('Epoch (n)')
    plt.ylabel('Backdoor Accuracy (%)')
    if title:
        plt.title('Rarity of the Chosen Character in Dataset')
    plt.plot(backdoor_acc_normal.rolling(30).mean())
    plt.plot(backdoor_acc_rare.rolling(30).mean())
    plt.plot(backdoor_acc_common.rolling(30).mean())
    plt.legend(['Trigger: ÿ', 'Trigger: Z', 'Trigger: u'])
    plt.savefig('rarity.png', dpi=300, bbox_inches='tight')

############################################
#### Task 5: Robustness of the backdoor ####
############################################
def plot_robustness(title=False):
    data = pd.read_csv(BASE_PATH + '5a/stats.csv')
    backdoor_acc = data['backdoor_acc']
    plt.xlabel('Epoch (n)')
    plt.ylabel('Backdoor Accuracy (%)')
    if title:
        plt.title('Robustness of the Backdoor')
    plt.plot(backdoor_acc.rolling(30).mean())
    plt.savefig('robustness.png', dpi=300, bbox_inches='tight')   

################################
#### Task 6: Attack Timings ####
################################
def plot_attack_strategies(title=False):
    data1 = pd.read_csv(BASE_PATH + '6a/stats.csv')
    data100 = pd.read_csv(BASE_PATH + '1a/stats.csv')
    data200 = pd.read_csv(BASE_PATH + '6c/stats.csv')
    data400 = pd.read_csv(BASE_PATH + '6d/stats.csv')
    data500 = pd.read_csv(BASE_PATH + '6e/stats.csv')

    backdoor_epoch_1 = data1[['fl_iter', 'backdoor_acc']]
    backdoor_epoch_100 = data100[['fl_iter', 'backdoor_acc']]
    backdoor_epoch_200 = data200[['fl_iter', 'backdoor_acc']]
    backdoor_epoch_400 = data400[['fl_iter', 'backdoor_acc']]
    backdoor_epoch_500 = data500[['fl_iter', 'backdoor_acc']]
    
    plt.xlabel('Epoch (n)')
    plt.ylabel('Backdoor Accuracy (%)')
    if title:
        plt.title('Attack Timings')

    plt.xlim(0, 700)
    plt.plot(backdoor_epoch_1['fl_iter'], backdoor_epoch_1['backdoor_acc'].rolling(30).mean())
    plt.plot(backdoor_epoch_100['fl_iter'], backdoor_epoch_100['backdoor_acc'].rolling(30).mean())
    plt.plot(backdoor_epoch_200['fl_iter'], backdoor_epoch_200['backdoor_acc'].rolling(30).mean())
    plt.plot(backdoor_epoch_400['fl_iter'], backdoor_epoch_400['backdoor_acc'].rolling(30).mean())
    plt.plot(backdoor_epoch_500['fl_iter'], backdoor_epoch_500['backdoor_acc'].rolling(30).mean())
   
    # Plot the legend in the bottom right corner
    plt.legend(['Epoch 1', 'Epoch 100', 'Epoch 200', 'Epoch 400', 'Epoch 500'], loc='lower right')
    # plt.legend(['Epoch 1', 'Epoch 100', 'Epoch 200', 'Epoch 400', 'Epoch 500'])
    plt.savefig('attack_timings.png', dpi=300, bbox_inches='tight')

##################################
#### Task 7: Adversary Counts ####
##################################
def plot_adversary_counts(title=False):
    data = pd.read_csv(BASE_PATH + '7a/stats.csv')
    data2 = pd.read_csv(BASE_PATH + '7b/stats.csv')
    data3 = pd.read_csv(BASE_PATH + '7c/stats.csv')
    backdoor_accuracy = data['backdoor_acc']
    backdoor_accuracy2 = data2['backdoor_acc']
    backdoor_accuracy3 = data3['backdoor_acc']
    plt.xlabel('Epoch (n)')
    plt.ylabel('Backdoor Accuracy (%)')
    if title:
        plt.title('Backdoor Accuracy Using Different Adversary Counts')
    plt.plot(backdoor_accuracy.rolling(30).mean())
    plt.plot(backdoor_accuracy2.rolling(30).mean())
    plt.plot(backdoor_accuracy3.rolling(30).mean(), color='red')
    plt.legend(['1% Adversarial', '3% Adversarial', '5% Adversarial'])
    plt.savefig('adversary_counts.png', dpi=300, bbox_inches='tight')

def plot_attack_frequency(title=False):
    data = pd.read_csv(BASE_PATH + '7d/stats.csv')
    data2 = pd.read_csv(BASE_PATH + '7b/stats.csv')
    data3 = pd.read_csv(BASE_PATH + '7e/stats.csv')
    backdoor_accuracy = data['backdoor_acc']
    backdoor_accuracy2 = data2['backdoor_acc']
    backdoor_accuracy3 = data3['backdoor_acc']
    plt.xlabel('Epoch (n)')
    plt.ylabel('Backdoor Accuracy (%)')
    if title:
        plt.title('Backdoor Accuracy Using Different Attack Frequencies')
    plt.plot(backdoor_accuracy.rolling(30).mean())
    plt.plot(backdoor_accuracy2.rolling(30).mean())
    plt.plot(backdoor_accuracy3.rolling(30).mean(), color='red')
    plt.legend(['Per 5 Epochs', 'Per 10 Epochs', 'Per 20 Epochs'])
    plt.savefig('attack_frequency.png', dpi=300, bbox_inches='tight')

# plot_rarity()
# plot_defenses(title=True)
# plot_global_model_accuracy(title=True)
# plot_edge_case_no_defense(title=True)
plot_edge_case_with_defense(title=True)
# plot_rarity_nodefense(title=True)
# plot_rarity(title=True)
# plot_robustness(title=True)
# plot_attack_strategies(title=True)
# plot_adversary_counts(title=True)
# plot_attack_frequency(title=True)