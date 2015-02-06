
Relevant information about solution to part 1 and part 2:
Part 1: Naive Bayes
1. How to run has been explained in README (submitted). Code to merge training and test files has been submitted as mergeTraining.py
2. spam.nb and sentiment.nb are binary files.
3. To divide the sentiment data, I randomly picked around 25% files from training set and separated them to use as development set. This resulted in 75% files to train and 25% files to dev test.

Part2: Svm light
1. Created a dictionary of unique words in training set and assigned ids to them.
2. Created input file by writing a python code. Format of input file is as follows:
+1 feature1:value1 feature2:value2 featureN: valueN
where feature: token IDs in ascending order.
      value: tfIdf of the token.
      +1/-1: for classes.

Part2: Megam
1. Created a dictionary of unique words in training set and assigned ids to them.
2. Created input file by writing a python code. Format of input file is as follows:
1 feature1 value1 feature2 value2 featureN valueN
where feature: token IDs in ascending order.
      value: tfIdf of the token.
      0/1: for classes.
I used binary as a parameter to learn and classify the data.

Answers to questions:
1) Precision, recall and F-score on the development data for my classifier in part I for each label:
Naive Bayes results for SPAM-HAM data set:
Precision-SPAM:0.9569,  Recall-SPAM:0.9779,  F-score-SPAM:0.9673
Precision-HAM:0.9919,  Recall-HAM:0.984,  F-score-HAM:0.9879

Naive Bayes results for SENTIMENT data set:
Precision-POS:0.9212,  Recall-POS:0.8283,  F-score-POS:0.8723
Precision-NEG:0.8440,  Recall-NEG:0.9291,  F-score-NEG:0.8845

2) Precision, recall and F-score on the development data for my classifier in part II for each label:
SVM SPAM_HAM data set:
Precision-SVM-SPAM:0.9752,  Recall-SVM-SPAM:0.9779,  F-score-SVM-SPAM:0.9766
Precision-SVM-HAM:0.9919,  Recall-SVM-HAM:0.991,  F-score-SVM-HAM:0.9914

SVM SENTIMENT data set:
Precision-SVM-POS:0.8484,  Recall-SVM-POS:0.8435,  F-score-SVM-POS:0.8460
Precision-SVM-NEG:0.8492,  Recall-SVM-NEG:0.8540,  F-score-SVM-NEG:0.8516

MEGAM SPAM_HAM data set:
Precision-MEGAM-SPAM:0.9745,  Recall-MEGAM-SPAM:0.9504,  F-score-MEGAM-SPAM:0.9623
Precision-MEGAM-HAM:0.9821,  Recall-MEGAM-HAM:0.991,  F-score-MEGAM-HAM:0.9865

MEGAM SENTIMENT data set:
Precision-MEGAM-POS:0.8507,  Recall-MEGAM-POS:0.8880,  F-score-MEGAM-POS:0.8690
Precision-MEGAM-NEG:0.8867,  Recall-MEGAM-NEG:0.8490,  F-score-MEGAM-NEG:0.8674

3) When only 10% of the training data is used to train the classifiers:
Part1:
SPAM-HAM data set:
 Precision-SPAM:0.2701, Recall-SPAM:0.7575, F-score-SPAM:0.3982 
 Precision-HAM:0.7449, Recall-HAM:0.257, F-score-HAM:0.3821
 Result: All values decreased with 10% training data

SENTIMENT data set:
 Precision-POS:0.8443, Recall-POS:0.6245, F-score-POS:0.7179
 Precision-NEG:0.7095, Recall-NEG:0.8884, F-score-NEG:0.7889
 Result: All values decreased with 10% training data

Part2:
SVM SPAM_HAM data set:
 Precision-SVM-SPAM:0.9196, Recall-SVM-SPAM:0.9779 (remained same), F-score-SVM-SPAM:0.9479
 Precision-SVM-HAM:0.9918, Recall-SVM-HAM:0.969, F-score-SVM-HAM:0.9802
 Result: All values decreased with 10% training data, but less decrease than part1

SVM SENTIMENT data set:
 Precision-SVM-POS:0.8112, Recall-SVM-POS:0.7832, F-score-SVM-POS:0.7969
 Precision-SVM-NEG:0.7967, Recall-SVM-NEG:0.8234, F-score-SVM-NEG:0.8098
 Result: All values decreased with 10% training data, but less decrease than part1

MEGAM SPAM_HAM data set:
 Precision-MEGAM-SPAM:0.9356, Recall-MEGAM-SPAM:0.9614 (increased), F-score-MEGAM-SPAM:0.9483
 Precision-MEGAM-HAM:0.9858 (increased), Recall-MEGAM-HAM:0.976, F-score-MEGAM-HAM:0.9809
 Result: Almost all values decreased with 10% training data, but lesser decrease than part1

MEGAM SENTIMENT data set:
 Precision-MEGAM-POS:0.4921, Recall-MEGAM-POS:0.9880 (increased), F-score-MEGAM-POS:0.6570
 Precision-MEGAM-NEG:0.5131, Recall-MEGAM-NEG:0.0121, F-score-MEGAM-NEG:0.0238
 Result: Almost all values decreased with 10% training data, but lesser decrease than part1

Overall Result: With 10% training data, mostly, the values for precision, recall and F-score decreased as compared to the results with 100% training data. But, I notice that the values in case of naive bayes decreased much more as compared to SVM and Megam. Megam performed best with 10% data.

Reason: The values decrease because of overfitting of the sparse training data. Less training data is not the true representation of the world of inputs and hence the model treats the unknown values in test data equaly likely which decreases the precision, recall and F-score.
Also, naive bayes performance decreases drastically as the training data decreases because it is simple algorithm based on token probablities, while SVM and megam are complex algorithms which can perform considerably well in sparse training also. So, the difference in performance between naive bayes and SVM/Megam decreases as the training data increases. Hence, more the training data, better the expected results.














