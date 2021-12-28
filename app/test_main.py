from fastapi.testclient import TestClient
from main import app


# API endpoint testing
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, this API calculates your Telco Score.'}

def test_predict():
    response = client.post('/predict', 
                             json={ "mobile": 9171234658, 
                                    "senior": "no", 
                                    "onlinesec":"No Internet Service",
                                    "contract":"One Year",
                                    "paymeth":"Electronic Check",
                                    "internet": "DSL",
                                    "paperless":"yes",
                                    "tenure":75,
                                    "totcharge":499,
                                    },)
    assert response.status_code == 200
    assert response.json() == {'Credit Score':515,
                               'Decision':'Application is ACCEPTED',}

# This is not working!
# def test_read_db():
#     response = client.get("/telcodata")
#     assert response.status_code == 200
#     assert response.json() == {'Mobile Number': 9171234658,
#                                'Senior Citizen': 'no',
#                                'Online Security': 'No Internet Service',
#                                'Contract': 'One Year',
#                                'Payment Method': 'Electronic Check',
#                                'Internet Service': 'DSL',
#                                'Paperless Billing': 'yes',
#                                'Tenure': 75,
#                                'Total Charges': 499,
#                                'Telco Score': 515, 
#                                'Decision': 'Application is ACCEPTED'}
# This is not working!
# def test_get_mobile():
#     response = client.get('/telco/{mobilenum}', 
#                              json={ "mobile": 9171234658,})
#     assert response.status_code == 200
#     assert response.json() == {'Mobile Number': 9171234658,
#                                'Senior Citizen': 'no',
#                                'Online Security': 'No Internet Service',
#                                'Contract': 'One Year',
#                                'Payment Method': 'Electronic Check',
#                                'Internet Service': 'DSL',
#                                'Paperless Billing': 'yes',
#                                'Tenure': 75,
#                                'Total Charges': 499,
#                                'Telco Score': 515, 
#                                'Decision': 'Application is ACCEPTED'}