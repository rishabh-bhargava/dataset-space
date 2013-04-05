'''
Simple interfaces to models

James Robert Lloyd 2013
'''

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

def GaussianNaiveBayes_c:

    def description():
        return 'GNB'
        
    def predict_p(X_train, y_train, X_test):
        return GaussianNB().fit(X_train, y_train).predict_proba(X_test)[,-1]     
        
def RandomForest_c:

    def description():
        return 'RF'

    def predict_p(X_train, y_train, X_test): 
        return RandomForestClassifier(n_estimators=500).fit(X_train, y_train).predict_proba(X_test)[,-1]

def LogisticRegression_c:

    def description():
        return 'LR'

    def predict_p(X_train, y_train, X_test): 
        return RandomForestClassifier(n_estimators=500).fit(X_train, y_train).predict_proba(X_test)[,-1]
    
