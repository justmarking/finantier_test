# Finantier Technical Test
##### The technical test is divided into 2 parts: (1) Model Development and (2) API Implementation

### (1) Model Development
#### Model development was created in jupyter notebook named "Model Dev.ipynb". A logistic model was used with having values of 1 for defaulted accounts and 0 for non-defaults. WOE interactive binning and scaling are imported from the scorecardpy package (<https://github.com/ShichenXie/scorecardpy>) for easier implementation. Final model consists of 8 feature variables.

### (2) API Implementation
#### A working api was tested and deployed via docker file. Main program *main.py* and *test_main.py* is included in the *app* folder. For validation of successful test, go into the *app* directory and run **python -m pytest**


