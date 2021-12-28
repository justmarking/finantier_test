from fastapi import FastAPI, Path
from pydantic import BaseModel
from enum import Enum
import numpy as np

description = """
Telco Credit Score API helps you calculate your Telco Score for a faster application decision. 💯

## Inputs

The below inputs are necessary for the calculation of your telco score. Take note, inputs are based from their **specific list of choices** and are **case sensitive**.

**Mobile Number**: input your 10-digit mobile number (e.g. 9171234567). This will serve as your identifier.

**Senior Citizen**: *Are you a Senior Citizen?*
* *yes*
* *no*

**Online Security**: *Do you have online security?*
* *yes*
* *no*

**Contract**: *What is the desired contract duration?*
* *Two Year*
* *One Year*
* *Month-to-Month*

**Payment Method**: *What is the desired method of payment?*
* *Bank Transfer / Credit Card*
* *Electronic Check*
* *Mailed Check*

**Internet Service**: *What kind is your existing Internet service?*
* *DSL*
* *Fiber Optic*
* *None*

**Paperless Billing**: *Are you opting for Paperless Billing?*
* *yes*
* *no*

**Tenure**: *How long is your current/latest telco tenure (in months)?*: input the longest tenure for a telco contract (sourced from bureau data).

**Total Charges**: *What is your current/latest total telco monthly bill?*: input the latest total charges (sourced from bureau data).

"""
tags_metadata = [
    {
        "name": "Welcome to Telco Score",
    },
    {
        "name": "Predict",
        "description": "Calculates the telco score based from user inputs.",
    },
    {
        "name": "Telco Data",
        "description": "Returns the current database.",
    },
    {
        "name": "Search Mobile",
        "description": "Returns the data inputs, score and decision based from mobile number.",
    },
    {
        "name": "Delete Mobile",
        "description": "Deletes data from database based from mobile number.",
    },
]

app = FastAPI(
    title="Telco Credit Score",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata)

tempdb = []

class SeniorCitizen(str, Enum):
    yes = "yes"
    no = "no"

class OnlineSecurity(str, Enum):
    yes = "yes"
    no = "no"
    noint = "No Internet Service"

class Contract(str, Enum):
    t = "Two Year"
    o = "One Year"
    m = "Month-to-Month"

class PaymentMethod(str, Enum):
    mail = "Mailed Check"
    elec = "Electronic Check"
    others = "Bank Transfer / Credit Card"

class InternetService(str, Enum):
    no = "None"
    dsl = "DSL"
    fo = "Fiber Optic"

class PaperlessBilling(str, Enum):
    yes = "yes"
    no = "no"

class Telco(BaseModel):
    mobile: int
    senior: SeniorCitizen
    onlinesec: OnlineSecurity
    contract: Contract
    paymeth: PaymentMethod
    internet:InternetService
    paperless: PaperlessBilling
    tenure: int
    totcharge: int

@app.get('/', tags=['Welcome to Telco Score'])
def read_root():
    return {'message': 'Hello, this API calculates your Telco Score.'}

@app.post('/predict', tags=["Predict"])
def predict_telco_score(data: Telco):
    data = data.dict()
    mobilenum = int(data['mobile'])
    # SeniorCitizen weights
    if(data['senior']=='yes'):
        SeniorCitizen = -20
    else:
        SeniorCitizen = 4
    # OnlineSecurity weights
    if(data['onlinesec']=='yes'):
        OnlineSecurity = 10
    elif(data['onlinesec']=='no'):
        OnlineSecurity = -10
    else:
        OnlineSecurity = 21
    # Contract weights
    if(data['contract']=='t'):
        Contract = 80
    elif(data['contract']=='o'):
        Contract = 33
    else:
        Contract = -23
    # PaymentMethod weights
    if(data['paymeth']=='mail'):
        PaymentMethod = 7
    elif(data['paymeth']=='elec'):
        PaymentMethod = -14
    else:
        PaymentMethod = 11
    # InternetService weights
    if(data['internet']=='no'):
        InternetService = 96
    elif(data['internet']=='dsl'):
        InternetService = 28
    else:
        InternetService = -44
    # PaperlessBilling weights
    if(data['paperless']=='yes'):
        PaperlessBilling = -10
    else:
        PaperlessBilling = 18
    # tenure weights
    if(data['tenure']<6):
        tenure = -39
    elif((data['tenure']>=6)&(data['tenure']<18)):
        tenure = -13
    elif((data['tenure']>=18)&(data['tenure']<71)):
        tenure = 18
    else:
        tenure = 90
    # Total Charges weights
    if(data['totcharge']<200):
        TotalCharges = -43
    elif((data['totcharge']>=200)&(data['totcharge']<400)):
        TotalCharges = -14
    elif((data['totcharge']>=400)&(data['totcharge']<3600)):
        TotalCharges = 5
    else:
        TotalCharges = 34
    # Compute for the Score
    Score = 461 + SeniorCitizen + OnlineSecurity + Contract + PaymentMethod + InternetService + PaperlessBilling + tenure + TotalCharges
    if(Score < 400):
        decision = 'Application is REJECTED'
    else:
        decision = 'Application is ACCEPTED'
    tempdb.append({'Mobile Number': data['mobile'],'Senior Citizen': data['senior'],'Online Security': data['onlinesec'],'Contract': data['contract'],
                   'Payment Method': data['paymeth'], 'Internet Service': data['internet'],'Paperless Billing': data['paperless'],'Tenure': data['tenure'],'Total Charges': data['totcharge'],
                   'Telco Score': Score, 'Decision': decision})
    return {'Credit Score': Score,
            'Decision': decision}

@app.get('/telcodata', tags=["Telco Data"])
def get_telco_database():
    return tempdb

@app.get('/telco/{mobilenum}', tags=["Search Mobile"])
def get_mobile_data(mobilenum:int):
    for s in range(len(tempdb)):
        if tempdb[s]["Mobile Number"] == mobilenum:
            return tempdb[s]     

@app.delete('/telco/{mobilenum}', tags=["Delete Mobile"])
def delete_mobile_data(mobilenum: int):
    for s in range(len(tempdb)):
        if tempdb[s]["Mobile Number"] == mobilenum:
            tempdb.pop(s)
            return {'task': 'deletion successful'}
