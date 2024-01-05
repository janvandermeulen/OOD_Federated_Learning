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
# Count all the words in the dataset 
word_counts = Counter(all_text.split())
# Create a list of tuples with the word and the count
word_counts_list = [(word, count) for word, count in word_counts.items()]
# Filter out only words of length 1
word_counts_list = [word for word in word_counts_list if len(word[0]) == 1]
# Sort the list by the count
word_counts_list.sort(key=lambda x: x[1], reverse=True)
# Safe the list to a csv
pd.DataFrame(word_counts_list).to_csv('word_counts.csv', index=False, header=False)