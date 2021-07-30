from typing import List

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


if __name__ == '__main__':
	print(read_prices('AAPL'))
