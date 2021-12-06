# NetworkConditionsPrediction

In this project we created two regression models. One is designed to predict the Packet Loss Ratio of a network connection, and the other is designed to predict the Latency of a network connection. All data used was gathered by the DANE Tool: https://github.com/dane-tool/dane

## Running the project

* Run the run.py file to train both models on the provided data
  - Model parameters and input data can be changed in config files
* Output of models is provided in the data/output/ folder
  - Output includes model predictions, true values, and model weights

### Config files

* data-params.json
  - rawdir: directory for the raw input data (formatted in DANE style)
    ^ default = "/data/raw/"
  - test_size: the proportion of the data to be used as test data
    ^ default = 0.33
* feature-params.json
  - features: list of which features will be included in the model (1-10)
    ^ default = [1,2,3,4,5,6,7,8,9,10]
* model-params.json
  - knn_regressor: controls the hyperparameters for the Packet Loss Ratio Model
  - ridge_regressor: controls the hyperparameters for the Latency Model
