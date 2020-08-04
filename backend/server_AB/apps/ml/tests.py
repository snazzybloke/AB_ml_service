import inspect
from apps.ml.registry import MLRegistry

from django.test import TestCase

from apps.ml.income_classifier.random_forest import RandomForestClassifier

class MLTests(TestCase):
    def test_rf_algorithm(self):
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
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual(False, response['label'])


# add below method to MLTests class:
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "income_classifier"
        algorithm_object = RandomForestClassifier()
        algorithm_name = "random forest"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "MrA"
        algorithm_description = "Random Forest with simple pre- and post-processing"
        algorithm_code = inspect.getsource(RandomForestClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)

