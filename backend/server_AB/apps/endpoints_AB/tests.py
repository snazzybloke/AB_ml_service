# Create your tests here.
# file backend/server/endpoints/tests.py

from django.test import TestCase
from rest_framework.test import APIClient

class EndpointTests(TestCase):

    def test_predict_view(self):
        client = APIClient()
        input_data = {
            "Age": 37,
            "Workclass": "Private",
            "Education-Num": 9,
            "Marital Status": "Married-civ-spouse",
            "Occupation": "Craft-repair",
            "Relationship": "Husband",
            "Race": "White",
            "Sex": "Male",
            "Capital Gain": 0,
            "Capital Loss": 0,
            "Hours per week": 68,
            "Country": "United-States"
        }
        classifier_url = "/api/v1/income_classifier/predict"
        response = client.post(classifier_url, input_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["label"], False)
        self.assertTrue("request_id" in response.data)
        self.assertTrue("status" in response.data)
