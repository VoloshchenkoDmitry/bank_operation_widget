import os
from unittest import TestCase, mock
from src.external_api import convert_to_rub


class TestExternalApi(TestCase):
    @mock.patch.dict(os.environ, {'API_KEY': 'test', 'API_URL': 'http://test.com'})
    @mock.patch('requests.get')
    def test_convert_usd_to_rub(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {'rates': {'RUB': 75.5}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        transaction = {'amount': '100', 'currency': 'USD'}
        result = convert_to_rub(transaction)
        self.assertAlmostEqual(result, 7550.0)

    def test_convert_rub_to_rub(self):
        transaction = {'amount': '100', 'currency': 'RUB'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)

    @mock.patch.dict(os.environ, {'API_KEY': '', 'API_URL': ''})
    def test_missing_api_credentials(self):
        transaction = {'amount': '100', 'currency': 'EUR'}
        with self.assertRaises(ValueError):
            convert_to_rub(transaction)
