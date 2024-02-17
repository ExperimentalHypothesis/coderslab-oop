
import random
from typing import Tuple


class CommandPrompt:
    def __init__(self, buy: Tuple[str, ...], sell: Tuple[str, ...], wait: Tuple[str, ...]):
        self.buy = buy
        self.sell = sell
        self.wait = wait

    def ask(self) -> str:
        valid_choices = self.buy + self.sell + self.wait
        while True:
            choice = input('Decision [b/s/w/buy/sell/wait]: ')
            if choice not in valid_choices:
                print(f"Invalid choice: {choice}")
                continue
            else:
                return choice

class Wallet:
    def __init__(self, pln: float, usd: float):
        self.pln = pln
        self.usd = usd

    def convert_pln_to_usd(self, usdpln_rate):
        self.usd += self.pln / usdpln_rate
        self.pln = 0

    def convert_usd_to_pln(self, usdpln_rate):
        self.pln += self.usd * usdpln_rate
        self.usd = 0


random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))


def main(usdpln_rates):
    wallet_pln = 100.0
    wallet_usd = 0.0

    cp = CommandPrompt(buy=tuple(["b", "buy"]), sell=tuple(["s", "sell"]), wait=tuple(["w", "wait", ""]))
    wallet = Wallet(pln=wallet_pln, usd=wallet_usd)

    for usdpln_rate in usdpln_rates:
        print(f'Balance: {round(wallet.pln, 2)} PLN, ${round(wallet.usd, 2)}, rate {usdpln_rate}')
        choice = cp.ask()
        if choice in ('b', 'buy'):
            wallet.convert_pln_to_usd(usdpln_rate)
        elif choice in ('s', 'sell'):
            wallet.convert_usd_to_pln(usdpln_rate)


    wallet.pln += wallet.usd * usdpln_rate
    wallet.usd = 0
    print(f'Your result: {wallet.pln} PLN!')


if __name__ == '__main__':
    main(random_usdpln_rates)
