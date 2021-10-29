In Classification Folder
- classification_data.py generates classification data for given range and size as a .json file that is used as the training set for practice.
- print_cdata.py prints the classification data for max. 2 variables and max. 3 classes.
using logistic regression
- logistic_regression.py performs logistic regression using gradient ascent technique, a discriminative learning algorithm, with .json file that contains the training data, alpha, and initial value of parameters as input and stores the parameter values in the same .json file.
- lr_predict_class.py uses the parameter values generated using logistic_regression.py to predict the class for given input variables.
using gaussian distribution analysis
- GDA.py uses Gaussian Distribution Analysis, a generative learning algorithm, with .json file that contains the training data as input and stores the required values in the same .json file.
- GDA_predict_class.py uses the values generated using GDA.py to predict the class for the given input variables.

In Regression Folder
- regression_data.py generates regression data for given range and size as a .json file that is used as the training set for practice.
- print_rdata.py prints the regression data.
using linear regression
- linear_regression.py performs linear regression using stochastic gradient descent technique, a supervised learning technique, with .json file that contains the training data, alpha, and initial values of parameters input and stores the parameter values in the same .json file.
- predict_value.py uses the parameter values generated using linear_regression.py to predict the output value for given input values.
using locally weighted linear regression
- lwlreg.py performs locally weighted linear regression using stochastic gradient descent technique, a supervised learning technique, with .json file that contains the training data, input point, bandwidth, alpha, and initial values of parameters.
