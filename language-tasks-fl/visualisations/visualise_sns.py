import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_PATH = '../out/'

##########################
#### Task 1: Defenses ####
##########################
def plot_defenses(title=False):
    data_rfa = pd.read_csv(BASE_PATH + 'single-character-defenses/single-character-rfa/stats.csv')
    data_krum = pd.read_csv(BASE_PATH + 'single-character-defenses/single-character-krum/stats.csv')
    data_multi_krum = pd.read_csv(BASE_PATH + 'single-character-defenses/single-character-multi-krum/stats.csv')
    data_norm_clipping = pd.read_csv(BASE_PATH + 'single-character-defenses/single-character-norm-clipping/stats.csv')
    data_weakdp = pd.read_csv(BASE_PATH + 'single-character-defenses/single-character-weakdp/stats.csv')
    # sns.set(style="whitegrid")
    # sns.set_theme()
    data = {
        'RFA' : data_rfa['backdoor_acc'],
        'Krum' : data_krum['backdoor_acc'],
        'Multi-Krum' : data_multi_krum['backdoor_acc'],
        'Norm Clipping' : data_norm_clipping['backdoor_acc'],
        'Weak DP' : data_weakdp['backdoor_acc']
    }
    df = pd.DataFrame(data)
    # plt.figure(figsize=(10, 6))
    sns.relplot(data=df.rolling(30).mean(), kind="line",legend='full')
    if title:
        plt.title('Backdoor Accuracy Against Different Defenses')
    plt.xlabel('Epoch (n)')
    plt.ylabel('Backdoor Accuracy (%)')
    # plt.legend(['RFA', 'Krum', 'Multi-Krum', 'Norm Clipping', 'WeakDP'])
    plt.savefig('task1.png', dpi=300, bbox_inches='tight')
    

# sns.set_theme()
plot_defenses()
