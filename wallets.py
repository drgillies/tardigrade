
wallets = {'EX001': {'BTC': 1, 'ETH': 0, 'XRP': 15}}


class wallet():
    tradeamount = 0.99    # it cost 1% of amount for every trade

    def __init__(self, experiment, crypto_name, balance):
        self.experiment = experiment
        self.crypto_name = crypto_name
        self.balance = balance

    def sell(self, amount):
        self.amount = amount
        self.balance = self.balance - (amount * tradeamount)

    def buy(self, amount):
        self.amount = amount
        self.balance = self.balance + (amount * tradeamount)


def balance(experiment):
    for i in wallets:
        print(wallets[experiment])