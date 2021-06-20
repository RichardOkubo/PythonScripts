class generic:
    def __init__(self, default):
        self.funcs = []
        self.default = default

    def when(self, pred):
        def add(func):
            self.funcs.append((pred, func))
            return func

        return add

    def __call__(self, *args, **kwargs):
        for pred, func in self.funcs:
            try:
                match = pred(*args, **kwargs)
            except Exception:
                match = False
            if match:
                return func(*args, **kwargs)
        return self.default(*args, **kwargs)


eventos: dict = {"cor": ["amarelo", "marrom", "roxo"]}


@generic
def pintor() -> str:
    print(f"O quê!? Não entendi.")


@pintor.when(lambda evento: evento not in eventos["cor"])
def _(evento: str) -> str:
    print(f"{evento.upper()}, certo... consigo fazer algo com isso.")


@pintor.when(lambda evento: evento in eventos["cor"])
def _(evento: str) -> str:
    print(f"{evento.upper()}! Não gosto dessa cor.")


if __name__ == "__main__":

    pintor("marrom")
    pintor("azul")
    pintor()
