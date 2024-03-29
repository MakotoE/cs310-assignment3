from timeit import timeit
from statistics import stdev, mean
from typing import List, Tuple
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

	numerator = 0
	for x, y in zip(x_prices, y_prices):
		numerator += (x - x_mean) * (y - y_mean)

	return numerator / ((len(x_prices) - 1) * stdev(x_prices) * stdev(y_prices))


def correlation(x_prices: List[float], y_prices: List[float]) -> float:
	return np.divide(
		np.multiply(
			np.array(x_prices) - np.array(x_prices).mean(),
			np.array(y_prices) - np.array(y_prices).mean(),
		).sum(),
		(len(x_prices) - 1) * np.array(x_prices).std(ddof=1) * np.array(y_prices).std(ddof=1),
	)


def print_correlations(correlations: List[Tuple[Tuple[str, str], float]]):
	for ((x_name, y_name), corr) in correlations:
		print(f'{x_name}:{y_name} = {corr}')


if __name__ == '__main__':
	stock_prices = [
		(s, read_prices(s))
		for s in ['AAPL', 'AMZN', 'FB', 'GOOG', 'IBM', 'MSFT', 'NFLX', 'ORCL', 'SAP', 'TSLA']
	]

	correlations_stdlib = [
		((x_name, y_name), correlation_using_stdlib(x_prices, y_prices))
		for ((x_name, x_prices), (y_name, y_prices)) in combinations(stock_prices, 2)
	]
	correlations_stdlib.sort(key=lambda item: item[1], reverse=True)

	print('non-NumPy version')

	print_correlations(correlations_stdlib)

	correlations_numpy = [
		((x_name, y_name), correlation(x_prices, y_prices))
		for ((x_name, x_prices), (y_name, y_prices)) in combinations(stock_prices, 2)
	]
	correlations_numpy.sort(key=lambda item: item[1], reverse=True)

	print('\nNumPy version')

	print_correlations(correlations_numpy)

	executions = 100
	stdlib_duration = timeit(
		lambda: correlation_using_stdlib(stock_prices[0][1], stock_prices[1][1]),
		number=executions,
	) / executions
	print(f'\nnon-NumPy version execution time: {stdlib_duration:.6f}s')

	numpy_duration = timeit(
		lambda: correlation(stock_prices[0][1], stock_prices[1][1]),
		number=executions,
	) / executions
	print(f'NumPy version execution time: {numpy_duration:.6f}s')
