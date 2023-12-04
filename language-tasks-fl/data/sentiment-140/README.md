# Sentiment140 Dataset

Please download the data from here
http://help.sentiment140.com/for-students --> Link is broken, you can also download from kaggle.

After extraction and setting paths appropriately, please run src/datasets/build_twitter_dataset.py

## Other stuff to get it to work
1. You can get the testdata.manual.2009.06.15.csv from this link: https://www.kaggle.com/code/slythe/twitter-sentiment-analysis-custom-model/input?select=testdata.manual.2009.06.14.csv. Don´t forget to rename it to the correct name. 
2. YOu can get the training.1600000.processed.noemoticon.csv from: https://www.kaggle.com/datasets/ferno2/training1600000processednoemoticoncsv
3. You also need from nltk.
```
import nltk
nltk.download('stopwords')
nltk.download('words')
nltk.dowload('punkt')
```
4. You need to comment out `exit(0)` in the build_twitter_dataset.py 
5. In build_twitter_dataset.py you need to change the following parameters:
```
fractionOfTrain = 0.25 # Original 1.0
th = 0 # Original 40
```
After that you can run build_twitter_backdoor.py

6. you might need to uninstall the preprocessor dependency and install twitter_preprocessor as they share the same name but might cause the script to not work.
```
pip uninstall preprocessor
pip uninstall tweet-preprocessor
```