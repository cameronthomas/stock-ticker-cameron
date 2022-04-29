from functools import reduce
import numpy as np


def find_max(stock_ticker_results, key):
    max_value = reduce(lambda old_value, new_value: old_value if old_value[key] > new_value[
        key] else new_value, stock_ticker_results)
    return max_value[key]


def find_min(stock_ticker_results, key):
    min_value = reduce(lambda old_value, new_value: old_value if old_value[key] < new_value[key] else new_value,
                       stock_ticker_results)
    return min_value[key]


### Another todo
# TODO could I find a more efficient way to compute these values? This could be a problem with big data
class TickerDataAnalyzer:
    def __init__(self):
        pass

    max_price_key = 'h'
    min_price_key = 'l'
    volume_key = 'v'
    price_significant_figures = 2

    def generate_report(self, stock_ticker_results):
        max_price = self._find_max_price(stock_ticker_results)
        min_price = self._find_min_price(stock_ticker_results)
        avg_price = self._find_avg_price(stock_ticker_results)
        max_volume = self._find_max_volume(stock_ticker_results)
        min_volume = self._find_min_volume(stock_ticker_results)
        avg_volume = self._find_avg_volume(stock_ticker_results)
        return {"max_price": max_price,
                "min_price": min_price,
                "avg_price": avg_price,
                "max_volume": max_volume,
                "min_volume": min_volume,
                "avg_volume": avg_volume}

    def _find_max_price(self, stock_ticker_results):
        max_price = find_max(stock_ticker_results, self.max_price_key)
        return round(max_price, self.price_significant_figures)

    def _find_min_price(self, stock_ticker_results):
        min_price = find_min(stock_ticker_results, self.min_price_key)
        return round(min_price, self.price_significant_figures)

    ### Another todo
    # TODO verify if we calculated average price the right way
    def _find_avg_price(self, stock_ticker_results):
        total_price = 0
        for result in stock_ticker_results:
            total_price += np.mean([
                result[self.max_price_key],
                result[self.min_price_key]
            ])
        avg_price = total_price / len(stock_ticker_results)
        return round(avg_price, self.price_significant_figures)

    def _find_max_volume(self, stock_ticker_results):
        return find_max(stock_ticker_results, self.volume_key)

    def _find_min_volume(self, stock_ticker_results):
        return find_min(stock_ticker_results, self.volume_key)

    def _find_avg_volume(self, stock_ticker_results):
        cumulative_volume = 0
        for result in stock_ticker_results:
            cumulative_volume += result[self.volume_key]
        return cumulative_volume / len(stock_ticker_results)
