from dataclasses import dataclass


@dataclass
class Bets:
    coef1: str  # коэффициент на первую команду
    coef2: str  # коэффициент на вторую команду
    cost1: int  # ставка на первую команду
    cost2: int  # ставка на вторую команду

    def calculate_for_owerall_win(self):
        bank = self.cost1 + self.cost2
        x = max(float(self.coef1), float(self.coef2))  # больший коэффициент
        y = min(float(self.coef1), float(self.coef2))  # меньший коэффициент
        c1 = max(self.cost1, self.cost2)  # большая ставка
        c2 = min(self.cost1, self.cost2)  # меньшая ставка
        if x * c2 > bank and y * c1 > bank:
            print("можно ставить на победу")
        else:
            print("выгодных ставок нет")
            print(x, y, c1, c2, bank)

    def calculate_for_total(self):
        pass

    def calculate_for_handicap(self):
        pass

    def calculate_for_it1(self):
        pass

    def calculate_for_it2(self):
        pass

    def calculate_for_set(self):
        pass
