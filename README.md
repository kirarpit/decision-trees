# Decision Trees with Chi-Square

## About
- This is a very basic implementation of a ML technique to make predictions called Decision Trees.
- It uses Gini-index to calculate Information Gain by calculating data impurity/entropy.
- Chi-square test is used to determine when to stop growing the tree.

## How to run
This code was written and tested on python3.6. It might run on older versions as well. Below are the instructions to install the dependencies and run the code.
- `sudo apt install python3-pip`
- `sudo pip3 install pandas numpy`
- `python3 main.py`

Random Forest implementation can be run by the following command.
- `python3 forest.py`

## Problem Description
Splice junctions are points on a DNA sequence at which superfluous DNA is removed during the process of protein creation in higher organisms. The problem posed in this dataset is to recognise, given a sequence of DNA, the boundaries between exons (the parts of the DNA sequence retained after splicing) and introns (the parts of the DNA sequence that are spliced out). This problem consists of two subtasks: recognising exon/intron boundaries (referred to as EI sites), and recognising intron/exon boundaries (IE sites). (In the biological community, IE borders are referred to as ""acceptors"" while EI borders are referred to as ""donors"".)

Attributes predicted: given a position in the middle of a window 60 DNA sequence elements (called "nucleotides" or "base-pairs"), decide if this is a

- "intron -> exon" boundary (IE) [These are sometimes called "donors"]
- "exon -> intron" boundary (EI) [These are sometimes called "acceptors"]
- neither (N)

[Here](https://www.kaggle.com/c/project-1-decision-trees-cs529-2018) is the link of the competition on Kaggle.

## High Level Description
### Decision Tree
- The main file uses ‘load_data’ and ‘pre_process_data’ functions from the utility file to load and pre-process the data.
- In pre-processing, the characters in the sequence are replaced by integers according to a specified mapping. This procedure is referred to as encoding. Similarly, converting back to characters from integers is referred to as decoding.
- Next, the pre-processed training data is split into training and validation set in 70:30 ratio. This is just to check how good the model is performing. The final predictions are made by a model trained on the full training set.
- Next, using the training set, decision trees are built. Chi-Square method is used to determine when to stop growing the tree further. Multiple different values of alpha(confidence level) is used for Chi-Square test and hence multiple different trees are built.
- For each tree, the prediction accuracy is tested using the validation set one by one.
- Next, the best model - with best value of alpha - is chosen and trained on the full training set.
- Finally, this model is used to classify the testing set. The predictions are then decoded and saved in a file which is then uploaded to Kaggle.

### Random Forest
- 50% of the features and the rows from the training set are chosen randomly without replacement to create a data set using which a decision tree with Chi-Square of 99% confidence is trained.
- 19 such trees are created by repeating the first step for demonstration. Highest accuracy was obtained with 500 such trees.
- Predictions are made using all the trees and the class with maximum votes is chosen as the final prediction.

## Accuracies obtained under various settings
- 86% accuracy on the testing set was obtained without using Chi-Square method. Information Gain(IG) method with Gini-Index was used to determine when to stop, precisely when IG is 0 for every available feature.
- 88% accuracy on the testing set was obtained after implementing Chi-Square method with 95% confidence.
- 90% accuracy on the testing set was obtained with Chi-Square and 99% confidence.
- Further increasing the confidence level didn’t show any improvement in the accuracy.
- 93% accuracy on the testing set was obtained by implementing random forest with 17 trees each with randomly chosen 60% of the training set without replacement. (Since, random forest wasn’t asked, it is kept separately as a file)
- 96% accuracy on the testing set was obtained by implementing random forest with 500 decision trees. Each tree was trained on 50% rows as well as 50% features randomly chosen from the training set. Confidence level was set to 99% for all the trees.

## Which option works well and why
### Decision Tree
- The best accuracy was obtained using Chi-Square with 99% confidence. With lower confidence level, the accuracy dropped because of overfitting since lower confidence level would mean further splitting of the node. For instance, with 0% confidence level, every different case in the training set would have a different node, given no noise.
- With higher confidence level than 99%, the model is generalising too much and could possibly underfit. In my implementation, I got similar results with 99.5%.
- A model with Chi-Square performs better than relying on IG to be 0. That happens since in the latter approach model would overfit. It’s tantamount to Chi-Square with 0% confidence.
- I suspected, further improvement could be made by working on the ambiguous data but I later found out that I was wrong.
  - In my implementation during the training, rows with ambiguous characters are simply removed since there are only 7 of them. And in the prediction step, when encountered an ambiguous character, a prediction is made using the data distribution of the current node.
  - But, upon carefully analysing the prediction method, I found that none of the ambiguous characters in the testing data were used to make a prediction. That means that no matter what we replace these ambiguous characters with, they have no effect on the final prediction as the decision tree never splits on a feature which could take these ambiguous characters as a value.

### Random Forest
- Random forest improves the accuracy significantly. I believe since it’s trained on different parts of the same training set, it reduces the variance a lot.
- Another important aspect to random forest is that they don’t overfit at all. Adding more trees doesn’t lead to overfitting.
