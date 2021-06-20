"""Módulo para construção de grafos."""
from collections import defaultdict


class Grafo:
    """Classe que implementa um grafo."""

    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)

    @property
    def vertices(self):
        """Retorna a lista de vértices do grafo."""
        return list(self.adj.keys())

    @property
    def arestas(self):
        """Retorna a lista de arestas do grafo."""
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adiciona_arestas(self, arestas):
        """Adiciona arestas ao grafo."""
        for u, v in arestas:
            self.adiciona_arco(u, v)

    def adiciona_arco(self, u, v):
        """Adiciona uma ligação (arco) entre os nodos 'u' e 'v'."""
        self.adj[u].add(v)
        # Se o grafo for não-direcionado, adicionar arcos nos dois sentidos.
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v):
        """Verifica se existe uma aresta entre os vértices 'u' e 'v'."""
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return f"{self.__class__.__name__}({dict(self.adj)})"

    def __repr__(self):
        return f"{self.__class__.__name__}({dict(self.adj)})"

    def __getitem__(self, v):
        return self.adj[v]


if __name__ == "__main__":

    aresta = [("A", "B")("B", "C"), ("B", "D"), ("C", "B")]
    grafo = Grafo(aresta, direcionado=True)
