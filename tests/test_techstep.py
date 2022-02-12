import requests

def test_get_successful_response():
    resp = requests.get("http://techstepacademy.com/training-ground")
    assert resp.status_code == 200

# def test_get_unsuccessful_response():
#     resp = requests.get("http://techstepacademy.com/training-grounddd")
#     assert resp.status_code == 404
