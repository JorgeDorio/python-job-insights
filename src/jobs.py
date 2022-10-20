from functools import lru_cache
import csv


@lru_cache
def read(path: str):
    with open(path) as file:
        data = [dict(row) for row in csv.DictReader(file)]
        return data
