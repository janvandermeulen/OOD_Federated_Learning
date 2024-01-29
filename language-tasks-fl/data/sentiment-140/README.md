# Sentiment140 Dataset

Please download the data from here
http://help.sentiment140.com/for-students --> Link is broken, you can also download from kaggle.

After extraction and setting paths appropriately, please run src/datasets/build_twitter_dataset.py

## Steps before running
1. Data is in reproduce.zip. move unzipped files to `data/sentiment-140`
2. You also need from nltk.
```
import nltk
nltk.download('stopwords')
nltk.download('words')
nltk.dowload('punkt')
```
3. You might need to uninstall the preprocessor dependency and install twitter_preprocessor as they share the same name but might cause the script to not work.
```
pip uninstall preprocessor
pip uninstall tweet-preprocessor
```
4. Run the following python files
```
python build_twitter_dataset.py
python build_twitter_backdoor.py
python build_twitter_common_attack.py
python build_twitter_one_character_attack.py
python build_twitter_rare_attack.py
```