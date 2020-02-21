from django.test import TestCase

from endpoints.api.models.wine_pred import RandomForestClassifier


class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            "row": 1,
            "int62_field_0": "55555",
            "country": "USA",
            "description": "A light-bodied, delicate style of Pinot Noir, with pretty cherry fruit and plenty of forest and earth complexity. Silky on the finish, with hints of tea leaf. Probably best over the next year or two.",
            "designation": "unknown",
            "points": 87,
            "price": 50,
            "province": "Marlborough",
            "region_1": "unknown",
            "region_2": "unknown",
            "variety": "malbec",
            "winery": "lees"
        }
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('<=50K', response['label'])
