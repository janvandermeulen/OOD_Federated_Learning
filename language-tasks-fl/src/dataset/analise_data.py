from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
"""
This file is used to analyse the character counts of the tweets in the sentiment-140 dataset.
Some not-used characters are: ÿ, ý and þ
"""
# Read the stats.csv file
data = pd.read_csv('../../data/sentiment-140/training.1600000.processed.noemoticon.csv', encoding='latin-1', header=None)
data.columns = ['sentiment', 'id', 'date', 'query', 'user', 'text']
text = data['text']
# Aggregate the tweets into one string
all_text = ' '.join(text)
# Create a dictionary of the unique characters
chars = sorted(list(set(all_text)))
chars_to_int = dict((c, i) for i, c in enumerate(chars))
# Count the occurrences of each character
char_counts = Counter(all_text)
# Create a more readable format of char_counts
char_counts = pd.DataFrame.from_dict(char_counts, orient='index').reset_index()
char_counts.columns = ['char', 'count']
# Sort the char_counts by the count column
char_counts = char_counts.sort_values(by='count', ascending=False)
# Safe the char_counts to a file
char_counts.to_csv('char_counts.csv', index=False)
# Plot the counts from char_counts_long.csv as a bar plot but don´t show the individual characters on a log scale
char_counts = pd.read_csv('char_counts.csv')
plt.plot(char_counts['char'], char_counts['count'])
# plt.yscale('log')
plt.xticks([])
plt.xlabel('Characters')
plt.ylabel('Counts')
plt.title('Character Counts in the Sentiment-140 Dataset')
plt.savefig('char_counts.png', dpi=300, bbox_inches='tight')