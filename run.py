import sys
import os
import json

sys.path.insert(0, 'src')

import pandas as pd
import numpy as np

from etl import load_data
from features import apply_features
from model import model_build

def main():
  """
  Runs all the src code in one script. The main method in our project that runs our project
  
  `main` runs the targets in order of data=>analysis=>model.
  """
  datalist = ['data/raw/20211023T012228_200-500-iperf.csv',
              'data/raw/20211023T012231_200-750-iperf.csv',
              'data/raw/20211104T232610_200-200-iperf.csv',
              'data/raw/20211105T000043_200-1000-iperf.csv',
              'data/raw/20211105T003333_200-2000-iperf.csv',
              'data/raw/20211105T003334_400-1600-iperf.csv',
              'data/raw/20211105T004748_400-1800-iperf.csv',
              'data/raw/20211105T164434_400-3000-iperf.csv',
              'data/raw/20211105T170902_400-4000-iperf.csv',
              'data/raw/20211105T180745_800-7000-iperf.csv',
              'data/raw/20211105T185733_800-8500-iperf.csv',
              'data/raw/20211105T205042_800-9500-iperf.csv',
              'data/raw/20211105T205041_800-10500-iperf.csv',
              'data/raw/20211105T205041_800-11000-iperf.csv']
  
  data = load_data(datalist)
  data = apply_features(data)
  
  with open('config/model-params.json') as fh:
    data_cfg = json.load(fh)
    
  X = data[['1->2Bytes', '2->1Bytes', '1->2Pkts', '2->1Pkts', 'max_packet_size', 
               'range_packet_size', 'avg_packet_size', 'longest_packet_dur', 'total_packet_dir',
               'total_packets', 'total_bytes', 'interaction_length', 'bytes_time_ratio', 'packets_time_ratio']]
  y = data.packet_loss_ratio
  y1 = data.latency
  
  #Packet Loss Predictions
  packet_loss_out = model_build(X, y, 'packet_loss_ratio', 0.33, **data_cfg['knn_regressor'])
  
  #Latency Predictions
  latency_out = model_build(X, y1, 'latency', 0.33, **data_cfg['ridge_regressor'])
  
  packet_loss_out.to_csv('/data/out/')
  latency_out.to_csv('/data/out/')
  
  return
  
if __name__ == '__main__':
    main()
