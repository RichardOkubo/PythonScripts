from argparse import ArgumentParser
from datetime import timedelta


def duration(file: str, speed: int=1) -> timedelta:
    sum_time = timedelta()

    with open(file, "r") as f:
        time_list = f.read().split()

    for time in time_list:
        hour, minute, second = [int(var) for var in time.split(":")]
        t = timedelta(hours=hour, minutes=minute, seconds=second)
        sum_time += (t / speed)

    return sum_time


parser = ArgumentParser()
parser.add_argument("--file", type=str)
parser.add_argument("--speed", type=int)
args = parser.parse_args()


if __name__ == "__main__":
    try:
        print(duration(args.file, args.speed))
    except TypeError as ex:
        print(ex)
    except FileNotFoundError as ex:
        print(ex)
