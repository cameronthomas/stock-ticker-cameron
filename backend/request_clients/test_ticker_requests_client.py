import unittest
from unittest import TestCase
from ticker_requests_client import TickerRequestClient


### Did you want this todo?
# TODO Mock responses from server
class TestTickerRequestClient(TestCase):
    def setUp(self):
        self.ticker_request_client = TickerRequestClient()

    def test_error_thrown_if_http_method_not_get(self):
        with self.assertRaises(ValueError):
            self.ticker_request_client.get_ticker_info(self.post_request_lambda_event)

    def test_get_ticker_info_returns_successfully(self):
        result = self.ticker_request_client.get_ticker_info(self.happy_path_lambda_event)

        assert result

    def test_error_thrown_when_ticker_query_param_missing(self):
        with self.assertRaises(ValueError):
            self.ticker_request_client.get_ticker_info(self.missing_ticker_lambda_event)

    def test_error_thrown_when_start_date_query_param_missing(self):
        with self.assertRaises(ValueError):
            self.ticker_request_client.get_ticker_info(self.missing_start_date_lambda_event)

    def test_error_thrown_when_ticker_query_param_is_empty(self):
        with self.assertRaises(ValueError):
            self.ticker_request_client.get_ticker_info(self.query_param_is_blank_lambda_event)

    def test_400_response_from_external_server_is_returned(self):
        # TODO convert this to use a mock
        result = self.ticker_request_client.get_ticker_info(self.invalid_start_date_lambda_event)

        self.assertEqual(result.json()['status'], "ERROR")

    happy_path_lambda_event = {'httpMethod': 'GET',
                               'queryStringParameters': {'ticker': 'AAPL',
                                                         'startDate': '2020-01-01',
                                                         'endDate': '2020-12-31'},
                               }

    missing_ticker_lambda_event = {'httpMethod': 'GET',
                                   'queryStringParameters': {'startDate': '2020-01-01',
                                                             'endDate': '2020-12-31'},
                                   }
    query_param_is_blank_lambda_event = {'httpMethod': 'GET',
                                         'queryStringParameters': {'ticker': '',
                                                                   'startDate': '2020-01-01',
                                                                   'endDate': '2020-12-31'},
                                         }
    post_request_lambda_event = {'httpMethod': 'POST',
                                 'queryStringParameters': {'ticker': 'AAPL',
                                                           'startDate': '2020-01-01',
                                                           'endDate': '2020-12-31'},
                                 }

    missing_start_date_lambda_event = {'httpMethod': 'GET',
                                       'queryStringParameters': {'ticker': 'AAPL',
                                                                 'endDate': '2020-12-31'},
                                       }

    invalid_start_date_lambda_event = {'httpMethod': 'GET',
                                       'queryStringParameters': {'ticker': 'AAPL',
                                                                 'startDate': 'INVALID',
                                                                 'endDate': '2020-12-31'},
                                       }


if __name__ == '__main__':
    unittest.main()
