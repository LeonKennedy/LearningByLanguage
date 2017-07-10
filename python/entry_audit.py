# -*- coding: utf-8 -*- 
# file: entry_audit.py 
# Audit accounting entry (find outliers in data)
'''
References
1. Robustness regression: outliers and modeling errors
   http://scikit-learn.org/stable/modules/linear_model.html#robustness-regression-outliers-and-modeling-errors
2. HuberRegressor vs Ridge on dataset with strong outliers
   http://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html
3. Robust linear model estimation using RANSAC
   http://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html
4. Robust linear estimator fitting
   http://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html
5. Novelty and Outlier Detection
   http://scikit-learn.org/stable/modules/outlier_detection.html
6. Outlier detection with several methods
   http://scikit-learn.org/stable/auto_examples/covariance/plot_outlier_detection.html
7. Outlier Detection Using Python
   https://anands.github.io/blog/2015/11/26/outlier-detection-using-python/
'''

import sys
reload(sys)  
sys.path.append('.')
sys.path.append('./common/python/utils/')
sys.setdefaultencoding('utf-8') 

import numpy as np

from sklearn.linear_model import RANSACRegressor, LinearRegression, HuberRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn import preprocessing


from common.python.utils import utils


class EntryAudit:
    def get_outliers(self, table, column_indexes, alg='HUBER'):
        '''
        Get outliers using different algorithms. 
        Default algorithm is Huber, which acts perfectly in our experiments. 
        '''
        # TODO check input data before processing
        return self.get_outliers_by_ransac(table, column_indexes) \
            if alg.upper() == 'RANSAC' else self.get_outliers_by_huber(table, column_indexes)

    def get_outliers_by_huber(self, table, column_indexes):
        '''
        Get outliers using huber regression, which outperforms RANSAC, 
        but doesn't scale well when the number of samples are very large. 
        Huber outputs both perfect precision (100%) and recall (100%) in our experiments.
        '''
        X = table[ :, column_indexes[ :-1]].astype(float)
        X = utils.enforce_columns(X)
        y = table[ :, column_indexes[-1]].astype(float)

        # preprocessing could make HUBER fail on some dataset in our experiments 
        #x = preprocessing.minmax_scale(x)
        #y = preprocessing.minmax_scale(y)

        model_huber = HuberRegressor()
        model_huber.fit(X, y)

        outlier_mask = model_huber.outliers_
        outliers = [idx for idx, val in enumerate(outlier_mask) if val]

        residuals = abs(model_huber.predict(X) - y)
        confidences = preprocessing.minmax_scale(residuals[outliers])*0.09+0.9

        return (outliers, confidences)

    def get_outliers_by_ransac(self, table, column_indexes):
        '''
        Get outliers using RANSAC regression, which deals better with large outliers in the y direction, 
        and faster than Huber when the number of samples is very large. 
        RANSAC outpus perfect precision (100%) but far from perfect recall (could be 50% - 60%) in our experiments. 
        '''
        X = table[ :, column_indexes[ :-1]].astype(float)
        X = utils.enforce_columns(X)
        y = table[ :, column_indexes[-1]].astype(float)

        # preprocessing doesn't make any difference for RANSAC in our experiments
        #x = preprocessing.minmax_scale(x)
        #y = preprocessing.minmax_scale(y)

        model_ransac = RANSACRegressor(LinearRegression())
        model_ransac.fit(X, y)

        inlier_mask = model_ransac.inlier_mask_
        outlier_mask = np.logical_not(inlier_mask)
        outliers = [idx for idx, val in enumerate(outlier_mask) if val]

        residuals = abs(model_ransac.predict(X) - y)
        confidences = preprocessing.minmax_scale(residuals[outliers])*0.09+0.9

        return (outliers, confidences)

    def validate(self, ground_truths, predicts):
        '''
        Calculate precision, recall and f score by comparing ground truths and predicts
        '''
        # predict true by the model but they are not true actually
        false_positive_list = [item for item in predicts if item not in ground_truths]
        # missing truthes byt the model
        false_negative_list = [item for item in ground_truths if item not in predicts] 

        tp_fp = len(predicts)
        tp_fn = len(ground_truths)
        fp = len(false_positive_list)
        fn = len(false_negative_list)

        precision = 1 - 1.0*fp/tp_fp if tp_fp != 0 else 0 # how much the model predicts is true
        recall = 1 - 1.0*fn/tp_fn if tp_fn != 0 else 0 # how much truths is covered by the model
        f_score = precision * recall * 2.0 / (precision + recall) if precision + recall != 0 else 0

        return (precision, recall, f_score, false_positive_list, false_negative_list)