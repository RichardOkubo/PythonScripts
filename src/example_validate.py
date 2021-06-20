from validate import validate


@validate
def sub(x: int, y: int) -> int:
    return x - y
