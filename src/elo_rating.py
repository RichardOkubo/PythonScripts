""" The Elo rating system is a method for calculating the relative
skill levels of players in zero-sum games such as chess. It is named
after its creator Arpad Elo, a Hungarian-American physics professor.
"""


class EloRatingSystem:

    def __init__(self, d=400, k=32):
        self.d = d
        self.k = k

    def __call__(self, r_x, r_y, is_winner):
        return r_x + self.k * (self.actual_score(is_winner) - self.expected_score(r_x, r_y))

    def expected_score(self, r_x, r_y):
        return 1 / (1 + 10 ** ((r_y - r_x) / self.d))

    def actual_score(self, is_winner):
        return 1 if is_winner else 0


if __name__ == "__main__":
    ers = EloRatingSystem()
    
    print(ers(1200, 1000, True))
