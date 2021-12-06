import pandas as pd
from sklearn import linear_model
from sklearn import neighbors
from sklearn.model_selection import train_test_split

def models():
  mdls = {
        "knn": neighbors.KNeighborsRegressor,
        "BayesianRidge": linear_model.BayesianRidge
    }

  return mdls

def model_build(features,truth,tag,test_size,**params):
  
 X_train, X_test, y_train, y_test = train_test_split(features, truth, test_size=test_size)
  
 if tag == 'packet_loss_ratio':
   mdl = neighbors.KNeighborsRegressor(**params) 
 elif tag == 'latency':
   mdl = linear_model.BayesianRidge(**params)
    
 mdl.fit(X_train, y_train)
 preds = mdl.predict(X_test)
 out = pd.concat([pd.Series(preds), y_test], axis=1)
  
 return out #returns a pandas df
