import pandas as pd
import numpy as np

def load_data(datalist):
  """
  Takes in a list of csvs that serve as the training/test data set
  and correctly extracts, transforms, and loads data into pandas 
  DFs
  
  datalist -> a list of csv file names to be loaded
  returns the final dataframe to be used as a train or test data
  """
  final_data = pd.DataFrame()
  
  for i in datalist:
    data = pd.read_csv(i)
    packet_loss = int(i.split('-')[1])
    latency = int(i.split('-')[0][-3:])
    
    data['packet_loss_ratio'] = np.ones(len(data)) * (1/packet_loss)
    data['latency'] = np.ones(len(data)) * (latency)
    
    final_data = final_data.append(data)
    
  return final_data

def load_train(datalist):
  """
  Takes in a list of csvs to be used as training data and returns
  the training dataset extracted, transformed, and loaded into a
  pandas data frame
  """
  
  return load_data(datalist)

def load_test(datalist):
  """
  Takes in a list of csvs to be used as test data and returns
  the test dataset extracted, transformed, and loaded into a
  pandas data frame
  """
  
  return load_data(datalist)
