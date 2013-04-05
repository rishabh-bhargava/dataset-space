'''
Routines to coordinate model x dataset evaluation

James Robert Lloyd 2013
'''

import numpy as np

from utils.pyroc import AUC
from utils.data import load_dictionary
import models

def evaluate_method(method, data):
    return np.mean(AUC(method().predict_p(fold['X_train'], fold['y_train'], fold['X_test']), fold['y_test']) for fold in data['folds'])
    
def split_into_folds(data, n):
    #### TODO - implement me properly
    folds = ['X_train' : data['X'][0:-200,], 'y_train' : data['y'][0:-200,], 'X_test' : data['X'][-200:][:], 'y_test' : data['y'][-200:]]
    return {'folds' : folds}
    
def evaluate_all(methods, data_files):
    for data_file in data_files:
        data = split_into_folds(load_dictionary(data_files))
        for method in methods:
            score = evaluate_method(method, data)
            print '%s %s %f' % (data_file, method().description(), score)
            
def test():
    methods = [models.GaussianNaiveBayes_c, models.LogisticRegression_c]
    data_files = ['../data/class/sonar.mat', '../data/class/ionosphere.mat']
    evaluate_all(methods, data_sets)
