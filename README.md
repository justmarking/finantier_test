# Finantier Technical Test
##### The technical test is divided into 2 parts: (1) Model Development and (2) API Implementation

### (1) Model Development
#### Model development was created in jupyter notebook named "Model Dev.ipynb". A logistic model was used with having values of 1 for defaulted accounts and 0 for non-defaults. WOE interactive binning and scaling are imported from the scorecardpy package (<https://github.com/ShichenXie/scorecardpy>) for easier implementation. Final model consists of 8 feature variables.

### (2) API Implementation
#### A working api, created via FastAPI, was tested and deployed via docker file. Instructions is found at the description of the API upon running. Main program and testing program (*main.py* and *test_main.py*) are included inside the */app* directory. 

#### For validation of successful API testing, follow below instructions:
> go into the */app* directory 

> run **python -m pytest**

#### The image of the container, *myimage*, has already been created, but if there are issues, run the following commands:
> go into working directory of *Dockerfile*

> run **docker build -t myimage .**

#### The API can be ran manually by its image, *myimage*, using the following commands:
> go into working directory of *Dockerfile*

> run **docker run -d --name mycontainer -p 80:80 myimage**

> open localhost in browser

#### It is better to open the API via the Swagger UI of FastAPI for easier interaction:
> open container which will direct to local host in browser after running the image

> add */docs* at the end of the URL

#### 3 screenshots (.png) of the working API are included for expected results of validation. 
