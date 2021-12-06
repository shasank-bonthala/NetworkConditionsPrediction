import pandas as pd
from sklearn import linear_model
from sklearn import svm
from sklearn.model_selection import train_test_split

def models():
  mdls = {
        "SVM": svm.SVR,
        "BayesianRidge": linear_model.BayesianRidge
    }

    return mdls

def model_build(features,truth,tag,test_size,**params):
  
  X_train, X_test, y_train, y_test = train_test_split(features, truth, test_size=test_size)
  
  
  
  
  
  
  
  

