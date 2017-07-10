#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: freight_audit.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2017-07-08 09:54:27
# @Last Modified: 2017-07-08 09:54:27

import numpy as np
from sklearn.linear_model import RANSACRegressor, LinearRegression, HuberRegressor
from sklearn import preprocessing
from common.python.utils import utils

class FreightAudit:
    def utliers_by_ransac(self, table, column_indexes):
        '''
        Get outliers using RANSAC regression, which deals better with large outliers in the y direction, 
        and faster than Huber when the number of samples is very large. 
        RANSAC outpus perfect precision (100%)  and perfect recall (100%) in our experiments. 
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
    
