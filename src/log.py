import logging

log_format = "%(asctime)s  %(levelname)s  %(filename)s  %(lineno)s  %(message)s"

logging.basicConfig(
    filename="exemplo_1.log",
    level=logging.DEBUG,
    filemode="w",  # "a" é o default
    format=log_format,
)

logger = logging.getLogger("root")

# logging.debug('Debug')
# logging.info('Info')
# logging.warning('Warning')
# logging.error('Error')
# logging.critical('Critical')

# try:
#     1/0
# except Exception as e:
#     logging.error(f'Erro -> {e}')


def add(x: int, y: int) -> int:
    if isinstance(x, int) and isinstance(y, int):
        logger.info(f" x: {x} | y {y}")
        return x + y
    else:
        logging.warning(f" x: {x} {type(x)} | y {y} {type(y)}")


if __name__ == "__main__":
    add(7, 7)
    add(7, 8.6)
