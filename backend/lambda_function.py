import json
from request_clients.ticker_requests_client import TickerRequestClient
from ticker_data_analyzer import TickerDataAnalyzer

print('Loading function')


def respond(status_code, res):
    return {
        'statusCode': status_code,
        'body': json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }


def lambda_handler(event, context):
    ticker_client = TickerRequestClient()
    report_generator = TickerDataAnalyzer()

    ticker_results = ticker_client.get_ticker_info(event)
    if ticker_results.json()['status'] == "ERROR":
        return respond(ticker_results.status_code, ticker_results.text)
    # TODO test
    # TODO handle non existent ticker ie ATLA
    # TODO handle wrong headers
    results = ticker_results.json()['results']

    report = report_generator.generate_report(results)

    return respond(200, report)
