from statistics import stdev, mean
from typing import List
from itertools import combinations

import numpy as np
import csv


def read_prices(name: str) -> List[float]:
	result = []
	with open(f'data/{name}.csv', newline='') as file:
		reader = csv.reader(file)
		next(reader)  # Skip header
		for row in reader:
			result.append(float(row[5]))

	return result


def correlation_using_stdlib(x_prices: List[float], y_prices: List[float]) -> float:
	x_mean = mean(x_prices)
	y_mean = mean(y_prices)
	x_stddev = stdev(x_prices)
	y_stddev = stdev(y_prices)

	numerator = 0
	for x, y in zip(x_prices, y_prices):
		numerator += (x - x_mean) * (y - y_mean)

	return numerator / ((len(x_prices) - 1) * x_stddev * y_stddev)


if __name__ == '__main__':
	symbols = ['AAPL', 'AMZN', 'FB', 'GOOG', 'IBM', 'MSFT', 'NFLX', 'ORCL', 'SAP', 'TSLA']
	stock_prices = [(s, read_prices(s)) for s in symbols]

	print('non-NumPy version')
	correlations = [
		((x_name, y_name), correlation_using_stdlib(x_prices, y_prices))
		for ((x_name, x_prices), (y_name, y_prices)) in combinations(stock_prices, 2)
	]
	correlations.sort(key=lambda item: item[1], reverse=True)

	for ((x_name, y_name), correlation) in correlations:
		print(f'{x_name}:{y_name} = {correlation}')
