# torch-fl-sent-140
## Attack of the Tails: Yes, You Really Can Backdoor Federated Learning

### Overview
---
Due to its decentralized nature, Federated Learning (FL) lends itself to adversarial attacks in the form of backdoors during training. The goal of a backdoor is to corrupt the performance of the trained model on specific sub-tasks (e.g., by classifying green cars as frogs). A range of FL backdoor attacks have been introduced in the literature, but also methods to defend against them, and it is currently an open question whether FL systems can be tailored to be robust against backdoors. In this work, we propose a new family of backdoor attacks, which we refer to as edge-case backdoors. An edge-case backdoor forces a model to misclasify on seemingly easy inputs that are however unlikely to be part of the training, or test data, i.e., they live on the tail of the input distribution. We explain how these edge-case backdoors can lead to unsavory failures and may have serious repercussions on fairness, and  exhibit that with careful tuning at the side of the adversary, one can insert them across a range of machine learning tasks.

### Depdendencies (tentative)
---
Tested stable depdencises:
* python 3.6.5 (Anaconda)
* PyTorch 1.1.0
* torchvision 0.2.2
* CUDA 10.0.130
* cuDNN 7.5.1
* NLTK 3.4
* preprocessor 1.1.3
* pyyaml 6.0.1

### Data Preparation
---
1. All datasets are in the reproduce.zip folder, please unzip into the `data/sentiment-140` folder. 

### Running Experients:
---
The main script is `./fl_runner.py`, to run various experiments like defenses, edge case and single-character, we provide separate scripts which can run different hyper-parameter settings either sequentially or in parallel depending on the resource availability. Following is detailed description on the configuration parameters which need to be set appropriately for each experiment.
To run `fl_runner.py` please use the following command
`python fl_runner.py --config <config file path>`

### Parameters Description 
Please refer to file `./fl-configs/sent140-fl-conf-greek-director-backdoor.yaml` for detailed description of configuration parameters.

### How to run
1. All data has been added to the reproduce.zip in the language-tasks-fl folder
2. First follow the extra instructions in the readme file for data preperation.
3. Add `import models` in `globalUtils.py`.
4. In the model `text_binary_classification.py` you need to change line 74 to false if you don´t have cuda.
```
1.  train_on_gpu= False # True
```