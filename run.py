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
  
  
if __name__ == '__main__':
    main()
