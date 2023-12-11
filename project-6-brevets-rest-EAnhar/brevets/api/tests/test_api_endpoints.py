# nosetests test_api_endpoints.py


import requests
import json
import csv
import nose

# Define the base URL for the API
base_url = "http://localhost:5001"

# Test case 1: Test /listAll endpoint
def test_listAll():
    response = requests.get(base_url + "/listAll")
    assert response.status_code == 200
    data = json.loads(response.text)
    # Add your assertions for testing the response data here

# Test case 2: Test /listOpenOnly endpoint
def test_listOpenOnly():
    response = requests.get(base_url + "/listOpenOnly")
    assert response.status_code == 200
    data = json.loads(response.text)
    # Add your assertions for testing the response data here

# Test case 3: Test /listCloseOnly endpoint
def test_listCloseOnly():
    response = requests.get(base_url + "/listCloseOnly")
    assert response.status_code == 200
    data = json.loads(response.text)
    # Add your assertions for testing the response data here

# Test case 4: Test /listAll/csv endpoint
def test_listAllCSV():
    response = requests.get(base_url + "/listAll/csv")
    assert response.status_code == 200
    # Add your assertions for testing the CSV response here

# Test case 5: Test /listOpenOnly/csv endpoint
def test_listOpenOnlyCSV():
    response = requests.get(base_url + "/listOpenOnly/csv")
    assert response.status_code == 200
    # Add your assertions for testing the CSV response here

# Test case 6: Test /listCloseOnly/csv endpoint
def test_listCloseOnlyCSV():
    response = requests.get(base_url + "/listCloseOnly/csv")
    assert response.status_code == 200
    # Add your assertions for testing the CSV response here

# Test case 7: Test /listAll/json endpoint
def test_listAllJSON():
    response = requests.get(base_url + "/listAll/json")
    assert response.status_code == 200
    data = json.loads(response.text)
    # Add your assertions for testing the JSON response here

# Test case 8: Test /listOpenOnly/json endpoint
def test_listOpenOnlyJSON():
    response = requests.get(base_url + "/listOpenOnly/json")
    assert response.status_code == 200
    data = json.loads(response.text)
    # Add your assertions for testing the JSON response here

# Test case 9: Test /listCloseOnly/json endpoint
def test_listCloseOnlyJSON():
    response = requests.get(base_url + "/listCloseOnly/json")
    assert response.status_code == 200
    data = json.loads(response.text)
    # Add your assertions for testing the JSON response here

# Test case 10: Test /listOpenOnly/csv with top parameter
def test_listOpenOnlyCSVWithTop():
    response = requests.get(base_url + "/listOpenOnly/csv?top=3")
    assert response.status_code == 200
    # Add your assertions for testing the CSV response with top parameter here

# Test case 11: Test /listOpenOnly/json with top parameter
def test_listOpenOnlyJSONWithTop():
    response = requests.get(base_url + "/listOpenOnly/json?top=5")
    assert response.status_code == 200
    data = json.loads(response.text)
    # Add your assertions for testing the JSON response with top parameter here

# Test case 12: Test /listCloseOnly/csv with top parameter
def test_listCloseOnlyCSVWithTop():
    response = requests.get(base_url + "/listCloseOnly/csv?top=6")
    assert response.status_code == 200
    # Add your assertions for testing the CSV response with top parameter here

# Test case 13: Test /listCloseOnly/json with top parameter
def test_listCloseOnlyJSONWithTop():
    response = requests.get(base_url + "/listCloseOnly/json?top=4")
    assert response.status_code == 200
    data = json.loads(response.text)
    # Add your assertions for testing the JSON response with top parameter here

if __name__ == '__main__':
    nose.run()
