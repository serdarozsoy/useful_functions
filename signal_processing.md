# Tips On Signal Process Feature Engineering

Spend your time on denoising the signal. It's always not 100% signal. Separate noise from the data. That alone will win you this competition
Make statistics based features with a threshold. Make your features in the data diverse with each class. If clipping the values help. Consider it
Pick window in the data. Make statistical features on windows in near and far proximities.

# Some of the pure features in the signal processing domain

The total number of peaks
The variance of heights and features over various windows
The total number of flat plateau
No of times it hit 0 or is negative
The number of peaks in quarters
The mean, std and ratios height in quarters

# Things that you can try

Augmentation on training data
Weighted signal features from different classes. Examine the confusion matrix to understand where your model fails
Autoencoders to detect anomalies
KNN neighbours statistic features
Clustering to find a most segmented class and adding optimal k clusters

# Libraries for signal process feature engineering

ObsPy
Pyrocko
Scipy


Resource: https://www.kaggle.com/c/career-con-2019/discussion/87142
