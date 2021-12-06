import pandas as pd
import numpy as np

# CUSTOM FEATURES

# Feature 1: Maximum Packet Size for each interaction
def max_size(x):
  """
  Helper function used to add max packet size feature
  """
  nums = x.split(';')[:-1]
  nums_int = list(map(int, nums))
  return max(nums_int)
  
# Feature 2: Range of Packet Size for each interaction
def range_size(x):
  """
  Helper function used to add range of packet size feature
  """
  nums = x.split(';')[:-1]
  nums_int = list(map(int, nums))
  return max(nums_int) - min(nums_int)
  
# Feature 3: Average of Packet Size for each interaction
def avg_size(x):
  """
  Helper function used to add average packet size feature
  """
  nums = x.split(';')[:-1]
  numsInt = list(map(int, nums))
  return np.mean(numsInt)
  
# Feature 4: Longest Packet Duration
def packet_dur(x):
  """
  Helper function used to add longest packet duration feature
  """
  nums = x.split(';')[:-1]
  numsInt = list(map(int, nums))
  return max(numsInt) - min(numsInt)
  
# Feature 5: Total packet Direction
def total_packet_dir(x):
  """
  Helper function used to add total packet direction feature
  """
  dirs = x.split(';')[:-1]
  totalDirs = 0
    
  for i in dirs:
      if i == '1':
          totalDirs += 1
      elif i == '2':
          totalDirs -= 1
           
  return totalDirs
  
# Feature 6: total packets -> Done in apply_features()
# Feature 7: total bytes -> Done in apply_features()

# Feature 8: Interaction length
def interaction_length(x):
  """
  Helper function used to add interaction length feature
  """
  times = x.split(';')[:-1]
  times2 = list(map(int, times))
  startTime = min(times2)
  endTime = max(times2)
           
  return endTime - startTime
  
# Feature 9: total packets over time ratio -> Done in apply_features()
# Feature 10: total bytes over time ratio -> Done in apply_features()

def apply_features(df):
  """
  Takes in a raw dataframe from etl.py and 
  applys all the custom features into one dataframe
  """
  df['max_packet_size'] = df['packet_sizes'].apply(max_size)
  df['range_packet_size'] = df['packet_sizes'].apply(range_ssize)
  df['avg_packet_size'] = df['packet_sizes'].apply(avg_size)
  df['longest_packet_dur'] = df['packet_times'].apply(packet_dur)
  df['total_packet_dir'] = df['packet_dirs'].apply(total_packet_dir)
  df['total_packets'] = df['1->2Pkts'] + df['2->1Pkts']
  df['total_bytes'] = df['1->2Bytes'] + df['2->1Bytes']
  df['interaction_length'] = df['packet_times'].apply(interaction_length)
  df['packets_time_ratio'] = df['totalPackets'] / df['longest_packet_dur']
  df['bytes_time_ratio'] = df['totalBytes'] / df['longest_packet_dur']
  
  def modify(x):
    if x == float('inf'):
      return 0
    else:
      return x
      
  df['packets_time_ratio'] = df['packets_time_ratio'].apply(modify)
  df['bytes_time_ratio'] = df['bytes_time_ratio'].apply(modify)
  
  return df
