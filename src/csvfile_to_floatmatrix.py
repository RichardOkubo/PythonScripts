from csv import reader
from typing import List, NewType

FloatMatrix = NewType('FloatMatrix', List[List[float]])


def load(csv_file: str) -> FloatMatrix:
    """Convert data in CSV files to float arrays."""

    assert csv_file.endswith(".csv") == True

    dataset =  []

    with open(csv_file) as f:
        for line in reader(f, delimiter=","):
            dataset.append([float(column) for column in line])
    
    return dataset


if __name__ == "__main__":

    print(load("db.csv"))
